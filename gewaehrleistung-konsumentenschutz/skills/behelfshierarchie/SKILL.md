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
3. **Sekundärbehelf (Stufe 2): Preisminderung** (relative Berechnungsmethode) **oder Wandlung** (Vertragsaufhebung; im VGG heißt sie **Vertragsauflösung**, § 13; ausgeschlossen bei bloß **geringfügigem** Mangel).
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
- `§ 932 ABGB` — Behelfe und Stufen · `§ 12 VGG` — primäre/sekundäre Behelfe · `§ 13 VGG` — Preisminderung/Vertragsauflösung

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen)
- Behelfshierarchie/Verbesserung: `tools/ris_client.py judikatur "Verbesserung Gewährleistung" --gericht OGH` (u. a. RIS-Justiz **RS0018921**, RS0018699 — vor Verwendung Leitsatz in RIS lesen).
- Wandlung/Preisminderung: `judikatur "Wandlung Preisminderung" --gericht OGH` (u. a. RS0126731, RS0127994 — live prüfen).

### Anwendung im Skill
Stufe 1 vor Stufe 2; Sprung nur mit Grund; Wandlung nicht bei Geringfügigkeit. Regime (VGG/ABGB) durchhalten.
