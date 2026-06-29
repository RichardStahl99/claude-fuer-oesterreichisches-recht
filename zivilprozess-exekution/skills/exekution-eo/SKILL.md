---
name: exekution-eo
description: "Führt durch die Exekution einer Geldforderung nach der EO: Exekutionstitel (§ 1 EO) und Vollstreckbarkeit (§ 7), Exekutionsantrag beim Bezirksgericht und Wahl des Exekutionsmittels (Fahrnis-, Gehalts-/Forderungsexekution, §§ 249, 290 ff EO) samt Existenzminimum. Österreich, kein deutsches Recht."
---

# Exekution einer Geldforderung (EO)

## Fachlicher Anker

- **Normen (über RIS prüfen):** § 1 EO (Exekutionstitel, taxativ), § 7 EO (Vollstreckbarkeit/Bestimmtheit), §§ 249 ff EO (Fahrnisexekution), §§ 290 ff EO (Forderungs-/Gehaltsexekution, Existenzminimum) — GNR 10001700; ergänzend ZPO/JN (§ 78 EO).
- **Vorgelagert:** ein **Exekutionstitel** muss vorliegen (rk. Zahlungsbefehl, Urteil, Vergleich, vollstreckbarer Notariatsakt).
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`.

## Worum geht es?

Mit einem **vollstreckbaren Titel** wird die Geldforderung zwangsweise hereingebracht. Zu klären: Ist der Titel exekutionsfähig (§§ 1, 7 EO)? Welches **Exekutionsmittel** passt zum (vermuteten) Vermögen des Schuldners?

## Schritt-für-Schritt

1. **Exekutionstitel prüfen (§ 1 EO):** Liegt einer der **taxativ** aufgezählten Titel vor — insbesondere **Urteil**, **rechtskräftiger Zahlungsbefehl**, gerichtlicher/prätorischer **Vergleich**, **vollstreckbarer Notariatsakt**? 
2. **Vollstreckbarkeit (§ 7 EO):** Titel rechtskräftig, Leistungsfrist abgelaufen, Anspruch **ausreichend bestimmt** (Person, Inhalt, Umfang). Vollstreckbarkeitsbestätigung beibringen.
3. **Exekutionsantrag** beim **Bezirksgericht** als Exekutionsgericht stellen (Anwälte per ERV). Das Exekutionspaket (Reform 2021) erlaubt gebündelte Anträge.
4. **Exekutionsmittel wählen** (zur Hereinbringung von Geld):
   - **Fahrnisexekution (§§ 249 ff EO):** Pfändung beweglicher körperlicher Sachen, Verwertung durch Versteigerung.
   - **Forderungsexekution**, v. a. **Gehaltsexekution/Lohnpfändung (§§ 290 ff EO):** Pfändung des Arbeitseinkommens (Drittschuldner = Arbeitgeber). Das **Existenzminimum** (unpfändbarer Freibetrag, § 291a EO; jährlich angepasst) bleibt unpfändbar — **aktuelle Werte live prüfen**. Ebenso Pfändung von Bankguthaben/sonstigen Geldforderungen.
   - **Zwangsversteigerung** unbeweglichen Vermögens (§§ 133 ff EO) — gesondert, hier nur Verweis.
5. **Einbringlichkeit realistisch einschätzen:** Ohne pfändbares Vermögen/Einkommen bleibt der Titel formal bestehen (30 Jahre, § 1478 ABGB), bringt aber nichts — **Vermögensverzeichnis** (Offenlegung des Vermögens, § 47 EO) erwägen (kein „Offenbarungseid" — das ist deutsche Terminologie).

## Typische Fehler / Kritik

- **Titel nicht exekutionsfähig:** unbestimmt oder noch nicht vollstreckbar (§§ 1, 7 EO).
- **Falsches Exekutionsmittel:** Fahrnisexekution bei vermögenslosem, aber erwerbstätigem Schuldner — Gehaltsexekution wäre zielführend.
- **Existenzminimum ignoriert:** bei der Lohnpfändung bleibt der Grundbetrag unpfändbar.
- **Deutsches Recht:** keine „Zwangsvollstreckung nach §§ 704 ff ZPO (DE)", kein „Gerichtsvollzieher/PfÜB" — in Österreich EO, Exekutionsbewilligung durch das BG.

## Quellen und Stand 06/2026

- §§ 1, 7, 78, 249 ff, 290 ff, 291a EO (RIS, GNR 10001700). Existenzminimum-Tabellen jährlich — live beziehen.
- `references/methodik-buergerliches-recht.md` Abschnitt 11–12. Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)
- `§ 1 EO` — Exekutionstitel · `§ 7 EO` — Vollstreckbarkeit/Bestimmtheit · `§ 249 EO` — Fahrnisexekution · `§ 290 EO` — Gehalts-/Forderungsexekution

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen)
Zur Laufzeit ausführen (nicht nur verweisen):
- Exekutionstitel/Bestimmtheit: `python3 tools/ris_client.py linie "Exekutionstitel" --gericht OGH --gesetz EO --paragraf 1` — OGH-Linie (3.-Senat/Exekution) nach Linientiefe + Leitsätze. Für eine konkret herangezogene Geschäftszahl `leit <GZ>` (Leitentscheidung/Stamm? wie gefestigt die Linie?).
- Aktualität vor Stützung auf eine ältere Entscheidung (Pflicht — EO-Reform 2021): `aktualitaet EO 1 --seit <Entscheidungsdatum>` bzw. `aktualitaet EO 7 --seit <Entscheidungsdatum>` — flaggt, ob die EO nach der Entscheidung geändert wurde; Alt-Judikatur vor 2021 nicht unbesehen übertragen.

### Anwendung im Skill
Titel (§ 1) → Vollstreckbarkeit (§ 7) → Exekutionsantrag (BG) → passendes Exekutionsmittel (Existenzminimum beachten). Vor Stützung auf ältere Judikatur die Aktualität (`aktualitaet`, EO-Reform 2021) prüfen.
