---
name: aenderungsregime
description: "Gate-Skill: trennt einvernehmliche Vertragsänderung, Änderungskündigung und konkludente Änderung (§ 863 ABGB); klärt, was ohne Unterschrift gilt. Kein deutsches Recht."
---

# Änderungsregime — Gate-Skill Vertragsänderung

## Fachlicher Anker

- **Normen (über RIS auflösen, `tools/ris_client.py`):** § 863, § 914, § 915 ABGB (Konsens, Auslegung, Unklarheitenregel) — GNR 10001622; §§ 861, 883 ABGB (Konsensualprinzip/Formfreiheit: Arbeitsverträge sind grundsätzlich formfrei; Bindung durch Annahme) — GNR 10001622; § 1163 ABGB (Dienstzettel-Pflicht seit 1.7.2024; vormals § 2 AVRAG — Formerfordernis für Dienstzettel, nicht für den Vertrag selbst) — GNR 10001622; § 20 AngG (Kündigungsfristen — relevant, weil die Änderungskündigung eine echte Kündigung ist: 6 Wochen bis 5 Monate, zum Quartal) — GNR 10008069 (Artikel 1); § 101, § 105, § 107 ArbVG (Mitwirkung bei Versetzungen/Verschlechterungsschutz [§ 101 — kollektiver Prong, setzt Betriebsrat voraus]; Kündigungsanfechtung [§ 105]; Anfechtung durch den Arbeitnehmer im betriebsratslosen Betrieb [§ 107 iVm § 105 Abs 4a]) — GNR 10008329.
- **Kernsatz (RIS-Justiz RS0109380, OGH 12.02.1998, 8 ObA 35/98z):** „Die einzige Möglichkeit, die Verschlechterung der Entgeltbedingungen rechtlich zulässig vorzunehmen, ist neben einer einvernehmlichen Vertragsänderung die Änderungskündigung." Ohne Unterschrift oder wirksame Änderungskündigung läuft der Bestandsvertrag weiter.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md`. Keine GZ aus Modellwissen — nur RIS-verifizierte Fundstellen verwenden.

## Einsatzlage

Dieser Gate-Skill klärt als erste Weiche, **auf welchem von drei Wegen** eine Änderung des aufrechten Arbeitsverhältnisses rechtlich vollzogen wird oder werden soll. Die Wahl des Weges bestimmt Formerfordernis, Zustimmungspflicht, Fristlauf und verfügbare Hebel.

**Drei Wege — kurze Merktafel:**

| Weg | Wesenskern | Zustimmung des AN | Folge ohne Zustimmung |
|---|---|---|---|
| **Einvernehmliche Vertragsänderung** | Vertragliche Einigung; Schweigen ist keine Annahme (RIS-Justiz RS0047273) | Ausdrücklich oder schlüssig erforderlich | Änderung unwirksam; Bestandsvertrag gilt |
| **Änderungskündigung** | Echte Kündigung + Angebot neuer Bedingungen im selben Akt; § 101 ArbVG bleibt bei verschlechternder Versetzung gewahrt (RIS-Justiz RS0131210, OGH 28.06.2016, 8 ObA 63/15w) — **§ 101 ArbVG ist der kollektive Prong** (setzt Betriebsrat voraus); Verschlechterungsbegriff RS0051209 (OGH 4 Ob 79/85): jede Änderung zum Nachteil des AN, materiell + immateriell, Entgelt im weitesten Sinn. Kein BR: § 879 Abs 3 ABGB als Individualschutz. Anfechtbarkeit wegen Sozialwidrigkeit nach § 105 Abs 3 Z 2 ArbVG (Linie RS0051746, zuletzt OGH 9 ObA 59/23a) | AN kann Angebot annehmen oder ablehnen | Lehnt AN ab: Kündigung wirkt; Arbeitsverhältnis endet mit Fristablauf |
| **Konkludente Änderung (§ 863 ABGB)** | Schlüssiges Verhalten beider Parteien (Duldung + Auszahlung); vorbehaltlose wiederholte Erhöhung bindet (RIS-Justiz RS0014526); Empfängerhorizont entscheidend (RIS-Justiz RS0014154; OGH 8 ObA 33/21t) | Kein Vorbehalt bei Annahme der Leistung = schlüssige Zustimmung | Verschlechterung wirkt nicht konkludent zurück; Vorbehalt nach Zufluss nicht mehr nachholbar (§ 863 ABGB + RS0042828 [strenge Anforderungen an schlüssige Erklärungen] + RS0014154 [Empfängerhorizont]; bloße Entgegennahme = kein Erklärungswert: RS0047273 [T2]) |

