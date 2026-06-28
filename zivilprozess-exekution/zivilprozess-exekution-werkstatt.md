# Zivilprozess / Exekution — Werkstatt

> Ausführliche Fassung für die Arbeit im Plugin. Ergänzt die Skills unter `skills/` und die geteilten `references/`. Österreichisches Recht; jede Fundstelle und jeden aktuellen Wert (Existenzminimum) über RIS (`tools/ris_client.py`) verifizieren.

## Zweck und Abgrenzung

Dritte **Pilot-Vertikale**: **Forderungsdurchsetzung** im streitigen Zivilverfahren samt Exekution. Headline-Kompetenz ist die **Zuständigkeits-Weiche (JN)** — strukturell parallel zur Regimewahl (Gewährleistung) und zum Anwendungsbereich (MRG).

**Nicht abgedeckt** (nur verweisen): Außerstreit (AußStrG), Insolvenz (IO), einstweilige Verfügung/Sicherungsexekution im Detail, Zwangsversteigerung von Liegenschaften, StPO, AVG/VwGVG, grenzüberschreitende Titel (EuGVVO/EuVTVO) im Detail.

## Pipeline der Skills

```
einstieg-zivilverfahren            (Triage; zuerst: Titel vorhanden?)
        |
        |-- Titel (+) -------------------------------> exekution-eo
        v
zustaendigkeit-jn                  (BG/LG, örtlich, Anwaltspflicht § 27 ZPO)
        |
        v
mahnverfahren                      (Zahlungsbefehl ≤ 75.000 €  -> Einspruch § 248 / sonst Titel)
        |
        |-- Einspruch --> verfahrensgang-rechtsmittel (Klage/Säumnis/Neuerungsverbot/Rechtsmittel)
        |-- kein Einspruch -------------------------> exekution-eo
        v
exekution-eo                       (Titel § 1 / Vollstreckbarkeit § 7 / Exekutionsmittel)

anschluss-routing                  (Router)
```

## Vier Merkpunkte (häufige Fehlerorte)

1. **Titel zuerst.** Liegt ein vollstreckbarer Titel vor, ist der Weg die Exekution — kein neuerliches Erkenntnisverfahren.
2. **Zuständigkeit/Anwaltspflicht:** BG ≤ 15.000 € (+ Eigenzuständigkeiten), Anwaltspflicht BG > 5.000 € / LG immer (§ 27 ZPO). Nicht die deutschen Grenzen unterstellen.
3. **Fristen:** Einspruch **4 Wochen** (§ 248), Berufung/Revision **4 Wochen** (§§ 464, 505), Rekurs **14 Tage** (§ 521). **Neuerungsverbot** (§ 482): alles erstinstanzlich.
4. **Exekution:** passendes Mittel zum Vermögen (Fahrnis vs. Gehalt/Forderung); **Existenzminimum** beachten.

## Quellenanbindung (verpflichtend)

- Normen über RIS-Permalink: `python3 tools/ris_client.py norm ZPO 248` bzw. `norm JN 49`, `norm EO 1`.
- Judikatur live: `python3 tools/ris_client.py judikatur "Neuerungsverbot" --gericht OGH`.
- **Existenzminimum/Gebühren** stets live — nie aus Modellwissen beziffern.
- Keine GZ/RS-Nummer aus Modellwissen (`references/ris-quellen.md`).

## Architektur (Phase-3-Muster)

Nutzt `references/zitierweise.md` und `references/methodik-buergerliches-recht.md` **unverändert**; `tools/ris_client.py` erhielt die verifizierten Gesetzesnummern JN (10001697), ZPO (10001699), EO (10001700).

## Verifikation

Regressionsfall `testakten/werklohn-mahnklage-exekution/`: muss Zuständigkeit/Anwaltspflicht korrekt zuordnen und ausschließlich RIS-auflösbare Fundstellen liefern.

## Berufsrechtlicher Rahmen

§ 9 RAO (Verschwiegenheit), DSGVO/DSG; ERV-Pflicht für Anwälte. Output ist anwaltliche Vorbereitung, nie Entscheidung.
