# Lösung / Triage — Dienstvertrag-Nachtrag: Änderungsangebot

> Musterlauf der Plugin-Pipeline gegen `sachverhalt.md`. **Jede** Norm-Fundstelle ist über RIS auflösbar (Permalinks unten); Geschäftszahlen/RS-Nummern über `tools/ris_client.py` verifizieren (Leitsatz vor Verwendung lesen). **KV-Inhalte und Beträge (IT-KV, UBIT) live beziehen.** Alle Zahlen fiktiv/illustrativ. Keine Rechtsberatung.

---

## (1) Einstieg-Dashboard — Sofort-Triage (`einstieg-vertragsaenderung`)

| Punkt | Befund | Quelle |
|---|---|---|
| Rolle | Angestellte:r (aufrechtes DV, ca. 1 Jahr); AN-Seite | Dienstvertrag |
| Betriebsrat | **kein eigener BR** (Schwestergesellschaft hat BR — eigene Rechtsperson, kein Übergriff) | Sachverhalt |
| **Änderungsweg** | Einvernehmliches Änderungsangebot via elektronisches Signaturtool; **nicht unterschrieben** → kein Konsens; Bestandsvertrag gilt | `aenderungsregime` |
| DE-Vorlage erkennbar? | **Ja** — ArbnErfG, Textform, EFZG, außerordentliche Kündigung ohne Abmahnung, BAG-Haftungsdeckel | `deutsche-vorlage-audit` |
| Hebel/Austritt | Unterschrift nicht gesetzt → § 26 Z 2 AngG-Backstop **erhalten**; Fix-Erhöhung möglicherweise bereits konkludent bindend (§ 863 ABGB, nächste Auszahlung prüfen) | `austritt-backstop-und-hebel` |
| Leitende:r Angestellte:r? | Führungsrolle Vertrieb — prüfen, ob echte Hire-&-Fire-/Gehaltskompetenz (§ 36 Abs 2 Z 3 ArbVG); bloßer Titel genügt nicht | Dienstvertrag, Vollmacht |

### Risiko-Ampel

- 🔴 **Konkludente Bindung an Fix-Erhöhung** — nimmt die Mandantin/der Mandant die nächste Gehaltszahlung vorbehaltlos an, ist die Fixerhöhung (€ +4.000) schlüssig akzeptiert (§ 863 ABGB, RS0014526). Die gleichzeitigen Verschlechterungen werden dadurch **nicht** automatisch mitgezogen — aber der Hebel schwächt sich. **Vorbehalt vor der nächsten Auszahlung sichern.**
- 🔴 **DE-Vorlage** — mehrere Klauseln basieren auf deutschem Recht ohne österreichische Entsprechung oder mit abweichendem Regelungsinhalt; in diesen Teilen unwirksam oder leer.
- 🟠 **Variabler Anteil ~35 %** — Widerrufsvorbehalt „jederzeit gänzlich oder teilweise" bedroht den wirtschaftlichen Kern des Angebots; § 879 Abs 3 ABGB-Kontrolle erforderlich.
- 🟠 **Urlaub** — Verfall der 5 Zusatztage ohne Ersatzleistung greift in den gesetzlichen Mindestanspruch ein, soweit die Gesamtdauer 25 Tage unterschreitet oder Hinweispflichten fehlen.

---

## (2) Änderungsregime (`aenderungsregime`)

### Einordnung

Der Nachtrag ist ein **einvernehmliches Änderungsangebot** — keine Änderungskündigung. Ohne Unterschrift besteht kein Konsens; § 863 ABGB setzt schlüssiges Verhalten beider Seiten voraus. Nach dem Kernsatz (RIS-Justiz RS0109380, OGH 12.02.1998, 8 ObA 35/98z): „Die einzige Möglichkeit, die Verschlechterung der Entgeltbedingungen rechtlich zulässig vorzunehmen, ist neben einer einvernehmlichen Vertragsänderung die Änderungskündigung." Da weder Konsens noch Änderungskündigung vorliegt, läuft der **Bestandsvertrag weiter**.

