# RIS — Quellenanbindung und Grounding-Protokoll

> Diese Datei beschreibt, **wie** österreichische Primärquellen verifiziert werden. Sie ist die Daten-Grundlage hinter `references/zitierweise.md`. Tooling: `tools/ris_client.py`.

## 1. Was ist RIS?

**RIS — Rechtsinformationssystem des Bundes** (`https://www.ris.bka.gv.at`) ist die amtliche, **kostenlose** Rechtsdatenbank Österreichs. Sie ersetzt funktional, was im deutschen Repository `gesetze-im-internet.de` + `rechtsprechung-im-internet.de` leisten — deckt aber zusätzlich Landesrecht und nahezu die gesamte Höchstgerichts-Judikatur ab.

Abdeckung u. a.: **Bundesrecht konsolidiert**, **Landesrecht**, **Judikatur** (OGH, OLG, LG; VwGH, VfGH, BVwG, LVwG; teils EGMR/EuGH-Verweise), Erlässe, BGBl.

**Wichtig — Grenze:** RIS enthält **Primärrecht** (Normtext + Entscheidungen), **keine Lehrmeinung**. Dogmatik/Kommentierung liegt in kostenpflichtigen Werken (rdb.at/Manz, LexisNexis, Linde). RIS-Grounding beweist daher, dass eine **Fundstelle existiert und einschlägig ist** — es ersetzt **nicht** die fachliche Richtigkeitsprüfung der Doktrin. Für diese bleibt der Anwalt zuständig (siehe Driver-Seat-Prinzip).

## 2. OGD-API (maschinell)

Offene Schnittstelle, **kein API-Key**, JSON oder XML:

```
Basis:  https://data.bka.gv.at/ris/api/v2.6/
```

(Version 2.6 verwenden — `v2.5` antwortet mit 404.) Kein veröffentlichtes Rate-Limit: **fair use, aggressiv cachen, Backoff** einbauen; Kontakt bei intensiver Nutzung `ris.it@bka.gv.at`. Die OGD-Nutzungsbedingungen (CC-BY-artig) vor produktiver Nutzung prüfen.

### Verifiziertes Antwortschema (Judikatur)

Die Antwort ist **tief verschachtelt** — nicht flach:

```
OgdSearchResult
└─ OgdDocumentResults
   ├─ Hits            { "@pageNumber", "@pageSize", "#text": <Gesamttreffer> }
   └─ OgdDocumentReference[]        (bei size=Ten bis zu 10)
      └─ Data
         └─ Metadaten
            ├─ Technisch   { ID, Applikation, Organ, ImportTimestamp }
            ├─ Allgemein   { Veroeffentlicht, Geaendert, DokumentUrl }
            └─ Judikatur   { Dokumenttyp, Geschaeftszahl{item}, Normen,
                             Entscheidungsdatum, EuropeanCaseLawIdentifier, Justiz }
```

**Fallstricke (alle empirisch bestätigt):**

1. **`Organ` steht unter `Technisch`**, nicht unter `Judikatur`. Werte wie `"OGH"` oder `"OGH; AUSL EGMR"` — bei reiner OGH-Recherche ausländische/überstaatliche Organe (`AUSL`, `EGMR`, `EUGH`) **herausfiltern**.
2. **Standardtreffer sind Rechtssätze** (Dokument-ID `JJR_…`, ECLI `…:RSxxxxxxx`). Bei einem Rechtssatz ist `Geschaeftszahl.item` eine **mit Semikolon getrennte Liste** *aller* bestätigenden Entscheidungen (oft 30+). Die **führende** GZ (erste der Liste) ist die Leitentscheidung; das `Entscheidungsdatum` ist das der **jüngsten** Bestätigung.
3. **`DokumentUrl`** (unter `Allgemein`) ist der zitierfähige Permalink.
4. **Gültige `DokumenteProSeite`-Werte:** `Ten`, `Twenty`, `Fifty`, `OneHundred` (alles andere → `OgdSearchResult.Error`).
5. **0 Treffer:** `OgdSearchResult` ohne `OgdDocumentResults` (kein Absturz — abfangen). Ungültige Parameter: `OgdSearchResult.Error{Applikation, Message}`.
6. **Strukturierte Norm-Filterung (`Norm=`) ist unzuverlässig.** Robuster ist Volltext (`Suchworte=`); jeden Norm-Treffer am Text gegenprüfen.

### Norm-Permalinks

```
https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=<GNR>&Paragraf=<§>
```

Gesetzesnummern (`GNR`) sind RIS-intern und **werden nie geraten**, sondern verifiziert. Verifiziert: **ABGB = 10001622** (`§ 932` → HTTP 200). Weitere Gesetze beim ersten Gebrauch über RIS auflösen und in `tools/ris_client.py` (`GESETZESNUMMER`) eintragen.

## 3. Grounding-Protokoll für Skills

Jeder Skill, der eine österreichische Rechtsaussage trifft, **führt diese Schritte zur Laufzeit aus** (nicht nur darauf verweisen) — und gibt nur aus, was die Tools live liefern:

