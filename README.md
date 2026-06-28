# Claude für österreichisches Recht

> 🚧 **Work in Progress — aktive Entwicklung.** Experimentelles, unfertiges Projekt. **Keine Rechtsberatung, kein geprüftes Produkt.** Inhalte können unvollständig oder fehlerhaft sein; **jede Fundstelle ist vor Verwendung selbst zu prüfen.** Verwendung auf eigenes Risiko.
>
> 🔗 **Abgeleitet von** [`Klotzkette/claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht). Dieses Repository übernimmt die *Arbeitsweise* (Plugin-Architektur, juristische Methode, Zitierdisziplin) des deutschen Vorbilds und schreibt die gesamte *Rechtsschicht* (Gesetze, Gerichte, Verfahren, Zitierform, Datenquelle) für **Österreich** neu. Es ist **kein** Fork des Rechtsinhalts — die deutschen Rechtsinhalte wurden bewusst **nicht** übernommen (Falschfreund-Gefahr).

Eine Sammlung von Claude-Skills zur Unterstützung anwaltlicher Arbeit im österreichischen Recht.

## Leitidee: Motor übernehmen, Rechtsschicht neu bauen

Das deutsche Repository ist zweierlei in einem — und nur das Erste lässt sich übernehmen:

- **Wiederverwendbarer Motor (jurisdiktionsneutral):** Plugin-/Marketplace-Gerüst, `SKILL.md`-Format, Dashboard-Ausgabe-Modul, die juristische *Methode* (Gutachtenstil, Subsumtion, Anspruchsaufbau) und die *Zitierdisziplin* („keine Blindzitate, jede Fundstelle verifizierbar, der Anwalt entscheidet").
- **Jurisdiktionsgebundene Rechtsschicht (neu geschrieben):** Gesetze (ABGB statt BGB, UGB statt HGB, VGG, MRG, EO, JN, ArbVG …), Gerichte (OGH/OLG/LG/BG, VwGH, VfGH), Zitierform (Geschäftszahl + **RIS-Justiz**-Rechtssatznummer statt Reporter-Fundstelle), Datenquelle (**RIS** statt gesetze-im-internet.de), Verfahrensrecht (öZPO/JN/EO, Außerstreit) und Berufsrecht (RAO statt BRAO).

> **Vorsicht Falschfreunde:** Gleiche Abkürzung, anderes Recht. `KSchG` = *Konsumentenschutzgesetz* (AT), nicht Kündigungsschutz. Paragrafennummern von ABGB/BGB stimmen **nie** überein. Es gibt **keinen** „Fachanwalt"-Titel in Österreich. Österreichisches Rechtsdeutsch weicht ab (*Jänner*, *Rekurs*, *Erkenntnis*, *Außerstreit*, *Vermögensverzeichnis*).

## Aufbau

```
.claude-plugin/marketplace.json     Marketplace-Manifest (registriert die Plugins)
references/                          Geteilte Grundlagen — jurisdiktionsstabil, von allen Skills genutzt
  ├─ methodik-buergerliches-recht.md ABGB-Methodik & Anspruchsaufbau
  ├─ zitierweise.md                  AT-Zitierweise (GZ, RS-Nummer, RIS)
  ├─ ris-quellen.md                  RIS-Anbindung & Grounding-Protokoll
  ├─ quellenhygiene.md               Quellen-Sperren (keine Blindzitate)
  ├─ dashboard-template.md           Output-Engine (übernommen)
  └─ anwalts-dashboard-konvention.md Einstiegs-Triage (AT-Verfahrensstände)
tools/
  └─ ris_client.py                   Verifizierender RIS-OGD-Client (+ Smoke-Test)
testakten/                           Regressions-Test-Akten (eine je Plugin)
gewaehrleistung-konsumentenschutz/   Plugin: Gewährleistung (VGG vs §§ 922 ff ABGB)
mietzins-mrg/                        Plugin: Mietzinsrecht (MRG, Richtwert, § 16 Abs 8)
zivilprozess-exekution/              Plugin: Forderungsdurchsetzung (JN/ZPO/EO)
arbeitsrecht-beendigung/             Plugin: Beendigung Arbeitsverhältnis (AngG/ArbVG/ASGG)
```

Wer ein Rechtsgebiet ergänzen will: siehe **`AGENTS.md`** (Architektur-Regeln, Muster, Pflichtprüfungen).

## Quellen-Grounding über RIS

Die Vertrauenswürdigkeit steht und fällt damit, dass **jede** Fundstelle auf eine freie Primärquelle auflöst. Österreichs Pendant zu den deutschen Justizportalen ist **RIS — Rechtsinformationssystem des Bundes** (`ris.bka.gv.at`), inklusive offener **OGD-API** (`data.bka.gv.at/ris/api/v2.6/`, kein Key).

`tools/ris_client.py` parst das (tief verschachtelte) API-Schema korrekt, dedupliziert Geschäftszahlen, filtert ausländische Gerichte heraus und formatiert nach `references/zitierweise.md`. Selbst prüfen:

```bash
python3 tools/ris_client.py smoke
```

Erwartet: `§ 932 ABGB` → Permalink HTTP 200; ein realer OGH-Rechtssatz (RS-Nummer + Geschäftszahl + ECLI + Permalink, HTTP 200). Jede ausgegebene Zahl stammt live aus RIS — nichts modellgeneriert.

> **Grenze:** RIS enthält **Primärrecht**, keine Lehrmeinung. Grounding fängt erfundene Fundstellen und tote Links, **nicht** dogmatische Fehler. Die herrschende Meinung lebt in (kostenpflichtigen) Kommentaren — diese nur **lizenziert oder vom Nutzer bereitgestellt** heranziehen, nie aus Modellwissen. Fachliche Richtigkeit bleibt anwaltliche Aufgabe.

## Plugins (Vertikalen)

Jede Vertikale folgt demselben Muster: eine Einstiegs-Triage, ein **Headline-Gate** (die entscheidende Weiche), darauf aufbauende Spezial-Skills und ein Router — plus eine RIS-geprüfte Test-Akte.

| Plugin | Gebiet | Headline-Gate |
|---|---|---|
| `gewaehrleistung-konsumentenschutz` | Gewährleistung bei Waren | Regimewahl **VGG vs §§ 922 ff ABGB** (lex specialis) |
| `mietzins-mrg` | Mietzinsrecht (MRG) | Anwendungsbereich **Voll-/Teil-/Vollausnahme** (§ 1 MRG) |
| `zivilprozess-exekution` | Forderungsdurchsetzung | **Zuständigkeit (JN)** + Anwaltspflicht (§ 27 ZPO) |
| `arbeitsrecht-beendigung` | Beendigung Arbeitsverhältnis | **Beendigungsart** (Kündigung/Entlassung/…) |

## Status / Roadmap

- [x] **Phase 0/1 — Gerüst & Grundlagen.** Marketplace, AT-Zitierweise, ABGB-Methodik, RIS-Client (live geprüft).
- [x] **Phase 2 — `gewaehrleistung-konsumentenschutz`** (VGG vs §§ 922 ff ABGB) + Test-Akte.
- [x] **Phase 3 — `mietzins-mrg`** (MRG/Richtwert) + Test-Akte. Beweis: Grundlagen blieben **unverändert** (`git diff`).
- [x] **Phase 4 — `zivilprozess-exekution`** (JN/ZPO/EO) + Test-Akte.
- [x] **Phase 5 — `arbeitsrecht-beendigung`** (AngG/ArbVG/ASGG) + Test-Akte.
- [ ] **Geplant:** Gesellschaftsrecht (UGB/GmbHG + Notariatsakt), Berufsrecht (RAO), Familienrecht/Außerstreit (AußStrG), Insolvenz (IO).

Stand: 4 Plugins, 24 Skills, 4 Test-Akten, 13 verifizierte Gesetzesnummern. Die geteilten Grundlagen wurden über alle Gebiete hinweg **nicht** verändert — der Schnitt Motor/Rechtsschicht trägt.

## Wichtige Vorbehalte

- **Keine Rechtsberatung, kein geprüftes Produkt.** Output ist anwaltliche Vorbereitung, nie Entscheidung.
- **Verschwiegenheit (§ 9 RAO; Verstoß = Disziplinarvergehen) + DSGVO/DSG:** Mandantendaten nur in rechtskonformer Umgebung in KI-Tools verarbeiten; Datenresidenz/DPA vor jedem Echtdaten-Einsatz klären.
- **Kein „Fachanwalt".** Österreich kennt keinen geschützten Spezialisierungstitel; allenfalls selbsterklärte Tätigkeitsschwerpunkte.
- Adaptiert die Arbeitsweise von [`Klotzkette/claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht) (Apache-2.0 OR MIT); die rechtlichen Inhalte sind eigenständig für Österreich erstellt.

## Lizenz

Apache-2.0 OR MIT.
