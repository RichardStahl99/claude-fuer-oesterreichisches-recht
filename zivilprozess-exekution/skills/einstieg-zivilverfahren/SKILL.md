---
name: einstieg-zivilverfahren
description: "Einstiegs-Triage für die zivilrechtliche Forderungsdurchsetzung (Österreich): Anwalts-Dashboard, das Rolle, Titelvorhandensein, Streitwert/Zuständigkeit, Verfahrensweg (Mahnverfahren/Klage/Exekution) und Fristen in einer scanbaren Tabelle erfasst und auf die Spezial-Skills weiterleitet. Kein deutsches Recht."
---

# Einstieg Zivilverfahren — Anwalts-Dashboard

## Fachlicher Anker

- **Normen (über RIS auflösen, `tools/ris_client.py`):** §§ 49, 50, 66, 104 JN (Zuständigkeit) — GNR 10001697; §§ 27, 244 ff, 248, 464, 505, 521 ZPO (Anwaltspflicht, Mahnverfahren, Rechtsmittel) — GNR 10001699; §§ 1, 7 EO (Exekutionstitel) — GNR 10001700.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md`. Keine Geschäftszahl aus Modellwissen.
- **Konvention:** Aufbau nach `references/anwalts-dashboard-konvention.md`.

## Einsatzlage

Erster Skill bei der Durchsetzung einer **Geldforderung**. Liefert die Triage, klärt zuerst, ob bereits ein **Exekutionstitel** vorliegt (dann direkt Exekution) oder erst ein Titel zu erwirken ist (Mahnverfahren/Klage), und benennt den nächsten Spezial-Skill. Nicht für Außerstreit, Insolvenz oder Strafverfahren (dorthin nur verweisen).

## Sofort-Triage (Tabelle, vor jeder Rückfrage)

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
|---|---|---|
| Rolle | Gläubiger (Kläger) oder Schuldner (Beklagter)? | Mandantenmail, Rechnung/Vertrag |
| **Titel vorhanden?** | Liegt schon ein Exekutionstitel (Urteil, rk. Zahlungsbefehl, Vergleich, vollstreckbarer Notariatsakt) vor? | Akt → falls ja: Skill `exekution-eo` |
| Streitwert / Zuständigkeit | BG (≤ 15.000 €) oder LG? Eigenzuständigkeit? Örtlich (Wohnsitz Beklagter)? | JN → Skill `zustaendigkeit-jn` |
| Anwaltspflicht | BG-Wertstreit > 5.000 € + LG absolut, ≤ 5.000 € kein Zwang (§ 27 Abs 1); BG-Eigenzuständigkeit relativ in Ehesachen/Sachen > 5.000 € an Orten mit ≥ 2 RA (§ 29 Abs 1), sonst kein Zwang | Streitwert → Skill `zustaendigkeit-jn` |
| Verfahrensweg | Geldforderung ≤ 75.000 € → Mahnverfahren (Zahlungsbefehl); sonst Klage | § 244 ZPO → Skill `mahnverfahren` |
| Frist | Einspruch (4 Wochen, § 248; vor dem BG ohne Anwalt § 448 Z 1, vor dem LG mit Anwalt), Rechtsmittel (4 Wochen / 14 Tage); Verjährung der Forderung? | Zustelldatum → Skill `verfahrensgang-rechtsmittel` |

## Risiko-Ampel

- 🔴/🟠/🟢 **Frist** — 🔴 Einspruchs-/Rechtsmittelfrist ≤ 7 Tage oder Verjährung droht; 🟠 ≤ 30 Tage; 🟢 sonst. Fristen aus dem **Zustelldatum** rechnen.
- 🔴/🟠/🟢 **Beweis** — 🔴 Forderung/Titel nicht belegbar; 🟠 lückenhaft; 🟢 belastbar (Urkunden, Rechnung, Lieferschein).
- 🔴/🟠/🟢 **Einbringlichkeit** — Bonität des Schuldners; ohne Vermögen/Einkommen ist auch ein Titel wenig wert.

## Anschluss-Skill-Router

| Wenn der Fall trägt … | dann Skill | Erwartung |
|---|---|---|
| **Titel vorhanden** | **`exekution-eo`** | Exekutionsantrag + passendes Exekutionsmittel |
| Gericht/Anwaltspflicht unklar | `zustaendigkeit-jn` | BG/LG, örtlich, Anwaltspflicht geklärt |
| Geldforderung, kein Titel | `mahnverfahren` | Zahlungsbefehl / Einspruchsbehandlung |
| Einspruch erhoben / streitig / Rechtsmittel | `verfahrensgang-rechtsmittel` | Verfahrensschritt + Frist |

Vorrangig: zuerst **Titel-Frage** klären — Titel vorhanden → Exekution; sonst → Zuständigkeit → Mahnverfahren.

## Norm-Radar

- `§ 49 JN` — sachliche Zuständigkeit BG (≤ 15.000 € + Eigenzuständigkeiten)
- `§ 50 JN` — Gerichtshof (LG)
- `§ 27 ZPO` — Anwaltspflicht (BG-Wertstreit > 5.000 € + LG absolut; ≤ 5.000 € kein Zwang; BG-Eigenzuständigkeit relativ in Ehesachen/Sachen > 5.000 € an Orten mit ≥ 2 RA, § 29 ZPO)
- `§ 244 ZPO` — Mahnverfahren / Zahlungsbefehl (≤ 75.000 €)
- `§ 248 ZPO` — Einspruch (4 Wochen)
- `§ 1 EO` — Exekutionstitel

## Genau eine Rückfrage (nur wenn nötig)

Trägt die Akte 80 %: Dashboard mit `[noch zu klären: …]`. Sonst die **eine** Weiche: *„Liegt bereits ein vollstreckbarer Titel vor, und wie hoch ist die Forderung?"* (entscheidet Exekution vs. Titelerwirkung + Zuständigkeit/Anwaltspflicht).

## Judikatur-Anker (Such-Wegweiser, kein Blindzitat)

Zur Laufzeit ausführen (nicht nur verweisen), **keine GZ behaupten** — nur Geliefertes übernehmen:

- Zuständigkeit/Gerichtsstandsvereinbarung — `python3 tools/ris_client.py linie "Gerichtsstandsvereinbarung Zuständigkeit" --gericht OGH --gesetz JN --paragraf 104`.
- Exekutionstitel/Bestimmtheit — `python3 tools/ris_client.py linie "Exekutionstitel" --gericht OGH --gesetz EO --paragraf 1`.
- Neuerungsverbot — `python3 tools/ris_client.py linie "Neuerungsverbot" --gericht OGH --gesetz ZPO --paragraf 482`.
- Gewicht/Aktualität: für eine konkret herangezogene Geschäftszahl `leit <GZ>` (Leitentscheidung/Stamm? Linientiefe?); vor Stützung auf eine ältere Entscheidung `aktualitaet <Gesetz> <§> --seit <Entscheidungsdatum>` (Verfahrensnormen JN/ZPO/EO ändern sich, vgl. EO-Reform 2021).

## Hinweis

Diese Triage ist Vorbereitung, nicht Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`.
