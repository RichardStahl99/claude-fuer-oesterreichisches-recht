---
name: anschluss-routing
description: "Anschluss-Routing für das Arbeitsrecht-Beendigung-Plugin: wählt nach einem Zwischenergebnis den nächsten Spezial-Skill (Beendigungsart, Fristen, Anfechtung, Ansprüche) und dokumentiert die Router-Entscheidung mit Begründung. Österreich, kein deutsches Recht."
---

# Anschluss-Routing — Arbeitsrecht (Beendigung)

## Einsatzlage

Wählt nach dem ersten Ergebnis die passende Vertiefung, Fristensicherung oder Anspruchsklärung. Aufruf, wenn unklar ist, welcher Spezial-Skill als Nächstes trägt.

## Fachlandkarte dieses Plugins

- `einstieg-arbeitsrecht` — Anwalts-Dashboard / Sofort-Triage
- `beendigungsart` — Kündigung / Entlassung / einvernehmlich / Zeitablauf / Austritt / Probezeit
- `kuendigungsfristen-termine` — § 20 AngG / § 1159 ABGB, Kündigungstermin
- `kuendigungsschutz-anfechtung` — § 105 ArbVG (Sozialwidrigkeit/Motiv), Betriebsrat, 2-Wochen-Frist, ASG
- `beendigungsansprueche` — Abfertigung (neu/alt), Urlaubsersatz, Kündigungsentschädigung

## Arbeitsweg

- **Ergebnis sichten:** Welche Frage ist beantwortet, welche bleibt offen?
- **Sofort bei AG-Kündigung:** die **2-Wochen-Anfechtungsfrist** (§ 105 Abs 4 ArbVG) markieren, bevor irgendetwas anderes — sie ist kurz und nicht verlängerbar.
- **Weiche stellen:**
  - Beendigungsart offen → `beendigungsart` (zuerst).
  - Kündigung, Frist/Termin fraglich → `kuendigungsfristen-termine`.
  - Kündigung anfechten → `kuendigungsschutz-anfechtung`.
  - Geld am Ende → `beendigungsansprueche`.
  - Verhältnis läuft weiter, Bedingungen ändern sich (Nachtrag/Änderungsangebot) → Skill `einstieg-vertragsaenderung` im Plugin `arbeitsrecht-vertragsaenderung`.
  - Außerhalb des Plugins (laufendes AV, Entgelt/Arbeitszeit, GlBG-Diskriminierung, Betriebsübergang AVRAG, Sozialversicherung, besonderer Kündigungsschutz im Detail) → ausdrücklich verweisen.
- **Konkreten Folge-Skill mit Slug benennen** — nicht generisch „weitermachen".
- **Fristen vorab markieren** (`[Frist prüfen: § 105 Abs 4 ArbVG — 2 Wochen]`), nie aus Modellwissen finalisieren.
- **Mandantenkommunikation vorbereiten:** Was ist bis wann zu tun, welche Unterlagen (Kündigungsschreiben mit Zugangsdatum, Dienstvertrag, Betriebsrats-Verständigung, KV)?

## Qualitätsanker

- Normen und Judikatur nach `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md` behandeln — keine GZ aus Modellwissen. Linie/Leitsätze **zur Laufzeit ausführen (nicht nur verweisen):** `python3 tools/ris_client.py linie "<Stichworte>" --gericht OGH`, eine konkret benannte GZ mit `leit <GZ>` als Leitentscheidung (Stamm) prüfen und ältere Entscheidungen vor Übernahme per `aktualitaet <Gesetz> <§> --seit <Entscheidungsdatum>` auf Aktualität gegenprüfen (z. B. `aktualitaet ABGB 1159 --seit <Datum>` für die Arbeiter-Angleichung seit 1.10.2021). Arbeitsrecht: 8./9. Senat (ObA); KV/Beträge stets live.
- Bei Zeitdruck zuerst die **Anfechtungsfrist (2 Wochen)** und das Verfahren (ASG) sichern.
- Eine Empfehlung ist eine Empfehlung; der Anwalt entscheidet.