### Konkludenz-Risiko: Fix-Erhöhung (§ 863 ABGB)

Wird die Fix-Erhöhung auf € 119.000 (fiktiv/illustrativ) erstmals ausbezahlt und von der Mandantin/dem Mandanten vorbehaltlos angenommen, entsteht durch schlüssiges Verhalten eine Bindung an diesen (günstigeren) Betrag — RS0014526 (konkludente Bindung durch wiederholte Annahme). **Nicht** damit verbunden wird die gleichzeitige Annahme der Verschlechterungen: Klauseln, die schlechter stellen, können nach § 863 ABGB (RS0042828 — strenge Anforderungen an schlüssige Erklärungen; RS0014154 — Empfängerhorizont) **nicht konkludent** in das Vertragsverhältnis einfließen; bloße Entgegennahme hat keinen Erklärungswert (RS0047273 [T2]). Vorbehaltlose Annahme des höheren Fixums bedeutet also: Fix-Bindung ja, Verschlechterungen nein — aber der Hebel für den Gesamtvorbehalt schwindet.

**Handlung:** Vor nächster Auszahlung schriftlichen Vorbehalt setzen: „Ich nehme die Auszahlung unter ausdrücklichem Vorbehalt aller Rechte entgegen und lehne den 1. Nachtrag in seiner vorliegenden Form ab."

### Zwischenergebnis Regime

| Aspekt | Ergebnis |
|---|---|
| Änderungsweg | Einvernehmliches Angebot, **nicht** Änderungskündigung |
| Status ohne Unterschrift | Bestandsvertrag gilt vollständig |
| Fix-Erhöhung konkludent | Möglich nach erster vorbehaltloser Auszahlung (§ 863 ABGB) |
| Verschlechterungen konkludent | Nein — § 863 ABGB + RS0042828 + RS0014154 |

---

## (3) Klausel-Inhaltskontrolle (`klausel-inhaltskontrolle`)

Die Klauselkontrolle erfolgt nach § 879 Abs 3 ABGB (GNR 10001622; Leitdoktrin RS0016914). Vorformulierte Klauseln sind nichtig, soweit sie den Vertragspartner gröblich benachteiligen.

### §8 Urlaub — 30 Tage → 25 + 5 verfallende Tage (🔴)

Das gesetzliche Urlaubsausmaß (§ 2 Abs 1 URLG) beträgt 30 Werktage (= 25 Arbeitstage / 5 Wochen) bei Dienstzeit unter 25 Jahren und 36 Werktage (= 30 Arbeitstage / 6 Wochen) ab dem vollendeten 25. Dienstjahr; die Unabdingbarkeit folgt aus § 12 URLG, der Verjährungs-/Hinweisschutz aus § 4 Abs 5 URLG (RS0134421). Der Bestandsvertrag gewährt 30 Tage — der übergesetzliche Teil (Tage über dem gesetzlichen Minimum) ist grundsätzlich modifizierbar. Soweit die 5 „verfallenden" Tage zum gesetzlichen Mindestanspruch gehören oder eine Ersatzleistung bei Nichtkonsumation entfällt, ist die Klausel unzulässig: Der Verfall ohne Ersatzleistung tastet den gesetzlichen Mindestanspruch an (RS0134421, OGH 27.06.2023, 8 ObA 23/23z — AG-Aufforderungs- und Hinweispflicht). **Ergebnis:** Klausel im gesetzlichen Teil unwirksam; übergesetzlicher Teil gesondert prüfen (Verschlechterungsschutz nach Regime-Triage).

### §4.2.3 Bonus-Widerruf „jederzeit gänzlich oder teilweise" (🟠)

