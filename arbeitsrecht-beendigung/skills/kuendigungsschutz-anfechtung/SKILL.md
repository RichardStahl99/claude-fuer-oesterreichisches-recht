---
name: kuendigungsschutz-anfechtung
description: "Prüft den allgemeinen Kündigungsschutz und die Anfechtung einer Arbeitgeberkündigung nach § 105 ArbVG: Sozialwidrigkeit oder verpöntes Motiv, das Betriebsrats-Vorverfahren, die Anfechtungsbefugnis (Betriebsrat/Arbeitnehmer) und die kurze 2-Wochen-Frist vor dem Arbeits- und Sozialgericht. Österreich, kein deutsches Recht (kein KSchG)."
---

# Kündigungsschutz und Anfechtung (§ 105 ArbVG)

## Fachlicher Anker

- **Normen (über RIS prüfen):** § 105 ArbVG (Anfechtung der Kündigung, Betriebsrat, Fristen) — GNR 10008329; § 120 ArbVG (Betriebsratsmitglieder); ASGG (Verfahren) — GNR 10000813; besonderer Schutz: MSchG, VKG, BEinstG (gesondert).
- **Vorgelagert:** `beendigungsart` (Arbeitgeber-**Kündigung**).
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`.

## Worum geht es?

Österreich hat **kein Kündigungsschutzgesetz** wie Deutschland. Der allgemeine Schutz wirkt über die **Anfechtung** der (an sich fristgerechten) Kündigung beim **Arbeits- und Sozialgericht**. Zwei Anfechtungsgründe, ein vorgeschaltetes Betriebsrats-Verfahren und eine **sehr kurze Frist** — das ist der kritische Pfad.

## Schritt-für-Schritt

1. **Betriebsrats-Vorverfahren (§ 105 Abs 1, 2 ArbVG):** Der Arbeitgeber muss den **Betriebsrat vor** Ausspruch der Kündigung **verständigen**. Der BR kann binnen **einer Woche** Stellung nehmen: **zustimmen**, **widersprechen** oder sich **nicht äußern**. (Ohne Betriebsrat entfällt das Vorverfahren.) **Achtung:** Stimmt der BR der Kündigung **ausdrücklich zu**, ist die Anfechtung wegen **Sozialwidrigkeit** (Abs 3 Z 2) **ausgeschlossen** — nur das verpönte Motiv (Abs 3 Z 1) bleibt anfechtbar (§ 105 Abs 6 ArbVG).
2. **Anfechtungsgrund prüfen:**
   - **Verpöntes Motiv (§ 105 Abs 3 Z 1 ArbVG):** Kündigung wegen eines verpönten Grundes — z. B. Gewerkschafts-/Betriebsratstätigkeit, offenbar nicht unberechtigte Geltendmachung von Ansprüchen, Gewerkschaftsmitgliedschaft.
   - **Sozialwidrigkeit (§ 105 Abs 3 Z 2 ArbVG):** Die Kündigung beeinträchtigt **wesentliche Interessen** des AN. Voraussetzungen: Betrieb dauernd **≥ 5 Arbeitnehmer**, AN bereits **≥ 6 Monate** beschäftigt (Wartezeit). Der AG kann **betriebsbedingte** oder **in der Person/im Verhalten** liegende Gründe einwenden; dann **Interessenabwägung** und ggf. **Sozialvergleich**.
3. **Anfechtungsbefugnis und Frist (§ 105 Abs 4 ArbVG):**
   - Hat der **BR widersprochen**: Auf Verlangen des AN kann der **Betriebsrat** binnen **einer Woche** anfechten. Tut er das nicht, kann der **Arbeitnehmer selbst** binnen **zwei Wochen nach Ablauf der dem BR offenstehenden Frist** anfechten.
   - Hat der BR **nicht widersprochen / sich nicht geäußert / kein BR vorhanden**: Der **Arbeitnehmer** kann **selbst** binnen **zwei Wochen ab Zugang der Kündigung** anfechten.
   - Anfechtung beim **Arbeits- und Sozialgericht**. **Die Frist ist kurz und nicht verlängerbar — zuerst sichern.**
4. **Besonderen Kündigungsschutz prüfen:** Betriebsratsmitglieder (§ 120 ArbVG), Schwangere/Eltern (MSchG/VKG), begünstigte Behinderte (BEinstG), Präsenz-/Zivildiener — hier ist die Kündigung schon **ohne vorherige gerichtliche/behördliche Zustimmung unwirksam** (anderes Schutzregime). 
5. **Rechtsfolge:** erfolgreiche Anfechtung → die Kündigung ist **rechtsunwirksam**, das Arbeitsverhältnis besteht fort.

## Typische Fehler / Kritik

- **2-Wochen-Frist versäumt:** der häufigste und fatalste Fehler.
- **Betriebsrats-Vorverfahren übersehen:** Anfechtungsbefugnis und Fristlauf hängen vom Verhalten des BR ab.
- **Sozialwidrigkeit ohne Schwellen prüfen:** Betrieb ≥ 5 AN und ≥ 6 Monate Beschäftigung sind Voraussetzung.
- **Deutsches Recht:** kein „§ 1 KSchG soziale Rechtfertigung / 3-Wochen-Klagefrist § 4 KSchG (DE)". In Österreich § 105 ArbVG, **2 Wochen**, ASG.

## Quellen und Stand 06/2026

- § 105 ArbVG (RIS, GNR 10008329); § 120 ArbVG; ASGG (GNR 10000813); MSchG/VKG/BEinstG gesondert.
- `references/methodik-buergerliches-recht.md` Abschnitt 12. Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)
- `§ 105 ArbVG` — Anfechtung (Sozialwidrigkeit/verpöntes Motiv), Betriebsrat, Fristen · `§ 120 ArbVG` — Schutz BR-Mitglieder

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen; ObA-Senat)
Zur Laufzeit ausführen (nicht nur verweisen):
- Sozialwidrigkeit: `python3 tools/ris_client.py linie "Kündigungsanfechtung Sozialwidrigkeit" --gericht OGH --gesetz ARBVG --paragraf 105` — OGH-Linie + Leitsätze nach Linientiefe (bereits gesichtet: RIS-Justiz RS0116698 — über `linie`/`leit` zu bestätigen, nicht aus Modellwissen).
- Verpöntes Motiv: `python3 tools/ris_client.py linie "verpöntes Motiv Kündigung" --gericht OGH --gesetz ARBVG --paragraf 105` (bereits gesichtet: RIS-Justiz RS0052037 — über `linie`/`leit` zu bestätigen).
- Gewicht einer konkret benannten GZ mit `leit <GZ>` prüfen (Stamm/Leitentscheidung? Linientiefe?); ältere Entscheidungen vor Übernahme per `aktualitaet ARBVG 105 --seit <Entscheidungsdatum>` auf Aktualität prüfen.

### Anwendung im Skill
BR-Vorverfahren → Anfechtungsgrund (Motiv/Sozialwidrigkeit + Schwellen) → Befugnis/**2-Wochen-Frist** → ASG. Frist zuerst sichern.
