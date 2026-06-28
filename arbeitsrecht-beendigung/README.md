# arbeitsrecht-beendigung

Vierte Pilot-Vertikale: **Beendigung des Arbeitsverhältnisses** (Österreich). Bewusst gewählt, weil das österreichische Arbeitsrecht hier **strukturell stark von Deutschland abweicht**: Es gibt **kein einheitliches Kündigungsschutzgesetz** — der Schutz ergibt sich aus AngG, ABGB (§ 1159), dem **ArbVG (§ 105)** mit der Rolle des **Betriebsrats** und dem Verfahren vor dem **Arbeits- und Sozialgericht (ASGG)**. Headline-Kompetenz ist — wie in den vorigen Plugins die Regime-/Anwendungsbereichs-/Zuständigkeitsweiche — die **Beendigungsart**.

## Skills (Pipeline)

| Skill | Aufgabe |
|---|---|
| `einstieg-arbeitsrecht` | Anwalts-Dashboard / Sofort-Triage (Rolle, Beendigungsart, Frist, Anfechtung, Ansprüche) |
| `beendigungsart` | **Kern:** Kündigung / Entlassung / einvernehmlich / Zeitablauf / Austritt / Probezeit |
| `kuendigungsfristen-termine` | § 20 AngG (Angestellte), § 1159 ABGB (Arbeiter, seit 1.10.2021 angeglichen), Kündigungstermin |
| `kuendigungsschutz-anfechtung` | Allgemeiner Kündigungsschutz § 105 ArbVG (Sozialwidrigkeit/verpöntes Motiv), Betriebsrat, 2-Wochen-Frist, ASG |
| `beendigungsansprueche` | Abfertigung neu (BMSVG) / alt (§ 23 AngG), Urlaubsersatzleistung (§ 10 UrlG), Kündigungsentschädigung (§ 29 AngG) |
| `anschluss-routing` | Router zwischen den obigen Skills |

Dazu `…-schnellstart.md` und `…-werkstatt.md`.

## Zuschnitt

Bewusst eng: **Beendigung** des Arbeitsverhältnisses. **Nicht** abgedeckt (nur Verweis): laufendes Arbeitsverhältnis (Entgelt, Arbeitszeit AZG, Urlaub im Detail), Gleichbehandlung (GlBG), Betriebsübergang (AVRAG), Kollektivvertragsrecht im Detail, Sozialversicherung, besonderer Kündigungsschutz im Detail (MSchG/BEinstG).

## Architektur (Phase-3-Muster)

Nutzt die geteilten Grundlagen `references/zitierweise.md` und `references/methodik-buergerliches-recht.md` **unverändert**; `tools/ris_client.py` erhielt die verifizierten Gesetzesnummern AngG (10008069, mit Artikel-1-Adressierung), ArbVG (10008329), BMSVG (20002088), ASGG (10000813), UrlG (10008376).

## Verifikation

Regressionsfall: `testakten/kuendigung-angestellte-anfechtung/`. Definition of Done: Aus der Test-Akte entsteht eine Triage, deren Beendigungsart-/Anfechtungs-Zuordnung und jede Norm-/Judikaturfundstelle live über RIS auflöst.
