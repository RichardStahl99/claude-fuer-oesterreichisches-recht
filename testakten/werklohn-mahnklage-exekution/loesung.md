# Lösung / Triage — Werklohn: Mahnklage und Exekution

> Musterlauf der Plugin-Pipeline gegen `sachverhalt.md`. **Jede** Norm-Fundstelle ist über RIS auflösbar (Permalinks unten); Geschäftszahlen/RS-Nummern über `tools/ris_client.py` verifizieren (Leitsatz vor Verwendung lesen). **Existenzminimum-Werte live beziehen.** Keine Rechtsberatung.

## Sofort-Triage (Dashboard)

| Punkt | Befund | Quelle |
|---|---|---|
| Rolle | Gläubigerin (Klägerin), Unternehmerin | Rechnung |
| Titel vorhanden? | **Nein** — Titel erst zu erwirken | Akt |
| **Zuständigkeit** | Streitwert 8.500 € → **BG Graz** (≤ 15.000 €, keine Eigenzuständigkeit); örtlich Wohnsitz des Beklagten (Graz) | `zustaendigkeit-jn`, §§ 49, 66 JN |
| Anwaltspflicht | 8.500 € > 5.000 € am BG → **absolute Anwaltspflicht (ja)** | § 27 Abs 1 ZPO |
| Verfahrensweg | Geldforderung ≤ 75.000 € → **Mahnverfahren** (Zahlungsbefehl) | `mahnverfahren`, § 244 ZPO |
| Frist | **Einspruch 4 Wochen** (§ 248) nach Zustellung; danach vollstreckbar | `mahnverfahren` |

## Risiko-Ampel

- 🟢 **Frist** — derzeit keine laufende Frist; nach Zustellung des Zahlungsbefehls die 4-Wochen-Einspruchsfrist beobachten.
- 🟢 **Beweis** — Auftrag, Lieferschein mit Übernahme, Rechnung: belastbar.
- 🟠 **Einbringlichkeit** — Schuldner unselbständig erwerbstätig → **Gehaltsexekution** aussichtsreich; sonstiges Vermögen unbekannt.

## Rechtliche Beurteilung (Kurzgutachten)

1. **Kein Titel:** Es ist zunächst ein Exekutionstitel zu erwirken.
2. **Zuständigkeit (JN):** Streitwert 8.500 €, keine Eigenzuständigkeit (kein Bestand-/Familienfall) → **sachlich BG** (≤ 15.000 €, § 49 JN). Örtlich der allgemeine Gerichtsstand des Beklagten (Wohnsitz Graz, § 66 JN); keine Gerichtsstandsvereinbarung. → **BG Graz**.
3. **Anwaltspflicht:** Am BG besteht ab einem Streitwert über 5.000 € **absolute Anwaltspflicht** (§ 27 Abs 1 ZPO) — hier (8.500 €) also **Anwaltspflicht**.
4. **Verfahrensweg:** Reine Geldforderung ≤ 75.000 € → zwingend **automatisches Mahnverfahren**: Mahnklage (per ERV) → bedingter **Zahlungsbefehl** (§§ 244 ff ZPO).
5. **Einspruch (§ 248):** Erhebt Herr Novak binnen **vier Wochen** Einspruch, wird ins streitige Verfahren übergeleitet (`verfahrensgang-rechtsmittel`; dort Neuerungsverbot/Fristen beachten). Andernfalls wird der Zahlungsbefehl **rechtskräftig und vollstreckbar**.
6. **Exekution (EO):** Mit dem vollstreckbaren Zahlungsbefehl (Titel § 1 EO, Vollstreckbarkeit § 7) Exekutionsantrag beim BG; angesichts unselbständiger Erwerbstätigkeit ist die **Gehaltsexekution** (§§ 290 ff EO) das naheliegende Mittel — **Existenzminimum** bleibt unpfändbar (§ 291a EO).

## Empfehlung (nächste Schritte)

- Mahnklage über ERV beim **BG Graz** einbringen (Forderung schlüssig, Urkunden anschließen).
- Zustellung/Einspruchsfrist überwachen.
- Bei Vollstreckbarkeit: Exekutionsantrag, vorrangig **Gehaltsexekution**; Vermögensauskunft erwägen.

## Verifizierte Quellen (RIS)

**Normen (Permalinks, HTTP 200 geprüft):**
- § 49 JN — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001697&Paragraf=49
- § 66 JN — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001697&Paragraf=66
- § 27 ZPO — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001699&Paragraf=27
- § 248 ZPO — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001699&Paragraf=248
- § 1 EO — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001700&Paragraf=1
- § 290 EO — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001700&Paragraf=290

**Judikatur (zur Laufzeit über RIS auflösen — Leitsatz vor Verwendung lesen; keine Geschäftszahl/Rechtssatz aus Modellwissen):**
- Einschlägige OGH-Judikatur zu Gerichtsstandsvereinbarung/Zuständigkeit (§ 104 JN), Zahlungsbefehl (§ 244 ZPO) und Exekutionstitel/Bestimmtheit (§§ 1, 7 EO) erst zur Laufzeit über die folgenden `linie`-Befehle beziehen; den Leitsatz vor Verwendung lesen und eine konkret herangezogene Geschäftszahl mit `leit <GZ>` (Leitentscheidung/Stamm? Linientiefe?) absichern.

Reproduzieren: `python3 tools/ris_client.py linie "Gerichtsstandsvereinbarung Zuständigkeit" --gericht OGH --gesetz JN --paragraf 104` bzw. `linie "Zahlungsbefehl" --gericht OGH --gesetz ZPO --paragraf 244` und `linie "Exekutionstitel" --gericht OGH --gesetz EO --paragraf 1` (Leitsätze nach Linientiefe; die je herangezogene Geschäftszahl mit `leit <GZ>` bestätigen). Aktualität vor Stützung auf ältere Entscheidungen (Verfahrensnormen, EO-Reform 2021): `aktualitaet EO 1 --seit <Entscheidungsdatum aus leit/linie>`, ebenso `aktualitaet JN 104` bzw. `aktualitaet ZPO 248`.

> Hinweis: Diese Triage ist Vorbereitung, nicht Entscheidung. Der Anwalt führt das Mandat.
