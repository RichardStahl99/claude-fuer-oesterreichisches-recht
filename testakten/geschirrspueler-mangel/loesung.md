# Lösung / Triage — Geschirrspüler-Mangel

> Musterlauf der Plugin-Pipeline gegen `sachverhalt.md`. **Jede** Fundstelle ist über RIS auflösbar (Permalinks unten). Geschäftszahlen/RS-Nummern sind über `tools/ris_client.py` zu verifizieren; Leitsätze vor Verwendung in RIS lesen. Keine Rechtsberatung.

## Sofort-Triage (Dashboard)

| Punkt | Befund | Quelle |
|---|---|---|
| Rolle | Käuferin (Übernehmerin), Verbraucherin | Rechnung, § 1 KSchG |
| **Regime** | **VGG** — Unternehmer→Verbraucher, Ware, Vertrag 2025 (ab 1.1.2022). Verdrängt §§ 922 ff ABGB | `regimewahl-vgg-vs-abgb` |
| Mangel | Undichte Pumpe = Sachmangel; binnen 8 Mon. (< 1 J.) hervorgekommen → **Vermutung** (§ 11 VGG), dass bei Übergabe vorhanden; Händler trägt Gegenbeweis | `mangel-und-vermutung` |
| Behelf | Stufe 1 (Verbesserung/Austausch) verweigert → **Sprung auf Stufe 2** zulässig; Mangel nicht geringfügig → **Vertragsauflösung oder Preisminderung** (§§ 14, 15 VGG) | `behelfshierarchie` |
| Frist | Übergabe 20.03.2025; Gewährleistungsfrist 2 J. (Ware) → bis ~20.03.2027; Anzeige 11/2025 **fristgerecht** | `verjaehrung-und-fristen` |
| Zuständigkeit | Streitwert 649 € → **BG Linz**; < 5.000 € → kein Anwaltszwang (§ 27 Abs 1 ZPO) | JN |

## Risiko-Ampel

- 🟢 **Frist** — Gewährleistungsfrist läuft bis 2027; kein Eildruck.
- 🟠 **Beweis** — Vermutung (§ 11 VGG) hilft der Mandantin; offen ist der Gegenbeweis des Händlers (Bedienungsfehler). Sachverständigengutachten zur Pumpe sichern.
- 🟢 **Wirtschaftlich** — überschaubarer Streitwert.

## Rechtliche Beurteilung (Kurzgutachten)

1. **Regime:** Es gilt das **VGG**: Die Elektro Bauer GmbH ist Unternehmerin, Frau Huber Verbraucherin (§ 1 KSchG), Vertragsgegenstand eine Ware, Vertragsschluss 2025. Das VGG ist lex specialis und verdrängt die §§ 922 ff ABGB (→ Vermutungsfrist 1 Jahr, nicht 6 Monate).
2. **Mangel:** Eine undichte Umwälzpumpe ist eine Abweichung von der gewöhnlich vorausgesetzten Beschaffenheit (Dichtheit/Funktion) → Sachmangel. Da er binnen eines Jahres ab Übergabe hervorkam, **vermutet § 11 VGG**, dass er bereits bei Übergabe vorlag; den Gegenbeweis (Bedienungs-/Anschlussfehler) hat der **Händler** zu führen.
3. **Behelf:** Primär schuldet der Händler Verbesserung oder Austausch (§ 12 VGG). Da er beides **verweigert**, kann Frau Huber auf die zweite Stufe wechseln und **Preisminderung oder Vertragsauflösung** verlangen (§§ 14, 15 VGG; die Vertragsauflösung entspricht der Wandlung des ABGB). Wegen Unbrauchbarkeit ist der Mangel nicht geringfügig → **Vertragsauflösung** (Rückabwicklung gegen Kaufpreis) ist eröffnet.
4. **Frist:** Die zweijährige Gewährleistungsfrist (ab Übergabe 20.03.2025) ist gewahrt; die gesonderte 3-Monats-Verjährungsfrist des § 28 VGG ist hier nicht einmal relevant.
5. **Schadenersatz (separate Schiene):** Der Parkettschaden (~400 €) ist **nicht** Gewährleistung, sondern **Schadenersatz** (§ 933a ABGB iVm Verschulden; Verjährung § 1489 ABGB, 3 J. ab Kenntnis) — eigener Prüfpunkt, hier nur markiert.

## Empfehlung (nächste Schritte)

- Schriftliche Fristsetzung an den Händler mit Wahl des Behelfs (vorrangig Austausch; bei Verweigerung Wandlung), Beweissicherung (Foto/Sachverständiger zur Pumpe).
- Bei weiterer Verweigerung: Klage beim **BG Linz** (Streitwert 649 €).
- Parkettschaden als Schadenersatz gesondert prüfen.

## Verifizierte Quellen (RIS)

**Normen (Permalinks, HTTP 200 geprüft):**
- § 11 VGG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20011654&Paragraf=11
- § 12 VGG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20011654&Paragraf=12
- § 932 ABGB — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001622&Paragraf=932
- § 933 ABGB — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001622&Paragraf=933

**Judikatur (Existenz/Permalink über RIS geprüft; Leitsatz vor Verwendung lesen):**
- Wandlung/Preisminderung — `RIS-Justiz RS0126731` (OGH 2 Ob 135/10g)
- Gewährleistung jüngere Linie — `RIS-Justiz RS0134544` (OGH 6 Ob 158/22m, 2023)

Reproduzieren: `python3 tools/ris_client.py linie "Verbesserung Gewährleistung" --gericht OGH --gesetz ABGB --paragraf 932` bzw. `"Wandlung Preisminderung"` (OGH-Linie mit Leitsätzen). Aktualität der Alt-Judikatur zu § 932 ABGB gegen die VGG-Neufassung (ab 1.1.2022) flaggen: `python3 tools/ris_client.py aktualitaet ABGB 932 --seit <Entscheidungsdatum>` bzw. im B2C-Fall `python3 tools/ris_client.py aktualitaet VGG 11 --seit <Entscheidungsdatum>`.

> Hinweis: Diese Triage ist Vorbereitung, nicht Entscheidung. Der Anwalt führt das Mandat.
