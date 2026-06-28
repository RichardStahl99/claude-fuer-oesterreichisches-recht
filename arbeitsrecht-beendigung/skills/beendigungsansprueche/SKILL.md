---
name: beendigungsansprueche
description: "Ermittelt die Geldansprüche bei Beendigung des Arbeitsverhältnisses: Abfertigung neu (BMSVG, 1,53 % an die BV-Kasse) bzw. alt (§ 23 AngG, vor 1.1.2003), Urlaubsersatzleistung (§ 10 UrlG) und Kündigungsentschädigung (§ 29 AngG) bei unberechtigter Entlassung/berechtigtem Austritt. Österreich, kein deutsches Recht."
---

# Beendigungsansprüche

## Fachlicher Anker

- **Normen (über RIS prüfen):** BMSVG (Abfertigung neu) — GNR 20002088 (§ 6 Beitrag, § 14 Anspruch); § 23 AngG (Abfertigung alt) — GNR 10008069 (Artikel 1); § 10 UrlG (Urlaubsersatzleistung) — GNR 10008376; § 29 AngG (Kündigungsentschädigung).
- **Vorgelagert:** `beendigungsart` (Art entscheidet, welche Ansprüche bestehen).
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`.

## Worum geht es?

Am Ende des Arbeitsverhältnisses sind die Geldansprüche zu klären. Welche bestehen, hängt von der **Beendigungsart** und vom **Beginn** des Arbeitsverhältnisses ab (Abfertigung alt vs. neu).

## Schritt-für-Schritt

1. **Abfertigung — System bestimmen (Stichtag 1. 1. 2003):**
   - **Abfertigung neu (BMSVG):** für Arbeitsverhältnisse **ab 1. 1. 2003** (oder übertragene). Der Arbeitgeber zahlt laufend **1,53 %** des Entgelts an die **Betriebliche Vorsorgekasse (BV-Kasse)** (§ 6 BMSVG); der Anspruch richtet sich gegen die **Kasse** (§ 14 BMSVG), **„Rucksackprinzip"** (er wandert mit). Auszahlung bei Beendigung nur unter Voraussetzungen: **mindestens 36 Beitragsmonate** (3 Jahre Einzahlung) **und** kein Auszahlungsausschluss — **nicht** bei **Arbeitnehmer-Kündigung**, unberechtigtem Austritt oder verschuldeter Entlassung (dann nur Weiterveranlagung in der Kasse).
   - **Abfertigung alt (§ 23 AngG):** für AV **vor 1. 1. 2003** (sofern nicht ins neue System übertragen). Direktanspruch gegen den AG, gestaffelt nach Dienstjahren (z. B. ab 3 Jahren 2 Monatsentgelte … bis 12 Monatsentgelte ab 25 Jahren). Entfällt bei AN-Kündigung, unberechtigtem Austritt oder verschuldeter Entlassung.
2. **Urlaubsersatzleistung (§ 10 UrlG):** für **nicht verbrauchten** Urlaub bei Beendigung — aliquot, in Höhe des Urlaubsentgelts. Kein Verfall offener Urlaubsansprüche durch die Beendigung selbst.
3. **Kündigungsentschädigung (§ 29 AngG):** bei **unberechtigter Entlassung** oder **berechtigtem vorzeitigen Austritt** schuldet der AG das Entgelt für den Zeitraum bis zum **nächsten möglichen Kündigungstermin** (fiktive Kündigungsfrist) — inkl. anteiliger Sonderzahlungen; Anrechnung anderweitigen Erwerbs möglich.
4. **Weitere offene Ansprüche** sichern: ausstehendes Entgelt, Überstunden, anteilige Sonderzahlungen, Zeugnis/Dienstzeugnis.
5. **Verjährung/Verfall:** kollektivvertragliche **Verfallsfristen** beachten (oft kurz!); allgemeine Verjährung nach ABGB. Live prüfen.

## Typische Fehler / Kritik

- **Abfertigung alt/neu verwechseln:** Stichtag 1. 1. 2003 entscheidet das System und den Schuldner (AG vs. BV-Kasse).
- **Abfertigung trotz AN-Kündigung erwartet:** bei AN-Kündigung/verschuldeter Entlassung idR kein Auszahlungsanspruch (neu: nur Weiterveranlagung; alt: Entfall).
- **KV-Verfallsfristen übersehen.**
- **Deutsches Recht:** keine „Abfindung nach § 1a KSchG (DE)", kein „§ 9 KSchG Auflösungsantrag". In Österreich Abfertigung (BMSVG/AngG), Urlaubsersatzleistung, Kündigungsentschädigung.

## Quellen und Stand 06/2026

- §§ 6, 14 BMSVG (RIS, GNR 20002088); § 23, § 29 AngG (RIS, GNR 10008069); § 10 UrlG (RIS, GNR 10008376).
- `references/methodik-buergerliches-recht.md`. Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)
- `§ 6 BMSVG` — Beitrag (1,53 %) · `§ 14 BMSVG` — Abfertigungsanspruch neu · `§ 23 AngG` — Abfertigung alt · `§ 10 UrlG` — Urlaubsersatzleistung · `§ 29 AngG` — Kündigungsentschädigung

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen; ObA-Senat)
- Abfertigung: `judikatur "Abfertigung Beendigung" --gericht OGH` (u. a. RIS-Justiz RS0047428 — live prüfen).
- Kündigungsentschädigung: `judikatur "Kündigungsentschädigung" --gericht OGH` (u. a. RIS-Justiz RS0039036 — live prüfen).

### Anwendung im Skill
Abfertigungssystem (Stichtag 2003) → Urlaubsersatz → Kündigungsentschädigung (nur bei unberechtigter Entlassung/berechtigtem Austritt) → KV-Verfallsfristen prüfen.
