---
name: anschluss-routing
description: "Anschluss-Routing für das Zivilprozess-/Exekutions-Plugin: wählt nach einem Zwischenergebnis den nächsten Spezial-Skill (Zuständigkeit, Mahnverfahren, Verfahrensgang/Rechtsmittel, Exekution) und dokumentiert die Router-Entscheidung mit Begründung. Österreich, kein deutsches Recht."
---

# Anschluss-Routing — Zivilprozess/Exekution

## Einsatzlage

Wählt nach dem ersten Ergebnis die passende Vertiefung, Fristensicherung oder den Vollstreckungsschritt. Aufruf, wenn unklar ist, welcher Spezial-Skill als Nächstes trägt.

## Fachlandkarte dieses Plugins

- `einstieg-zivilverfahren` — Anwalts-Dashboard / Sofort-Triage
- `zustaendigkeit-jn` — sachliche/örtliche Zuständigkeit (JN) + Anwaltspflicht (§ 27 ZPO)
- `mahnverfahren` — Zahlungsbefehl (≤ 75.000 €), Einspruch (§ 248)
- `verfahrensgang-rechtsmittel` — Klage/Säumnis/Neuerungsverbot, Berufung/Revision/Rekurs
- `exekution-eo` — Exekutionstitel (§ 1 EO), Exekutionsmittel

## Arbeitsweg

- **Ergebnis sichten:** Welche Frage ist beantwortet, welche bleibt offen?
- **Weiche stellen:**
  - **Titel vorhanden** → `exekution-eo`.
  - Gericht/Anwaltspflicht offen → `zustaendigkeit-jn`.
  - Geldforderung ≤ 75.000 €, kein Titel → `mahnverfahren`.
  - Einspruch erhoben / streitig / Rechtsmittel → `verfahrensgang-rechtsmittel`.
  - Außerhalb des Plugins (Außerstreit/AußStrG, Insolvenz/IO, einstweilige Verfügung, Liegenschaftsversteigerung im Detail, StPO, AVG/VwGVG) → ausdrücklich verweisen.
- **Konkreten Folge-Skill mit Slug benennen** — nicht generisch „weitermachen".
- **Fristen vorab markieren** (`[Frist prüfen: § 248 ZPO Einspruch / § 464 Berufung / § 521 Rekurs]`), nie aus Modellwissen finalisieren.
- **Mandantenkommunikation vorbereiten:** Was ist bis wann zu tun, welche Unterlagen (Titel, Zustellnachweis, Vermögensauskunft)?

## Qualitätsanker

- Normen und Judikatur nach `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md` behandeln — keine GZ aus Modellwissen; Existenzminimum-Werte stets live.
- Bei Zeitdruck zuerst Frist (Einspruch/Rechtsmittel), Zuständigkeit und Anwaltspflicht (§ 27 ZPO) sichern; ERV beachten.
- Eine Empfehlung ist eine Empfehlung; der Anwalt entscheidet.
