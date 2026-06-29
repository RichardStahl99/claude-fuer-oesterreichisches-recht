---
name: anschluss-routing
description: "Abschluss-Router: verweist je nach Fall auf die Beendigungs-Vertikale, AK/Arbeitsrechtsanwalt, Betriebsrat und Steuerberater. Kein deutsches Recht."
---

# Anschluss-Routing — Arbeitsrecht (Vertragsänderung)

## Fachlicher Anker

- **Normen (über RIS auflösen, `tools/ris_client.py`):** § 40 ArbVG (Betriebsrat-Gründung) — GNR 10008329; `python3 tools/ris_client.py norm ARBVG 40` → HTTP 200. Nur **prospektiv** relevant: § 40 ArbVG schafft die Rechtsgrundlage für die Gründung eines Betriebsrats, setzt aber Mindestbelegschaft (≥ 5 wahlberechtigte Arbeitnehmer) voraus.
- **Laufzeit-Grounding (Pflicht):** Vor Empfehlung einer Betriebsrat-Gründung `aktualitaet ARBVG 40` ausführen — Fassungsstand des § 40 ArbVG (Wahlvoraussetzungen, Mindestbelegschaft) bestätigen, bevor die prospektive Handlungsempfehlung ausgegeben wird.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md`. Keine GZ aus Modellwissen — nur RIS-verifizierte Fundstellen verwenden.
- **EStG-Hinweis (Steuer):** Steuerliche Fragen (Jahressechstel, lohnsteuerliche Behandlung von Sonderzahlungen) liegen außerhalb des Kompetenzbereichs dieses Plugins und werden als Verweis zum Steuerberater ausgegeben — dieses Plugin trifft dazu keine eigene steuerrechtliche Subsumtion. (Das EStG 1988 ist im RIS sehr wohl permalink-fähig, GNR 10004570; die steuerliche Beurteilung bleibt dennoch dem Steuerberater vorbehalten.)

## Einsatzlage

Dieser Skill schließt die Vertragsänderungs-Vertikale ab. Er wird aktiv, wenn

- der ursprüngliche Änderungsfall (Regime, Klausel, Austritt, ausländische Vorlage) abschließend bewertet wurde und
- ein Restrisiko oder Anschlussbedarf außerhalb des Plugins liegt.

Dieser Skill **entscheidet nicht** — er benennt den nächsten Schritt außerhalb des Plugins und begründet die Weiterleitung.

## Sofort-Triage

Vier Fragen bestimmen, wohin weitergeleitet wird:

| Frage | Indikator | Ziel |
|---|---|---|
| **Ist eine echte Kündigung oder Entlassung im Raum?** | Arbeitgeber hat Kündigung ausgesprochen oder Entlassung angedroht (auch als Druckmittel hinter der Änderungsklausel) | Plugin `arbeitsrecht-beendigung` |
| **Braucht der Mandant eine verbindliche anwaltliche Beurteilung?** | Rechtslage unklar, Prozessrisiko relevant, Verhandlung mit Arbeitgeber, RIS-Ergebnis allein nicht ausreichend | AK Wien / Arbeitsrechtsanwalt |
| **Fehlt ein Betriebsrat, und sind strukturelle Schutzmechanismen mittelfristig relevant?** | Betrieb hat ≥ 5 wahlberechtigte Arbeitnehmer; kein Betriebsrat vorhanden; Änderungsanliegen betrifft kollektive Arbeitsbedingungen | Betriebsrat (§ 40 ArbVG — prospektiv) |
| **Sind Sonderzahlungen, Jahressechstel oder steuerliche Optimierung ein Thema?** | Entgeltsänderung berührt Jahressechstel-Ausschöpfung oder Steuerbelastung bei Sonderzahlungen | Steuerberater |

## Risiko-Ampel

- 🔴 **Kündigung oder Entlassung bereits ausgesprochen** — Weiterleitung zu `arbeitsrecht-beendigung` ist vorrangig; Anfechtungsfrist (**2 Wochen**) sofort markieren, bevor der Router weitere Schritte prüft: im betriebsratslosen (aber betriebsratspflichtigen) Betrieb **§ 107 ArbVG (iVm § 105 Abs 4a)** — der Arbeitnehmer ficht selbst an; wo ein Betriebsrat besteht, gilt § 105 Abs 4 ArbVG.
- 🔴 **Verbindliche Rechtsfrage ohne gesichertes RIS-Ergebnis** — Kein Ergebnis aus diesem Plugin ausgeben; unmittelbar zu AK Wien / Arbeitsrechtsanwalt verweisen.
- 🟠 **Betrieb ohne Betriebsrat, kollektive Schutzlücke erkennbar** — Gründungshinweis nach § 40 ArbVG als prospektiven Schritt erwähnen; Zeitrahmen für Wahl klären (Betriebsratswahl erfordert Initiative der Belegschaft, nicht Anwalt).
- 🟠 **Entgeltänderung mit Steuerrelevanz** — Steuerberater einbeziehen; keine steuerrechtliche Subsumtion ohne Fachmandat.
- 🟢 **Fall vollständig abgeschlossen, kein Anschlussbedarf** — Dokumentation abschließen; Mandant über Fristen informieren (laufende Verjährungs- oder Anfechtungsfristen aus vorherigen Skills).

## Anschluss-Skill-Router

| Wenn der Fall trägt … | dann Stelle / Plugin | Erwartung |
|---|---|---|
| Echte Kündigung oder Entlassung im Raum (auch als Drohung hinter Änderungsangebot) | Plugin **`arbeitsrecht-beendigung`** | Beendigungsart, Fristen, Anfechtung, Abfertigungsansprüche |
| Verbindliche rechtliche Beurteilung, Verhandlungsstrategie oder Klagseinbringung | **AK Wien** (Arbeiterkammer Wien, arbeitsrechtsberatung@akwien.at) / **Arbeitsrechtsanwalt** | Anwaltliches Mandat; Klagseinbringung beim ASG |
| Struktureller Schutz: Betrieb hat ≥ 5 AN, kein Betriebsrat, kollektive Schutzlücke | **Betriebsrat gründen** (§ 40 ArbVG — prospektiv; Initiative der Belegschaft) | Betriebsratswahl nach §§ 40 ff ArbVG; GNR 10008329 |
| Jahressechstel-Ausschöpfung, steuerliche Optimierung bei Sonderzahlungen, Entgeltstruktur | **Steuerberater** | Steuerliche Beurteilung der Entgeltänderung (Jahressechstel, lohnsteuerliche Behandlung von Sonderzahlungen — EStG; keine §-Zitation ohne verifizierten RIS-Permalink) |

## Hinweis

Dieser Skill ist Abschlussweiche, nicht Entscheidungsinstanz. Der Anwalt entscheidet; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Cross-Vertical: Das Plugin `arbeitsrecht-beendigung` enthält seinerseits einen Rückverweis auf diese Vertikale (Vertragsänderungs-Kontext bei laufendem AV).
