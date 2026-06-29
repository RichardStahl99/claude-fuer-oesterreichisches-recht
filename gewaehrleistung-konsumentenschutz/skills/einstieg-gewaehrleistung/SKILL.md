---
name: einstieg-gewaehrleistung
description: "Einstiegs-Triage für Gewährleistung bei Waren (Österreich): Anwalts-Dashboard, das Rolle, Regime (VGG vs §§ 922 ff ABGB), Mangel, Behelf, Fristen in einer scanbaren Tabelle erfasst und auf die passenden Spezial-Skills weiterleitet. Kein deutsches Recht."
---

# Einstieg Gewährleistung — Anwalts-Dashboard

## Fachlicher Anker

- **Normen (über RIS auflösen, `tools/ris_client.py`):** §§ 922, 924, 932, 933 ABGB (Gesetzesnummer 10001622); §§ 5, 11, 12, 13 VGG (Gesetzesnummer 20011654).
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md`. Keine Geschäftszahl aus Modellwissen.
- **Konvention:** Aufbau nach `references/anwalts-dashboard-konvention.md`.

## Einsatzlage

Erster Skill bei jedem Gewährleistungs-Mandat zu **Waren** (Kauf beweglicher Sachen). Liefert in den ersten Zeilen eine Triage-Tabelle, ordnet das anwendbare Regime zu und benennt den nächsten Spezial-Skill. Nicht für Werkverträge, Liegenschaften oder Miete (dorthin nur verweisen).

## Sofort-Triage (Tabelle, vor jeder Rückfrage)

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
|---|---|---|
| Rolle | Käufer (Übernehmer) oder Verkäufer (Übergeber)? | Mandantenmail, Rechnung, Vertrag |
| Regime | **Unternehmer↔Verbraucher + Ware + ab 1.1.2022 → VGG**; sonst §§ 922 ff ABGB | Parteienstellung, Vertragsdatum → Skill `regimewahl-vgg-vs-abgb` |
| Mangel | Liegt ein Sach-/Rechtsmangel vor? Lag er bei Übergabe (vor)? | Fotos, Gutachten, Übergabedatum → Skill `mangel-und-vermutung` |
| Behelf | Primär (Verbesserung/Austausch) oder sekundär (Preisminderung/Wandlung)? | Mängelsachverhalt → Skill `behelfshierarchie` |
| Frist | Gewährleistungsfrist (2 J. beweglich) gewahrt? Verjährung? | Übergabedatum → Skill `verjaehrung-und-fristen` |
| Zuständigkeit | Streitwert → BG (≤ 15.000 €) / LG; Anwaltspflicht (Wertstreit): BG > 5.000 € und LG absolut, ≤ 5.000 € kein Anwaltszwang (§ 27 Abs 1 ZPO) | JN, Gerichtsstandsvereinbarung |

## Risiko-Ampel

- 🔴/🟠/🟢 **Frist** — 🔴 Gewährleistungs-/Verjährungsfrist ≤ 7 Tage; 🟠 ≤ 30 Tage; 🟢 sonst. Frist aus dem **Übergabedatum** rechnen, nicht aus dem Kaufdatum.
- 🔴/🟠/🟢 **Beweis** — 🔴 Mangel-/Übergabezeitpunkt unklar und Vermutungsfrist (1 J. VGG / 6 Mon. ABGB) abgelaufen; 🟠 lückenhaft; 🟢 belastbar.
- 🔴/🟠/🟢 **Wirtschaftlich** — nach Streitwert/Mandanteninteresse.

## Anschluss-Skill-Router

| Wenn der Fall trägt … | dann Skill | Erwartung |
|---|---|---|
| **Parteienstellung/Vertragsdatum unklar oder B2C** | **`regimewahl-vgg-vs-abgb`** | Klares Ergebnis: VGG oder ABGB, mit Begründung |
| Streit, *ob* / *wann* ein Mangel vorlag | `mangel-und-vermutung` | Mangelbegriff + Beweislast/Vermutung geklärt |
| Mangel (+), Streit über den richtigen Behelf | `behelfshierarchie` | Zulässiger Behelf in der richtigen Stufe |
| Frist-/Verjährungsfrage | `verjaehrung-und-fristen` | Fristenstatus + nächste Handlung |

Vorrangig fast immer **`regimewahl-vgg-vs-abgb`** — das anwendbare Regime steuert alles Weitere.

## Norm-Radar

- `§ 922 ABGB` — Mangelbegriff (Soll-Ist-Abweichung, bedungene/gewöhnliche Eigenschaften)
- `§ 924 ABGB` — Vermutung der Mangelhaftigkeit (allgemein **6 Monate**)
- `§ 932 ABGB` — Behelfshierarchie (Verbesserung/Austausch vor Preisminderung/Wandlung)
- `§ 933 ABGB` — Gewährleistungsfrist (**2 J.** bewegliche, 3 J. unbewegliche Sachen)
- `§ 11 VGG` — Vermutung **1 Jahr** im Verbrauchergeschäft (ab 1.1.2022)
- `§§ 12 f VGG` — Behelfshierarchie im Verbrauchergeschäft

## Genau eine Rückfrage (nur wenn nötig)

Trägt die Akte 80 % der Triage: kein Vorab-Fragenkatalog, sondern Dashboard mit `[noch zu klären: …]`. Sonst die **eine** weichenstellende Frage — meist: *„Ist der Käufer Verbraucher und der Verkäufer Unternehmer, und wann wurde die Ware übergeben?"* (entscheidet VGG vs ABGB).

## Judikatur-Anker (Such-Wegweiser, kein Blindzitat)

Zur Laufzeit ausführen (nicht nur verweisen) — **keine GZ behaupten**, nur live Geliefertes übernehmen:

- Behelfshierarchie § 932 — `python3 tools/ris_client.py linie "Verbesserung Gewährleistung" --gericht OGH --gesetz ABGB --paragraf 932` (OGH-Linie mit Leitsätzen nach Linientiefe).
- Wandlung/Preisminderung — `python3 tools/ris_client.py linie "Wandlung Preisminderung" --gericht OGH --gesetz ABGB --paragraf 932`.
- Verjährung Gewährleistung — `python3 tools/ris_client.py linie "Verjährung Gewährleistung" --gericht OGH --gesetz ABGB --paragraf 933`.
- Gewicht einer konkret genannten Geschäftszahl: `python3 tools/ris_client.py leit <GZ>` (Leitentscheidung/Stamm + Linientiefe).
- **Aktualität (Pflicht vor Übernahme älterer Entscheidungen):** § 932 ABGB wurde durch das VGG (ab 1.1.2022) neu gefasst — Alt-Judikatur (vor 2022) vor Verwendung flaggen mit `python3 tools/ris_client.py aktualitaet ABGB 932 --seit <Entscheidungsdatum>` bzw. `python3 tools/ris_client.py aktualitaet VGG 11 --seit <Entscheidungsdatum>`.

## Hinweis

Diese Triage ist Vorbereitung, nicht Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`.
