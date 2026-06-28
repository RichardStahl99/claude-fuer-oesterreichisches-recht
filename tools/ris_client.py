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
import datetime
import html
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
    "MRG": "10002531",    # Mietrechtsgesetz (BGBl 520/1981) — verifiziert (§1/§16/§37 HTTP 200)
    "RICHTWG": "10003166",  # Richtwertgesetz (BGBl 800/1993) — verifiziert (§1/§5 HTTP 200)
    "JN": "10001697",     # Jurisdiktionsnorm (RGBl 111/1895) — verifiziert (§49/§104 HTTP 200)
    "ZPO": "10001699",    # Zivilprozessordnung (RGBl 113/1895) — verifiziert (§27/§244/§464 HTTP 200)
    "EO": "10001700",     # Exekutionsordnung (RGBl 79/1896) — verifiziert (§1/§7 HTTP 200)
    "ANGG": "10008069",   # Angestelltengesetz (BGBl 292/1921) — verifiziert (§20/§23 HTTP 200)
    "ARBVG": "10008329",  # Arbeitsverfassungsgesetz (BGBl 22/1974) — verifiziert (§105 HTTP 200)
    "BMSVG": "20002088",  # Betriebl. Mitarbeiter- u. Selbständigenvorsorgegesetz (BGBl I 100/2002) — verifiziert
    "ASGG": "10000813",   # Arbeits- und Sozialgerichtsgesetz (BGBl 104/1985) — verifiziert
    "URLG": "10008376",   # Urlaubsgesetz (BGBl 390/1976) — verifiziert (§10 HTTP 200)
}

# Gesetze, deren Paragrafen in RIS unter einem Artikel adressiert werden (sonst 404).
# Das AngG wurde als "Artikel I" eines Stammgesetzes 1921 erlassen; seine §§ brauchen
# in der NormDokument-URL zusätzlich &Artikel=1.
LAW_ARTIKEL = {
    "ANGG": "1",
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
    geschaeftszahl: str | None = None,
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
    if geschaeftszahl:
        params["Geschaeftszahl"] = geschaeftszahl

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
    """RIS-Permalink für eine Bundesnorm. 'ABGB' wird zur Gesetzesnummer aufgelöst.
    Gesetze in LAW_ARTIKEL (z.B. AngG) bekommen den nötigen &Artikel=-Parameter."""
    key = abbrev_or_gnr.upper()
    gnr = GESETZESNUMMER.get(key, abbrev_or_gnr)
    url = RIS_WEB + "NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=" + urllib.parse.quote(str(gnr))
    artikel = LAW_ARTIKEL.get(key)
    if artikel:
        url += "&Artikel=" + urllib.parse.quote(artikel)
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
# Volltext, Leitsatz, Leitentscheidungs-Signal, Fassungsstand (Aktualität)
# --------------------------------------------------------------------------- #
def _strip_html(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw)).strip()


def get_document_text(doknr: str) -> str | None:
    """Volltext eines RIS-Justiz-Dokuments (Rechtssatz JJR_ oder Entscheidung JJT_)."""
    url = f"{RIS_WEB}Dokumente/Justiz/{doknr}/{doknr}.html"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return _strip_html(resp.read().decode("utf-8", "replace"))
    except Exception:  # noqa: BLE001
        return None


def rechtssatz_leitsatz(doknr: str) -> dict:
    """Den vom OGH formulierten Leitsatz (Rechtssatz) und die interpretierte Norm
    aus einem JJR_-Dokument ziehen — die frei verfügbare 'Doktrin' des Gerichts."""
    text = get_document_text(doknr) or ""
    norm = None
    m = re.search(r"\bNorm\b\s+(.+?)\s+(?:Rechtssatz|Schlagworte|European|Kopf)", text)
    if m:
        norm = m.group(1).strip()[:160]
    leitsatz = None
    m = re.search(
        r"\bRechtssatz\b\s+(.+?)\s+(?:European Case Law|Im RIS seit|Schlagworte|Dokumentnummer|Zuletzt akt)",
        text,
    )
    if m:
        leitsatz = m.group(1).strip()
    return {"doknr": doknr, "norm": norm, "leitsatz": leitsatz}