**Nicht für:** Beendigung des Arbeitsverhältnisses (→ Skill `einstieg-arbeitsrecht`), Betriebsübergang, Sozialversicherungsfragen oder reine Klauselprüfung (→ `klausel-inhaltskontrolle`).

## Sofort-Triage

Drei Fragen klären das Regime — vor jeder weiteren Analyse stellen:

| Frage | Prüfpunkt | Konsequenz |
|---|---|---|
| **Welcher Weg?** | Liegt ein schriftliches Änderungsangebot vor? Wurde eine Kündigung ausgesprochen? Oder wurde eine neue Bedingung einfach praktiziert (Duldung + Zahlung)? | Einordnung in Weg 1, 2 oder 3 (→ Merktafel oben) |
| **Gab es einen Vorbehalt?** | Hat der AN die geänderte Leistung unter ausdrücklichem Vorbehalt (am besten schriftlich) angenommen oder ohne jeden Kommentar entgegengenommen? | Ohne Vorbehalt: schlüssige Zustimmung nach § 863 ABGB möglich; **Vorbehalt muss vor oder bei der Annahme gesetzt werden** |
| **Ist die Erhöhung/Änderung schon zugeflossen?** | Wurde das geänderte Entgelt bereits ausbezahlt? Wie viele Male? | Mehrmalige vorbehaltlose Annahme → konkludente Bindung (RS0014526); Verschlechterung ohne Vorbehalt nicht mehr rückwirkend möglich |

## Risiko-Ampel

- 🔴 **Kein Vorbehalt, Zahlung bereits zugeflossen** — Konkludente Bindung an die geänderten (oft günstigeren) Bedingungen ist wahrscheinlich eingetreten; nachträglicher Vorbehalt ohne Wirkung. Sofortiger Handlungsbedarf.
- 🔴 **Änderungskündigung ausgesprochen, Anfechtungsfrist läuft** — **§ 107 ArbVG** (iVm § 105 Abs 4a): im betriebsratslosen, aber betriebsratspflichtigen Betrieb kann der Arbeitnehmer selbst anfechten; **2 Wochen** Anfechtungsfrist ab Zugang der Kündigung. Frist nicht verlängerbar — zuerst sichern, dann prüfen.
- 🟠 **Änderung angekündigt, kein formeller Abschluss** — Prüfen, ob Änderungskündigung oder bloßes Angebot vorliegt; Vorbehalt sichern bevor Leistung angenommen wird.
- 🟠 **Mündlicher Vorbehalt oder unklare Dokumentation** — Beweisrisiko. Schriftliche Bestätigung des Vorbehalts nachholen; Unklarheit geht nach § 915 ABGB zulasten des Verwenders (i.d.R. Arbeitgeber).
- 🟢 **Schriftlicher Vorbehalt vor Annahme gesetzt, dokumentiert** — Keine schlüssige Bindung; Prüfung der Änderungsklausel kann geordnet erfolgen.

## Anschluss-Skill-Router

| Wenn der Fall trägt … | dann Skill | Erwartung |
|---|---|---|
| Klauseltext prüfen (Bestand oder Angebot; § 879 Abs 3 ABGB) | `klausel-inhaltskontrolle` | Bewertung: wirksam / sittenwidrig / Grenzfall |
| Änderungskündigung ausgesprochen; Frist läuft oder Austritt erwogen | `austritt-backstop-und-hebel` | § 26 AngG Austrittsrecht + Druckmittel / Vorbehaltsstrategie |
| Weiterleitung nach Abschluss der Regime-Klärung | `anschluss-routing` | Nächsten Spezial-Skill benennen |

