---
name: anwendungsbereich-mrg
description: "Kernkompetenz des Plugins: Bestimmt, ob ein Mietverhältnis der Vollanwendung, der Teilanwendung (§ 1 Abs 4 MRG) oder der Vollausnahme (§ 1 Abs 2 MRG) unterliegt — die Weiche, die darüber entscheidet, ob die Mietzinsbeschränkungen der §§ 16 ff MRG überhaupt gelten. Österreich, kein deutsches Recht."
---

# Anwendungsbereich des MRG (die Weiche)

## Fachlicher Anker

- **Normen (über RIS prüfen):** § 1 MRG — Abs 1 (Grundsatz), **Abs 2** (Vollausnahmen), **Abs 4** (Teilausnahmen) — GNR 10002531; §§ 1090 ff ABGB (allgemeines Bestandrecht, gilt in der Vollausnahme) — GNR 10001622.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`; keine GZ aus Modellwissen — `tools/ris_client.py`.
- **Methodik:** `references/methodik-buergerliches-recht.md` (Subsumtion; § 1 MRG ist Auslegungs- und Subsumtionsarbeit am Sachverhalt).

## Worum geht es?

§ 1 MRG kennt **drei Stufen**. Diese Stufe entscheidet, ob der Mietzins **beschränkt** ist:

- **Vollanwendung** (Grundsatz, § 1 Abs 1): Das gesamte MRG gilt, **inklusive Mietzinsbeschränkung** (§§ 15a, 16 ff) und Kündigungsschutz.
- **Teilanwendung** (§ 1 Abs 4): Nur **Teile** des MRG gelten (u. a. Kündigungsschutz) — die **Mietzinsbeschränkung gilt nicht**, der Hauptmietzins ist **frei vereinbar**.
- **Vollausnahme** (§ 1 Abs 2): Das MRG gilt **nicht**; es bleibt beim allgemeinen Bestandrecht der §§ 1090 ff ABGB — freie Mietzinsvereinbarung, kein MRG-Kündigungsschutz.

Wer die Stufe falsch bestimmt, prüft die Mietzinshöhe nach dem falschen (oder gar keinem) Maßstab.

## Wann brauchen Sie diese Skill?

- Immer am Anfang eines Mietzins-Mandats — vor `mietzinsbildung` und `mietzinsueberpruefung`.
- Wenn Baujahr/Baubewilligung, Zahl der Wohnungen, Förderung oder Art der Nutzung unklar sind.

## Schritt-für-Schritt (Entscheidungsbaum)

1. **Vollausnahme prüfen (§ 1 Abs 2 MRG)?** Liegt einer der taxativen Fälle vor — insbesondere:
   - Gebäude mit **nicht mehr als zwei selbständigen Wohnungen** (Ein-/Zweifamilienhaus, § 1 Abs 2 Z 5);
   - **Zweit-/Ferienwohnung** bzw. Vermietung zu Geschäftszwecken für höchstens sechs Monate;
   - **Dienst-/Werkswohnung**; Beherbergung.
   → **MRG gilt nicht.** Nur §§ 1090 ff ABGB, freie Mietzinsvereinbarung. Ende.
2. **Teilausnahme prüfen (§ 1 Abs 4 MRG)?** Insbesondere:
   - **Neubau:** Mietgegenstand in einem Gebäude, das aufgrund einer **nach dem 30. 6. 1953** erteilten Baubewilligung **ohne öffentliche Mittel** neu errichtet wurde (§ 1 Abs 4 Z 1);
   - durch **Dach(boden)ausbau/Aufbau** aufgrund einer **nach dem 31. 12. 2001** erteilten Baubewilligung neu geschaffene Wohnung (§ 1 Abs 4 Z 2);
   - durch **Zubau** neu errichteter Mietgegenstand.
   → **Nur Teile des MRG** (u. a. Kündigungsschutz §§ 29 ff). **Keine** Mietzinsbeschränkung — Hauptmietzins **frei** vereinbar (Grenze: § 879 ABGB, Wucher). Ende.
3. **Sonst: Vollanwendung.** §§ 15a, 16 ff MRG gelten → weiter zu `mietzinsbildung` (Richtwert/Kategorie/angemessen).

```
Vollausnahme (§1 Abs2: Ein-/Zweifam.-Haus, Ferien-/Dienstwohnung) ? --ja--> nur ABGB, freier Mietzins
        | nein
Teilausnahme (§1 Abs4: Neubau n. 30.6.1953 / Dachausbau n. 31.12.2001 / Zubau) ? --ja--> MRG teilweise, freier Mietzins
        | nein
   VOLLANWENDUNG --> Mietzins beschränkt (§§ 15a, 16 ff) --> mietzinsbildung
```

## Typische Fehler / Kritik

- **Mietzins prüfen, ohne den Anwendungsbereich zu klären.** Ohne Vollanwendung gibt es keine Höchstmietzins-Grenze.
- **Teilanwendung mit Vollanwendung verwechseln.** Der häufige „Altbau vs. Neubau"-Fehler: frei finanzierter Neubau (Baubewilligung nach 30. 6. 1953) ist **Teilanwendung** → freier Mietzins, **kein** Richtwert.
- **Vollausnahme übersehen** (Ein-/Zweifamilienhaus): dann gilt überhaupt nur das ABGB.
- **Deutsches Recht:** kein „§ 556d BGB", keine „Mietpreisbremse" — in Österreich Richtwert/Kategorie nach MRG.

## Quellen und Stand 06/2026

- § 1 Abs 1, 2, 4 MRG (RIS, GNR 10002531); §§ 1090 ff ABGB (RIS, GNR 10001622).
- `references/methodik-buergerliches-recht.md`. Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)
- `§ 1 Abs 1 MRG` — Grundsatz (Vollanwendung) · `§ 1 Abs 2 MRG` — Vollausnahmen · `§ 1 Abs 4 MRG` — Teilausnahmen · `§§ 1090 ff ABGB` — Bestandrecht (Vollausnahme)

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen; Wohnrecht = 5. Senat)
- Vollausnahme/Anwendungsbereich: `tools/ris_client.py judikatur "Ein- oder Zweifamilienhaus" --gericht OGH` bzw. `"Vollausnahme"` — den einschlägigen **5-Ob**-Rechtssatz live abrufen und Leitsatz lesen; **keine GZ aus Modellwissen** behaupten (Wohnrecht entscheidet der 5. Senat, nicht der 4. Senat).
- Reichweite der §§ 16 ff nur in Vollanwendung: am Gesetzestext argumentieren.

### Anwendung im Skill
Stufe zuerst (Vollausnahme → Teilausnahme → Vollanwendung), Ergebnis festhalten und an `mietzinsbildung`/`mietzinsueberpruefung` weitergeben.
