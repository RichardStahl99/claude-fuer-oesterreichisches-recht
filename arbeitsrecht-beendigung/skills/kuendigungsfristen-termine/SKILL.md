---
name: kuendigungsfristen-termine
description: "Berechnet Kündigungsfristen und -termine: Angestellte nach § 20 AngG (6 Wochen bis 5 Monate je Dienstdauer, Termin Quartalsende), Arbeiter nach § 1159 ABGB (seit 1.10.2021 an Angestellte angeglichen). Kollektivvertragliche Abweichungen beachten. Österreich, kein deutsches Recht."
---

# Kündigungsfristen und -termine

## Fachlicher Anker

- **Normen (über RIS prüfen):** § 20 AngG (Angestellte) — GNR 10008069 (Artikel 1); § 1159 ABGB (Arbeiter) — GNR 10001622; einschlägiger Kollektivvertrag.
- **Vorgelagert:** `beendigungsart` muss eine **Kündigung** ergeben haben.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`.

## Worum geht es?

Die ordentliche Kündigung ist nur wirksam, wenn **Frist und Termin** eingehalten sind. Beides hängt von der Dienstdauer und davon ab, **wer** kündigt — und seit 2021 sind Arbeiter weitgehend den Angestellten angeglichen.

## Schritt-für-Schritt

1. **Arbeitgeberkündigung von Angestellten (§ 20 Abs 2 AngG):** Frist gestaffelt nach **Dienstjahren**:
   - bis 2 Jahre: **6 Wochen**
   - ab 2 Jahren: **2 Monate**
   - ab 5 Jahren: **3 Monate**
   - ab 15 Jahren: **4 Monate**
   - ab 25 Jahren: **5 Monate**
   **Kündigungstermin:** zum **Quartalsende** (31. 3. / 30. 6. / 30. 9. / 31. 12.); zulässig vereinbar ist der **15.** oder **Letzte** jedes Kalendermonats (§ 20 Abs 3 AngG).
2. **Arbeitnehmerkündigung (Angestellte, § 20 Abs 4 AngG):** Frist **1 Monat** zum **Monatsletzten** (vertragliche Verlängerung möglich, höchstens auf das Maß der AG-Frist).
3. **Arbeiter (§ 1159 ABGB):** **seit 1. 10. 2021** weitgehend **an die Angestellten angeglichen** (gleiche gestaffelte Fristen und Quartalstermine). Achtung: Für bestimmte **Saisonbranchen** kann der Kollektivvertrag abweichende (kürzere) Regelungen vorsehen.
4. **Kollektivvertrag/Einzelvertrag prüfen:** KV kann die gesetzlichen Fristen modifizieren; günstigere Einzelvereinbarungen zulässig.
5. **Rechnen:** Frist ab Zugang der Kündigung; Endtermin auf den nächsten zulässigen Kündigungstermin legen. Wird Frist/Termin **nicht** gewahrt, verschiebt sich die Beendigung auf den nächsten korrekten Termin (Konversion) — keine fristlose Wirkung.

## Typische Fehler / Kritik

- **Kündigungstermin vergessen:** Frist allein genügt nicht — der **Quartalstermin** (bzw. 15./Letzter, wenn vereinbart) muss getroffen werden.
- **Arbeiter mit altem Recht behandeln:** seit 1. 10. 2021 § 1159 ABGB (Angleichung) — nicht mehr die alten kurzen Arbeiterfristen unterstellen (außer Saison-KV).
- **KV übersehen.**
- **Deutsches Recht:** keine „§ 622 BGB"-Fristen, kein „zum 15. oder Monatsende" als gesetzlicher Regeltermin — in Österreich Quartalsende (Angestellte).

## Quellen und Stand 06/2026

- § 20 AngG (RIS, GNR 10008069); § 1159 ABGB (RIS, GNR 10001622). KV jeweils einschlägig.
- `references/methodik-buergerliches-recht.md` Abschnitt 12. Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)
- `§ 20 AngG` — Fristen/Termine Angestellte · `§ 1159 ABGB` — Fristen Arbeiter (angeglichen)

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen; ObA-Senat)
- Kündigungstermin/Konversion: `judikatur "Kündigungstermin Angestelltengesetz" --gericht OGH` — live prüfen.

### Anwendung im Skill
Dienstjahre → Frist (§ 20 / § 1159) → richtiger Kündigungstermin (Quartalsende) → KV gegenprüfen.
