---
name: zustaendigkeit-jn
description: "Kernkompetenz des Plugins: Bestimmt die sachliche Zuständigkeit (Bezirksgericht ≤ 15.000 € bzw. Eigenzuständigkeit / Landesgericht), die örtliche Zuständigkeit (allgemeiner Gerichtsstand, Gerichtsstandsvereinbarung) nach der JN und die Anwaltspflicht (§ 27 ZPO). Österreich, kein deutsches Recht."
---

# Zuständigkeit (JN) und Anwaltspflicht

## Fachlicher Anker

- **Normen (über RIS prüfen):** § 49 JN (BG, Wert- und Eigenzuständigkeit), § 50 JN (Gerichtshof/LG), §§ 65 ff, 66 JN (allgemeiner Gerichtsstand), § 104 JN (Gerichtsstandsvereinbarung/Prorogation) — GNR 10001697; § 27 ZPO (Anwaltspflicht) — GNR 10001699.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`; keine GZ aus Modellwissen — `tools/ris_client.py`.

## Worum geht es?

Bevor geklagt wird, müssen **drei** Fragen beantwortet sein: **sachliche** Zuständigkeit (welche Gerichtsart?), **örtliche** Zuständigkeit (welches konkrete Gericht?) und **Anwaltspflicht** (muss/kann die Partei sich selbst vertreten?). Die JN ist das eigene österreichische Zuständigkeitsgesetz — sie hat **kein** direktes deutsches Gegenstück und ist hier zentral.

## Schritt-für-Schritt

1. **Sachliche Zuständigkeit (§§ 49, 50 JN):**
   - **Eigenzuständigkeit des BG** (wertunabhängig, § 49 Abs 2 JN): u. a. **Bestandstreitigkeiten** (Miete) und bestimmte ehe-/familienrechtliche Streitsachen. Fällt der Streit darunter → **BG**, egal welcher Wert. (Abstammungs- und viele Familiensachen sind allerdings **Außerstreit** — § 104a JN/AußStrG — bleiben aber beim BG.)
   - Sonst **Wertzuständigkeit:** Streitwert **bis 15.000 € → BG**; **über 15.000 € → Landesgericht** (Gerichtshof, § 50 JN). Eigenzuständigkeiten des LG (z. B. Amtshaftung, gewerblicher Rechtsschutz) beachten.
2. **Örtliche Zuständigkeit:** **allgemeiner Gerichtsstand** des Beklagten (Wohnsitz/gewöhnlicher Aufenthalt natürlicher Personen, § 66 JN; Sitz juristischer Personen, § 75 JN). Daneben **Wahlgerichtsstände** (z. B. Gerichtsstand des Erfüllungsorts) und die **Gerichtsstandsvereinbarung** (§ 104 JN, Prorogation — schriftlich nachweisbar).
3. **Anwaltspflicht (§ 27 ZPO):**
   - **Bezirksgericht:** **relative** Anwaltspflicht — Anwaltszwang erst bei Streitwert **über 5.000 €**; darunter kann die Partei selbst auftreten.
   - **Landesgericht:** **absolute** Anwaltspflicht in allen Verfahren.
4. **Ergebnis** (Gericht + Anwaltspflicht) festhalten und an `mahnverfahren`/`verfahrensgang-rechtsmittel` durchreichen.

```
Eigenzuständigkeit BG (§49 Abs2: Bestand, Familie ...) ? --ja--> BG (wertunabhängig)
        | nein
Streitwert ≤ 15.000 € ?  --ja--> BG     --nein--> LG (§ 50)
Anwaltspflicht: BG > 5.000 € relativ | LG absolut (§ 27 ZPO)
Örtlich: Wohnsitz/Sitz Beklagter (§§ 66, 75) | Gerichtsstandsvereinbarung (§ 104)
```

## Typische Fehler / Kritik

- **Eigenzuständigkeit übersehen:** Bestand-/Familiensachen sind wertunabhängig BG — nicht nach Streitwert einordnen.
- **Anwaltspflicht falsch:** beim BG erst über 5.000 €; beim LG immer. Nicht die deutschen Wertgrenzen unterstellen.
- **Örtliche Zuständigkeit am Kläger** statt am Beklagten orientiert.
- **Deutsches Recht:** keine „sachliche Zuständigkeit nach §§ 23, 71 GVG", kein „Streitwert 5.000 € AG/LG" — in Österreich JN + § 27 ZPO, Grenze 15.000 €.

## Quellen und Stand 06/2026

- §§ 49, 50, 66, 75, 104 JN (RIS, GNR 10001697); § 27 ZPO (RIS, GNR 10001699).
- `references/methodik-buergerliches-recht.md` Abschnitt 12. Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)
- `§ 49 JN` — BG (Wert/Eigenzuständigkeit) · `§ 50 JN` — LG · `§ 66 JN` — allgemeiner Gerichtsstand · `§ 104 JN` — Gerichtsstandsvereinbarung · `§ 27 ZPO` — Anwaltspflicht

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen)
- Gerichtsstandsvereinbarung/Zuständigkeit: `judikatur "Gerichtsstandsvereinbarung Zuständigkeit" --gericht OGH` (u. a. RIS-Justiz RS0118239, RS0018023 — live prüfen).

### Anwendung im Skill
Sachlich (Eigenzuständigkeit vor Wert) → örtlich → Anwaltspflicht. Ergebnis festhalten und weitergeben.