Widerrufsvorbehalt ohne sachliche Begrenzung ist nach § 879 Abs 3 ABGB-Linie (RS0016914; Grenzfall-Analyse RS0112269, OGH 8 ObA 16/03s) bedenklich, wenn er dem Arbeitgeber unbegrenzte Willkür erlaubt. Bereits verdiente Bonusanteile (Periode abgelaufen, Ziel erreicht) sind unwiderruflich — dieser Teilbereich ist 🔴 (RS0028333, OGH 9 ObA 101/90, 09.05.1990: nach Beginn des Erfolgszeitraums darf der DG die Prämie weder einseitig widerrufen noch an Bedingungen im alleinigen DG-Einflussbereich knüpfen; Norm: ABGB § 879 BIIh, AngG § 16 IV). Für künftige variable Anteile: Klausel wohl § 879 Abs 3-widrig, wenn sie keine sachliche Schranke enthält. [Prüfpunkt: Volltext 8 ObA 16/03s via RIS abrufen — Toleranzschwelle (~10 %) bestätigen.]

### §3 Versetzung auf „geringerwertige Tätigkeiten" (🟠)

Kein Betriebsrat im eigenen Betrieb → § 101 ArbVG-Zustimmungspflicht entfällt. Hinweis: § 101 ArbVG ist der **kollektive** Prong und setzt einen Betriebsrat voraus — die Mandantin/der Mandant erhält keinen § 101-Schutz. Der Verschlechterungsbegriff nach RS0051209 (OGH 4 Ob 79/85; Norm: ArbVG § 101; 17 E) — jede Änderung zum Nachteil des AN (materiell + immateriell; Entgelt im weitesten Sinn; T3: Wegfall Überstundenpauschale; T4: Entgeltverschlechterung) — dient als Referenz für den Schweregrad; das operative Kontrollinstrument ohne Betriebsrat bleibt § 879 Abs 3 ABGB (RS0016914). Als Individualschutz bleibt § 879 Abs 3 ABGB: Eine Klausel, die einseitig Versetzung auf geringerwertige Tätigkeiten nach „billigem Ermessen" erlaubt, ist bei fehlender sachlicher Begrenzung und Entgeltschmälerungsrisiko gröblich benachteiligend. **Ergebnis:** Klausel 🟠 — in dieser Pauschalformulierung wohl unwirksam; Bestandsschutz (gleichwertige Tätigkeit, keine Entgeltschmälerung) bleibt.

### §7 Arbeitszeit — AG ändert Lage „dauerhaft" (🟠 → 🔴)

§ 19c AZG (GNR 10008238) ist für Vollzeitkräfte die zwingende Norm für die Lage der Arbeitszeit (RS0118331, OGH 8 ObA 86/03k). OGH 9 ObA 57/22f folgt RS0118331, sein Beisatz stützt sich jedoch auf § 19d Abs 2 AZG (Teilzeit/Schriftform). Eine Klausel, die dem Arbeitgeber das dauerhafte einseitige Festlegen der Arbeitszeitlage erlaubt, ist nach § 19c AZG insoweit **unwirksam**.

### §4.10 All-in (neu eingefügt) (🟠)

§ 2g AVRAG (GNR 10008872) schreibt Transparenz vor: Die Überstundenkomponente muss vom Grundentgelt trennbar ausgewiesen sein. Der Durchrechnungszeitraum ist das Kalenderjahr — das folgt aus AZG § 19 (RS0131677, OGH 27.09.2017, 9 ObA 28/17h). Fehlt diese Trennbarkeit oder wird eine Pauschalabgeltung ohne Nachweis der tatsächlichen Deckung vereinbart, ist § 2g AVRAG verletzt — Folge: Einzelverrechnung aller tatsächlich geleisteten Überstunden, Sonn-/Feiertags- und Nachtarbeitszuschläge. AG trägt die Deckungsprüfungspflicht (RS0051519 [T4/T6], OGH 4 Ob 66/84; Norm: AZG § 10; 28 E): AG hat grundsätzlich zu überprüfen, ob geleistete Überstunden durch das Pauschale gedeckt waren; fehlende Deckung → AN kann über das Pauschale hinausgehende unabdingbare Ansprüche erheben; AG trägt das Deckungsrisiko. Zu prüfen: Deckt das Pauschalentgelt von € 119.000 (fiktiv/illustrativ) die prognostizierten Überstunden bei Führungsrolle Vertrieb tatsächlich ab?

