# Lösung / Triage — Kündigung Angestellte: Anfechtung

> Musterlauf der Plugin-Pipeline gegen `sachverhalt.md`. **Jede** Norm-Fundstelle ist über RIS auflösbar (Permalinks unten); Geschäftszahlen/RS-Nummern über `tools/ris_client.py` verifizieren (Leitsatz vor Verwendung lesen). **KV-Inhalte und Beträge live beziehen.** Keine Rechtsberatung.

## Sofort-Triage (Dashboard)

| Punkt | Befund | Quelle |
|---|---|---|
| Rolle | Arbeitnehmerin (Angestellte), 9 Dienstjahre | Dienstvertrag |
| Beendigungsart | **Arbeitgeber-Kündigung** (ordentlich, ohne Begründung — zulässig) | `beendigungsart` |
| Frist/Termin | § 20 AngG, ~9 J → **3-Monats-Frist**; Kündigung 15. 6. zum 30. 9. (Quartalsende) → **gewahrt** (spätestens 30. 6. für 30. 9.) | `kuendigungsfristen-termine` |
| **Anfechtung** | § 105 ArbVG **Sozialwidrigkeit**: Betrieb ≥ 5 AN (40) ✓, > 6 Monate ✓, wesentl. Interessenbeeinträchtigung (54 J., schwer vermittelbar) plausibel; **BR hat widersprochen** | `kuendigungsschutz-anfechtung` |
| **Frist Anfechtung** | 🔴 **kurz**: BR kann (auf Verlangen) binnen **1 Woche** anfechten; sonst AN **binnen 2 Wochen** danach — beim **ASG** (§ 105 Abs 4 ArbVG) | `kuendigungsschutz-anfechtung` |
| Ansprüche | **Abfertigung neu** (AV ab 2017 → BMSVG/BV-Kasse; bei AG-Kündigung Auszahlung), **Urlaubsersatzleistung** (12 Tage, § 10 UrlG); **keine** Kündigungsentschädigung | `beendigungsansprueche` |

## Risiko-Ampel

- 🔴 **Frist** — die Anfechtungsfrist (§ 105 Abs 4 ArbVG) läuft sehr kurz und ist nicht verlängerbar; Abstimmung mit dem **Betriebsrat** (Widerspruch erfolgt) sofort.
- 🟠 **Beweis** — Sozialwidrigkeit erfordert Darlegung der Interessenbeeinträchtigung; AG wird betriebs-/personenbezogene Gründe einwenden (Sozialvergleich).
- 🟠 **Wirtschaftlich** — Fortbestand des Arbeitsverhältnisses vs. Abfertigung/Vergleich; Prozessrisiko.

## Rechtliche Beurteilung (Kurzgutachten)

1. **Beendigungsart:** ordentliche **Arbeitgeber-Kündigung**; sie ist **nicht begründungspflichtig**, aber nach § 105 ArbVG anfechtbar.
2. **Frist/Termin (§ 20 AngG):** Bei rund 9 Dienstjahren beträgt die Kündigungsfrist **3 Monate** (ab 5 Jahren), Kündigungstermin **Quartalsende**. Für den Termin 30. 9. 2026 musste spätestens zum 30. 6. 2026 gekündigt werden; die Kündigung vom **15. 6. 2026** wahrt **Frist und Termin**. Die Kündigung ist also **formell wirksam** — angreifbar nur über die Anfechtung.
3. **Anfechtung (§ 105 ArbVG):** **Sozialwidrigkeit** (Abs 3 Z 2) kommt in Betracht: Der Betrieb hat dauernd ≥ 5 AN (40) und die Mandantin ist > 6 Monate beschäftigt; angesichts Alter (54), Gesundheit und schlechter Vermittelbarkeit ist eine **wesentliche Interessenbeeinträchtigung** plausibel. Die Arbeitgeberin kann betriebsbedingte oder personenbezogene Gründe einwenden → **Interessenabwägung/Sozialvergleich**.
4. **Verfahren/Frist:** Da der **Betriebsrat widersprochen** hat, kann auf Verlangen der Mandantin der **Betriebsrat** binnen **einer Woche** anfechten; nutzt er das nicht, kann die Mandantin **binnen zwei Wochen** danach **selbst** beim **Arbeits- und Sozialgericht** anfechten (§ 105 Abs 4 ArbVG). **Frist sofort sichern.**
5. **Ansprüche:** Da das Dienstverhältnis 2017 begann, gilt **Abfertigung neu** (BMSVG); bei Arbeitgeber-Kündigung und erfüllter **3-Jahres-Schwelle (≥ 36 Beitragsmonate — hier ~9 Jahre)** besteht ein **Auszahlungsanspruch gegen die BV-Kasse**. Hinzu kommt die **Urlaubsersatzleistung** für 12 offene Tage (§ 10 UrlG). Eine **Kündigungsentschädigung** (§ 29 AngG) besteht **nicht**, weil ordnungsgemäß (mit Frist) gekündigt wurde.

## Empfehlung (nächste Schritte)

- **Sofort** mit dem Betriebsrat klären, ob er anficht; andernfalls Eigenanfechtung der Mandantin fristwahrend vorbereiten (ASG).
- Interessenbeeinträchtigung dokumentieren (Alter, Gesundheit, Arbeitsmarkt), Sozialvergleich antizipieren.
- Abfertigung neu (BV-Kasse) und Urlaubsersatzleistung beziffern; KV-Verfallsfristen prüfen.

## Verifizierte Quellen (RIS)

**Normen (Permalinks, HTTP 200 geprüft):**
- § 20 AngG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008069&Artikel=1&Paragraf=20
- § 105 ArbVG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008329&Paragraf=105
- § 14 BMSVG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20002088&Paragraf=14
- § 10 UrlG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008376&Paragraf=10

**Judikatur (Existenz/Permalink über RIS geprüft; Leitsatz vor Verwendung lesen; ObA-Senat):**
- Kündigungsanfechtung/Sozialwidrigkeit (inkl. Interessenabwägung) — `RIS-Justiz RS0116698` (OGH 8 ObA 1/02h)
- Sozialwidrigkeit (weitere Interessenabwägungs-/Abfertigungs-Rechtssätze) erst zur Laufzeit über die unten genannten `linie`-Befehle beziehen und mit `leit <GZ>` (ObA-Senat) absichern — keine GZ aus Modellwissen.

Reproduzieren (zur Laufzeit ausführen, nicht nur verweisen): `python3 tools/ris_client.py linie "Kündigungsanfechtung Sozialwidrigkeit" --gericht OGH --gesetz ARBVG --paragraf 105` bzw. `linie "Abfertigung Beendigung" --gericht OGH --gesetz BMSVG --paragraf 14`. Die oben genannten Rechtssätze/GZ mit `leit <GZ>` als Leitentscheidung (Stamm) bestätigen und ältere Entscheidungen vor Übernahme mit `aktualitaet ARBVG 105 --seit <Entscheidungsdatum>` auf Aktualität prüfen.

> Hinweis: Diese Triage ist Vorbereitung, nicht Entscheidung. Der Anwalt führt das Mandat.
