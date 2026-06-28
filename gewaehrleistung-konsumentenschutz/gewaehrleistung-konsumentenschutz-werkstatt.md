# Gewährleistung/Konsumentenschutz — Werkstatt

> Ausführliche Fassung für die Arbeit im Plugin. Ergänzt die Skills unter `skills/` und die geteilten `references/`. Österreichisches Recht; jede Fundstelle über RIS (`tools/ris_client.py`) verifizieren.

## Zweck und Abgrenzung

Dieses Plugin ist die **Pilot-Vertikale** des Repositorys und bewusst eng geschnitten: **Gewährleistung bei Waren** (Kauf beweglicher Sachen). Es übt die Kernkompetenz **Regimewahl** (VGG als lex specialis vs. allgemeines ABGB-Recht), die nur das österreichische Recht in dieser Form kennt.

**Nicht abgedeckt** (nur verweisen): Werkverträge, Liegenschaften/WEG, Miete (MRG), das fernabsatzrechtliche Rücktrittsrecht (FAGG), Produkthaftung (PHG), Garantie (vertraglich, neben der gesetzlichen Gewährleistung).

## Pipeline der Skills

```
einstieg-gewaehrleistung   (Triage-Dashboard)
        |
        v
regimewahl-vgg-vs-abgb     (VGG oder §§ 922 ff ABGB?  -> steuert alles Weitere)
        |
        v
mangel-und-vermutung       (Mangel +? bei Übergabe?  Vermutung 6 Mon./1 J.)
        |
        v
behelfshierarchie          (Stufe 1 Verbesserung/Austausch -> Stufe 2 Preisminderung/Wandlung)
        |
        v
verjaehrung-und-fristen    (§ 933 ABGB 2/3 J. / § 10 VGG; Fristbeginn = Übergabe)

anschluss-routing          (Router; wählt aus den obigen Skills)
```

## Die drei Regime-/Fristen-Fallen (Merkblatt)

1. **VGG übersehen.** B2C-Warenkauf ab 1.1.2022 → VGG, nicht § 932 ABGB. Reine Alt-Judikatur zu § 932 nicht ungeprüft übertragen.
2. **Vermutungsfrist ≠ Gewährleistungsfrist.** Vermutung (§ 924 ABGB 6 Mon. / § 11 VGG 1 J.) betrifft nur die Beweislast für den Übergabezeitpunkt; die Frist zur Geltendmachung ist § 933 ABGB (2/3 J.) bzw. § 10 VGG.
3. **Fristbeginn = Übergabe**, nicht Kauf-/Rechnungsdatum.

## Quellenanbindung (verpflichtend)

- Normen über RIS-Permalink belegen: `python3 tools/ris_client.py norm ABGB 932` bzw. `norm VGG 12`.
- Judikatur live holen: `python3 tools/ris_client.py judikatur "Verbesserung Gewährleistung" --gericht OGH`.
- **Keine** Geschäftszahl/RS-Nummer aus Modellwissen. RIS liefert Primärrecht, keine Lehrmeinung — dogmatische Richtigkeit bleibt anwaltliche Aufgabe (`references/ris-quellen.md`).

## Verifikation des Piloten

Die Test-Akte `testakten/geschirrspueler-mangel/` ist der Regressionsfall: Sie muss die korrekte Regimezuordnung (VGG) und durchgängig RIS-auflösbare Fundstellen produzieren. Vor jeder Änderung am Plugin gegen diese Akte gegenprüfen.

## Output

Dashboard nach `references/dashboard-template.md` und `references/anwalts-dashboard-konvention.md`. Ausgaben (HTML) in
`~/.claude/plugins/config/claude-fuer-oesterreichisches-recht/gewaehrleistung-konsumentenschutz/ausgaben/`.

## Berufsrechtlicher Rahmen

§ 9 RAO (Verschwiegenheit), DSGVO/DSG: Mandantendaten nur in rechtskonformer Umgebung verarbeiten. Output ist anwaltliche Vorbereitung, nie Entscheidung.
