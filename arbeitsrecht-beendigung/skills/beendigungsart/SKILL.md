---
name: beendigungsart
description: "Kernkompetenz des Plugins: Ordnet die Beendigung des Arbeitsverhältnisses der richtigen Art zu — Kündigung (ordentlich), Entlassung (außerordentlich, § 27 AngG), vorzeitiger Austritt (§ 26 AngG), einvernehmliche Auflösung, Zeitablauf oder Auflösung in der Probezeit (§ 19 AngG). Die Art steuert Frist, Anfechtung und Ansprüche. Österreich, kein deutsches Recht."
---

# Beendigungsart (die Weiche)

## Fachlicher Anker

- **Normen (über RIS prüfen):** § 19 AngG (Probezeit/Befristung), § 20 AngG (Kündigung), § 26 AngG (vorzeitiger Austritt), § 27 AngG (Entlassungsgründe) — GNR 10008069 (Artikel 1); § 1159 ABGB (Arbeiter); § 105 ArbVG (Anfechtung der Kündigung).
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`; keine GZ aus Modellwissen — `tools/ris_client.py`.

## Worum geht es?

Die **Art** der Beendigung entscheidet alles Weitere: Fristen/Termine, Anfechtbarkeit und die Geldansprüche. Anders als in Deutschland ist die **ordentliche Kündigung in Österreich grundsätzlich nicht begründungspflichtig** — der Schutz wirkt über die **Anfechtung** (§ 105 ArbVG), nicht über ein Kündigungsschutzgesetz.

## Schritt-für-Schritt (Einordnung)

1. **Wer beendet?** Arbeitgeber oder Arbeitnehmer.
2. **Probezeit (§ 19 Abs 2 AngG)?** In den ersten **max. 1 Monat** (wenn vereinbart) kann **jederzeit ohne Frist und Grund** gelöst werden. → kurze Prüfung, dann Ende.
3. **Befristetes Arbeitsverhältnis?** Endet durch **Zeitablauf** ohne Kündigung (Kettenbefristungen können unzulässig sein).
4. **Einvernehmliche Auflösung?** Beidseitige Vereinbarung — kein Anfechtungsschutz, aber Beratungs-/Übereilungsschutz beachten.
5. **Sonst Beendigung durch einseitige Erklärung:**
   - **Kündigung (ordentlich):** Beendigung **mit** Frist und Termin (§ 20 AngG / § 1159 ABGB). AG-Kündigung **ohne Begründungspflicht**, aber **anfechtbar** (§ 105 ArbVG) → `kuendigungsschutz-anfechtung`.
   - **Entlassung (außerordentlich, fristlos durch AG):** nur bei **wichtigem Grund** (§ 27 AngG, demonstrativ [„insbesondere"] — z. B. Vertrauensunwürdigkeit, beharrliche Pflichtverletzung). **Unberechtigte** Entlassung → **Kündigungsentschädigung** (§ 29 AngG).
   - **Vorzeitiger Austritt (durch AN, fristlos):** nur bei **wichtigem Grund** (§ 26 AngG — z. B. Entgeltvorenthaltung, Gesundheitsgefährdung). Berechtigter Austritt → Ansprüche wie bei AG-Kündigung; unberechtigter Austritt → Schadenersatz des AG.
6. **Ergebnis** (Beendigungsart + Datum + Rolle) festhalten und an `kuendigungsfristen-termine` / `kuendigungsschutz-anfechtung` / `beendigungsansprueche` durchreichen.

```
AG/AN ?  --> Probezeit (§19, ≤1 Monat) ? --ja--> jederzeit lösbar
                | nein
        befristet ? --ja--> Zeitablauf      einvernehmlich ? --ja--> Vereinbarung
                | nein einseitig
   Kündigung (ordentl., Frist+Termin §20/§1159; anfechtbar §105)
   Entlassung (fristlos AG, §27; unberechtigt -> §29 Kündigungsentschädigung)
   Austritt   (fristlos AN, §26; berechtigt -> Ansprüche wie AG-Kündigung)
```

## Typische Fehler / Kritik

- **Kündigung mit Entlassung verwechseln:** Kündigung = mit Frist; Entlassung = fristlos aus wichtigem Grund. Folgen (Frist, Entschädigung) unterscheiden sich grundlegend.
- **Begründungspflicht der Kündigung unterstellen:** Die ordentliche Kündigung braucht in Österreich **keinen** Grund (Schutz über § 105 ArbVG).
- **Deutsches Recht:** kein „KSchG, ordentliche/außerordentliche Kündigung § 622/§ 626 BGB", keine „soziale Rechtfertigung § 1 KSchG (DE)". In Österreich AngG/ABGB + Anfechtung § 105 ArbVG.
- **Probezeit überdehnen:** max. 1 Monat (§ 19 Abs 2 AngG).

## Quellen und Stand 06/2026

- §§ 19, 20, 26, 27, 29 AngG (RIS, GNR 10008069); § 1159 ABGB (RIS, GNR 10001622); § 105 ArbVG (RIS, GNR 10008329).
- `references/methodik-buergerliches-recht.md`. Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)
- `§ 19 AngG` — Probezeit/Befristung · `§ 20 AngG` — Kündigung · `§ 26 AngG` — Austritt · `§ 27 AngG` — Entlassung · `§ 29 AngG` — Kündigungsentschädigung · `§ 105 ArbVG` — Anfechtung

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen; ObA-Senat)
Zur Laufzeit ausführen (nicht nur verweisen):
- Entlassungsgründe/Austritt: `python3 tools/ris_client.py linie "Entlassung wichtiger Grund" --gericht OGH --gesetz ANGG --paragraf 27` — OGH-Linie + Leitsätze nach Linientiefe; keine GZ aus Modellwissen.
- Eine konkret herangezogene Geschäftszahl mit `leit <GZ>` prüfen (Leitentscheidung/Stamm? wie gefestigt die Linie?).
- Vor Übernahme älterer Entscheidungen Aktualität prüfen: `aktualitaet <Gesetz> <§> --seit <Entscheidungsdatum>` — für Arbeiter besonders `aktualitaet ABGB 1159 --seit <Datum>` (Angleichung seit 1.10.2021).

### Anwendung im Skill
Art zuerst (Probezeit/Befristung/einvernehmlich → Kündigung/Entlassung/Austritt), Ergebnis festhalten und an die Folge-Skills weitergeben. Bei AG-Kündigung sofort die Anfechtungsfrist im Blick behalten; bei Arbeitern Alt-Judikatur per `aktualitaet ABGB 1159 --seit <Datum>` gegen die Angleichung (1.10.2021) prüfen.
