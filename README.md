# Claude für österreichisches Recht

> **Experimentell. Nicht geprüft. Kein Rechtsrat.** Eine Sammlung von Claude-Skills zur Unterstützung anwaltlicher Arbeit im **österreichischen** Recht. Adaptiert die *Arbeitsweise* des deutschen Vorbilds [`Klotzkette/claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht) — der **rechtliche Rahmen** (geltende Gesetze, Gerichte, Verfahrensrecht, Berufsrecht, Zitierweise) ist vollständig auf Österreich neu geschrieben.

## Leitidee: Motor übernehmen, Rechtsschicht neu bauen

Das deutsche Repository ist zweierlei in einem — und nur das Erste lässt sich übernehmen:

- **Wiederverwendbarer Motor (jurisdiktionsneutral):** Plugin-/Marketplace-Gerüst, `SKILL.md`-Format, das Dashboard-Ausgabe-Modul, die juristische *Methode* (Gutachtenstil, Subsumtion, Anspruchsaufbau) und die *Zitierdisziplin* („keine Blindzitate, jede Fundstelle verifizierbar, der Anwalt entscheidet").
- **Jurisdiktionsgebundene Rechtsschicht (neu geschrieben):** Gesetze (ABGB statt BGB, UGB statt HGB, **VGG**, MRG, EO, JN, AußStrG …), Gerichte (OGH/OLG/LG/BG, VwGH, VfGH), Zitierform (Geschäftszahl + **RIS-Justiz**-Rechtssatznummer statt Reporter-Fundstelle), Datenquelle (**RIS** statt gesetze-im-internet.de), das Verfahrensrecht (öZPO/JN/EO) und das Berufsrecht (RAO statt BRAO).

> **Vorsicht Falschfreunde:** Gleiche Abkürzung, anderes Recht. `KSchG` = *Konsumentenschutzgesetz* (AT), nicht Kündigungsschutz. Paragrafennummern von ABGB/BGB stimmen **nie** überein. Es gibt **keinen** „Fachanwalt"-Titel in Österreich. Österreichisches Rechtsdeutsch weicht ab (*Jänner*, *Rekurs*, *Erkenntnis*, *Außerstreit*).

## Aufbau

```
.claude-plugin/marketplace.json     Marketplace-Manifest (Plugin-Registrierung)
references/                          Geteilte Grundlagen (von allen Skills genutzt)
  ├─ methodik-buergerliches-recht.md ABGB-Methodik & Anspruchsaufbau
  ├─ zitierweise.md                  AT-Zitierweise (GZ, RS-Nummer, RIS)
  ├─ ris-quellen.md                  RIS-Anbindung & Grounding-Protokoll
  ├─ quellenhygiene.md               Quellen-Sperren (keine Blindzitate)
  ├─ dashboard-template.md           Output-Engine (übernommen)
  └─ anwalts-dashboard-konvention.md Einstiegs-Triage (AT-Verfahrensstände)
tools/
  └─ ris_client.py                   Verifizierender RIS-OGD-Client (+ Smoke-Test)
gewaehrleistung-konsumentenschutz/   Pilot-Plugin (Skelett; Skills folgen in Phase 2)
```

## Quellen-Grounding über RIS

Die Vertrauenswürdigkeit steht und fällt damit, dass **jede** Fundstelle auf eine freie Primärquelle auflöst. Österreichs Pendant zu den deutschen Justizportalen ist **RIS — Rechtsinformationssystem des Bundes** (`ris.bka.gv.at`), inklusive offener **OGD-API** (`data.bka.gv.at/ris/api/v2.6/`, kein Key).

`tools/ris_client.py` parst das (tief verschachtelte) API-Schema korrekt, dedupliziert Geschäftszahlen, filtert ausländische Gerichte heraus und formatiert nach `references/zitierweise.md`. Selbst prüfen:

```bash
python3 tools/ris_client.py smoke
```

Erwartet: `§ 932 ABGB` → Permalink HTTP 200; ein realer OGH-Rechtssatz (RS-Nummer + Geschäftszahl + ECLI + Permalink, HTTP 200). Jede ausgegebene Zahl stammt live aus RIS — nichts modellgeneriert.

> **Grenze:** RIS enthält Primärrecht, keine Lehrmeinung. Grounding fängt erfundene Fundstellen und tote Links, **nicht** dogmatische Fehler. Fachliche Richtigkeit bleibt anwaltliche Aufgabe.

## Pilot: Gewährleistung / Konsumentenschutz

Bewusst klein gewählte erste Vertikale (`gewaehrleistung-konsumentenschutz/`): hohe Methodenüberschneidung mit Deutschland (EU-Warenkauf-RL), gut begrenzt, exzellente RIS-Abdeckung — und sie erzwingt die Kernkompetenz **Regimewahl**: VGG (B2C, ab 1.1.2022) *verdrängt* die §§ 922 ff ABGB (lex specialis), gilt aber nicht für B2B/C2C/Liegenschaften.

## Status / Roadmap

- [x] **Phase 0 — Gerüst.** Frisches Repository, Marketplace-Manifest, Pilot-Plugin-Skelett.
- [x] **Phase 1 — Grundlagen.** AT-Zitierweise + RIS-Client (live geprüft) und ABGB-Methodik.
- [ ] **Phase 2 — Pilot-Vertikale** end-to-end inkl. einer realen Test-Akte.
- [ ] **Phase 3 — Zweite Vertikale**, die beide Grundlagen **unverändert** wiederverwendet (Beweis, dass der Schnitt Motor/Rechtsschicht trägt).
- [ ] Danach: weitere Gebiete (Arbeitsrecht AngG/ArbVG/ASGG, Gesellschaftsrecht UGB/GmbHG + Notariatsakt), Verfahrens-Plugins (öZPO/JN/EO, ERV), Berufsrecht.

## Wichtige Vorbehalte

- **Keine Rechtsberatung, kein geprüftes Produkt.** Output ist anwaltliche Vorbereitung, nie Entscheidung.
- **Verschwiegenheit (§ 9 RAO; Verstoß = Disziplinarvergehen) + DSGVO/DSG:** Mandantendaten nur in rechtskonformer Umgebung in KI-Tools verarbeiten; Datenresidenz/DPA vor jedem Echtdaten-Einsatz klären.
- **Kein „Fachanwalt".** Österreich kennt keinen geschützten Spezialisierungstitel; allenfalls selbsterklärte Tätigkeitsschwerpunkte.
- Adaptiert die Arbeitsweise von `Klotzkette/claude-fuer-deutsches-recht` (Apache-2.0 OR MIT); rechtliche Inhalte sind eigenständig für Österreich erstellt.

## Lizenz

Apache-2.0 OR MIT.
