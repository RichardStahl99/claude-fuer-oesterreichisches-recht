---
name: mahnverfahren
description: "Führt durch das österreichische automatische Mahnverfahren: Mahnklage und bedingter Zahlungsbefehl bei Geldforderungen bis 75.000 € (§§ 244 ff ZPO), Einspruch binnen vier Wochen (§ 248 ZPO) mit Überleitung ins streitige Verfahren, sonst rechtskräftiger und vollstreckbarer Titel. Österreich, kein deutsches Recht."
---

# Mahnverfahren und Zahlungsbefehl

## Fachlicher Anker

- **Normen (über RIS prüfen):** §§ 244–251 ZPO (automatisches Mahnverfahren, Zahlungsbefehl), § 248 ZPO (Einspruch) — GNR 10001699; Zuständigkeit nach JN (siehe `zustaendigkeit-jn`).
- **Vorgelagert:** `zustaendigkeit-jn` (Gericht + Anwaltspflicht).
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`.

## Worum geht es?

Bei **Geldforderungen bis 75.000 €** ist das **automatische Mahnverfahren zwingend**: Auf die **Mahnklage** erlässt das Gericht ohne Anhörung des Beklagten einen **bedingten Zahlungsbefehl**. Erhebt der Beklagte nicht rechtzeitig **Einspruch**, wird der Zahlungsbefehl **rechtskräftig und vollstreckbar** — ein Exekutionstitel ohne streitiges Verfahren.

## Schritt-für-Schritt

1. **Anwendbarkeit prüfen:** reine **Geldforderung** in inländischer Währung, Betrag **≤ 75.000 €**, kein Ausnahmefall → Mahnverfahren. (Über 75.000 € oder Nicht-Geldforderung → normale Klage, Skill `verfahrensgang-rechtsmittel`.)
2. **Mahnklage einbringen** (Anwälte zwingend per **ERV**), mit schlüssiger Darstellung von Forderung und Fälligkeit. Zuständigkeit nach JN (BG/LG, örtlich), Anwaltspflicht nach § 27 ZPO.
3. **Bedingter Zahlungsbefehl** ergeht und wird dem Beklagten zugestellt.
4. **Einspruch (§ 248 ZPO):** Der Beklagte kann binnen **vier Wochen** ab Zustellung Einspruch erheben; der Einspruch hat grundsätzlich den **Inhalt einer Klagebeantwortung** (§ 248 Abs 1). **Im bezirksgerichtlichen Mahnverfahren** braucht der Einspruch (und seine Zurücknahme) **keinen Anwalt** (§ 448 Z 1 ZPO) — auch im Bereich der absoluten Anwaltspflicht; es genügt, dass die Einspruchsabsicht deutlich hervorgeht (einfache Ausfertigung, ohne Rubriken), notfalls **mündlich zu Protokoll** beim BG des Aufenthalts (§ 448 Z 2 ZPO). **Im Mahnverfahren vor dem Landesgericht** (Streitwert über 15.000 € bis 75.000 €) gilt diese Erleichterung **nicht**: dort bleibt es beim Klagebeantwortungs-Inhalt (§ 248 Abs 1) und der absoluten Anwaltspflicht (§ 27 ZPO).
   - **Einspruch erhoben:** Der Zahlungsbefehl tritt außer Kraft; die Sache wird ins **ordentliche (streitige) Verfahren** übergeleitet (die Mahnklage gilt als Klage) → weiter zu `verfahrensgang-rechtsmittel`.
   - **Kein/verspäteter Einspruch:** Der Zahlungsbefehl wird **rechtskräftig und vollstreckbar** = **Exekutionstitel** → weiter zu `exekution-eo`.
5. **Frist sichern:** Die 4-Wochen-Einspruchsfrist (bzw. ihr Ablauf) ist der kritische Punkt; aus dem Zustelldatum rechnen.

## Typische Fehler / Kritik

- **Wertgrenze verkennen:** über 75.000 € kein Mahnverfahren.
- **Einspruchsfrist (4 Wochen) versäumt** auf Schuldnerseite → vollstreckbarer Titel; auf Gläubigerseite verfrüht Exekution beantragt, obwohl Frist noch läuft.
- **Einspruchs-Anwaltspflicht verwechseln:** Im **bezirksgerichtlichen** Mahnverfahren nimmt § 448 Z 1 ZPO den Einspruch von der Anwaltspflicht aus (formfrei) — den Schuldner nicht von der fristgerechten Einspruchserhebung abhalten. Im **LG-Mahnverfahren** (> 15.000 €) gilt das nicht: Anwalt + Klagebeantwortungs-Inhalt (§§ 248 Abs 1, 27 ZPO).
- **ERV ignoriert:** anwaltliche Eingaben sind elektronisch einzubringen.
- **Deutsches Recht:** kein „Mahnbescheid/Vollstreckungsbescheid nach §§ 688 ff ZPO (DE)", kein zentrales Mahngericht — in Österreich Zahlungsbefehl beim zuständigen BG/LG, Einspruch (nicht „Widerspruch").

## Quellen und Stand 06/2026

- §§ 244–251 ZPO, § 248 ZPO (RIS, GNR 10001699). Grenzüberschreitend: Europäisches Mahnverfahren (VO (EG) 1896/2006) — gesondert.
- `references/methodik-buergerliches-recht.md` Abschnitt 12. Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)
- `§ 244 ZPO` — Mahnverfahren/Zahlungsbefehl · `§ 248 ZPO` — Einspruch (4 Wochen) · `§ 448 ZPO` — bezirksgerichtliche Mahnverfahren-Besonderheiten (Einspruch ohne Anwalt, formfrei, zu Protokoll)

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen)
Zur Laufzeit ausführen (nicht nur verweisen):
- Zahlungsbefehl/Einspruch: `python3 tools/ris_client.py linie "Zahlungsbefehl" --gericht OGH --gesetz ZPO --paragraf 244` — OGH-Linie nach Linientiefe + Leitsätze. Für eine konkret herangezogene Geschäftszahl `leit <GZ>` (Leitentscheidung/Stamm? wie gefestigt die Linie?).
- Aktualität vor Stützung auf eine ältere Entscheidung: `aktualitaet ZPO 248 --seit <Entscheidungsdatum>` — flaggt eine Änderung der Einspruchsregelung nach der Entscheidung.

### Anwendung im Skill
Wertgrenze (≤ 75.000 €) → Mahnklage (ERV) → Zahlungsbefehl → Einspruch (4 Wo.) entscheidet: streitig oder vollstreckbarer Titel. Vor Stützung auf ältere Judikatur die Aktualität (`aktualitaet`) prüfen.
