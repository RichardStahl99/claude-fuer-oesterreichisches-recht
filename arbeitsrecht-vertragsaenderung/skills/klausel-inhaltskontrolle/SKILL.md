---
name: klausel-inhaltskontrolle
description: "Klauselweise Inhaltskontrolle nach § 879 Abs 3 ABGB (gröbliche Benachteiligung): Bonus-Widerruf, Versetzung, All-in, Urlaub, Haftungsdeckel. Kein deutsches Recht."
---

# Klausel-Inhaltskontrolle — § 879 Abs 3 ABGB

## Fachlicher Anker

- **Zentrale Norm:** § 879 Abs 3 ABGB (GNR 10001622) — in Kraft seit 1992-07-01; Fassungsstand unverändert (RIS-Aktualitätsprüfung). Klauselkontrolle gilt für **jede vorformulierte Klausel** in jedem Vertragsverhältnis (B2B ebenso wie B2C); der Maßstab der gröblichen Benachteiligung ist keine Verbraucherschutznorm, sondern allgemein vertragsrechtlich.
- **Leitdoktrin:** RIS-Justiz RS0016914 (OGH 1 Ob 581/83, 177 Entscheidungen): „Durch die Bestimmung des § 879 Abs 3 ABGB wurde eine objektive Äquivalenzstörung und ‚verdünnte Willensfreiheit' berücksichtigendes bewegliches System geschaffen. Bei der Abweichung einer Klausel von dispositiven Rechtsvorschriften liegt gröbliche Benachteiligung eines Vertragspartners schon dann vor, wenn sie unangemessen ist." — OGH 1 Ob 105/10p folgt dieser Linie (Entgeltklausel-Kontrolle; Linientiefe 177 Entscheidungen; RIS verifiziert).
- **Weitere Normen (alle HTTP 200 in RIS verifiziert):**
  - § 19c AZG (GNR 10008238) — Arbeitszeitgesetz; Lage der Normalarbeitszeit (Ausmaß = §§ 3 ff AZG); zwingend nach RS0118331.
  - § 2g AVRAG (GNR 10008872) — All-in-Vereinbarung: Transparenzgebot, Trennbarkeit Grundentgelt/Überstundenanteil.
  - § 2 Abs 1 URLG (GNR 10008376) — Urlaubsausmaß: 30 Werktage (= 25 Arbeitstage / 5 Wochen) bei Dienstzeit unter 25 Jahren; 36 Werktage (= 30 Arbeitstage / 6 Wochen) ab dem vollendeten 25. Dienstjahr.
  - § 12 URLG (GNR 10008376) — Unabdingbarkeit: der gesetzliche Urlaubsanspruch (§ 2 Abs 1 URLG) ist nicht abdingbar.
  - § 2 DHG (GNR 10008209, Artikel 1) — Dienstnehmerhaftpflichtgesetz: Haftungsmaßstab (leichte/grobe Fahrlässigkeit, Vorsatz).
  - § 5 DHG (GNR 10008209, Artikel 1) — DHG: Mäßigungsrecht des Gerichts; Haftungsdeckel nicht unter DHG-Boden absenkbar.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md` (§ 3 Grounding-Protokoll). Keine GZ aus Modellwissen — nur RIS-verifizierte Fundstellen verwenden.

## Einsatzlage

Dieser Skill prüft konkrete Klauseln eines Arbeitsvertrags oder einer Vertragsänderung nach dem Maßstab des § 879 Abs 3 ABGB. Er ist **nachgelagert** zum Änderungs-Regime-Gate-Skill (`aenderungsregime`) und bewertet: Ist die Klausel wirksam, gröblich benachteiligend (sittenwidrig/nichtig) oder ein Grenzfall?

**Typische Klauseltypen im Arbeitsvertrag:**

| Klauseltyp | Typischer Wortlaut (Vorlage) | Kernrisiko |
|---|---|---|
| **Bonus-Widerruf** | „Der Bonus kann jederzeit nach freiem Ermessen widerrufen werden." | Bereits verdiente Anteile sind unwiderruflich: nach Beginn des Erfolgszeitraums darf der DG die Prämie weder einseitig widerrufen noch an Bedingungen im alleinigen DG-Einflussbereich knüpfen (**RS0028333**, OGH 9 ObA 101/90, 09.05.1990; Norm: ABGB § 879 BIIh, AngG § 16 IV); Widerrufsklausel ggf. § 879 Abs 3-widrig |
| **Versetzung geringerwertig** | „Der Arbeitgeber kann den AN auf eine geringerwertige Stelle versetzen." | Entgelt- und Bestandsschutz; ohne Betriebsrat: § 879 Abs 3 als Individualkontrolle |
| **All-in** | „Das Gehalt von X Euro pauschal deckt alle Überstunden ab." | Transparenzgebot § 2g AVRAG; kein Verzicht auf das Übersteigende; Durchrechnungszeitraum = Kalenderjahr |
| **Arbeitszeit-Lage** | „Die Einteilung der Arbeitszeit obliegt allein dem Arbeitgeber." | § 19c AZG: Lage der Normalarbeitszeit zwingend; einseitiger Gestaltungsvorbehalt unwirksam |
| **Urlaub** | „Der Urlaubsanspruch (inkl. der 6. Woche) kann nach Ermessen des Arbeitgebers verändert werden." | Gesetzliches Urlaubsausmaß (§ 2 Abs 1 URLG) nicht abdingbar (§ 12 URLG); 6. Woche klauselfähig, nicht der Kern |
| **Haftungsdeckel** | „Die Haftung des AN ist auf X Monatsgehälter begrenzt." | DHG-Boden (§§ 2, 5 DHG) nicht unterschreitbar; Vorsatz-Ausschluss nichtig |

**Nicht für:** Regime-Frage (einvernehmlich/Änderungskündigung → `aenderungsregime`), Beendigungsrecht (→ `einstieg-arbeitsrecht`), Fremdrechts-Prüfung (→ `deutsche-vorlage-audit`).

## Sofort-Triage

Eine Zeile pro Klauseltyp — Erstbewertung anhand des Klauseltexts **ohne Sachverhaltsdetails**:

| Klauseltyp | Prüfpunkt | Ampel | Norm-Anker | Judikatur-Linie |
|---|---|---|---|---|
| **Bonus-Widerruf — bereits verdient** | Steht die Periode ab? Wurde der Bonus nach Zielvereinbarung erzielt? Vorbehaltlose Auszahlung in Vorperioden? | 🔴 | § 879 Abs 3 ABGB | RS0016914; **RS0028333** (OGH 9 ObA 101/90 — verdiente Prämie unwiderruflich nach Beginn des Erfolgszeitraums; ABGB § 879 BIIh, AngG § 16 IV); OGH 8 ObA 33/21t folgt RS0042828 (272 E) + RS0014154 (68 E) |
| **Bonus-Widerruf — künftige Variable (Widerrufsvorbehalt)** | Ist der Vorbehalt klar und begrenzt? Oder grenzenlos? Grober Ermessensspielraum = Grenzfall | 🟠 | § 879 Abs 3 ABGB | RS0016914; OGH 8 ObA 16/03s folgt RS0112269 (25 E); [Toleranzschwelle: Prüfpunkt — Volltext RIS abrufen] |
| **Versetzung auf geringerwertige Tätigkeit** | Kein Betriebsrat? Nur § 879 Abs 3 ABGB als Individualschutz. Mit BR: Zustimmungspflicht nach § 101 ArbVG vorgelagert — **§ 101 ArbVG ist der kollektive Prong** (setzt Betriebsrat voraus); der no-BR-Mandant erhält keinen § 101-Schutz. Verschlechterungsbegriff nach RS0051209: jede Änderung zum Nachteil des AN (materiell + immateriell); Entgelt im weitesten Sinn; Beisätze: Wegfall Überstundenpauschale [T3], Entgeltverschlechterung [T4]. | 🔴 | § 879 Abs 3 ABGB (kein BR); § 101 ArbVG (mit BR) | RS0016914 (Entgeltklausel-Kontrolle); RS0051209 (OGH 4 Ob 79/85; 17 E; Verschlechterungsbegriff § 101 ArbVG) |
| **All-in — fehlende Transparenz (§ 2g AVRAG)** | Deckt das Pauschalentgelt die geleisteten Überstunden tatsächlich ab? Ist die Überstundenkomponente trennbar ausgewiesen? | 🔴 | § 2g AVRAG (Transparenz); § 879 Abs 3 ABGB | § 2g AVRAG: Trennbarkeit Grundentgelt/Überstundenanteil (Transparenzgebot); RS0131677 (Leitentscheidung OGH 9 ObA 28/17h — AZG § 19: Durchrechnungszeitraum = Kalenderjahr, nicht § 2g AVRAG); RS0130178 (Trennbarkeit All-in bei Elternteilzeit: OGH 8 ObA 22/22a; 9 ObA 62/25w); **RS0051519** (OGH 4 Ob 66/84; 28 E; Norm: AZG § 10): Pauschalentlohnung grundsätzlich zulässig, hindert AN aber nicht, über das Pauschale hinausgehende **unabdingbare** Ansprüche zu erheben, soweit nicht gedeckt — **AG hat grundsätzlich zu überprüfen, ob die geleisteten Überstunden durch das Pauschale gedeckt waren** (T4; T6: AG trägt das Deckungsrisiko). Aktualitätshinweis: § 10 AZG geändert durch BGBl I Nr. 53/2018 (12-h-Reform, in Kraft seit 2018-09-01); die Deckungsdoktrin (RS0051519) ist von dieser Änderung inhaltlich unberührt. |
| **All-in — Verzicht auf das Übersteigende** | Sagt die Klausel, das Pauschalentgelt decke „alle" Überstunden ungeachtet der tatsächlichen Leistung? | 🔴 | § 2g AVRAG (Transparenz); § 879 Abs 3 ABGB | RS0131677 (Leitentscheidung 9 ObA 28/17h — AZG § 19): Verfall-Frist beginnt erst mit Ende des Durchrechnungszeitraums (Kalenderjahr); kein Vorab-Verzicht. RS0051519: AN kann über das Pauschale hinausgehende unabdingbare Ansprüche erheben, soweit die tatsächlich geleisteten Überstunden nicht gedeckt sind. |
| **Arbeitszeit-Lage — einseitiger Gestaltungsvorbehalt** | Macht die Klausel Ausmaß oder Lage der Arbeitszeit einseitig vom Arbeitgeber-Ermessen abhängig? | 🔴 | § 19c AZG | RS0118331 (OGH 8 ObA 86/03k): § 19c AZG für Vollzeit-Lage zwingend; OGH 9 ObA 57/22f folgt RS0118331, sein Beisatz stützt sich auf § 19d Abs 2 AZG (Teilzeit/Schriftform); einseitiger Gestaltungsvorbehalt ist insoweit unwirksam |
| **Urlaub — gesetzliches Minimum (§ 2 Abs 1 URLG)** | Tastet die Klausel den gesetzlich garantierten Jahresurlaub an? Fehlt Aufforderungs-/Hinweispflicht des AG? | 🔴 | § 2 Abs 1 URLG; § 12 URLG | RS0134421 (Leitentscheidung OGH 8 ObA 23/23z): gesetzlicher Urlaubsanspruch verjährt nicht ohne AG-Hinweis; RS0114580 (OGH 9 ObA 135/14i): Urlaubsvorgriff muss vollem Urlaubsäquivalent entsprechen |
| **Urlaub — 6. Woche (vertraglicher Mehranspruch)** | Betrifft die Klausel nur die vertraglich gewährte 6. Woche, nicht das gesetzliche Minimum? | 🟠 | § 2 Abs 1 URLG; § 12 URLG | Kernschutz des § 2 Abs 1 URLG (Ausmaß, unabdingbar nach § 12 URLG) gilt für das gesetzliche Mindestausmaß; vertraglicher Mehranspruch ist grundsätzlich modifizierbar (Prüfpunkt: Verschlechterungsschutz nach Regime-Triage) |
| **Haftungsdeckel unter DHG-Boden** | Setzt die Klausel die Haftung des AN unter den DHG-Mindeststandard (grobe Fahrlässigkeit/Vorsatz)? Schließt sie Vorsatz aus? | 🔴 | §§ 2, 5 DHG | DHG-Haftungsrahmen zwingend; vertragliche Unterschreitung des Mindestrahmens (Vorsatz, grobe Fahrlässigkeit) ist nach § 879 Abs 3 ABGB sittenwidrig und nichtig |

## Risiko-Ampel

- 🔴 **Klausel greift in zwingenden Kernbereich ein** — Verstoß gegen § 19c AZG (Arbeitszeit), § 2 Abs 1 URLG (Urlaubsausmaß), § 12 URLG (Unabdingbarkeit), §§ 2, 5 DHG (Haftungsrahmen) oder bereits verdientes Entgelt (§ 879 Abs 3 ABGB): Klausel im betroffenen Umfang **nichtig**, Restklausel ggf. nach § 879 Abs 1 ABGB aufrechterhaltbar. Sofortiger Handlungsbedarf.
- 🔴 **All-in ohne nachweisbaren Überstundenanteil / Deckungslücke** — § 2g AVRAG-Verstoß; Arbeitgeber trägt Beweislast und Deckungsrisiko (RS0051519 [T4/T6]): hat grundsätzlich zu überprüfen, ob die geleisteten Überstunden durch das Pauschale gedeckt waren. Fehlt die betragsmäßige Angabe des Grundgehalts (§ 2 Abs 2 Z 9), greift § 2g AVRAG als **Berechnungsgrundlage**: zwingender Anspruch auf das branchen- und ortsübliche Ist-Grundgehalt vergleichbarer Arbeitnehmer:innen, das der Abgeltung der Entgeltbestandteile zugrunde zu legen ist (**keine** Einzelverrechnung *aller* Überstunden). Zusätzlich verrechenbar bleiben nur die durch das Pauschale **nicht gedeckten** Überstunden (RS0051519). Sofortiger Handlungsbedarf.
- 🟠 **Bonus-Widerrufsvorbehalt — unklare Reichweite** — Klausel möglicherweise § 879 Abs 3-widrig, wenn sie unbegrenzte Willkür erlaubt. Grenzfall: Verhältnismäßigkeitsprüfung (konkrete Umstände erforderlich). Vorbehalt sichern, Volltext der einschlägigen OGH-Entscheidungen über RIS abrufen.
- 🟠 **6. Urlaubswoche als alleiniges Zielobjekt der Klausel** — Modifikation des Mehrurlaubs über den gesetzlichen Mindestanspruch hinaus grundsätzlich möglich, aber: Verschlechterungsverbot nach `aenderungsregime` prüfen (einvernehmlich, Änderungskündigung oder konkludent?). Vorsicht bei kombinierten Klauseln.
- 🟢 **Klausel betrifft nur disponibles Recht, Ausgestaltung angemessen** — § 879 Abs 3 ABGB erfordert kein Missverhältnis, wenn die Regelung vertretbarer Kompromiss auf Basis der konkreten Verhandlungsposition ist.

## Anschluss-Skill-Router

| Wenn der Fall trägt … | dann Skill | Erwartung |
|---|---|---|
| Klauseltext trägt Merkmale eines deutschen Rechtsmusters (§§ BGB-Zitate, „Treu und Glauben" ohne österreichischen Bezug, HGB-Terminologie) | `deutsche-vorlage-audit` | Falsche-Freunde-Analyse; Anpassung auf AT-Recht |
| Klausel ist unwirksam und AN erwägt Austritt oder Gehaltsrückforderung | `austritt-backstop-und-hebel` | § 26 AngG Austrittsrecht; Druckmittel / Vorbehaltsstrategie |

Priorität: Bei **§ 19c AZG**, **§ 2 Abs 1 URLG** und **§ 12 URLG**-Verstößen die Verjährung beachten — die **Entgeltansprüche** der Arbeitnehmer (z.B. nicht abgegoltene Überstunden) verjähren nach der besonderen 3-Jahres-Frist des **§ 1486 Z 5 ABGB**. Das ist eine Frist für die dort enumerierten Forderungsarten (Z 5 = Entgelt aus dem Dienstvertrag), keine pauschale Frist für jeden Anspruch, und sie läuft unabhängig davon, ob ein Vorbehalt gesetzt wurde.

## Judikatur-Anker (Such-Wegweiser, kein Blindzitat)

Zur Laufzeit ausführen — **keine GZ aus Modellwissen behaupten**, nur RIS-geliefertes übernehmen:

- **Leitdoktrin § 879 Abs 3 ABGB / Entgeltklausel-Kontrolle:**
  `python3 tools/ris_client.py judikatur "RS0016914" --gericht OGH` → RIS-Justiz RS0016914 (OGH 1 Ob 581/83; zuletzt OGH 1 Ob 105/10p bestätigt).
- **Bonus-Widerruf / Empfängerhorizont:**
  `python3 tools/ris_client.py leit "8 ObA 33/21t"` → folgt RS0042828 (272 E) + RS0014154 (68 E); Klauselkontrolle im Entgeltbereich.
- **Bonus-Widerruf / verdiente Prämie unwiderruflich nach Beginn des Erfolgszeitraums:**
  `python3 tools/ris_client.py volltext "JJR_19900509_OGH0002_009OBA00101_9000000_002"` → RS0028333 (OGH 9 ObA 101/90, 09.05.1990; Norm: ABGB § 879 BIIh, AngG § 16 IV): Freiwilligkeit/Widerruflichkeit berechtigt DG, für **künftige** Zeiträume von der Prämiengewährung abzugehen; ist die Prämie jedoch für die Erreichung eines Erfolges in einem bestimmten Zeitabschnitt zugesagt, darf sie nach Beginn dieses Zeitraumes vom Arbeitgeber weder einseitig widerrufen werden noch darf die Zahlung von Bedingungen abhängig gemacht werden, deren Eintritt ausschließlich im Einflussbereich des Arbeitgebers liegt.
- **Widerrufsvorbehalt / Gestaltungsrecht:**
  `python3 tools/ris_client.py leit "8 ObA 16/03s"` → folgt RS0112269 (25 E — Änderungsvorbehalt nach billigem Ermessen); Toleranzschwelle: Volltext abrufen.
- **All-in / Durchrechnungszeitraum Kalenderjahr (AZG § 19):**
  `python3 tools/ris_client.py volltext "JJR_20170927_OGH0002_009OBA00028_17H0000_001"` → RS0131677, OGH 27.09.2017, 9 ObA 28/17h (Leitentscheidung).
- **All-in / Elternteilzeit / Trennbarkeit:**
  `python3 tools/ris_client.py judikatur "RS0130178" --gericht OGH` → folgt OGH 8 ObA 22/22a (24.10.2022) + OGH 9 ObA 62/25w (19.02.2026).
- **All-in / Deckungsprüfung AG / unabdingbare Ansprüche (AZG § 10):**
  `python3 tools/ris_client.py leit "4 Ob 66/84"` → RS0051519 (OGH 4 Ob 66/84; 28 Entscheidungen; Norm: AZG § 10): Pauschalentlohnung zulässig, hindert AN aber nicht, über das Pauschale hinausgehende unabdingbare Ansprüche zu erheben; T4: Sache des AG, sich zu unterrichten, ob geleistete Überstunden gedeckt waren; T6: AG hat grundsätzlich zu überprüfen, ob Überstundenpauschale tatsächlich abdeckt. Aktualitätshinweis: § 10 AZG geändert durch BGBl I Nr. 53/2018 — Deckungsdoktrin unberührt.
- **Versetzung / Verschlechterungsbegriff § 101 ArbVG (kollektiver Prong):**
  `python3 tools/ris_client.py leit "4 Ob 79/85"` → RS0051209 (OGH 4 Ob 79/85; 17 Entscheidungen; Norm: ArbVG § 101): Verschlechterung = jede Änderung zum Nachteil des AN (materiell + immateriell); Vergleich Lage vor/nach Versetzung; Entgelt im weitesten Sinn; T3: Wegfall Überstundenpauschale; T4: Entgeltverschlechterung. **Hinweis: § 101 ArbVG setzt Betriebsrat voraus (kollektiver Prong); kein Schutz für no-BR-Betrieb über § 101 — dort gilt § 879 Abs 3 ABGB (RS0016914).**
- **§ 19c AZG zwingend (Vollzeit-Lage):**
  `python3 tools/ris_client.py volltext "JJR_20031113_OGH0002_008OBA00086_03K0000_001"` → RS0118331 (OGH 8 ObA 86/03k, Stamm); OGH 9 ObA 57/22f (14.07.2022) folgt RS0118331, sein Beisatz stützt sich auf § 19d Abs 2 AZG (Teilzeit/Schriftform).
- **Urlaubsrecht / Verjährung / Aufforderungspflicht:**
  `python3 tools/ris_client.py volltext "JJR_20230627_OGH0002_008OBA00023_23Z0000_000"` → RS0134421, OGH 27.06.2023, 8 ObA 23/23z (Leitentscheidung).
- **Urlaubsvorgriff / Äquivalenzgebot:**
  `python3 tools/ris_client.py judikatur "RS0114580" --gericht OGH` → OGH 9 ObA 135/14i (29.01.2015) bestätigt.
- **Aktualität (Pflicht vor Übernahme älterer Entscheidungen):**
  `python3 tools/ris_client.py aktualitaet ABGB 879 --seit 1992-07-01` → unverändert (in Kraft seit 1992-07-01).
  `python3 tools/ris_client.py aktualitaet AZG 19c --seit 2003-11-13` (Datum RS0118331-Stamm; manuell prüfen).

## Hinweis

Dieser Skill bewertet einzelne Klauseln, nicht den Vertrag als Ganzes. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Das Mandat führen Sie; der Skill liefert die rechtliche Karte.
