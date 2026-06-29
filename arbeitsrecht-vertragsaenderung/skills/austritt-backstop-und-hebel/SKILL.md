---
name: austritt-backstop-und-hebel
description: "Strategischer Hebel: berechtigter vorzeitiger Austritt (§ 26 Z 2 AngG) + Kündigungsentschädigung (§ 29 AngG) bei zu aggressiver Verschlechterung; warnt, dass die Unterschrift diesen Backstop abbaut. Kein deutsches Recht."
---

# Austritt-Backstop und Hebel — § 26 Z 2 AngG / § 29 AngG

## Fachlicher Anker

- **Normen (über RIS auflösen, `tools/ris_client.py`):** § 26 Z 2 AngG (berechtigter vorzeitiger Austritt bei erheblicher Entgeltkürzung / Herabstufung) — GNR 10008069 (Artikel 1); § 29 AngG (Kündigungsentschädigung) — GNR 10008069 (Artikel 1); § 863 ABGB (schlüssiges Verhalten / Vorbehalt) — GNR 10001622.
- **Kernsätze (Laufzeit-Verifikation erforderlich):**
  1. Eine zu aggressive einseitige Herabstufung oder Entgeltkürzung — ohne wirksame einvernehmliche Vertragsänderung oder Änderungskündigung — berechtigt den Arbeitnehmer nach § 26 Z 2 AngG zum vorzeitigen Austritt, wenn der Arbeitgeber die wesentliche Vertragspflicht (Entgelt, Verwendung) erheblich verletzt.
  2. Rechtsfolge des berechtigten Austritts: Kündigungsentschädigung nach § 29 AngG — voller Bezugsersatz für die fiktive Restlaufzeit der Kündigungsfrist; in den ersten drei Monaten der Schadensminderungsfrist keine Anrechnung anderweitiger Erwerbe.
  3. Wer die Verschlechterung vorbehaltlos unterschreibt oder die geänderte Leistung vorbehaltlos weiterhin annimmt, stimmt konkludent zu (§ 863 ABGB) und baut damit den § 26-Backstop ab; ein nachträglicher Vorbehalt wirkt nicht rückwirkend (RIS-Justiz RS0124521, OGH 24.02.2009, 9 ObA 113/08w — Linie aus `aenderungsregime`).
  4. Reagiert der Arbeitnehmer auf die aufgezwungene Änderung sofort schriftlich „unter Protest" / „unter ausdrücklichem Vorbehalt aller Rechte", bleibt das Austrittsrecht erhalten — vorausgesetzt, der Austritt wird zeitnah zum auslösenden Anlass erklärt (GZ RIS-bestätigt: OGH 05.06.2008, 9 ObA 164/07v — die Proposition „schriftlich unter Protest" erst nach Volltext-Prüfung übernehmen; siehe Judikatur-Anker).
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md`. Keine GZ aus Modellwissen — nur RIS-verifizierte Fundstellen verwenden.

## Einsatzlage

Dieser Skill greift, wenn das Arbeitsverhältnis **nicht durch Kündigung, sondern durch faktische oder angebotene Verschlechterung** unter Druck gesetzt wird und der Arbeitnehmer überlegt, ob Verbleib noch zumutbar ist oder ein Austritt die bessere Option darstellt.

**Drei Szenarien:**

| Szenario | Sachverhalt | Hebel |
|---|---|---|
| **Herabstufung** | Arbeitgeber versetzt einseitig auf eine schlechter entlohnte oder statusmäßig niedrigere Stelle | § 26 Z 2 AngG — Austrittsrecht, wenn Entgelt- oder Verwendungspflicht erheblich verletzt |
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

- **Ankerbeschluss „unter Protest" / Vorbehalt bei Versetzung:** `python3 tools/ris_client.py leit "9 ObA 164/07v"` → bestätigt als Folgeentscheidung (OGH 05.06.2008); folgt RIS-Justiz RS0112755 (Stamm OGH 9 ObA 255/99m, 10 Entscheidungen — Feststellungsbegehren Unwirksamkeit Versetzung), RS0029509 (Stamm OGH 9 ObA 29/93, 25 Entscheidungen — dienstvertragliche Beurteilung Versetzung), RS0021252 (Stamm OGH 9 ObA 34/88, 4 Entscheidungen — vertragsändernde vs. direktoriale Versetzung). Volltext des Erkenntnisses: RIS-Websuche `https://www.ris.bka.gv.at/Ergebnis.wxe?Abfrage=Justiz&Suchworte=9%20ObA%20164/07v` — Proposition „schriftlich unter Protest" im Entscheidungstext bestätigen.
- **Konkludente Bindung / Vorbehalt nach Zufluss:** `python3 tools/ris_client.py volltext "JJR_20090224_OGH0002_009OBA00113_08W0000_001"` → RIS-Justiz RS0124521, OGH 24.02.2009, 9 ObA 113/08w (Verschlechterung wirkt nicht konkludent zurück; Vorbehalt nach Zufluss nicht mehr nachholbar).
- **Aktualität § 26 AngG:** `python3 tools/ris_client.py aktualitaet ANGG 26 --seit 2008-06-05` → Fassung unverändert seit 1921-07-01; keine Gesetzesänderung nach dem Ankerbeschluss.
- **Aktualität § 29 AngG:** `python3 tools/ris_client.py aktualitaet ANGG 29 --seit 2008-06-05` → Fassung unverändert seit 1971-08-01; keine Gesetzesänderung nach dem Ankerbeschluss.

## Hinweis

Dieser Skill klärt das strategische Kräfteverhältnis beim vorzeitigen Austritt. Er ist kein Rechtsmittel und kein Mandatsentscheid. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Das Mandat führen Sie; der Skill liefert die Karte.
