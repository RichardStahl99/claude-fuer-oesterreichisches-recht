# mietzins-mrg

Zweite Pilot-Vertikale: **Mietzinsrecht nach dem MRG** in Österreich. Headline-Kompetenz ist — wie beim Gewährleistungs-Plugin die Regimewahl — eine **Anwendungsbereichs-Weiche**: Voll- / Teilausnahme / Vollausnahme des MRG (§ 1), die darüber entscheidet, ob die Mietzinsbeschränkungen überhaupt gelten.

## Skills (Pipeline)

| Skill | Aufgabe |
|---|---|
| `einstieg-mietzins` | Anwalts-Dashboard / Sofort-Triage (Rolle, Anwendungsbereich, Mietzinssystem, Frist, Verfahren) |
| `anwendungsbereich-mrg` | **Kern:** Vollanwendung / Teilanwendung (§ 1 Abs 4) / Vollausnahme (§ 1 Abs 2 MRG) |
| `mietzinsbildung` | Richtwert (§ 16 Abs 2 + RichtWG), Kategorie (§ 15a), angemessener Mietzins (§ 16 Abs 1), Zuschläge, Befristungsabschlag (§ 16 Abs 7) |
| `mietzinsueberpruefung` | Zulässigkeit, Überschreitung & Teilnichtigkeit (§ 16 Abs 8 MRG), Rückforderung, Präklusivfristen |
| `verfahren-schlichtung-ausserstreit` | § 37 MRG Außerstreitverfahren, sukzessive Zuständigkeit der Schlichtungsstelle (§ 39 MRG) |
| `anschluss-routing` | Router zwischen den obigen Skills |

Dazu `…-schnellstart.md` und `…-werkstatt.md`.

## Zuschnitt

Bewusst eng: **Mietzins** in der Vollanwendung des MRG. **Nicht** abgedeckt (nur Verweis): Kündigung/Beendigung (§§ 29 ff MRG), Eintritts-/Abtretungsrechte, Betriebskosten (§§ 21 ff), Geschäftsraummiete im Detail, Wohnungseigentum (WEG), allgemeines Bestandrecht außerhalb des MRG (§§ 1090 ff ABGB).

## Architektur-Beweis (Phase 3)

Dieses Plugin nutzt die geteilten Grundlagen **unverändert**: `references/zitierweise.md` und `references/methodik-buergerliches-recht.md` werden **nicht** angepasst; lediglich `tools/ris_client.py` erhält die verifizierten Gesetzesnummern MRG (10002531) und RichtWG (10003166) — der vorgesehene Erweiterungspunkt. Damit ist gezeigt: Motor und Rechtsschicht sind sauber getrennt.

## Verifikation

Regressionsfall: `testakten/altbau-richtwert-ueberschreitung/`. Definition of Done: Aus der Test-Akte entsteht eine Triage, deren Anwendungsbereichs-Zuordnung (Vollanwendung) und jede Norm-/Judikaturfundstelle live über RIS auflöst.