### §14.5 Haftungsdeckel 3 Monatsgehälter (⚪ — DHG-Boden prüfen)

§§ 2, 5 DHG (GNR 10008209, Artikel 1) bilden den zwingenden Mindestrahmen: Vorsatz und grobe Fahrlässigkeit dürfen nicht vertraglich ausgeschlossen werden; das Mäßigungsrecht des Gerichts (§ 5 DHG) ist unentziehbar. Soweit der 3-Monats-Deckel nur die Haftung der **Mandantin/des Mandanten** begrenzt (zugunsten der Mandantin/des Mandanten), ist er zulässig und neutral. Kritisch wird er, wenn er Vorsatz einschließt oder den DHG-Boden unterschreitet — Volltext prüfen.

---

## (4) Deutsche Vorlage-Audit (`deutsche-vorlage-audit`)

| Klausel-Indiz | Deutsche Wurzel (DE) | Österreichische Folge | Ampel |
|---|---|---|---|
| „Arbeitnehmererfindungsgesetz" / 4-Monats-Fiktion | § 6 ArbnErfG (DE) | §§ 6–9 PatG (GNR 10002181): kein ex-lege-Erwerb; Rechtsübergang erfordert schriftliche Vereinbarung | 🔴 |
| „außerordentliche Kündigung ohne Abmahnung" | § 626 BGB (DE) | § 27 AngG (GNR 10008069, Artikel 1): Entlassung; demonstrativer Tatbestand, restriktiv ausgelegt (RIS: „insbesondere"); keine Abmahnpflicht nach deutschem Muster | 🔴 |
| „in Textform" | § 126b BGB (DE) | In AT nicht kodifiziert; Schriftform = § 886 ABGB (GNR 10001622); Klausel muss klargestellt werden | 🟠 |
| „§ 2 Entgeltfortzahlungsgesetz" | EFZG (DE) | § 8 AngG (GNR 10008069, Artikel 1): § 1 Abs 2 EFZG (DE) nimmt Angestellte aus; für AT gilt § 8 AngG eigenständig | 🔴 |
| Fixer 3-Monats-Haftungsdeckel (BAG-Stil) | BAG-Muster (DE) | §§ 2, 5 DHG (GNR 10008209, Artikel 1): DHG-Boden zwingend; Vorsatz/grobe Fahrlässigkeit nicht ausschließbar | 🔴 |

**Zwischenergebnis:** Der Nachtrag basiert in mehreren Klauseln auf einer deutschen Vertragsvorlage. Die betroffenen Klauseln sind im jeweiligen Umfang unwirksam oder leer. Nach Umstellung auf die AT-Norm schließt die vollständige Inhaltskontrolle nach § 879 Abs 3 ABGB an.

---

## (5) Austritts-Backstop (`austritt-backstop-und-hebel`)

### Aktuelle Lage

- **Unterschrift nicht gesetzt** → Der § 26 Z 2 AngG-Backstop ist **erhalten**. Eine zu aggressive einseitige Durchsetzung der verschlechternden Klauseln (Entgeltkürzung, Herabstufung) würde das Austrittsrecht aktivieren.
- **Vorbehalt noch nicht gesetzt** → Wenn die Mandantin/der Mandant die Fix-Erhöhung ohne schriftlichen Vorbehalt annimmt, entsteht konkludente Bindung an den neuen Fixbetrag (§ 863 ABGB), aber der Austrittsgrund für die Verschlechterungen bleibt — sofern er zeitnah geltend gemacht wird.

### Was eine Unterschrift abbauen würde

Wer die Verschlechterungen (Versetzung auf geringerwertige Tätigkeit, Widerrufsvorbehalt, All-in, Urlaubsverfall) unterzeichnet, stimmt einvernehmlich zu (§ 863 ABGB). Der § 26-Backstop entfällt dann in diesem Umfang — die noch verbleibende Kontrolle läuft über § 879 Abs 3 ABGB (Inhaltskontrolle der Klauseln) und die DE-Vorlage-Audit-Ergebnisse.

### Ansprüche im Austrittsfall (§ 29 AngG)

