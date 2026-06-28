# gewaehrleistung-konsumentenschutz (Skelett)

Pilot-Vertikale dieses Repositorys. **Noch ohne Skills** — dieses Plugin ist in Phase 0 als Skelett angelegt, damit der Marketplace lädt. Die Skill-Inhalte entstehen in **Phase 2**.

## Geplanter Zuschnitt (Phase 2)

Eng begrenzt auf **Gewährleistung bei Waren**, eine Regimewahl als Kernkompetenz:

- **VGG** (Verbrauchergewährleistungsgesetz, ab 1.1.2022) als *lex specialis* für B2C-Warenkauf — verdrängt die §§ 922 ff ABGB; Vermutung der Mangelhaftigkeit **1 Jahr** (§ 11 VGG), Behelfshierarchie §§ 12–13 VGG.
- **§§ 922 ff ABGB** als Auffangregime (B2B, C2C, Liegenschaften): Mangelbegriff § 922, Vermutung § 924, Behelfshierarchie § 932, Verjährung § 933 (2/3 Jahre).
- **Kein FAGG/Rücktrittsrecht im Piloten** — bewusst ausgeklammert (eigene Doktrin, testet den Kern nicht).

Geplante Skills (Arbeitstitel): `einstieg-gewaehrleistung` (Anwalts-Dashboard-Triage), `regimewahl-vgg-vs-abgb`, `mangel-pruefung`, `behelfshierarchie`, `verjaehrung-fristen`.

## Grundlagen

Dieses Plugin baut zwingend auf den geteilten Referenzen auf:
`references/methodik-buergerliches-recht.md`, `references/zitierweise.md`, `references/ris-quellen.md`, `references/quellenhygiene.md`, `references/anwalts-dashboard-konvention.md`.

Definition of Done (Phase 2): Eine reale österreichische Test-Akte (Verbraucher-Mangelfall) erzeugt ein Triage-Dashboard, dessen **jede** Norm- und Judikaturfundstelle live über RIS auflöst und dessen Regimezuordnung (VGG vs. ABGB) korrekt ist.