1. **Norm zuerst.** Einschlägige(n) Paragrafen bestimmen; Permalink über `norm` / `ris_client.norm_permalink(...)` bilden, Existenz (HTTP 200) belegen.
2. **Linie holen.** `python3 tools/ris_client.py linie "<Stichworte>" --gericht OGH [--gesetz <G> --paragraf <§>]` — liefert die OGH-Rechtssätze nach Linientiefe mit den vom Gericht formulierten **Leitsätzen** (Rohmaterial der Doktrin) und dem Fassungsstand. Nur die so gelieferten RS-Nummern/GZ/Leitsätze verwenden.
3. **Gewicht prüfen.** Für eine konkret herangezogene Geschäftszahl `leit <GZ>` aufrufen: Ist sie **Leitentscheidung** (Stamm) und wie tief ist die Linie? Eine isolierte Einzelentscheidung anders gewichten als gefestigte stRsp.
4. **Aktualität prüfen (Pflicht bei älteren Entscheidungen).** `aktualitaet <Gesetz> <§> --seit <Entscheidungsdatum>` — wurde die Norm **nach** der Entscheidung geändert (⚠️)? Dann nicht unbesehen übertragen (z. B. VGG ab 1.1.2022 vs. Alt-Judikatur zu § 932 ABGB).
5. **Formatieren** nach `references/zitierweise.md` (`format_citation(...)`); **Unsicheres als Prüfpunkt** ausweisen. Leitsätze sind Rohmaterial, keine geprüfte Doktrin — Bewertung bleibt anwaltliche Aufgabe.

## 4. CLI

```bash
# Norm-Permalink bauen und prüfen
python3 tools/ris_client.py norm ABGB 932

# OGH-Judikatur ab 2022 zu Stichworten
python3 tools/ris_client.py judikatur "Gewährleistung Verbesserung" --gericht OGH --von 2022-01-01

# Phase-1-Grounding-Smoke-Test (Norm + Judikatur, je HTTP-200-geprüft)
python3 tools/ris_client.py smoke
```

Als Modul: `from tools.ris_client import search_judikatur, norm_permalink, format_citation`.

## 5. Was RIS-Grounding leistet — und was nicht

- **Fängt:** erfundene Geschäftszahlen, RS-Nummern, nicht existierende Paragrafen, tote Permalinks; **Gesetzesänderungen nach dem Entscheidungsdatum** (Aktualitäts-Flag, s. u. Abschnitt 6).
- **Fängt nicht:** dogmatische Fehlinterpretation einer real existierenden Entscheidung; ob eine erkannte Gesetzesänderung die Aussage *inhaltlich* überholt (geflaggt wird die Änderung, nicht ihre Tragweite); akademischer Lehrstreit. Dafür braucht es Kommentarliteratur und/oder anwaltliche Prüfung. Ein bekanntes Test-Set mit *bekannten richtigen Antworten* (Regressionsfälle) ergänzt die reine Linkprüfung.

## 6. Linie, Leitentscheidung, Aktualität, Volltext

Über die reine Permalink-Prüfung hinaus liefert `tools/ris_client.py` strukturiertes **Rohmaterial** für eine (anwaltlich zu verantwortende) Synthese:

- **`linie "<Stichworte>" [--gesetz ABGB --paragraf 932]`** — OGH-Rechtssätze zum Thema, sortiert nach **Linientiefe** (Anzahl Entscheidungen in der Linie), je mit dem **vom Gericht formulierten Leitsatz** (die frei verfügbare Doktrin) und dem **Fassungsstand** der Norm.
- **`leit <Geschäftszahl>`** — Leitentscheidungs-Signal: Ist die GZ **Stamm** (führende GZ) eines Rechtssatzes, hat sie die Linie **begründet** (Leitentscheidung). Die Linientiefe misst, wie gefestigt sie ist (z. B. RS0039018: 157 Entscheidungen = gefestigte ständige Rechtsprechung).
- **`aktualitaet <Gesetz> <§> [--seit JJJJ-MM-TT]`** — Fassungsstand: seit wann die geltende Fassung in Kraft ist (Inkrafttretensdatum + änderndes BGBl). Mit `--seit <Entscheidungsdatum>` wird **geflaggt**, ob der Paragraf **nach** der Entscheidung geändert wurde (⚠️ ggf. überholt). Erkennt die Änderung, beurteilt sie **nicht**.
- **`volltext <GZ|Dokumentnummer>`** — Volltext einer Entscheidung (Begründung) bzw. eines Rechtssatzes.

**Doktrin ohne Kommentar — was geht (frei, verifizierbar):** die vom OGH selbst formulierten **Leitsätze** (Rechtssätze) und die **Begründungen** der Entscheidungen sind kostenlos und zitierfähig; sie geben die *gerichtliche* Sicht der gefestigten Linie. **Was nicht geht:** der akademische Meinungsstreit (Lehre) lebt in kostenpflichtigen Kommentaren und ist nicht in RIS. Eine `linie`-Ausgabe ist **Rohmaterial**, keine geprüfte Doktrin — Auswahl, Gewichtung und Bewertung bleiben anwaltliche Aufgabe.
