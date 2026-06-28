---
name: verfahrensgang-rechtsmittel
description: "Führt durch den streitigen Verfahrensgang und die Rechtsmittel im österreichischen Zivilprozess: Klage/Klagebeantwortung, Säumnis/Versäumungsurteil, Neuerungsverbot in der Berufung (§ 482 ZPO), Berufung (§ 464, 4 Wochen), Revision (§§ 502, 505), Rekurs (§ 521) und ERV. Kein deutsches Recht."
---

# Verfahrensgang und Rechtsmittel

## Fachlicher Anker

- **Normen (über RIS prüfen):** §§ 226 ff ZPO (Klage), § 230, § 257 ZPO (Klagebeantwortung/Tagsatzung), § 396 ZPO (Versäumungsurteil), § 482 ZPO (Neuerungsverbot), § 464 ZPO (Berufungsfrist), §§ 502, 505 ZPO (Revision), § 521 ZPO (Rekurs) — GNR 10001699; ERV: § 89c GOG.
- **Vorgelagert:** `zustaendigkeit-jn`; ggf. `mahnverfahren` (nach Einspruch).
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`.

## Worum geht es?

Nach Einspruch (oder bei direkter Klage) läuft das **streitige Verfahren**: Klage → Klagebeantwortung → Tagsatzung(en) → Beweisverfahren → Urteil — und danach die Rechtsmittel. Zwei AT-Spezifika sind kritisch: das **Neuerungsverbot** in der Berufung und die kurzen, harten **Fristen**.

## Schritt-für-Schritt

1. **Klage/Klagebeantwortung:** Nach Klagezustellung hat der Beklagte die **Klagebeantwortung** (Frist idR **4 Wochen**) zu erstatten. Versäumt er sie, kann auf Antrag ein **Versäumungsurteil** ergehen (§ 396 ZPO).
2. **Verfahren erster Instanz:** vorbereitende Tagsatzung, Beweisanbote, Beweisaufnahme, Schluss der Verhandlung, **Urteil**. Alle Tatsachen und Beweise vollständig **in erster Instanz** vorbringen.
3. **Neuerungsverbot beachten (§ 482 ZPO):** In der **Berufung** sind neue Tatsachen und Beweismittel grundsätzlich **unzulässig**. Wer erstinstanzlich etwas versäumt, kann es in zweiter Instanz regelmäßig nicht nachholen.
4. **Rechtsmittel wählen und befristen:**
   - **Berufung** (gegen Urteile, §§ 461 ff ZPO): Frist **4 Wochen** ab Zustellung (§ 464). Berufungsgericht: LG (gegen BG-Urteile) bzw. OLG (gegen LG-Urteile).
   - **Revision** (an den OGH, §§ 502 ff ZPO): Frist **4 Wochen** (§ 505). Zulässig nur bei **erheblicher Rechtsfrage** (§ 502 Abs 1) und innerhalb der Streitwertschranken (jedenfalls unzulässig bis 5.000 €; im mittleren Bereich nur außerordentliche Revision/Zulassung — **aktuelle Grenzen in RIS prüfen**).
   - **Rekurs** (gegen Beschlüsse, §§ 514 ff ZPO): Frist idR **14 Tage** (§ 521); gegen End-/Aufhebungsbeschlüsse (§ 521 Abs 1 iVm § 519) **4 Wochen**.
5. **ERV:** Anwaltliche Schriftsätze elektronisch einbringen (§ 89c GOG).

## Typische Fehler / Kritik

- **Neuerungsverbot übersehen:** Beweise zu spät (erst in der Berufung) anbieten → präkludiert.
- **Frist verwechseln:** Berufung/Revision **4 Wochen**, Rekurs **14 Tage** (nicht generell „1 Monat" wie in Deutschland).
- **Revision ohne erhebliche Rechtsfrage** erheben (§ 502) — unzulässig/zurückgewiesen.
- **Deutsches Recht:** keine „Berufung 1 Monat / Revision § 548 ZPO (DE)", kein „Beschwerde" gegen Beschlüsse — in Österreich Rekurs.

## Quellen und Stand 06/2026

- §§ 226 ff, 396, 482, 464, 502, 505, 521 ZPO (RIS, GNR 10001699); § 89c GOG (ERV).
- `references/methodik-buergerliches-recht.md` Abschnitt 12. Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)
- `§ 396 ZPO` — Versäumungsurteil · `§ 482 ZPO` — Neuerungsverbot · `§ 464 ZPO` — Berufungsfrist · `§ 502 ZPO` — Revision (erhebliche Rechtsfrage) · `§ 505 ZPO` — Revisionsfrist · `§ 521 ZPO` — Rekursfrist

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen)
Zur Laufzeit ausführen (nicht nur verweisen):
- Neuerungsverbot: `python3 tools/ris_client.py linie "Neuerungsverbot" --gericht OGH --gesetz ZPO --paragraf 482` — OGH-Linie nach Linientiefe + Leitsätze. Vorhandene RS-Nummern (RS0042274, RS0042493) über `linie`/`leit` zu bestätigen.
- Eventualmaxime: `python3 tools/ris_client.py linie "Eventualmaxime" --gericht OGH` — Linie + Leitsätze; RS0074226 über `linie`/`leit` zu bestätigen; für eine konkret herangezogene Geschäftszahl `leit <GZ>` (Leitentscheidung/Stamm?).
- Aktualität vor Stützung auf eine ältere Entscheidung: `aktualitaet ZPO 482 --seit <Entscheidungsdatum>` — flaggt eine ZPO-Änderung nach der Entscheidung.

### Anwendung im Skill
Vollständiges Vorbringen erster Instanz (Neuerungsverbot) → Urteil → Rechtsmittel mit der richtigen Frist (4 Wochen / 14 Tage). Vor Stützung auf ältere Judikatur die Aktualität (`aktualitaet`) prüfen.
