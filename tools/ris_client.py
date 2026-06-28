#!/usr/bin/env python3
"""
ris_client.py — minimaler, abhängigkeitsfreier Client für die RIS-Open-Data-API.

RIS = Rechtsinformationssystem des Bundes (https://www.ris.bka.gv.at).
OGD-API-Basis: https://data.bka.gv.at/ris/api/v2.6/  (kein API-Key, JSON oder XML).

Zweck: Österreichische Primärquellen (Normen + Judikatur) verifizierbar auflösen,
damit Skills in diesem Repository **keine** Geschäftszahlen, Rechtssatznummern oder
Fundstellen erfinden. Norm zuerst, dann verifizierte Judikatur — vgl.
`references/zitierweise.md` und `references/ris-quellen.md`.

Empirisch verifiziertes Verhalten der OGD-Judikatur-Suche (Stand: live geprüft):
  * Antwort ist tief verschachtelt:
      OgdSearchResult -> OgdDocumentResults -> {Hits, OgdDocumentReference[]}
      OgdDocumentReference -> Data -> Metadaten -> {Technisch, Allgemein, Judikatur}
  * `Organ` (z.B. "OGH", "OGH; AUSL EGMR") steht unter **Technisch**, NICHT unter Judikatur.
  * `DokumentUrl` steht unter **Allgemein**.
  * `Judikatur` enthält: Dokumenttyp, Geschaeftszahl{item}, Normen,
      Entscheidungsdatum, EuropeanCaseLawIdentifier (ECLI), Justiz.
  * Die Suche liefert standardmäßig **Rechtssätze** (Dokument-ID `JJR_…`, ECLI `…:RSxxxxxxx`).
      Bei einem Rechtssatz ist `Geschaeftszahl.item` eine **mit Semikolon getrennte Liste**
      aller bestätigenden Entscheidungen; das Entscheidungsdatum ist das der jüngsten.
  * Gültige Seitengrößen (`DokumenteProSeite`): Ten, Twenty, Fifty, OneHundred.
  * Leere/fehlerhafte Anfragen liefern `OgdSearchResult.Error{Applikation,Message}`
      bzw. ein `OgdSearchResult` ohne `OgdDocumentResults` (0 Treffer).
  * Strukturierte Norm-Filterung (`Norm=`) ist nicht zuverlässig — Volltextsuche
      (`Suchworte=`) ist robuster; Norm-Treffer immer am Text gegenprüfen.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

OGD_BASE = "https://data.bka.gv.at/ris/api/v2.6/"
RIS_WEB = "https://www.ris.bka.gv.at/"
USER_AGENT = "at-law-ris-client/0.1 (+oesterreichisches-recht)"
VALID_PAGE_SIZES = ("Ten", "Twenty", "Fifty", "OneHundred")

# Live-verifizierte Gesetzesnummern (Bundesrecht konsolidiert). Beim Erweitern
# IMMER über die Web-Permalink-Prüfung verifizieren, nie raten.
GESETZESNUMMER = {
    "ABGB": "10001622",   # Allgemeines bürgerliches Gesetzbuch — verifiziert (HTTP 200)
    "VGG": "20011654",    # Verbrauchergewährleistungsgesetz (BGBl I 175/2021) — verifiziert (§11/§12 HTTP 200)
}

# Organe ausländischer/überstaatlicher Gerichte, die bei reiner OGH-Recherche
# herausgefiltert werden (RIS mischt sie gelegentlich in `Organ` ein).
FOREIGN_MARKERS = ("AUSL", "EGMR", "EUGH", "EU-G")


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #
def _request(endpoint: str, params: dict):
    url = OGD_BASE + endpoint + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url, headers={"Accept": "application/json", "User-Agent": USER_AGENT}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return url, json.load(resp)


def http_status(url: str):
    """HTTP-Status einer URL prüfen (HEAD, Fallback GET). Für Permalink-Verifikation."""
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(
                url, method=method, headers={"User-Agent": USER_AGENT}
            )
            with urllib.request.urlopen(req, timeout=20) as resp:
                return resp.status
        except urllib.error.HTTPError as exc:
            if method == "GET":
                return exc.code
        except Exception as exc:  # noqa: BLE001
            if method == "GET":
                return str(exc)
    return None


# --------------------------------------------------------------------------- #
# Geschäftszahl-Normalisierung
# --------------------------------------------------------------------------- #
_GZ_RE = re.compile(r"^(\d+)\s*([A-Za-zÄÖÜäöüß]+)\s*(\d+/\d+\s*[a-zäöü]?)$")


def normalize_gz(gz: str) -> str:
    """'6Ob158/22m' -> '6 Ob 158/22m' (kanonische Zitier-Schreibweise mit Spatien)."""
    gz = (gz or "").strip()
    match = _GZ_RE.match(gz)
    if match:
        senat, register, rest = match.groups()
        return f"{senat} {register} {rest.replace(' ', '')}"
    return gz


def split_geschaeftszahlen(item) -> list[str]:
    """Semikolon-Liste -> deduplizierte, normalisierte Einzel-GZ.
    'A; B (B2); A' -> ['A', 'B'] (führende GZ je Eintrag, Klammer-Parallel-GZ verworfen)."""
    if isinstance(item, dict):
        item = item.get("item")
    out, seen = [], set()
    for part in (item or "").split(";"):
        lead = part.split("(")[0].strip()
        if not lead:
            continue
        norm = normalize_gz(lead)
        if norm not in seen:
            seen.add(norm)
            out.append(norm)
    return out


def _as_list(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


# --------------------------------------------------------------------------- #
# Judikatur
# --------------------------------------------------------------------------- #
def search_judikatur(
    suchworte: str | None = None,
    gericht: str | None = None,
    norm: str | None = None,
    von: str | None = None,
    bis: str | None = None,
    applikation: str = "Justiz",
    page: int = 1,
    size: str = "Ten",
    include_foreign: bool = False,
) -> dict:
    """RIS-Judikatur durchsuchen. Gibt {url, total, results[]} zurück.

    Jedes result: dokumenttyp, rs_number, organ, leading_gz, gz_list[],
    entscheidungsdatum, ecli, dokument_url, normen, doc_id.
    """
    if size not in VALID_PAGE_SIZES:
        raise ValueError(f"size muss aus {VALID_PAGE_SIZES} sein (war: {size!r})")
    params = {"Applikation": applikation, "DokumenteProSeite": size, "Seitennummer": str(page)}
    if suchworte:
        params["Suchworte"] = suchworte
    if gericht:
        params["Gericht"] = gericht
    if norm:
        params["Norm"] = norm
    if von:
        params["EntscheidungsdatumVon"] = von
    if bis:
        params["EntscheidungsdatumBis"] = bis

    url, data = _request("Judikatur", params)
    root = data.get("OgdSearchResult", {})
    if "Error" in root:
        raise RuntimeError("RIS-Fehler: " + (root["Error"].get("Message") or "unbekannt"))
    results_node = root.get("OgdDocumentResults")
    if not results_node:  # 0 Treffer
        return {"url": url, "total": 0, "results": []}

    total = int(results_node["Hits"]["#text"])
    parsed = []
    for ref in _as_list(results_node.get("OgdDocumentReference")):
        meta = ref.get("Data", {}).get("Metadaten", {})
        jud = meta.get("Judikatur", {}) or {}
        tech = meta.get("Technisch", {}) or {}
        allg = meta.get("Allgemein", {}) or {}

        organ = (tech.get("Organ") or "").strip()
        if not include_foreign and any(mk in organ.upper() for mk in FOREIGN_MARKERS):
            continue

        ecli = jud.get("EuropeanCaseLawIdentifier")
        doc_id = tech.get("ID", "") or ""
        is_rechtssatz = doc_id.startswith("JJR") or bool(ecli and ":RS" in ecli)
        gz_list = split_geschaeftszahlen(jud.get("Geschaeftszahl"))
        rs_number = ecli.split(":")[-1] if (ecli and ":RS" in ecli) else None

        parsed.append(
            {
                "dokumenttyp": "Rechtssatz" if is_rechtssatz else "Entscheidungstext",
                "rs_number": rs_number,
                "organ": organ,
                "leading_gz": gz_list[0] if gz_list else None,
                "gz_list": gz_list,
                "entscheidungsdatum": jud.get("Entscheidungsdatum"),
                "ecli": ecli,
                "dokument_url": allg.get("DokumentUrl"),
                "normen": jud.get("Normen"),
                "doc_id": doc_id,
            }
        )
    return {"url": url, "total": total, "results": parsed}


# --------------------------------------------------------------------------- #
# Normen (Permalinks)
# --------------------------------------------------------------------------- #
def norm_permalink(abbrev_or_gnr: str, paragraf: str | None = None) -> str:
    """RIS-Permalink für eine Bundesnorm. 'ABGB' wird zur Gesetzesnummer aufgelöst."""
    gnr = GESETZESNUMMER.get(abbrev_or_gnr.upper(), abbrev_or_gnr)
    url = RIS_WEB + "NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=" + urllib.parse.quote(str(gnr))
    if paragraf:
        url += "&Paragraf=" + urllib.parse.quote(str(paragraf))
    return url


# --------------------------------------------------------------------------- #
# Zitat-Formatierung (gem. references/zitierweise.md)
# --------------------------------------------------------------------------- #
def format_citation(result: dict) -> str:
    """Ein result aus search_judikatur als AT-Zitat formatieren."""
    organ = result.get("organ") or "Gericht"
    gz = result.get("leading_gz") or "?"
    datum = result.get("entscheidungsdatum") or "?"
    if result.get("dokumenttyp") == "Rechtssatz" and result.get("rs_number"):
        return f"RIS-Justiz {result['rs_number']} ({organ} {gz})"
    return f"{organ} {datum}, {gz}"


# --------------------------------------------------------------------------- #
# Smoke-Test = Phase-1 Definition-of-Done
# --------------------------------------------------------------------------- #
def smoke() -> int:
    print("RIS-Grounding Smoke-Test (Phase-1 DoD)\n" + "=" * 42)
    ok = True

    # (1) Norm: § 932 ABGB -> Permalink, HTTP 200
    url = norm_permalink("ABGB", "932")
    status = http_status(url)
    norm_ok = status == 200
    ok &= norm_ok
    print(f"[{'PASS' if norm_ok else 'FAIL'}] § 932 ABGB -> {url}")
    print(f"        HTTP {status}")

    # (2) Judikatur: OGH-Rechtssätze zu Gewährleistung/Verbesserung ab 2022
    res = search_judikatur(
        suchworte="Gewährleistung Verbesserung",
        gericht="OGH",
        von="2022-01-01",
        size="Ten",
    )
    print(f"\n[INFO] Judikatur-Treffer gesamt: {res['total']}  ({res['url']})")
    # ersten Rechtssatz mit RS-Nummer + echter führender GZ wählen
    pick = next(
        (r for r in res["results"] if r["rs_number"] and r["leading_gz"]), None
    )
    jud_ok = pick is not None
    ok &= jud_ok
    if pick:
        link_status = http_status(pick["dokument_url"])
        link_ok = link_status == 200
        ok &= link_ok
        print(f"[{'PASS' if jud_ok else 'FAIL'}] Rechtssatz gefunden:")
        print(f"        {format_citation(pick)}")
        print(f"        ECLI: {pick['ecli']}")
        print(f"        führende GZ: {pick['leading_gz']}  |  bestätigt durch {len(pick['gz_list'])} Entscheidung(en)")
        print(f"        Permalink: {pick['dokument_url']}")
        print(f"        [{'PASS' if link_ok else 'FAIL'}] Permalink HTTP {link_status}")
    else:
        print("[FAIL] Kein Rechtssatz mit RS-Nummer + Geschäftszahl gefunden.")

    print("\n" + "=" * 42)
    print("ERGEBNIS:", "ALLE CHECKS BESTANDEN ✓" if ok else "FEHLGESCHLAGEN ✗")
    print("Jede ausgegebene Zahl stammt live aus RIS — nichts modellgeneriert.")
    return 0 if ok else 1


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _cli(argv=None) -> int:
    parser = argparse.ArgumentParser(description="RIS-OGD-Client (Normen + Judikatur).")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_jud = sub.add_parser("judikatur", help="Judikatur durchsuchen")
    p_jud.add_argument("suchworte")
    p_jud.add_argument("--gericht", default=None)
    p_jud.add_argument("--von", default=None, help="EntscheidungsdatumVon YYYY-MM-DD")
    p_jud.add_argument("--bis", default=None)
    p_jud.add_argument("--norm", default=None)
    p_jud.add_argument("--size", default="Ten", choices=VALID_PAGE_SIZES)
    p_jud.add_argument("--foreign", action="store_true", help="ausländische Organe NICHT filtern")
    p_jud.add_argument("--json", action="store_true")

    p_norm = sub.add_parser("norm", help="Norm-Permalink bauen + prüfen")
    p_norm.add_argument("gesetz", help="Kurzbezeichnung (ABGB) oder Gesetzesnummer")
    p_norm.add_argument("paragraf", nargs="?", default=None)

    sub.add_parser("smoke", help="Phase-1 Grounding-Smoke-Test")

    args = parser.parse_args(argv)

    if args.cmd == "smoke":
        return smoke()

    if args.cmd == "norm":
        url = norm_permalink(args.gesetz, args.paragraf)
        print(url)
        print("HTTP", http_status(url))
        return 0

    if args.cmd == "judikatur":
        res = search_judikatur(
            suchworte=args.suchworte, gericht=args.gericht, norm=args.norm,
            von=args.von, bis=args.bis, size=args.size, include_foreign=args.foreign,
        )
        if args.json:
            print(json.dumps(res, ensure_ascii=False, indent=2))
            return 0
        print(f"# {res['total']} Treffer  ({res['url']})\n")
        for r in res["results"]:
            print(format_citation(r))
            print(f"   typ={r['dokumenttyp']}  ecli={r['ecli']}  gz={r['leading_gz']}")
            print(f"   {r['dokument_url']}")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(_cli())
