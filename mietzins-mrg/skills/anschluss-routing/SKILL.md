---
name: anschluss-routing
description: "Anschluss-Routing für das Mietzins-MRG-Plugin: wählt nach einem Zwischenergebnis den nächsten Spezial-Skill (Anwendungsbereich, Mietzinsbildung, Überprüfung, Verfahren) und dokumentiert die Router-Entscheidung mit Begründung. Österreich, kein deutsches Recht."
---

# Anschluss-Routing — Mietzins (MRG)

## Einsatzlage

Wählt nach dem ersten Ergebnis die passende Vertiefung, Fristensicherung oder den Verfahrensweg. Aufruf, wenn unklar ist, welcher Spezial-Skill als Nächstes trägt.

## Fachlandkarte dieses Plugins

- `einstieg-mietzins` — Anwalts-Dashboard / Sofort-Triage
- `anwendungsbereich-mrg` — Voll-/Teilanwendung/Vollausnahme (§ 1 MRG)
- `mietzinsbildung` — Richtwert/Kategorie/angemessen + Zuschläge (§§ 15a, 16)
- `mietzinsueberpruefung` — Überschreitung, Teilnichtigkeit, Rückforderung (§ 16 Abs 8)
- `verfahren-schlichtung-ausserstreit` — § 37/§ 39 MRG, Schlichtungsstelle → BG

## Arbeitsweg

- **Ergebnis sichten:** Welche Frage ist beantwortet, welche bleibt offen?
- **Weiche stellen:**
  - Anwendungsbereich offen → `anwendungsbereich-mrg` (fast immer zuerst).
  - Vollanwendung (+), Streit über Höhe → `mietzinsbildung`.
  - Zulässiger Höchstmietzins steht, Vereinbarung womöglich zu hoch → `mietzinsueberpruefung`.
  - Antrag/Zuständigkeit/Fristen → `verfahren-schlichtung-ausserstreit`.
  - Außerhalb des Plugins (Kündigung §§ 29 ff, Betriebskosten §§ 21 ff, Eintrittsrecht, WEG, ABGB-Bestandrecht außerhalb MRG) → ausdrücklich verweisen.
- **Konkreten Folge-Skill mit Slug benennen** — nicht generisch „weitermachen".
- **Fristen vorab markieren** (`[Frist prüfen: § 16 Abs 8 MRG / § 40 MRG]`), nie aus Modellwissen finalisieren.
- **Mandantenkommunikation vorbereiten:** Was ist bis wann zu tun, welche Unterlagen (Mietvertrag, Vorschreibungen, Baujahrnachweis)?

## Qualitätsanker

- Normen und Judikatur nach `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md` behandeln — keine GZ aus Modellwissen; Richtwerte stets live. **Zur Laufzeit ausführen (nicht nur verweisen):** die OGH-Linie über `python3 tools/ris_client.py linie "<Stichworte>" --gericht OGH --gesetz MRG --paragraf <§>` holen, eine benannte Geschäftszahl mit `leit <GZ>` gewichten und ältere Judikatur vor Verwendung mit `aktualitaet MRG <§> --seit <Entscheidungsdatum>` auf zwischenzeitliche Novellen prüfen (§ 16 MRG zuletzt 2026 novelliert).
- Bei Zeitdruck zuerst Frist (§ 16 Abs 8, § 40 MRG), Zuständigkeit (Schlichtungsstelle/BG) und Verfahrensart (Außerstreit) sichern.
- Eine Empfehlung ist eine Empfehlung; der Anwalt entscheidet.