Priorität: **Frist** vor allem — bei Änderungskündigung sofort § 105 ArbVG-Anfechtungsfrist (2 Wochen) sichern.

## Judikatur-Anker (Such-Wegweiser, kein Blindzitat)

Zur Laufzeit ausführen — **keine GZ aus Modellwissen behaupten**, nur RIS-geliefertes übernehmen:

- **Schweigen / einvernehmliche Änderung:** `python3 tools/ris_client.py volltext "JJR_19950509_OGH0002_0100OB00511_9500000_001"` → RIS-Justiz RS0047273 (Schweigen = keine Annahme).
- **Konkludente Bindung durch wiederholte Leistung:** `python3 tools/ris_client.py volltext "JJR_19890913_OGH0002_009OBA00205_8900000_001"` → RIS-Justiz RS0014526.
- **Empfängerhorizont bei schlüssigem Verhalten:** `python3 tools/ris_client.py volltext "JJR_19790508_OGH0002_0040OB00035_7900000_002"` → RIS-Justiz RS0014154 (68 Entscheidungen; OGH 8 ObA 33/21t folgt).
- **Änderungsregime / Kernsatz Bestandsvertrag:** `python3 tools/ris_client.py volltext "JJR_19980212_OGH0002_008OBA00035_98Z0000_001"` → RIS-Justiz RS0109380, OGH 12.02.1998, 8 ObA 35/98z.
- **Änderungskündigung + § 101 ArbVG:** `python3 tools/ris_client.py volltext "JJR_20160628_OGH0002_008OBA00063_15W0000_001"` → RIS-Justiz RS0131210, OGH 28.06.2016, 8 ObA 63/15w.
- **Verschlechterungsbegriff § 101 ArbVG (kollektiver Prong):** `python3 tools/ris_client.py leit "4 Ob 79/85"` → RS0051209 (OGH 4 Ob 79/85; 17 Entscheidungen; Norm: ArbVG § 101): Verschlechterung = jede Änderung zum Nachteil des AN (materiell + immateriell); Entgelt im weitesten Sinn; T3: Wegfall Überstundenpauschale; T4: Entgeltverschlechterung. **§ 101 setzt Betriebsrat voraus — kein Schutz für no-BR-Betrieb über § 101; dort § 879 Abs 3 ABGB (RS0016914) als Individualschutz.**
- **Verschlechterung wirkt nicht konkludent zurück / Vorbehalt:** Proposition gestützt auf § 863 ABGB + RS0042828 (strenge Anforderungen an schlüssige Erklärungen) + RS0014154 (Empfängerhorizont) + RS0047273 [T2] (bloße Entgegennahme = kein Erklärungswert). — RS0124521 (9 ObA 113/08w) betrifft den Unverbindlichkeitsvorbehalt für Sonderzahlungen und ist für diese Proposition nicht einschlägig.
- **Anfechtungsfähigkeit Änderungskündigung (Zumutbarkeit/Sozialwidrigkeit):** `python3 tools/ris_client.py linie "Kündigungsanfechtung Sozialwidrigkeit" --gericht OGH --gesetz ARBVG --paragraf 105` → Linie RS0051746 (51 Entscheidungen; OGH 9 ObA 59/23a folgt).
- **Aktualität (Pflicht vor Übernahme älterer Entscheidungen):** `python3 tools/ris_client.py aktualitaet ABGB 863 --seit 1998-02-12` (Datum des Kernsatzes); `aktualitaet ARBVG 101 --seit 2016-06-28`.

## Hinweis

Dieser Skill ist Weiche, nicht Entscheidung. Er identifiziert das zutreffende Regime und leitet weiter. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Das Mandat führen Sie; der Skill liefert die Karte.
