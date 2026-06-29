---
name: einstieg-vertragsaenderung
description: "Einstiegs-Triage für Vertragsänderungen im aufrechten Dienstverhältnis (Anwalts-Dashboard): erfasst Rolle, Änderungsweg, Klausel-Bewertung (Bestand→Angebot), Fristen und Hebel in einer scanbaren Tabelle und leitet weiter. Kein deutsches Recht."
---

# Einstieg Vertragsänderung — Anwalts-Dashboard

## Fachlicher Anker

- **Normen (über RIS auflösen, `tools/ris_client.py`):** § 863, § 879 Abs 3 ABGB (konkludenter Konsens; sittenwidrige Klausel) — GNR 10001622; § 26, § 29 AngG (Austrittsrecht; Ansprüche) — GNR 10008069 (Artikel 1); § 36 Abs 2 Z 3, § 101, § 107 ArbVG (leitende:r Angestellte:r [§ 36]; Mitwirkung bei Versetzungen/Versetzungsschutz [§ 101 — kollektiver Prong, setzt Betriebsrat voraus]; Anfechtung durch den Arbeitnehmer im betriebsratslosen Betrieb [§ 107 iVm § 105 Abs 4a]) — GNR 10008329.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md`. Keine Geschäftszahl aus Modellwissen.
- **Konvention:** Aufbau nach `references/anwalts-dashboard-konvention.md`.

## Einsatzlage

Erster Skill bei Vertragsänderungen in einem **aufrechten** Dienstverhältnis: Gehaltserhöhung mit Änderungsbedingungen, einseitige Dienstanweisung, Änderungskündigung, konkludente Änderung, Versetzung, Betriebsvereinbarung vs. Einzelvertrag. Liefert Triage, klärt zuerst den **Änderungsweg**, bewertet Klauseln (Bestand→Angebot), sichert Hebel und leitet weiter.

**Nicht für:** Beendigung des Arbeitsverhältnisses (→ Skill `einstieg-arbeitsrecht`), Sozialversicherung, Ausbildungsverhältnisse oder Betriebsübergang.

## Sofort-Triage (Tabelle, vor jeder Rückfrage)

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
|---|---|---|
| Rolle | Angestellte:r oder Arbeiter:in? AN- oder AG-Seite? | Dienstvertrag, Kollektivvertrag |
| **Änderungsweg** | Einvernehmlich / Änderungskündigung / konkludent (Duldung + Auszahlung, § 863 ABGB)? | Schreiben, Sachverhalt → Skill `aenderungsregime` |
| Klausel-Bewertung | Bestand→Angebot: ✅ wirksam / 🔴 gröblich benachteiligend → Teilnichtigkeit (§ 879 Abs 3 ABGB; Entgelt-Modalitäten/Nebenabreden, nicht Hauptleistung) / 🟠 Grenzfall / ⚪ unklar | Klauseltext → Skill `klausel-inhaltskontrolle` |
| DE-Vorlage erkennbar? | Deutsches Rechtsdeutsch, BGB-Normen, „Urlaubsgeld" statt Urlaubsentgelt, 3-Monatsfrist? | Vertragstext → Skill `deutsche-vorlage-audit` |
| Hebel/Austritt | Austrittsrecht (§ 26 AngG) bei unzumutbarer Änderung? Vorbehalt gesetzt? | Änderungsschreiben → Skill `austritt-backstop-und-hebel` |
| **Leitende:r Angestellte:r?** | § 36 ArbVG: echte Hire-&-Fire- oder Gehaltskompetenz (nicht Titel allein) — ArbVG-Schutz reduziert | Anstellungsvertrag, Vollmacht |

## Risiko-Ampel

- 🔴/🟠/🟢 **Frist** — 🔴 Konkludente Bindung läuft mit nächster Auszahlung (kein Vorbehalt mehr setzbar); 🟠 Änderung angekündigt, Reaktionsfrist ≤ 30 Tage; 🟢 Schreiben zugegangen, Prüfung läuft.
- 🔴/🟠/🟢 **Beweis** — 🔴 Kein Vorbehalt bei Gehaltserhöhung mit Änderungsbedingungen gesetzt; 🟠 Vorbehalt mündlich oder unklar dokumentiert; 🟢 schriftlicher Vorbehalt belegt.
- 🔴/🟠/🟢 **Wirtschaftlich** — Wert der aufgegebenen Schutzrechte (Überstundenpauschale, Sonderzahlungen, Dienstwagen, Versetzungsschutz) konkret benennen.

## Anschluss-Skill-Router

| Wenn der Fall trägt … | dann Skill | Erwartung |
|---|---|---|
| **Änderungsweg unklar oder Änderungskündigung** | **`aenderungsregime`** | Klare Einordnung + Wirksamkeitsprüfung |
| Klausel prüfen (Bestand oder neues Angebot) | `klausel-inhaltskontrolle` | Bewertung § 879 Abs 3 ABGB + KV-Mindest |
| Verdacht deutsches Vertragsformular | `deutsche-vorlage-audit` | Audit + Österreich-Anpassung |
| Austritt / Gegenhebel / Vorbehalt sichern | `austritt-backstop-und-hebel` | § 26 AngG Austrittsrecht + Druckmittel |
| Weiterleitung nach Abschluss der Triage | `anschluss-routing` | Nächsten Spezial-Skill benennen |

Vorrangig **`aenderungsregime`** — der Änderungsweg ist die Weiche; bei Änderungskündigung sofort die **Kündigungsfrist + Anfechtbarkeit** prüfen.

## Norm-Radar

- `§ 863 ABGB` — konkludenter Konsens (Bindung durch Duldung und Annahme der Leistung)
- `§ 879 Abs 3 ABGB` — Inhaltskontrolle: gröblich benachteiligende Klausel in vorformulierten Vertragsbestimmungen (AGB/Formularbindung) nichtig
- `§ 26 AngG` — Austrittsrecht bei unzumutbarer Verschlechterung der Arbeitsbedingungen
- `§ 29 AngG` — Ansprüche bei berechtigt erklärtem Austritt (Abfertigung, Kündigungsentschädigung)
- `§ 36 Abs 2 Z 3 ArbVG` — Definition leitende:r Angestellte:r (Hire-&-Fire-/Gehaltskompetenz)
- `§ 101 ArbVG` — Mitwirkung des Betriebsrats bei Versetzungen (Versetzungsschutz; setzt Betriebsrat voraus — kollektiver Prong)
- `§ 107 ArbVG` — Anfechtung durch den Arbeitnehmer im betriebsratspflichtigen, aber betriebsratslosen Betrieb (iVm § 105 Abs 4a; 2-Wochen-Frist ab Zugang der Kündigung)

## Genau eine Rückfrage (nur wenn nötig)

Trägt die Akte 80 %: Dashboard mit `[noch zu klären: …]`. Sonst die **eine** Weiche: *„Auf welchem Weg will der Arbeitgeber die Änderung durchsetzen — einvernehmlich, per Änderungskündigung oder durch konkludente Änderung (Duldung + Auszahlung)?"* (entscheidet Änderungsregime, Fristlauf und Hebel).

## Judikatur-Anker (Such-Wegweiser, kein Blindzitat)

Zur Laufzeit ausführen (nicht nur verweisen) — **keine GZ aus Modellwissen behaupten**, nur Geliefertes übernehmen; Arbeitsrecht entscheidet der **8./9. Senat (ObA)**:

- Konkludente Vertragsänderung (§ 863 ABGB) — `python3 tools/ris_client.py linie "konkludente Vertragsänderung Arbeitsverhältnis" --gericht OGH --gesetz ABGB --paragraf 863` (OGH-Linie + Leitsätze nach Linientiefe).
- Sittenwidrige Klausel Arbeitsvertrag (§ 879 Abs 3 ABGB) — `python3 tools/ris_client.py linie "gröblich benachteiligend Arbeitsvertrag" --gericht OGH --gesetz ABGB --paragraf 879`.
- Austrittsrecht unzumutbare Änderung (§ 26 AngG) — `python3 tools/ris_client.py linie "Austritt unzumutbar Verschlechterung" --gericht OGH --gesetz ANGG --paragraf 26`.
- Gewicht einer konkret genannten Geschäftszahl: `python3 tools/ris_client.py leit <GZ>` (Leitentscheidung/Stamm + Linientiefe).
- **Aktualität (Pflicht vor Übernahme älterer Entscheidungen):** `python3 tools/ris_client.py aktualitaet ABGB 863 --seit <Entscheidungsdatum>` bzw. `python3 tools/ris_client.py aktualitaet ANGG 26 --seit <Entscheidungsdatum>`.

## Hinweis

Diese Triage ist Vorbereitung, nicht Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`.