def leitentscheidung(gz: str) -> dict:
    """Leitentscheidungs-Signal für eine Geschäftszahl, abgeleitet aus dem
    Rechtssatz-System: Ist die GZ der STAMM (führende GZ) eines Rechtssatzes,
    hat sie diese Linie begründet. Die Linientiefe (Anzahl Entscheidungen in
    der Linie) misst, wie gefestigt sie ist."""
    target = normalize_gz(gz).replace(" ", "")
    res = search_judikatur(geschaeftszahl=gz, size="Fifty")
    stamm_of, member_of = [], []
    for r in res["results"]:
        if not r.get("rs_number"):
            continue
        entry = {
            "rs": r["rs_number"],
            "stamm_gz": r["leading_gz"],
            "linientiefe": len(r["gz_list"]),
            "doknr": r["doc_id"],
        }
        if (r.get("leading_gz") or "").replace(" ", "") == target:
            stamm_of.append(entry)
        else:
            member_of.append(entry)
    depths = [e["linientiefe"] for e in stamm_of + member_of]
    return {
        "gz": gz,
        "ist_leitentscheidung": bool(stamm_of),
        "stamm_von": stamm_of,
        "folgt_linie": member_of,
        "max_linientiefe": max(depths, default=0),
    }


def stamm_entscheidung_doknr(gz: str) -> str | None:
    """JJT_-Dokumentnummer der Entscheidung, die unter dieser GZ eine Rechtssatz-
    Linie begründet hat (nur wenn die GZ Stamm ist)."""
    for e in leitentscheidung(gz)["stamm_von"]:
        if (e.get("doknr") or "").startswith("JJR_"):
            return e["doknr"].replace("JJR_", "JJT_", 1)
    return None


def _para_num(s: str | None):
    m = re.search(r"(\d+)", s or "")
    return int(m.group(1)) if m else None


def norm_inkrafttreten(abbrev_or_gnr: str, paragraf: str) -> dict | None:
    """Fassungsstand eines Paragrafen: seit wann die geltende Fassung in Kraft ist
    und durch welches BGBl sie zuletzt geändert wurde. Paginiert über die (ggf.
    sehr lange) konsolidierte Norm, bricht ab, sobald der Paragraf gefunden oder
    überschritten ist (für große Gesetze wie das ABGB)."""
    gnr = GESETZESNUMMER.get(abbrev_or_gnr.upper(), abbrev_or_gnr)
    target = re.sub(r"[^0-9a-zäöüß]", "", str(paragraf).lower())
    target_num = _para_num(paragraf)
    today = datetime.date.today().isoformat()
    for page in range(1, 30):
        params = {
            "Applikation": "BrKons",
            "Gesetzesnummer": str(gnr),
            "Fassung.FassungVom": today,
            "DokumenteProSeite": "OneHundred",
            "Seitennummer": str(page),
        }
        _, data = _request("Bundesrecht", params)
        res = data.get("OgdSearchResult", {}).get("OgdDocumentResults")
        if not res:
            break
        refs = _as_list(res.get("OgdDocumentReference"))
        last_num = None
        for ref in refs:
            brk = (
                ref.get("Data", {}).get("Metadaten", {})
                .get("Bundesrecht", {}).get("BrKons", {})
            )
            pn = brk.get("Paragraphnummer") or brk.get("ArtikelParagraphAnlage") or ""
            cand = re.sub(r"[^0-9a-zäöüß]", "", pn.lower())
            if cand == target:
                return {
                    "paragraf": (brk.get("ArtikelParagraphAnlage") or f"§ {paragraf}").strip(),
                    "inkrafttretensdatum": brk.get("Inkrafttretensdatum"),
                    "idf": brk.get("Kundmachungsorgan"),
                }
            n = _para_num(pn)
            if n is not None:
                last_num = n
        # Paragrafen kommen aufsteigend — abbrechen, sobald wir den Zielparagrafen
        # überschritten haben (Puffer für Buchstaben-§§ wie 932a).
        if target_num is not None and last_num is not None and last_num > target_num + 3:
            break
        if len(refs) < 100:
            break
    return None


