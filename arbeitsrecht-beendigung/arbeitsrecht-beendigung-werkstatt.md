# Arbeitsrecht (Beendigung) — Werkstatt

> Ausführliche Fassung für die Arbeit im Plugin. Ergänzt die Skills unter `skills/` und die geteilten `references/`. Österreichisches Recht; jede Fundstelle und jeden KV-/Betragswert über RIS (`tools/ris_client.py`) verifizieren.

## Zweck und Abgrenzung

Vierte **Pilot-Vertikale**: **Beendigung des Arbeitsverhältnisses**. Gewählt, weil hier die **Divergenz zu Deutschland am größten** ist: kein einheitliches KSchG, sondern AngG + ABGB (§ 1159) + **ArbVG § 105** (Anfechtung, Betriebsrat) + Verfahren vor dem **ASG**. Headline-Kompetenz ist die **Beendigungsart**.

**Nicht abgedeckt** (nur verweisen): laufendes Arbeitsverhältnis (Entgelt, AZG-Arbeitszeit, Urlaub im Detail), Gleichbehandlung (GlBG), Betriebsübergang (AVRAG), Sozialversicherung, besonderer Kündigungsschutz im Detail (MSchG/VKG/BEinstG).

## Pipeline der Skills

```
einstieg-arbeitsrecht              (Triage; bei AG-Kündigung sofort 2-Wochen-Frist markieren)
        |
        v
beendigungsart                     (Kündigung / Entlassung / einvernehmlich / Zeitablauf / Austritt)
        |
        |-- Kündigung --> kuendigungsfristen-termine (§20 AngG / §1159 ABGB, Quartalstermin)
        |-- Kündigung --> kuendigungsschutz-anfechtung (§105 ArbVG: BR, Grund, 2-Wochen-Frist, ASG)
        v
beendigungsansprueche              (Abfertigung neu/alt, Urlaubsersatz §10 UrlG, Kündigungsentschädigung §29 AngG)

anschluss-routing                  (Router)
```

## Vier Merkpunkte (häufige Fehlerorte)

1. **Keine Begründungspflicht der Kündigung — aber Anfechtung.** Schutz wirkt über § 105 ArbVG, nicht über ein KSchG.
2. **2-Wochen-Anfechtungsfrist (§ 105 Abs 4 ArbVG)** ist der fatale Punkt — zuerst sichern; sie hängt am Betriebsrats-Vorverfahren.
3. **Frist UND Termin (Quartalsende, § 20 AngG)** müssen stimmen; Arbeiter seit 1.10.2021 angeglichen (§ 1159 ABGB).
4. **Abfertigung neu vs. alt** nach Stichtag 1.1.2003; KV-**Verfallsfristen** für Ansprüche.

## Quellenanbindung (verpflichtend)

- Normen über RIS-Permalink: `python3 tools/ris_client.py norm ANGG 20` (AngG wird mit Artikel-1-Adressierung aufgelöst), `norm ARBVG 105`, `norm BMSVG 14`.
- Judikatur live: `python3 tools/ris_client.py judikatur "Kündigungsanfechtung Sozialwidrigkeit" --gericht OGH` (Arbeitsrecht = **ObA-Senat**).
- **KV-Inhalte, Beträge, Verfallsfristen** stets live — nie aus Modellwissen.
- Keine GZ/RS-Nummer aus Modellwissen (`references/ris-quellen.md`).

## Architektur (Phase-3-Muster)

Nutzt `references/zitierweise.md` und `references/methodik-buergerliches-recht.md` **unverändert**; `tools/ris_client.py` erhielt die verifizierten Gesetzesnummern AngG (10008069, Artikel-1-Adressierung), ArbVG (10008329), BMSVG (20002088), ASGG (10000813), UrlG (10008376).

## Verifikation

Regressionsfall `testakten/kuendigung-angestellte-anfechtung/`: muss Beendigungsart/Anfechtbarkeit korrekt zuordnen und ausschließlich RIS-auflösbare Fundstellen liefern.

## Berufsrechtlicher Rahmen

§ 9 RAO (Verschwiegenheit), DSGVO/DSG. In Arbeits- und Sozialrechtssachen erster Instanz besteht **keine** absolute Anwaltspflicht (qualifizierte Vertretung, z. B. durch AK/Gewerkschaft, möglich). Output ist anwaltliche Vorbereitung, nie Entscheidung.
