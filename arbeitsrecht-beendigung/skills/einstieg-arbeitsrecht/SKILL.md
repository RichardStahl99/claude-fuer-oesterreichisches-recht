---
name: einstieg-arbeitsrecht
description: "Einstiegs-Triage für die Beendigung des Arbeitsverhältnisses (Österreich): Anwalts-Dashboard, das Rolle, Beendigungsart, Fristen/Termine, Anfechtbarkeit (§ 105 ArbVG) und Beendigungsansprüche in einer scanbaren Tabelle erfasst und auf die Spezial-Skills weiterleitet. Kein deutsches Recht."
---

# Einstieg Arbeitsrecht (Beendigung) — Anwalts-Dashboard

## Fachlicher Anker

- **Normen (über RIS auflösen, `tools/ris_client.py`):** § 20 AngG (Kündigungsfristen) — GNR 10008069 (Artikel 1); § 1159 ABGB (Arbeiter) — GNR 10001622; § 105 ArbVG (Anfechtung) — GNR 10008329; BMSVG (Abfertigung neu) — GNR 20002088; § 10 UrlG (Urlaubsersatzleistung) — GNR 10008376; ASGG (Verfahren) — GNR 10000813.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md`. Keine Geschäftszahl aus Modellwissen.
- **Konvention:** Aufbau nach `references/anwalts-dashboard-konvention.md`.

## Einsatzlage

Erster Skill bei der **Beendigung** eines Arbeitsverhältnisses. Liefert die Triage, klärt zuerst die **Beendigungsart** (sie steuert Fristen, Anfechtung und Ansprüche) und benennt den nächsten Spezial-Skill. Nicht für das laufende Arbeitsverhältnis (Entgelt, Arbeitszeit) oder Sozialversicherung (dorthin nur verweisen).

## Sofort-Triage (Tabelle, vor jeder Rückfrage)

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
|---|---|---|
| Rolle | Arbeitnehmer oder Arbeitgeber? Angestellte/r oder Arbeiter/in? | Dienstvertrag, Mandantenmail |
| **Beendigungsart** | Kündigung / Entlassung / einvernehmlich / Zeitablauf / Austritt / Probezeit? | Schreiben, Sachverhalt → Skill `beendigungsart` |
| Frist/Termin | Kündigungsfrist (§ 20 AngG / § 1159 ABGB) und -termin (Quartalsende) gewahrt? | Eintrittsdatum, Dienstjahre → Skill `kuendigungsfristen-termine` |
| Anfechtung | Anfechtbar? Sozialwidrigkeit / verpöntes Motiv (§ 105 ArbVG); Betrieb ≥ 5 AN? Betriebsrat? | Betriebsgröße, Motiv → Skill `kuendigungsschutz-anfechtung` |
| Ansprüche | Abfertigung (neu/alt), Urlaubsersatzleistung, Kündigungsentschädigung? | Eintrittsdatum, Beendigungsart → Skill `beendigungsansprueche` |
| Verfahren | Arbeits- und Sozialgericht (ASGG) | ASG → Skill `kuendigungsschutz-anfechtung` |

## Risiko-Ampel

- 🔴/🟠/🟢 **Frist** — 🔴 **2-Wochen-Anfechtungsfrist (§ 105 Abs 4 ArbVG)** läuft! 🟠 ≤ 30 Tage. Die Anfechtungsfrist ist sehr kurz und nicht verlängerbar — zuerst sichern.
- 🔴/🟠/🟢 **Beweis** — 🔴 Motiv/Interessenbeeinträchtigung/Betriebsgröße unklar; 🟠 lückenhaft; 🟢 belastbar.
- 🔴/🟠/🟢 **Wirtschaftlich** — Höhe von Abfertigung, Kündigungsentschädigung, Verfahrensrisiko.

## Anschluss-Skill-Router

| Wenn der Fall trägt … | dann Skill | Erwartung |
|---|---|---|
| **Art der Beendigung unklar** | **`beendigungsart`** | Klare Einordnung (Kündigung/Entlassung/…) |
| Kündigung — Frist/Termin fraglich | `kuendigungsfristen-termine` | Frist + Termin geprüft |
| Kündigung anfechten (Sozialwidrigkeit/Motiv) | `kuendigungsschutz-anfechtung` | Anfechtbarkeit + **2-Wochen-Frist** + ASG |
| Geld am Ende des Arbeitsverhältnisses | `beendigungsansprueche` | Abfertigung/Urlaubsersatz/Kündigungsentschädigung |

Vorrangig **`beendigungsart`** — sie ist die Weiche; bei AG-Kündigung sofort die **Anfechtungsfrist** prüfen.

## Norm-Radar

- `§ 20 AngG` — Kündigungsfristen/-termine (Angestellte)
- `§ 1159 ABGB` — Kündigungsfristen Arbeiter (seit 1.10.2021 angeglichen)
- `§ 105 ArbVG` — Anfechtung (Sozialwidrigkeit / verpöntes Motiv), Betriebsrat, 2-Wochen-Frist
- `BMSVG` — Abfertigung neu (1,53 % an BV-Kasse)
- `§ 23 AngG` — Abfertigung alt (vor 1.1.2003)
- `§ 10 UrlG` — Urlaubsersatzleistung

## Genau eine Rückfrage (nur wenn nötig)

Trägt die Akte 80 %: Dashboard mit `[noch zu klären: …]`. Sonst die **eine** Weiche: *„Welche Beendigungsart liegt vor, wann ging das Schreiben zu, und wie viele Mitarbeiter hat der Betrieb (Betriebsrat)?"* (entscheidet Frist, Anfechtbarkeit und das knappe 2-Wochen-Fenster).

## Judikatur-Anker (Such-Wegweiser, kein Blindzitat)

Zur Laufzeit ausführen (nicht nur verweisen) — **keine GZ aus Modellwissen behaupten**, nur Geliefertes übernehmen; Arbeitsrecht entscheidet der **8./9. Senat (ObA)**:

- Sozialwidrigkeit — `python3 tools/ris_client.py linie "Kündigungsanfechtung Sozialwidrigkeit" --gericht OGH --gesetz ARBVG --paragraf 105` (OGH-Linie + Leitsätze nach Linientiefe).
- Verpöntes Motiv — `python3 tools/ris_client.py linie "verpöntes Motiv Kündigung" --gericht OGH --gesetz ARBVG --paragraf 105`.
- Kündigungsentschädigung — `python3 tools/ris_client.py linie "Kündigungsentschädigung" --gericht OGH --gesetz ANGG --paragraf 29`.
- Eine konkret benannte Geschäftszahl mit `leit <GZ>` als Leitentscheidung (Stamm) und Linientiefe gewichten; ältere Entscheidungen vor Übernahme per `aktualitaet <Gesetz> <§> --seit <Entscheidungsdatum>` auf Aktualität prüfen — bei Arbeitern besonders `aktualitaet ABGB 1159 --seit <Datum>` (Angleichung seit 1.10.2021).

## Hinweis

Diese Triage ist Vorbereitung, nicht Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`.
