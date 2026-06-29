---
name: behelfshierarchie
description: "Bestimmt den zulässigen Gewährleistungsbehelf in der richtigen Stufe: primär Verbesserung/Austausch, sekundär Preisminderung/Wandlung (§ 932 ABGB bzw. §§ 12 f VGG), inkl. Voraussetzungen für den Sprung auf die zweite Stufe. Österreich, kein deutsches Recht."
---

# Behelfshierarchie der Gewährleistung

## Fachlicher Anker

- **Normen (über RIS prüfen):** § 932 ABGB (Behelfe, Stufen) — GNR 10001622; §§ 12, 13 VGG (Behelfe im Verbrauchergeschäft) — GNR 20011654.
- **Vorgelagert:** `regimewahl-vgg-vs-abgb` (Regime) und `mangel-und-vermutung` (Mangel +).
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`.

## Worum geht es?

Der Übernehmer kann nicht frei wählen. Die Behelfe stehen in einer **zweistufigen Hierarchie**: zuerst die **primären** Behelfe (Verbesserung oder Austausch), erst unter Zusatzvoraussetzungen die **sekundären** (Preisminderung oder Wandlung). ABGB (§ 932) und VGG (§§ 12 f) sind im Aufbau parallel, in Details unterschiedlich.

## Schritt-für-Schritt

1. **Primärbehelf (Stufe 1): Verbesserung (Reparatur) oder Austausch.**
   - Wahlrecht grundsätzlich beim Übernehmer, begrenzt durch Unmöglichkeit und Unverhältnismäßigkeit (§ 932 Abs 2/4 ABGB; § 12 VGG).
   - Pflicht des Übergebers: in angemessener Frist, unentgeltlich, ohne erhebliche Unannehmlichkeiten.
2. **Sprung auf Stufe 2 (Preisminderung oder Wandlung) — nur wenn ein Grund vorliegt:**
   - beide Primärbehelfe **unmöglich** oder für den Übergeber **unverhältnismäßig**; **oder**
   - der Übergeber verweigert sie / führt sie **nicht in angemessener Frist** durch; **oder**
   - Verbesserung/Austausch mit **erheblichen Unannehmlichkeiten** verbunden; **oder**
   - Unzumutbarkeit aus triftigen, in der Person des Übergebers liegenden Gründen.
3. **Sekundärbehelf (Stufe 2): Preisminderung** (relative Berechnungsmethode) **oder Wandlung** (Vertragsaufhebung; im VGG heißt sie **Vertragsauflösung**, § 15 VGG; ausgeschlossen bei bloß **geringfügigem** Mangel, § 12 Abs 5 VGG).
4. **Ergebnis** mit Begründung der Stufe dokumentieren und an `verjaehrung-und-fristen` übergeben (Behelf muss fristgerecht geltend gemacht werden).

```
Mangel (+) --> Stufe 1: Verbesserung / Austausch
                   | (unmöglich / unverhältnismäßig / verweigert /
                   |  nicht fristgerecht / erhebliche Unannehmlichkeiten)
                   v
              Stufe 2: Preisminderung   oder   Wandlung
                                               (nicht bei geringfügigem Mangel)
```

## Typische Fehler / Kritik

- **Sofort Wandlung verlangen.** Ohne Grund für den Stufensprung ist nur ein Primärbehelf zulässig.
- **Wandlung bei geringfügigem Mangel.** Ausgeschlossen — dann allenfalls Preisminderung.
- **Deutsches Recht:** „Rücktritt/Minderung nach §§ 437, 441 BGB", „Nacherfüllung" — falsche Rechtsordnung. In Österreich: Verbesserung/Austausch, Preisminderung/Wandlung.
- **Regime ignorieren:** Im B2C-Fall §§ 12 f VGG prüfen, nicht (nur) § 932 ABGB.

## Quellen und Stand 06/2026

- § 932 ABGB (RIS, GNR 10001622); §§ 12, 13 VGG (RIS, GNR 20011654).
- `references/methodik-buergerliches-recht.md` Abschnitt 10. Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)
- `§ 932 ABGB` — Behelfe und Stufen · `§ 12 VGG` — primäre/sekundäre Behelfe (Stufenfolge) · `§ 13 VGG` — Verbesserung/Austausch · `§ 14 VGG` — Preisminderung · `§ 15 VGG` — Vertragsauflösung

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen)
Zur Laufzeit ausführen (nicht nur verweisen):
- Behelfshierarchie/Verbesserung — OGH-Linie samt Leitsätzen nach Linientiefe holen: `python3 tools/ris_client.py linie "Verbesserung Gewährleistung" --gericht OGH --gesetz ABGB --paragraf 932` (Leitsatz vor Verwendung lesen; keine RS-Nummer aus Modellwissen übernehmen — die Hierarchie folgt primär aus § 932 ABGB / §§ 12 f VGG).
- Wandlung/Preisminderung — `python3 tools/ris_client.py linie "Wandlung Preisminderung" --gericht OGH --gesetz ABGB --paragraf 932` (Leitsatz vor Verwendung lesen; keine RS-Nummer aus Modellwissen übernehmen).
- Für eine konkret herangezogene Geschäftszahl `python3 tools/ris_client.py leit <GZ>` — ist sie Leitentscheidung (Stamm) und wie tief/gefestigt die Linie.
- **Aktualität (Pflicht vor Übernahme älterer Entscheidungen):** § 932 ABGB wurde durch das VGG (ab 1.1.2022) neu gefasst; Alt-Judikatur (vor 2022) vor Verwendung flaggen mit `python3 tools/ris_client.py aktualitaet ABGB 932 --seit <Entscheidungsdatum>` bzw. im B2C-Fall `python3 tools/ris_client.py aktualitaet VGG 11 --seit <Entscheidungsdatum>` (erkennt die Gesetzesänderung nach dem Entscheidungsdatum, beurteilt sie nicht).

### Anwendung im Skill
Stufe 1 vor Stufe 2; Sprung nur mit Grund; Wandlung nicht bei Geringfügigkeit. Regime (VGG/ABGB) durchhalten. Alt-Judikatur zu § 932 ABGB vor Übernahme per `aktualitaet ABGB 932 --seit <Entscheidungsdatum>` gegen die VGG-Neufassung prüfen.