Bei berechtigtem vorzeitigem Austritt nach § 26 Z 2 AngG (GNR 10008069, Artikel 1; Z 2 = Entgelt-Prong: erhebliche Entgeltschmälerung; bare Herabstufung ohne Entgelteinbuße = allgemeiner wichtiger Grund): **Kündigungsentschädigung** (§ 29 AngG) — nicht als Entgelt, sondern als Schadenersatz zu qualifizieren (RS0028724 [T3], OGH 4 Ob 95/76; Norm: AngG § 29 Abs 1; 15 E) = voller Bezugsersatz für die fiktive Restlaufzeit der Kündigungsfrist; soweit der Zeitraum 3 Monate nicht übersteigt, sofort mit Beendigung des Arbeitsverhältnisses fällig [RS0028724 T2]; darüber hinaus Anrechnung anderweitigen Erwerbs. Abfertigung neu (BMSVG) — Auszahlungsanspruch gegen BV-Kasse bei Erfüllung der 3-Jahres-Schwelle (hier noch nicht erreicht; Anwartschaft läuft weiter).

§ 26 AngG verlangt, dass der vorzeitige Austritt ohne unnötigen Aufschub aus dem aktuellen wichtigen Grund erklärt wird — RS0028687 (OGH 14 Ob 215/86; Norm: AngG § 26 II; 10 E): Unverzüglichkeitsgrundsatz gilt auch für den Austritt; Zuwarten verwirkt das Austrittsrecht [T2]; nach OGH 9 ObA 22/03f [T4]: eine 6-tägige Verzögerung (inkl. Wochenende) ist im Allgemeinen verspätet, wenn zum Zeitpunkt des Austrittsgrundes Austrittsabsicht bestand und keine Erhebungen notwendig waren. Vorbehaltlose Weiterarbeit kann den Austrittsgrund ebenfalls verwirken.

---

## (6) Routing / Nächste Schritte (`anschluss-routing`)

| Handlungsbedarf | Stelle | Begründung |
|---|---|---|
| **Sofort: Vorbehalt setzen** | Schriftlich an Arbeitgeber | Vor nächster Auszahlung; erhält § 26-Backstop und verhindert konkludente Bindung an Verschlechterungen |
| Verbindliche rechtliche Beurteilung, Verhandlungsstrategie | **AK Wien** / Arbeitsrechtsanwalt | Keine verbindliche Subsumtion ohne Anwaltsmandat; Verhandlung mit AG über Klausel-Streichungen |
| Leitende:r Angestellte:r (§ 36 ArbVG) | Anwalt | Prüfen: echte Hire-&-Fire-/Gehaltskompetenz → ArbVG-Schutz reduziert |
| Steuerliche Optimierung | **Steuerberater** | Jahressechstel-Ausschöpfung, steuerliche Behandlung Fix/variabel-Split, Sonderzahlungen (EStG — keine §-Zitation ohne verifizierten RIS-Permalink) |
| Betriebsrat (prospektiv) | § 40 ArbVG (GNR 10008329) | Kein BR im eigenen Betrieb; Gründung ab ≥ 5 wahlberechtigten AN möglich (Initiative der Belegschaft) |

**Keine Kündigung oder Entlassung ausgesprochen** → Plugin `arbeitsrecht-beendigung` noch nicht aktiv; Backstop-Strategie und Klausel-Nachverhandlung sind vorrangig.

---

## Verifizierte Quellen (RIS)

**Normen (alle aus den Skills; Permalinks HTTP 200 geprüft):**

- § 863 ABGB — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001622&Paragraf=863
- § 879 Abs 3 ABGB — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001622&Paragraf=879
- § 886 ABGB — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001622&Paragraf=886
- § 8 AngG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008069&Artikel=1&Paragraf=8
- § 26 AngG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008069&Artikel=1&Paragraf=26
- § 27 AngG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008069&Artikel=1&Paragraf=27
- § 29 AngG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008069&Artikel=1&Paragraf=29
- § 36 ArbVG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008329&Paragraf=36
- § 40 ArbVG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008329&Paragraf=40
- § 19c AZG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008238&Paragraf=19c
- § 2g AVRAG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008872&Paragraf=2g
- § 2 URLG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008376&Paragraf=2
- § 12 URLG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008376&Paragraf=12
- §§ 2, 5 DHG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008209&Artikel=1&Paragraf=2
- §§ 6–9 PatG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002181&Paragraf=6