def currency_flag(abbrev_or_gnr: str, paragraf: str, decision_date: str | None) -> dict:
    """Aktualitäts-Flag: Wurde § <paragraf> NACH <decision_date> geändert?
    Erkennt (flaggt) eine Änderung — beurteilt NICHT, ob sie die Aussage betrifft."""
    info = norm_inkrafttreten(abbrev_or_gnr, paragraf)
    label = f"§ {paragraf} {abbrev_or_gnr.upper()}"
    if not info or not info.get("inkrafttretensdatum"):
        return {"status": "unbekannt",
                "message": f"Fassungsstand von {label} nicht ermittelbar — Fassung manuell in RIS prüfen."}
    ikd = info["inkrafttretensdatum"]
    if decision_date and ikd > decision_date:
        return {"status": "geaendert", "inkrafttretensdatum": ikd, "idf": info.get("idf"),
                "message": (f"⚠️  {label}: geltende Fassung in Kraft seit {ikd} ({info.get('idf')}) — "
                            f"also NACH der Entscheidung vom {decision_date}. "
                            "Die Entscheidung kann überholt sein; Leitsatz an der geltenden Fassung prüfen.")}
    if decision_date:
        return {"status": "aktuell", "inkrafttretensdatum": ikd, "idf": info.get("idf"),
                "message": f"✓  {label}: Fassung seit der Entscheidung ({decision_date}) unverändert (in Kraft seit {ikd})."}
    return {"status": "info", "inkrafttretensdatum": ikd, "idf": info.get("idf"),
            "message": f"ℹ️  {label}: geltende Fassung in Kraft seit {ikd} ({info.get('idf')})."}


