---
name: anschluss-routing
description: "Anschluss-Routing für das Gewährleistungs-Plugin: wählt nach einem Zwischenergebnis den nächsten Spezial-Skill (Regime, Mangel, Behelf, Frist) und dokumentiert die Router-Entscheidung mit Begründung. Österreich, kein deutsches Recht."
---

# Anschluss-Routing — Gewährleistung/Konsumentenschutz

## Einsatzlage

Wählt nach dem ersten Ergebnis die passende Vertiefung, Fristensicherung oder Dokumentenerstellung. Aufruf, wenn unklar ist, welcher Spezial-Skill als Nächstes trägt.

## Fachlandkarte dieses Plugins

- `einstieg-gewaehrleistung` — Anwalts-Dashboard / Sofort-Triage
- `regimewahl-vgg-vs-abgb` — anwendbares Regime (VGG vs §§ 922 ff ABGB)
- `mangel-und-vermutung` — Mangelbegriff + Vermutung/Beweislast
- `behelfshierarchie` — zulässiger Behelf in der richtigen Stufe
- `verjaehrung-und-fristen` — Gewährleistungs-/Verjährungsfristen

## Arbeitsweg

- **Ergebnis sichten:** Welche Frage ist beantwortet, welche bleibt offen oder entsteht neu?
- **Weiche stellen:**
  - Regime noch offen → `regimewahl-vgg-vs-abgb` (fast immer zuerst).
  - Regime geklärt, Mangel/Übergabezeitpunkt strittig → `mangel-und-vermutung`.
  - Mangel (+), Streit über Behelf → `behelfshierarchie`.
  - Frist-/Verjährungsfrage → `verjaehrung-und-fristen`.
  - Außerhalb des Plugins (Werkvertrag, Liegenschaft, Miete, FAGG-Rücktritt, Schadenersatz im Detail) → ausdrücklich verweisen, nicht hier behandeln.
- **Konkreten Folge-Skill mit Slug benennen** — nicht generisch „weitermachen".
- **Fristen vorab markieren** (`[Frist prüfen: …]`), nie aus Modellwissen finalisieren.
- **Mandantenkommunikation vorbereiten:** Was ist bis wann zu tun, welche Unterlagen, welche Risiken offen?

## Qualitätsanker

- Normen und Judikatur nach `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md` behandeln — keine GZ aus Modellwissen. **Zur Laufzeit ausführen (nicht nur verweisen):** die OGH-Linie über `python3 tools/ris_client.py linie "<Stichworte>" --gericht OGH [--gesetz <G> --paragraf <§>]` holen, eine genannte Geschäftszahl mit `python3 tools/ris_client.py leit <GZ>` gewichten und vor Übernahme älterer Entscheidungen die Aktualität prüfen — § 932 ABGB wurde durch das VGG (ab 1.1.2022) neu gefasst: `python3 tools/ris_client.py aktualitaet ABGB 932 --seit <Entscheidungsdatum>` bzw. `python3 tools/ris_client.py aktualitaet VGG 11 --seit <Entscheidungsdatum>`.
- Bei Zeitdruck zuerst Frist, Zuständigkeit (BG/LG, JN), Form (ERV) und Beweislast sichern.
- Eine Empfehlung ist eine Empfehlung; der Anwalt entscheidet.
