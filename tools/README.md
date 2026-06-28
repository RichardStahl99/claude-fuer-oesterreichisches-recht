# tools/

## `ris_client.py`

Abhängigkeitsfreier Python-Client (nur Standardbibliothek) für die **RIS-Open-Data-API**
(`data.bka.gv.at/ris/api/v2.6/`). Löst österreichische Normen und Judikatur verifizierbar auf,
damit Skills keine Geschäftszahlen, Rechtssatznummern oder Paragrafen erfinden.

Vollständige Beschreibung des API-Verhaltens und des Grounding-Protokolls:
**`references/ris-quellen.md`**.

### CLI

```bash
# Norm-Permalink bauen und HTTP-Status prüfen
python3 tools/ris_client.py norm ABGB 932

# OGH-Judikatur ab 2022 zu Stichworten (ausländische Organe werden gefiltert)
python3 tools/ris_client.py judikatur "Gewährleistung Verbesserung" --gericht OGH --von 2022-01-01

# Roh-JSON (geparst/normalisiert)
python3 tools/ris_client.py judikatur "laesio enormis" --gericht OGH --json

# Phase-1-Grounding-Smoke-Test: Norm (§ 932 ABGB) + Judikatur, je HTTP-200-geprüft
python3 tools/ris_client.py smoke
```

### Als Modul

```python
from tools.ris_client import search_judikatur, norm_permalink, format_citation, http_status

res = search_judikatur(suchworte="Behelfshierarchie", gericht="OGH", von="2022-01-01")
for r in res["results"]:
    print(format_citation(r), "->", r["dokument_url"])
```

### Wichtige Eigenschaften

- Parst das **verschachtelte** OGD-Schema korrekt (`Organ` unter `Technisch`, `DokumentUrl` unter `Allgemein`).
- **Dedupliziert** die semikolon-getrennte Geschäftszahl-Liste eines Rechtssatzes und **normalisiert** die Schreibweise (`6Ob158/22m` → `6 Ob 158/22m`).
- **Filtert ausländische Organe** (`AUSL`, `EGMR`, `EUGH`) bei OGH-Recherche heraus.
- Behandelt 0-Treffer- und Fehler-Envelopes ohne Absturz.
- Erweiterung um weitere Gesetze: Gesetzesnummer **über RIS verifizieren** (Permalink HTTP 200) und in `GESETZESNUMMER` eintragen — nie raten.

### Grenze

RIS liefert **Primärrecht**, keine Lehrmeinung. Der Client fängt erfundene Fundstellen und tote Links —
**nicht** dogmatische Fehlinterpretation. Fachliche Richtigkeit bleibt anwaltliche Aufgabe.
