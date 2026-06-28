---
name: einstieg-mietzins
description: "Einstiegs-Triage für Mietzinsfragen nach dem MRG (Österreich): Anwalts-Dashboard, das Rolle, Anwendungsbereich (Voll-/Teil-/Vollausnahme), Mietzinssystem, Fristen und das zuständige (Außerstreit-)Verfahren in einer scanbaren Tabelle erfasst und auf die Spezial-Skills weiterleitet. Kein deutsches Recht."
---

# Einstieg Mietzins (MRG) — Anwalts-Dashboard

## Fachlicher Anker

- **Normen (über RIS auflösen, `tools/ris_client.py`):** § 1 MRG (Anwendungsbereich), §§ 15a, 16 MRG (Mietzins), § 16 Abs 8 MRG (Überprüfung), § 37 MRG (Verfahren) — GNR 10002531; RichtWG — GNR 10003166; § 1096 ABGB (Erhaltung/Mietzinsminderung) — GNR 10001622.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md`. Keine Geschäftszahl aus Modellwissen.
- **Konvention:** Aufbau nach `references/anwalts-dashboard-konvention.md`.

## Einsatzlage

Erster Skill bei Mietzins-Mandaten zu **Wohnungen** (Hauptmiete). Liefert die Triage, klärt zuerst den **Anwendungsbereich** des MRG (der über die Mietzinsbeschränkung entscheidet) und benennt den nächsten Spezial-Skill. Nicht für Kündigung/Räumung, Betriebskosten oder Geschäftsraummiete (dorthin nur verweisen).

## Sofort-Triage (Tabelle, vor jeder Rückfrage)

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
|---|---|---|
| Rolle | Mieter oder Vermieter? Hauptmiete/Untermiete? | Mietvertrag, Mandantenmail |
| **Anwendungsbereich** | **Vollanwendung** (Mietzins beschränkt) / **Teilanwendung** § 1 Abs 4 (frei) / **Vollausnahme** § 1 Abs 2 (nur ABGB)? | Baujahr/Baubewilligung, Zahl der Wohnungen → Skill `anwendungsbereich-mrg` |
| Mietzinssystem | Richtwert (§ 16 Abs 2) / Kategorie (§ 15a) / angemessen (§ 16 Abs 1)? | Lage, Ausstattungskategorie, Vertragsdatum → Skill `mietzinsbildung` |
| Zulässigkeit | Vereinbarter Hauptmietzins über dem zulässigen Höchstmaß? | Mietvertrag → Skill `mietzinsueberpruefung` |
| Frist | Präklusivfrist § 16 Abs 8 MRG (befristet/unbefristet unterschiedlich) gewahrt? | Vertragsdatum/Befristung → Skill `mietzinsueberpruefung` |
| Verfahren | Schlichtungsstelle vorhanden (Wien u. a.)? Außerstreit vor BG | § 37, § 39 MRG → Skill `verfahren-schlichtung-ausserstreit` |

## Risiko-Ampel

- 🔴/🟠/🟢 **Frist** — Präklusivfrist der Mietzinsüberprüfung (§ 16 Abs 8 MRG): 🔴 ≤ 7 Tage, 🟠 ≤ 30 Tage. Bei befristeten Verträgen Sonderregel beachten.
- 🔴/🟠/🟢 **Beweis** — 🔴 Ausstattung/Lage/Baujahr unklar (entscheidet System und Zuschläge); 🟠 lückenhaft; 🟢 belastbar.
- 🔴/🟠/🟢 **Wirtschaftlich** — nach Höhe der möglichen Überschreitung/Rückforderung.

## Anschluss-Skill-Router

| Wenn der Fall trägt … | dann Skill | Erwartung |
|---|---|---|
| **Baujahr/Wohnungszahl/Förderung unklar** | **`anwendungsbereich-mrg`** | Klares Ergebnis: Voll-/Teil-/Vollausnahme |
| Vollanwendung (+), Streit über die Mietzinshöhe | `mietzinsbildung` | Richtiges System + zulässige Höhe |
| Vereinbarter Zins zu hoch | `mietzinsueberpruefung` | Überschreitung, Teilnichtigkeit, Rückforderung, Frist |
| Antrag/Zuständigkeit | `verfahren-schlichtung-ausserstreit` | Richtiger Weg (Schlichtungsstelle → BG) |

Vorrangig fast immer **`anwendungsbereich-mrg`** — ohne Anwendungsbereich keine Mietzinsprüfung.

## Norm-Radar

- `§ 1 MRG` — Anwendungsbereich (Voll-/Teil-/Vollausnahme)
- `§ 15a MRG` — Ausstattungskategorien A–D / Kategoriemietzins
- `§ 16 Abs 2 MRG` — Richtwertmietzins (+ RichtWG)
- `§ 16 Abs 7 MRG` — Befristungsabschlag (25 %)
- `§ 16 Abs 8 MRG` — Unwirksamkeit der Überschreitung, Rückforderung, Frist
- `§ 37, § 39 MRG` — Außerstreitverfahren / Schlichtungsstelle

## Genau eine Rückfrage (nur wenn nötig)

Trägt die Akte 80 %: Dashboard mit `[noch zu klären: …]`. Sonst die **eine** Weiche: *„Wann wurde das Gebäude baubewilligt, wie viele selbständige Wohnungen hat es, und ist der Vertrag befristet?"* (entscheidet Anwendungsbereich + Mietzinssystem + Frist).

## Judikatur-Anker (Such-Wegweiser, kein Blindzitat)

Über RIS (`tools/ris_client.py judikatur "<Stichworte>" --gericht OGH`) zu verifizieren, **keine GZ behaupten** — das Wohnrecht entscheidet der **5. Senat (5 Ob)**:

- Anwendungsbereich/Vollausnahme — Suchworte „Vollausnahme".
- Richtwert/Zuschläge — Suchworte „Richtwert Zuschlag".
- Unzulässige Mietzinsvereinbarung — Suchworte „unzulässige Mietzinsvereinbarung".

## Hinweis

Diese Triage ist Vorbereitung, nicht Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`.
