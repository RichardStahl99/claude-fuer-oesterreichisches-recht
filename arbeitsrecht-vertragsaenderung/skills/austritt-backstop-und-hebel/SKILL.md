---
name: austritt-backstop-und-hebel
description: "Strategischer Hebel: berechtigter vorzeitiger Austritt (§ 26 Z 2 AngG) + Kündigungsentschädigung (§ 29 AngG) bei zu aggressiver Verschlechterung; warnt, dass die Unterschrift diesen Backstop abbaut. Kein deutsches Recht."
---

# Austritt-Backstop und Hebel — § 26 Z 2 AngG / § 29 AngG

## Fachlicher Anker

- **Normen (über RIS auflösen, `tools/ris_client.py`):** § 26 Z 2 AngG (berechtigter vorzeitiger Austritt bei erheblicher Entgeltschmälerung — Z 2 = Entgelt-Prong; bare Herabstufung ohne Entgelteinbuße = allgemeiner wichtiger Grund § 26 AngG) — GNR 10008069 (Artikel 1); § 29 AngG (Kündigungsentschädigung) — GNR 10008069 (Artikel 1); § 863 ABGB (schlüssiges Verhalten / Vorbehalt) — GNR 10001622.
- **Kernsätze (Laufzeit-Verifikation erforderlich):**
  1. Eine erhebliche Entgeltkürzung ohne vertragliche Grundlage berechtigt den Arbeitnehmer nach § 26 Z 2 AngG (Entgelt-Prong) zum vorzeitigen Austritt; eine Herabstufung, die nicht mit einer Entgeltschmälerung verbunden ist, kann allgemeiner wichtiger Grund nach § 26 AngG sein, fällt aber nicht unter Z 2.
  2. Rechtsfolge des berechtigten Austritts: Kündigungsentschädigung nach § 29 AngG — voller Bezugsersatz für die fiktive Restlaufzeit der Kündigungsfrist; in den ersten drei Monaten der Schadensminderungsfrist keine Anrechnung anderweitiger Erwerbe.
  3. Wer die Verschlechterung vorbehaltlos unterschreibt oder die geänderte Leistung vorbehaltlos weiterhin annimmt, stimmt konkludent zu (§ 863 ABGB) und baut damit den § 26-Backstop ab; ein nachträglicher Vorbehalt wirkt nicht rückwirkend (§ 863 ABGB + RS0042828 [strenge Anforderungen an schlüssige Erklärungen] + RS0014154 [Empfängerhorizont]; bloße Entgegennahme = kein Erklärungswert: RS0047273 [T2]).
  4. § 26 AngG verlangt, dass der vorzeitige Austritt ohne unnötigen Aufschub aus dem aktuellen wichtigen Grund erklärt wird; vorbehaltlose Weiterarbeit kann den Austrittsgrund verwirken.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md`. Keine GZ aus Modellwissen — nur RIS-verifizierte Fundstellen verwenden.

## Einsatzlage

Dieser Skill greift, wenn das Arbeitsverhältnis **nicht durch Kündigung, sondern durch faktische oder angebotene Verschlechterung** unter Druck gesetzt wird und der Arbeitnehmer überlegt, ob Verbleib noch zumutbar ist oder ein Austritt die bessere Option darstellt.

**Drei Szenarien:**

| Szenario | Sachverhalt | Hebel |
|---|---|---|
| **Herabstufung** | Arbeitgeber versetzt einseitig auf eine schlechter entlohnte oder statusmäßig niedrigere Stelle | § 26 Z 2 AngG — Austrittsrecht bei Entgeltschmälerung; bare Herabstufung ohne Entgelteinbuße = allgemeiner wichtiger Grund (§ 26 AngG, nicht Z 2) |
| **Entgeltkürzung** | Arbeitgeber kürzt Grundgehalt, Zulagen oder laufende Prämien ohne vertragliche Deckung | § 26 Z 2 AngG — Nichterfüllung der Entgeltpflicht als Austrittsgrund |
| **Unterschrift bereits geleistet** | Arbeitnehmer hat einem Widerrufs- oder Versetzungsvorbehalt schriftlich zugestimmt | **Backstop abgebaut** — vertragliche Grundlage für die Herabstufung besteht; § 26-Schutz stark reduziert; Klausel auf § 879 Abs 3 ABGB prüfen (→ `klausel-inhaltskontrolle`) |

**Nicht für:** Beendigungsrecht nach Arbeitgeberkündigung (→ `einstieg-arbeitsrecht`), isolierte Klauselprüfung (→ `klausel-inhaltskontrolle`), Klärung des Änderungsregimes (→ `aenderungsregime`).

## Sofort-Triage

| Frage | Prüfpunkt | Konsequenz |
|---|---|---|
| **Austrittsanlass noch aktuell?** | Wann trat die Verschlechterung ein? Arbeitet der Arbeitnehmer seitdem vorbehaltlos weiter? | Vorbehaltlose Weiterarbeit über längeren Zeitraum → konkludente Zustimmung (§ 863 ABGB); § 26-Austrittsrecht kann verwirkt sein |
| **Protest dokumentiert?** | Liegt eine schriftliche „unter Protest"- / Vorbehalts-Erklärung nach Bekanntgabe der Verschlechterung vor? | Ohne Dokumentation: Beweislast beim Arbeitnehmer; mündlicher Vorbehalt im Streit schwer beweisbar |
| **Versetzungs-/Widerrufsvorbehalt unterschrieben?** | Enthält der Vertrag oder ein Nachtrag eine wirksame Widerrufs- oder Versetzungsklausel? | Wenn ja: vertragliche Erlaubnis der Herabstufung; § 26 Z 2 AngG greift in diesem Bereich nicht mehr — Klausel zuerst auf Unwirksamkeit prüfen |
| **Größenordnung der Entgelteinbuße?** | Wie hoch ist die monatliche Einbuße? Wie lang ist die fiktive Kündigungsfrist? | Bestimmt die wirtschaftliche Basis der Kündigungsentschädigung (§ 29 AngG) und den Vergleichswert „Bleiben vs. Austritt" |

## Risiko-Ampel

- 🔴 **Frist: Austritt nicht zeitnah zum Anlass** — § 26 AngG setzt voraus, dass der vorzeitige Austritt aus einem konkreten, aktuellen wichtigen Grund erklärt wird; längeres Zuwarten nach Kenntnis des Grundes wertet die Rechtsprechung regelmäßig als Akzeptanz. Sofortige schriftliche Erklärung des Austritts nach Abklärung des Sachverhalts ist unverzichtbar.
- 🔴 **Beweis: Kein dokumentierter Protest** — Ohne schriftlichen Vorbehalt muss der Arbeitnehmer im Streitfall beweisen, dass er nie einverstanden war. Vorbehaltserklärung schriftlich vor oder unmittelbar bei Annahme der geänderten Leistung setzen; mündliche Erklärungen genügen nicht zuverlässig.
- 🟠 **Wirtschaftlich: Überbrückungsrisiko bis Ausgleich** — Kündigungsentschädigung (§ 29 AngG) deckt die fiktive Kündigungsfrist (volle Bezüge, erste 3 Monate ohne Anrechnung anderweitiger Erwerbe), setzt aber Einigung oder Klage voraus; bis dahin kein laufendes Entgelt. Liquiditätsplanung und AMS-Ansprüche prüfen.
- 🟠 **Unterschrift auf Widerrufs-/Versetzungsklausel** — Vertragliche Erlaubnis der Herabstufung macht den § 26-Backstop schwerer erreichbar. Klausel auf § 879 Abs 3 ABGB (geltungserhaltende Reduktion) prüfen, bevor Austritt erwogen wird.
- 🟢 **Protest schriftlich dokumentiert, Austritt unverzüglich, keine Widerrufsklausel** — Optimale Ausgangslage; § 26 Z 2 AngG greift, Kündigungsentschädigung § 29 AngG schlüssig begründbar.

## Anschluss-Skill-Router

| Wenn der Fall trägt … | dann Skill | Erwartung |
|---|---|---|
| Änderungsregime unklar (Versetzung, Änderungskündigung, konkludente Änderung) | `aenderungsregime` | Welches Regime gilt — Grundlage für § 26-Beurteilung |
| Widerrufs-/Versetzungsklausel liegt vor; Prüfung auf Unwirksamkeit | `klausel-inhaltskontrolle` | Wirksamkeit nach § 879 Abs 3 ABGB; ggf. Wegfall des Backstop rückgängig |
| Weiterleitung nach Abschluss der Austrittsbeurteilung | `anschluss-routing` | Nächsten Spezial-Skill benennen |

Priorität: **Frist** vor allem — Austritt zeitnah zum auslösenden Anlass erklären; Verzögerung kann den Austrittsgrund vernichten.

## Judikatur-Anker (Such-Wegweiser, kein Blindzitat)

Zur Laufzeit ausführen — **keine GZ aus Modellwissen behaupten**, nur RIS-geliefertes übernehmen:

- **Zeitnähe des Austritts / vorbehaltlose Weiterarbeit:** § 26 AngG verlangt, dass der vorzeitige Austritt ohne unnötigen Aufschub aus dem aktuellen wichtigen Grund erklärt wird; vorbehaltlose Weiterarbeit kann den Austrittsgrund verwirken. (9 ObA 164/07v ist eine Versetzungs-/Feststellungsklage ohne § 26/Austritt-Inhalt — kein Zitat.)
- **Konkludente Bindung / Vorbehalt nach Zufluss:** Gestützt auf § 863 ABGB + RS0042828 (strenge Anforderungen an schlüssige Erklärungen) + RS0014154 (Empfängerhorizont) + RS0047273 [T2] (bloße Entgegennahme = kein Erklärungswert). — RS0124521 (9 ObA 113/08w) betrifft Unverbindlichkeitsvorbehalt für Sonderzahlungen, nicht diese Proposition.
- **Aktualität § 26 / § 29 AngG:** `python3 tools/ris_client.py aktualitaet ANGG 26` / `aktualitaet ANGG 29` — Fassungsstand der Austritts-/Entschädigungsnormen prüfen; Änderung der Normen würde Austrittsvoraussetzungen oder Entschädigungsberechnung berühren.

## Hinweis

Dieser Skill klärt das strategische Kräfteverhältnis beim vorzeitigen Austritt. Er ist kein Rechtsmittel und kein Mandatsentscheid. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Das Mandat führen Sie; der Skill liefert die Karte.
