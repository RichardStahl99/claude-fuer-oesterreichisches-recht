---
name: mietzinsbildung
description: "Bestimmt in der Vollanwendung des MRG das richtige Mietzinssystem und die zulässige Höhe: angemessener Mietzins (§ 16 Abs 1), Richtwertmietzins (§ 16 Abs 2 + RichtWG) mit Zu-/Abschlägen und Lagezuschlag (§ 16 Abs 3/4), Kategorie (§ 15a) und Befristungsabschlag 25 % (§ 16 Abs 7). Österreich, kein deutsches Recht."
---

# Mietzinsbildung (Vollanwendung MRG)

## Fachlicher Anker

- **Normen (über RIS prüfen):** § 15a MRG (Ausstattungskategorien A–D), § 16 Abs 1 MRG (angemessener Mietzins), § 16 Abs 2 MRG (Richtwertmietzins), § 16 Abs 3/4 MRG (Lagezuschlag), § 16 Abs 7 MRG (Befristungsabschlag) — GNR 10002531; RichtWG (Richtwerte je Bundesland) — GNR 10003166.
- **Vorgelagert:** `anwendungsbereich-mrg` muss **Vollanwendung** ergeben haben (sonst freier Mietzins).
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`.

## Worum geht es?

Nur in der **Vollanwendung** ist der Hauptmietzins beschränkt. Dann ist das richtige **System** zu wählen und die zulässige **Höhe** zu berechnen. Drei Systeme, plus Zu-/Abschläge und der Befristungsabschlag.

## Schritt-für-Schritt

1. **Ausstattungskategorie bestimmen (§ 15a MRG):** A / B / C / D nach Ausstattung (Bad/WC im Inneren, Heizung, brauchbarer Zustand). Kategorie D = Substandard.
2. **System wählen:**
   - **Angemessener Mietzins (§ 16 Abs 1):** für die taxativ genannten Fälle — u. a. **Geschäftsräumlichkeiten**, **Wohnungen der Kategorie A/B mit über 130 m² Nutzfläche** (binnen Frist vermietet), denkmalgeschützte Gebäude mit erheblichem Aufwand. Höhe = ortsüblich/angemessen.
   - **Richtwertmietzins (§ 16 Abs 2):** der **Regelfall** für brauchbare Wohnungen (Kategorie A, B oder C), die nicht unter Abs 1 fallen. **Richtwert** (je Bundesland, RichtWG, valorisiert) ± **Zu-/Abschläge** für werterhöhende/-mindernde Umstände (Lage, Stockwerk, Ausstattung, Erhaltungszustand, befristungsbedingte Umstände).
   - **Kategoriemietzins (§ 15a Abs 3):** fixer, valorisierter Betrag je Kategorie — v. a. für ältere Verträge/Substandard.
3. **Lagezuschlag prüfen (§ 16 Abs 3, 4 MRG):** nur bei **überdurchschnittlicher Lage**; zwingend ist die **schriftliche Bekanntgabe** der lagezuschlagsbegründenden Umstände an den Mieter **bei Vertragsabschluss** (§ 16 Abs 4) — fehlt sie, ist der Lagezuschlag **unwirksam**. (Gründerzeitviertel-Problematik beachten.)
4. **Befristungsabschlag (§ 16 Abs 7):** bei befristeten Hauptmietverträgen ist der zulässige Hauptmietzins um **25 %** zu **vermindern**.
5. **Zulässigen Höchst-Hauptmietzins** zusammenrechnen und an `mietzinsueberpruefung` übergeben.

## Typische Fehler / Kritik

- **Lagezuschlag ohne schriftliche Bekanntgabe** ansetzen → unwirksam (§ 16 Abs 4).
- **Befristungsabschlag (25 %) vergessen** bei befristeten Verträgen.
- **Falsches System:** Richtwert statt angemessen (oder umgekehrt) — die § 16 Abs 1-Fälle sind taxativ.
- **Kategorie falsch** eingestuft (Bad/WC/Heizung) → falscher Maßstab.
- **Deutsches Recht** (ortsübliche Vergleichsmiete, Mietspiegel) — gibt es in Österreich so nicht; hier Richtwert/Kategorie.

## Quellen und Stand 06/2026

- §§ 15a, 16 MRG (RIS, GNR 10002531); RichtWG (RIS, GNR 10003166); aktuelle Richtwerte je Bundesland sind valorisiert — **live prüfen**, nie aus Modellwissen beziffern.
- `references/methodik-buergerliches-recht.md`. Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)
- `§ 15a MRG` — Kategorien · `§ 16 Abs 1 MRG` — angemessen · `§ 16 Abs 2 MRG` — Richtwert · `§ 16 Abs 3/4 MRG` — Lagezuschlag · `§ 16 Abs 7 MRG` — Befristungsabschlag · `RichtWG` — Richtwerte

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen; 5. Senat)
- Richtwert/Zuschläge: `judikatur "Richtwert Zuschlag" --gericht OGH` (u. a. RIS-Justiz RS0117876, RS0047403 — live prüfen).
- Befristungsabschlag: `judikatur "Befristungsabschlag" --gericht OGH` (u. a. RIS-Justiz RS0131441 — live prüfen).

### Anwendung im Skill
Kategorie → System → Lagezuschlag (nur mit schriftlicher Bekanntgabe) → Befristungsabschlag → zulässiger Höchstmietzins. Aktuelle Richtwerte stets live.
