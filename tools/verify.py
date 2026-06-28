#!/usr/bin/env python3
"""
verify.py — CI-Link-Rot- und Integritätsprüfung für das at-law-Repository.

Zweck: In CI (GitHub Action) sicherstellen, dass die in diesem Repository
zitierten österreichischen Primärquellen **weiterhin auflösbar** sind und die
strukturellen Grundlagen unversehrt bleiben. Anders als `ris_client.py` (das
Quellen abruft) prüft `verify.py` *bestehende* Inhalte gegen die Realität:

  (a) Es sammelt alle Markdown-Dateien unter den Plugin-Verzeichnissen,
      `references/` und `testakten/` ein.
  (b) Es extrahiert Norm-Zitate ("§ 932 ABGB", "§ 16 Abs 8 MRG", "§§ 12 f VGG",
      "§ 105 ArbVG" …) per Regex, matcht die Gesetzes-Abkürzung gegen die in
      `ris_client.GESETZESNUMMER` bekannten Schlüssel, baut für jedes eindeutige
      (Gesetz, Paragraf) den RIS-Permalink (`norm_permalink`) und prüft den
      HTTP-Status (`http_status`). Jeder Status ≠ 200 ist Link-Rot.
  (c) Es zählt RS-Rechtssatznummern (RS\\d{7}); Auflösung optional.
  (d) Es validiert das JSON von `.claude-plugin/marketplace.json` und jedem
      `*/.claude-plugin/plugin.json`.
  (e) Es lässt den RIS-Grounding-Smoke-Test laufen (`ris_client.smoke`).
  (f) Es prüft die Integrität der geschützten Grundlagen
      (`references/zitierweise.md`, `references/methodik-buergerliches-recht.md`)
      via sha256 gegen eingebettete Baseline-Werte.
  (g) Es liefert Exit-Code ≠ 0 bei ungelöstem Permalink, JSON-Fehler,
      Smoke-Fehler oder Foundation-Abweichung und druckt eine klare
      Zusammenfassung.

Abhängigkeitsfrei: nur Standardbibliothek; `from ris_client import …` ist
erlaubt, da `ris_client.py` im selben Verzeichnis liegt.

Aufruf:
    python tools/verify.py                 # volle Prüfung (CI-Standard)
    python tools/verify.py tools mietzins-mrg   # nur diese Wurzeln scannen (Stichprobe)
    python tools/verify.py --no-smoke      # Smoke überspringen
    python tools/verify.py --no-net        # offline (keine Permalink-/Smoke-Netzcalls)
    python tools/verify.py --foundations-warn-only   # Foundation-Abweichung nur warnen
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

# ris_client liegt im selben Verzeichnis — direkter Import ist gewollt.
import ris_client

# --------------------------------------------------------------------------- #
# Pfade
# --------------------------------------------------------------------------- #
TOOLS_DIR = Path(__file__).resolve().parent
REPO_ROOT = TOOLS_DIR.parent

# --------------------------------------------------------------------------- #
# Geschützte Grundlagen — sha256-Baselines (JETZT aus den Dateien berechnet).
# Bei einer absichtlichen Änderung dieser Dateien müssen die Werte hier bewusst
# nachgezogen werden: `shasum -a 256 references/zitierweise.md ...`. Genau diese
# Reibung ist gewollt (Tripwire gegen unbemerkte Drift der Fundamente).
# --------------------------------------------------------------------------- #
FOUNDATION_BASELINES = {
    "references/zitierweise.md":
        "a3ed363300df58f2bead06f0b32ea1bf5520c7b1af0d19bb9c3980022f6253d4",
    "references/methodik-buergerliches-recht.md":
        "dbfa6490b5ab0293090752e14eaf170700fbc15229c3a35be208a9b247aa2d63",
}

# --------------------------------------------------------------------------- #
# Norm-Zitat-Erkennung
#
# Die Gesetzes-Alternative wird aus den in ris_client bekannten Schlüsseln
# gebaut — so prüfen wir genau die Gesetze, die wir auch auflösen können.
# Längste zuerst, damit kein Präfix einen längeren Schlüssel verdeckt.
# IGNORECASE deckt die übliche Mischschreibung ab (AngG↔ANGG, ArbVG↔ARBVG,
# RichtWG↔RICHTWG, UrlG↔URLG).
# --------------------------------------------------------------------------- #
_LAW_ALT = "|".join(sorted(ris_client.GESETZESNUMMER, key=len, reverse=True))

# Optionale Paragrafen-Zusätze zwischen Paragrafennummer und Gesetz:
#   "Abs 8", "Z 2a", "lit a", "Satz 1", "ff", "f" …
# Wichtig: Wert-Zusätze sind ziffern-geführt ([0-9]+[a-z]?), damit der greedy
# Buchstaben-Teil nicht den ersten Buchstaben des Gesetzes ("VGG") verschluckt.
_VALUE_KW = r"(?:Abs|Z|Zif|Ziff|Satz|Halbsatz|HS|Fall|Anm)"
_QUALIFIER = (
    r"(?:"
    r"\s+ff?\b"                                       # "f" / "ff" (folgende)
    r"|\s+" + _VALUE_KW + r"\.?\s*[0-9]+[a-z]?"       # "Abs 8", "Z 2a", "Satz 1"
    r"|\s+lit\.?\s*[a-z]\b"                           # "lit a"
    r")"
)
NORM_RE = re.compile(
    r"§§?\s*"                       # § oder §§
    r"(\d+[a-z]?)"                  # Gruppe 1: Paragraf (z.B. 932, 933a, 1159)
    + _QUALIFIER + r"*"            # beliebig viele optionale Zusätze
    r"\s+(" + _LAW_ALT + r")\b",   # Gruppe 2: Gesetzes-Abkürzung (bekannter Schlüssel)
    re.IGNORECASE,
)

# RS-Rechtssatznummer, exakt 7 Ziffern (z.B. RS0018547).
RS_RE = re.compile(r"\bRS\d{7}\b")

# Fremdrechts-Marker direkt NACH einem Zitat: die Skills nennen bewusst deutsche
# Normen als Anti-Pattern ("kein § 704 ff ZPO (DE)"). Solche Treffer sind KEINE
# österreichischen Fundstellen und dürfen nicht als Link-Rot gewertet werden.
FOREIGN_AFTER_RE = re.compile(r"\s*\((?:DE|de|dt\.?)\)")


# --------------------------------------------------------------------------- #
# Sammeln & Extrahieren
# --------------------------------------------------------------------------- #
def discover_plugin_dirs() -> list[Path]:
    """Plugin-Verzeichnisse anhand `*/.claude-plugin/plugin.json` autodetektieren
    (das Wurzel-`.claude-plugin/marketplace.json` ist KEIN Plugin)."""
    return sorted({p.parent.parent for p in REPO_ROOT.glob("*/.claude-plugin/plugin.json")})


def default_roots() -> list[Path]:
    """Standard-Scan-Wurzeln: alle Plugin-Verzeichnisse + references/ + testakten/."""
    roots = discover_plugin_dirs()
    for extra in ("references", "testakten"):
        d = REPO_ROOT / extra
        if d.is_dir():
            roots.append(d)
    # nur existierende, dedupliziert, stabile Reihenfolge
    seen, out = set(), []
    for r in roots:
        rp = r.resolve()
        if rp.is_dir() and rp not in seen:
            seen.add(rp)
            out.append(rp)
    return out


def collect_markdown(roots: list[Path]) -> list[Path]:
    """Alle *.md unter den gegebenen Wurzeln einsammeln (rekursiv, .git ausgenommen)."""
    files: list[Path] = []
    for root in roots:
        for md in sorted(root.rglob("*.md")):
            if ".git" in md.parts:
                continue
            files.append(md)
    # Deduplizieren (überlappende Wurzeln)
    seen, out = set(), []
    for f in files:
        rp = f.resolve()
        if rp not in seen:
            seen.add(rp)
            out.append(rp)
    return out


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_norm_citations(text: str) -> set[tuple[str, str]]:
    """(GESETZ_SCHLUESSEL, paragraf) für jedes erkannte Norm-Zitat.
    Der Gesetzes-Schlüssel wird auf die Großschreibung von ris_client normalisiert."""
    out: set[tuple[str, str]] = set()
    for m in NORM_RE.finditer(text):
        # Fremdrechts-Abgrenzungszitate (z.B. "§ 704 ff ZPO (DE)") überspringen:
        # bewusste Anti-Pattern-Hinweise auf deutsches Recht, keine AT-Fundstellen.
        if FOREIGN_AFTER_RE.match(text, m.end()):
            continue
        paragraf = m.group(1)
        gesetz = m.group(2).upper()  # -> kanonischer Schlüssel in GESETZESNUMMER
        out.add((gesetz, paragraf))
    return out


def extract_rs_numbers(text: str) -> set[str]:
    return set(RS_RE.findall(text))


# --------------------------------------------------------------------------- #
# Prüfungen
# --------------------------------------------------------------------------- #
def check_permalinks(citations: set[tuple[str, str]], do_net: bool) -> tuple[int, list]:
    """Für jedes eindeutige (Gesetz, Paragraf) Permalink bauen und HTTP prüfen.
    Gibt (#geprüft, [fehlschläge]) zurück; ein Fehlschlag ist (gesetz, paragraf, url, status)."""
    failures: list = []
    checked = 0
    for gesetz, paragraf in sorted(citations):
        url = ris_client.norm_permalink(gesetz, paragraf)
        if not do_net:
            continue
        status = ris_client.http_status(url)
        checked += 1
        ok = status == 200
        marker = "ok " if ok else "ROT"
        print(f"   [{marker}] § {paragraf} {gesetz}  HTTP {status}")
        if not ok:
            failures.append((gesetz, paragraf, url, status))
    return checked, failures


def validate_json() -> tuple[bool, list]:
    """marketplace.json + jede plugin.json parsen. Gibt (ok, [fehler]) zurück."""
    errors: list = []
    targets: list[Path] = []
    market = REPO_ROOT / ".claude-plugin" / "marketplace.json"
    if market.is_file():
        targets.append(market)
    else:
        errors.append((str(market), "Datei fehlt"))
    targets.extend(sorted(REPO_ROOT.glob("*/.claude-plugin/plugin.json")))

    for path in targets:
        rel = path.relative_to(REPO_ROOT)
        try:
            json.loads(_read(path))
            print(f"   [ok ] {rel}")
        except json.JSONDecodeError as exc:  # noqa: PERF203
            print(f"   [ERR] {rel}: {exc}")
            errors.append((str(rel), str(exc)))
    return (not errors), errors


def run_smoke() -> bool:
    """RIS-Grounding-Smoke-Test (ris_client.smoke) ausführen; True bei Rückgabe 0."""
    try:
        return ris_client.smoke() == 0
    except Exception as exc:  # noqa: BLE001
        print(f"   [FAIL] Smoke-Test warf Ausnahme: {exc}")
        return False


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def check_foundations() -> tuple[bool, list]:
    """sha256 der geschützten Grundlagen gegen die eingebetteten Baselines.
    Gibt (ok, [abweichungen]) zurück; Abweichung = (rel, erwartet, ist)."""
    deviations: list = []
    for rel, expected in FOUNDATION_BASELINES.items():
        path = REPO_ROOT / rel
        if not path.is_file():
            print(f"   [FAIL] {rel}: Datei fehlt")
            deviations.append((rel, expected, "<fehlt>"))
            continue
        actual = _sha256(path)
        if actual == expected:
            print(f"   [ok ] {rel}")
        else:
            print(f"   [DEV] {rel}")
            print(f"          erwartet: {expected}")
            print(f"          ist:      {actual}")
            deviations.append((rel, expected, actual))
    return (not deviations), deviations


# --------------------------------------------------------------------------- #
# Hauptlauf
# --------------------------------------------------------------------------- #
def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="CI-Link-Rot- und Integritätsprüfung für at-law."
    )
    parser.add_argument(
        "roots", nargs="*",
        help="Optionale Scan-Wurzeln (Default: Plugin-Dirs + references/ + testakten/).",
    )
    parser.add_argument("--no-smoke", action="store_true", help="Smoke-Test überspringen.")
    parser.add_argument("--no-net", action="store_true",
                        help="Offline: keine Permalink-/Smoke-Netzwerkprüfung.")
    parser.add_argument("--foundations-warn-only", action="store_true",
                        help="Foundation-Abweichung nur warnen (Exit-Code 0).")
    args = parser.parse_args(argv)

    do_net = not args.no_net
    do_smoke = do_net and not args.no_smoke

    # Wurzeln bestimmen
    if args.roots:
        roots = []
        for raw in args.roots:
            p = Path(raw)
            if not p.is_absolute():
                p = (REPO_ROOT / raw).resolve() if (REPO_ROOT / raw).exists() else p.resolve()
            roots.append(p)
    else:
        roots = default_roots()

    print("at-law verify — Link-Rot & Integrität")
    print("=" * 60)
    print("Repo-Wurzel:", REPO_ROOT)
    print("Scan-Wurzeln:")
    for r in roots:
        print("   ·", r)

    # (a) Markdown sammeln
    md_files = collect_markdown(roots)
    print(f"\n[1] Markdown-Dateien gesammelt: {len(md_files)}")

    # (b/c) Zitate + RS-Nummern extrahieren
    citations: set[tuple[str, str]] = set()
    rs_numbers: set[str] = set()
    for md in md_files:
        text = _read(md)
        citations |= extract_norm_citations(text)
        rs_numbers |= extract_rs_numbers(text)
    print(f"[2] Eindeutige Norm-Zitate (bekanntes Gesetz): {len(citations)}")
    print(f"[3] Eindeutige RS-Nummern (Auflösung optional): {len(rs_numbers)}")

    # (b) Permalinks prüfen
    print(f"\n[4] Permalink-Prüfung ({'live' if do_net else 'übersprungen — offline'}):")
    checked, link_failures = check_permalinks(citations, do_net)

    # (d) JSON validieren
    print("\n[5] JSON-Validierung:")
    json_ok, json_errors = validate_json()

    # (e) Smoke
    print("\n[6] RIS-Grounding-Smoke-Test:")
    if do_smoke:
        smoke_ok = run_smoke()
    else:
        smoke_ok = True
        print("   [skip] übersprungen (--no-smoke/--no-net).")

    # (f) Foundations
    print("\n[7] Integrität geschützter Grundlagen (sha256):")
    foundations_ok, foundation_dev = check_foundations()

    # ------------------------------------------------------------------ #
    # (g) Zusammenfassung + Exit-Code
    # ------------------------------------------------------------------ #
    print("\n" + "=" * 60)
    print("ZUSAMMENFASSUNG")
    print("-" * 60)
    print(f"Markdown-Dateien gescannt : {len(md_files)}")
    print(f"Norm-Zitate (eindeutig)   : {len(citations)}")
    print(f"Permalinks geprüft        : {checked}")
    print(f"Permalinks fehlgeschlagen : {len(link_failures)}")
    for gesetz, paragraf, url, status in link_failures:
        print(f"    ✗ § {paragraf} {gesetz}  HTTP {status}  {url}")
    print(f"RS-Nummern gefunden       : {len(rs_numbers)}")
    print(f"JSON                      : {'ok' if json_ok else 'FEHLERHAFT'}")
    for rel, msg in json_errors:
        print(f"    ✗ {rel}: {msg}")
    if do_smoke:
        print(f"Smoke                     : {'ok' if smoke_ok else 'FEHLGESCHLAGEN'}")
    else:
        print("Smoke                     : übersprungen")
    print(f"Foundations               : {'ok' if foundations_ok else 'ABWEICHUNG'}")
    for rel, _exp, _act in foundation_dev:
        print(f"    ✗ {rel}: sha256 weicht von Baseline ab")

    # Exit-Code-Logik (g): Permalink-Rot ODER JSON-Fehler ODER Smoke-Fehler
    # ODER (sofern nicht warn-only) Foundation-Abweichung -> ≠ 0.
    foundations_fatal = (not foundations_ok) and (not args.foundations_warn_only)
    if (not foundations_ok) and args.foundations_warn_only:
        print("\nWARN: Foundation-Abweichung (nur Warnung wegen --foundations-warn-only).")

    failed = bool(link_failures) or (not json_ok) or (not smoke_ok) or foundations_fatal
    print("\nERGEBNIS:", "FEHLGESCHLAGEN ✗" if failed else "BESTANDEN ✓")
    print("=" * 60)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
