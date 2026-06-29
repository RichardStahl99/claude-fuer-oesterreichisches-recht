---
name: mangel-und-vermutung
description: "Prüft, ob ein Gewährleistungsmangel vorliegt (Soll-Ist-Abweichung, § 922 ABGB bzw. Vertragsmäßigkeit nach VGG) und ob er bei Übergabe vorlag — samt der Vermutungsregel (§ 924 ABGB: 6 Monate; § 11 VGG: 1 Jahr) und Beweislast. Österreich, kein deutsches Recht."
---

# Mangel und Vermutung der Mangelhaftigkeit

## Fachlicher Anker

- **Normen (über RIS prüfen):** § 922 ABGB (Mangelbegriff), § 924 ABGB (Vermutung 6 Monate), § 928 ABGB (offenkundige Mängel) — GNR 10001622; §§ 4 ff VGG (Vertragsmäßigkeit), § 11 VGG (Vermutung 1 Jahr) — GNR 20011654.
- **Vorgelagert:** `regimewahl-vgg-vs-abgb` muss das Regime geklärt haben.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`; keine GZ aus Modellwissen.

## Worum geht es?

Zwei Fragen: **(1)** Liegt überhaupt ein Mangel vor? **(2)** Lag er **bei Übergabe** vor (nur dann wird gewährleistet)? Frage (2) entscheidet die **Vermutungsregel**, die die Beweislast für den Übergabezeitpunkt umkehrt.

## Schritt-für-Schritt

1. **Geschuldete Beschaffenheit bestimmen.**
   - **ABGB (§ 922):** bedungene Eigenschaften (ausdrücklich/schlüssig vereinbart) **und** gewöhnlich vorausgesetzte Eigenschaften (Verkehrsüblichkeit, Probe, Beschreibung).
   - **VGG (§§ 4 ff):** Vertragsmäßigkeit nach **subjektiven** (Vereinbarung) **und objektiven** Anforderungen (übliche Beschaffenheit, Zubehör, Aktualisierungspflicht bei digitalen Elementen).
2. **Ist-Beschaffenheit feststellen** (Fotos, Befund, Sachverständiger).
3. **Soll-Ist-Abweichung** = Mangel (Sach- oder Rechtsmangel). Bagatellen prüfen.
4. **Maßgeblicher Zeitpunkt: Übergabe (Gefahrübergang).** Der Mangel muss bei Übergabe zumindest in der Anlage vorhanden gewesen sein; spätere, vom Käufer verursachte Schäden sind kein Gewährleistungsfall.
5. **Vermutungsregel anwenden:**
   - Mangel kommt binnen **6 Monaten** (ABGB § 924) bzw. **1 Jahr** (VGG § 11, B2C) ab Übergabe hervor → es wird **vermutet**, dass er schon bei Übergabe vorlag. Beweislast für das Gegenteil trägt der **Übergeber/Unternehmer**.
   - Danach: Käufer/Übernehmer trägt die Beweislast, dass der Mangel bei Übergabe vorlag.
   - Grenze der Vermutung: Unvereinbarkeit mit Art der Sache oder des Mangels (§ 924 Satz 3 ABGB; § 11 Abs 1 VGG).
6. **Offenkundige Mängel** (§ 928 ABGB): in die Augen fallende Mängel sind grundsätzlich nicht zu gewährleisten, wenn der Käufer sie kannte/kennen musste.

## Typische Fehler / Kritik

- **Falsche Vermutungsfrist** je Regime (6 Mon. ABGB vs. 1 J. VGG) — der häufigste Fehler.
- **Vermutung mit Frist verwechseln.** Die Vermutung (§ 924/§ 11) betrifft den **Übergabezeitpunkt**, nicht die **Gewährleistungsfrist** (§ 933 ABGB) — zwei verschiedene Fristen, siehe `verjaehrung-und-fristen`.
- **Mangelbegriff aus deutschem Recht** (§ 434 BGB, „Nacherfüllung") — gehört nicht hierher.
- **Beweislast pauschal umgekehrt.** Nach Ablauf der Vermutungsfrist trägt der Käufer die Beweislast.

## Quellen und Stand 06/2026

- §§ 922, 924, 928 ABGB (RIS, GNR 10001622); §§ 4 ff, 11 VGG (RIS, GNR 20011654).
- `references/methodik-buergerliches-recht.md` Abschnitt 9–10. Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)
- `§ 922 ABGB` — Mangelbegriff · `§ 924 ABGB` — Vermutung 6 Monate · `§ 928 ABGB` — offenkundige Mängel
- `§ 11 VGG` — Vermutung 1 Jahr · `§§ 4 ff VGG` — Vertragsmäßigkeit

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen)
Zur Laufzeit ausführen (nicht nur verweisen):
- OGH zur Soll-Ist-Abweichung und zum Übergabezeitpunkt — OGH-Linie samt Leitsätzen holen: `python3 tools/ris_client.py linie "Mangel Übergabe Gewährleistung" --gericht OGH --gesetz ABGB --paragraf 922`.
- Für eine konkret herangezogene Geschäftszahl `python3 tools/ris_client.py leit <GZ>` — Leitentscheidung (Stamm) oder Folgeentscheidung, wie gefestigt die Linie.
- **Aktualität (Pflicht vor Übernahme älterer Entscheidungen):** Die Vermutungsregel wurde im B2C-Bereich durch das VGG (ab 1.1.2022) neu geordnet (§ 11 VGG: 1 Jahr statt § 924 ABGB: 6 Monate). Alt-Judikatur zur 6-Monats-Vermutung vor Verwendung flaggen: `python3 tools/ris_client.py aktualitaet ABGB 924 --seit <Entscheidungsdatum>` bzw. im B2C-Fall `python3 tools/ris_client.py aktualitaet VGG 11 --seit <Entscheidungsdatum>`.
- Keine Geschäftszahl behaupten, die nicht live aufgelöst wurde.

### Anwendung im Skill
Erst Mangel (+ richtiges Regime), dann Vermutung/Beweislast nach Übergabezeitpunkt, dann weiter zu `behelfshierarchie`.
