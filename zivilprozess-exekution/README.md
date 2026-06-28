# zivilprozess-exekution

Dritte Pilot-Vertikale: **Forderungsdurchsetzung im Zivilverfahren** (Österreich) — von der Zuständigkeit über das Mahnverfahren und die Rechtsmittel bis zur Exekution. Headline-Kompetenz ist — wie in den vorigen Plugins die Regime-/Anwendungsbereichs-Weiche — die **Zuständigkeits-Weiche (JN)**: welches Gericht, mit/ohne Anwaltspflicht, auf welchem Weg.

## Skills (Pipeline)

| Skill | Aufgabe |
|---|---|
| `einstieg-zivilverfahren` | Anwalts-Dashboard / Sofort-Triage (Rolle, Titel?, Streitwert/Zuständigkeit, Weg, Frist) |
| `zustaendigkeit-jn` | **Kern:** sachliche (BG/LG, Eigenzuständigkeiten) + örtliche Zuständigkeit (JN) + Anwaltspflicht (§ 27 ZPO) |
| `mahnverfahren` | Automatisches Mahnverfahren, Zahlungsbefehl (≤ 75.000 €), Einspruch (§ 248 ZPO, 4 Wochen) |
| `verfahrensgang-rechtsmittel` | Klage/Klagebeantwortung, Säumnis, Neuerungsverbot, Berufung/Revision/Rekurs + Fristen, ERV |
| `exekution-eo` | Exekutionstitel (§ 1 EO), Vollstreckbarkeit (§ 7), Exekutionsmittel (Fahrnis-/Gehalts-/Forderungsexekution) |
| `anschluss-routing` | Router zwischen den obigen Skills |

Dazu `…-schnellstart.md` und `…-werkstatt.md`.

## Zuschnitt

Bewusst eng: **streitige Geldforderung** (Klage → Mahnverfahren → Urteil → Exekution). **Nicht** abgedeckt (nur Verweis): Außerstreitverfahren (AußStrG), Insolvenz (IO), Sicherungsverfahren/einstweilige Verfügung im Detail, Strafverfahren (StPO), Verwaltungsverfahren (AVG/VwGVG), Zwangsversteigerung von Liegenschaften im Detail.

## Architektur (Phase-3-Muster)

Nutzt die geteilten Grundlagen `references/zitierweise.md` und `references/methodik-buergerliches-recht.md` **unverändert**; `tools/ris_client.py` erhielt die verifizierten Gesetzesnummern JN (10001697), ZPO (10001699) und EO (10001700) — der vorgesehene Erweiterungspunkt.

## Verifikation

Regressionsfall: `testakten/werklohn-mahnklage-exekution/`. Definition of Done: Aus der Test-Akte entsteht eine Triage, deren Zuständigkeits-/Anwaltspflicht-Zuordnung und jede Norm-/Judikaturfundstelle live über RIS auflöst.