**Judikatur (Existenz/Permalink über RIS geprüft; Leitsatz vor Verwendung lesen; ObA-Senat):**

- Änderungsregime / Bestandsvertrag — RS0109380 (OGH 12.02.1998, 8 ObA 35/98z)
- Konkludente Bindung durch wiederholte Annahme — RS0014526
- Empfängerhorizont bei schlüssigem Verhalten — RS0014154
- Strenge Anforderungen an schlüssige Erklärungen — RS0042828
- Bloße Entgegennahme = kein Erklärungswert — RS0047273 [T2]
- Verschlechterung wirkt nicht konkludent zurück — § 863 ABGB + RS0042828 + RS0014154 (RS0124521 betrifft Unverbindlichkeitsvorbehalt für Sonderzahlungen, nicht diese Proposition)
- § 879 Abs 3 ABGB Leitdoktrin — RS0016914 (OGH 1 Ob 581/83; bestätigt OGH 1 Ob 105/10p)
- Bonus-Widerrufsvorbehalt / Toleranzschwelle — RS0112269 (OGH 8 ObA 16/03s) [Volltext abrufen]
- All-in / Durchrechnungszeitraum Kalenderjahr (AZG § 19) — RS0131677 (OGH 27.09.2017, 9 ObA 28/17h)
- § 19c AZG zwingend (Vollzeit-Lage) — RS0118331 (OGH 8 ObA 86/03k; 9 ObA 57/22f folgt RS0118331, Beisatz stützt sich auf § 19d Abs 2 AZG/Teilzeit)
- Urlaubsrecht / Verjährung / AG-Hinweispflicht — RS0134421 (OGH 27.06.2023, 8 ObA 23/23z)
- Bereits verdiente Prämie unwiderruflich nach Beginn des Erfolgszeitraums — RS0028333 (OGH 9 ObA 101/90, 09.05.1990; Norm: ABGB § 879 BIIh, AngG § 16 IV)
- Austritt / Unverzüglichkeit / Zuwarten = Verlust / ~6-Tage-Grenze — RS0028687 (OGH 14 Ob 215/86; Norm: AngG § 26 II; 10 E)
- Kündigungsentschädigung als Schadenersatz / erste 3 Monate sofort fällig — RS0028724 (OGH 4 Ob 95/76; Norm: AngG § 29 Abs 1; 15 E)
- All-in / Deckungsprüfungspflicht AG / unabdingbare Mehransprüche AN — RS0051519 (OGH 4 Ob 66/84; Norm: AZG § 10; 28 E)
- Versetzung / Verschlechterungsbegriff § 101 ArbVG (kollektiver Prong; kein Schutz ohne Betriebsrat — dort gilt § 879 Abs 3 ABGB) — RS0051209 (OGH 4 Ob 79/85; Norm: ArbVG § 101; 17 E)

**Deutsche Kontrast-Normen (bewusste Anti-Muster, kein österreichisches Recht; von verify.py übersprungen):**
- § 6 ArbnErfG (DE), § 626 BGB (DE), § 126b BGB (DE), EFZG (DE), BAG-Stil (DE)

Reproduzieren (zur Laufzeit ausführen): `python3 tools/ris_client.py linie "konkludente Vertragsänderung Arbeitsverhältnis" --gericht OGH --gesetz ABGB --paragraf 863`; `python3 tools/ris_client.py linie "gröblich benachteiligend Arbeitsvertrag" --gericht OGH --gesetz ABGB --paragraf 879`; `python3 tools/ris_client.py aktualitaet ABGB 863 --seit 1998-02-12`.

> Hinweis: Diese Triage ist Vorbereitung, nicht Entscheidung. Der Anwalt führt das Mandat.
