# gewaehrleistung-konsumentenschutz

Pilot-Vertikale dieses Repositorys: **Gewährleistung bei Waren** in Österreich, mit der Regimewahl **VGG vs. §§ 922 ff ABGB** als Kernkompetenz.

## Skills (Pipeline)

| Skill | Aufgabe |
|---|---|
| `einstieg-gewaehrleistung` | Anwalts-Dashboard / Sofort-Triage (Rolle, Regime, Mangel, Behelf, Frist) |
| `regimewahl-vgg-vs-abgb` | **Kern:** VGG (B2C, ab 1.1.2022) als lex specialis vs. §§ 922 ff ABGB |
| `mangel-und-vermutung` | Mangelbegriff + Vermutung (§ 924 ABGB 6 Mon. / § 11 VGG 1 J.) |
| `behelfshierarchie` | Verbesserung/Austausch → Preisminderung/Wandlung (§ 932 ABGB / §§ 12 f VGG) |
| `verjaehrung-und-fristen` | § 933 ABGB (2/3 J.) / § 10 VGG; Fristbeginn = Übergabe |
| `anschluss-routing` | Router zwischen den obigen Skills |

Dazu `…-schnellstart.md` (Kurzfassung zum Einkopieren in beliebige LLMs) und `…-werkstatt.md` (ausführlich).

## Zuschnitt

Bewusst eng: nur Warenkauf. **Nicht** abgedeckt (nur Verweis): Werkvertrag, Liegenschaft/WEG, Miete (MRG), FAGG-Rücktrittsrecht, Produkthaftung (PHG), vertragliche Garantie.

## Grundlagen

Baut auf den geteilten Referenzen auf: `references/methodik-buergerliches-recht.md`, `zitierweise.md`, `ris-quellen.md`, `quellenhygiene.md`, `anwalts-dashboard-konvention.md`.

## Verifikation

Regressionsfall: `testakten/geschirrspueler-mangel/`. Definition of Done: Aus der Test-Akte entsteht ein Triage-Dashboard, dessen **jede** Norm-/Judikaturfundstelle live über RIS auflöst und dessen Regimezuordnung (VGG vs. ABGB) korrekt ist.