def linie(suchworte: str, gericht: str = "OGH", von: str | None = None,
          norm_gesetz: str | None = None, norm_paragraf: str | None = None,
          size: str = "Ten", max_lines: int = 8) -> dict:
    """Doktrinäre Linie zu einem Thema: OGH-Rechtssätze nach Linientiefe sortiert,
    je mit dem vom Gericht formulierten Leitsatz, plus Fassungsstand der Norm.
    ROHMATERIAL für eine Synthese — die Bewertung bleibt anwaltliche Aufgabe."""
    res = search_judikatur(suchworte=suchworte, gericht=gericht, von=von, size=size)
    rss = [r for r in res["results"] if r.get("rs_number")]
    rss.sort(key=lambda r: len(r["gz_list"]), reverse=True)
    linien = []
    for r in rss[:max_lines]:
        ls = rechtssatz_leitsatz(r["doc_id"])
        linien.append({
            "rs": r["rs_number"],
            "leitsatz": ls.get("leitsatz"),
            "norm": ls.get("norm"),
            "stamm_gz": r["leading_gz"],
            "stamm_datum": r["entscheidungsdatum"],
            "linientiefe": len(r["gz_list"]),
            "permalink": r["dokument_url"],
        })
    fassung = (norm_inkrafttreten(norm_gesetz, norm_paragraf)
               if (norm_gesetz and norm_paragraf) else None)
    return {"suchworte": suchworte, "total": res["total"], "linien": linien, "norm_fassung": fassung}


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

    p_linie = sub.add_parser("linie", help="Doktrinäre Linie: OGH-Leitsätze nach Linientiefe + Fassungsstand")
    p_linie.add_argument("suchworte")
    p_linie.add_argument("--gericht", default="OGH")
    p_linie.add_argument("--von", default=None)
    p_linie.add_argument("--gesetz", default=None, help="Norm für Fassungsstand, z.B. ABGB")
    p_linie.add_argument("--paragraf", default=None)
    p_linie.add_argument("--size", default="Ten", choices=VALID_PAGE_SIZES)

    p_leit = sub.add_parser("leit", help="Leitentscheidungs-Signal für eine Geschäftszahl")
    p_leit.add_argument("gz")

    p_akt = sub.add_parser("aktualitaet", help="Fassungsstand eines Paragrafen (optional relativ zu einem Entscheidungsdatum)")
    p_akt.add_argument("gesetz")
    p_akt.add_argument("paragraf")
    p_akt.add_argument("--seit", default=None, help="Entscheidungsdatum YYYY-MM-DD: flaggt Änderung danach")

    p_vt = sub.add_parser("volltext", help="Volltext einer Entscheidung/Rechtssatzes (GZ oder Dokumentnummer)")
    p_vt.add_argument("gz_oder_doknr")
    p_vt.add_argument("--chars", type=int, default=3000)

    args = parser.parse_args(argv)

    if args.cmd == "smoke":
        return smoke()

    if args.cmd == "leit":
        info = leitentscheidung(args.gz)
        print(f"Geschäftszahl {args.gz}: "
              f"{'LEITENTSCHEIDUNG (Stamm einer Rechtssatz-Linie)' if info['ist_leitentscheidung'] else 'Folgeentscheidung'}")
        for e in info["stamm_von"]:
            print(f"  ★ Stamm von RIS-Justiz {e['rs']}  ({e['linientiefe']} Entscheidungen in der Linie)")
        for e in info["folgt_linie"]:
            print(f"  · folgt Linie {e['rs']} (Stamm {e['stamm_gz']}, {e['linientiefe']} Entscheidungen)")
        print(f"  größte Linientiefe: {info['max_linientiefe']}")
        return 0

    if args.cmd == "aktualitaet":
        print(currency_flag(args.gesetz, args.paragraf, args.seit)["message"])
        return 0

    if args.cmd == "volltext":
        arg = args.gz_oder_doknr
        doknr = arg if arg.startswith(("JJR_", "JJT_")) else stamm_entscheidung_doknr(arg)
        if not doknr:
            print("Kein Stamm-Entscheidungstext zur GZ gefunden. RIS-Web-Suche:")
            print(f"{RIS_WEB}Ergebnis.wxe?Abfrage=Justiz&Suchworte={urllib.parse.quote(arg)}")
            return 1
        text = get_document_text(doknr)
        if not text:
            print("Dokument nicht abrufbar:", doknr)
            return 1
        print(f"# {doknr}\n")
        print(text[:args.chars] + (" …" if len(text) > args.chars else ""))
        return 0

    if args.cmd == "linie":
        data = linie(args.suchworte, gericht=args.gericht, von=args.von,
                     norm_gesetz=args.gesetz, norm_paragraf=args.paragraf, size=args.size)
        print(f'# Linie zu „{data["suchworte"]}"  ({data["total"]} Treffer; OGH-Rechtssätze nach Linientiefe)\n')
        for ln in data["linien"]:
            print(f"RIS-Justiz {ln['rs']}  ·  {ln['linientiefe']} Entscheidungen  ·  Stamm {ln['stamm_gz']} ({ln['stamm_datum']})")
            if ln.get("norm"):
                print(f"   Norm: {ln['norm']}")
            if ln.get("leitsatz"):
                print(f"   Leitsatz: {ln['leitsatz'][:400]}")
            print(f"   {ln['permalink']}")
        nf = data.get("norm_fassung")
        if nf:
            print(f"\nFassungsstand {nf['paragraf']}: in Kraft seit {nf['inkrafttretensdatum']} ({nf.get('idf')}).")
            print("→ Leitsätze mit Stamm-Datum VOR diesem Datum auf die geltende Fassung prüfen.")
        print("\nHinweis: Rohmaterial (Gerichts-Leitsätze), keine geprüfte Doktrin. Synthese/Bewertung bleibt anwaltliche Aufgabe.")
        return 0

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
