# Arbeitsrecht (Vertragsänderung) — Werkstatt

> Ausführliche Fassung für die Arbeit im Plugin. Ergänzt die Skills unter `skills/` und die geteilten `references/`. Österreichisches Recht; jede Fundstelle und jeden KV-/Betragswert über RIS (`tools/ris_client.py`) verifizieren.

## Zweck und Abgrenzung

Fünfte **Pilot-Vertikale**: **Vertragsänderungen im aufrechten Arbeitsverhältnis**. Gewählt, weil hier die **Divergenz zu Deutschland am stärksten verdeckt** ist: Auf den ersten Blick klingen Änderungsangebote österreichisch, enthalten aber häufig BGB-Klauseln (ArbnErfG-Fiktion, § 626 BGB (DE)-Entlassungsmuster, § 126b BGB (DE)-Textform, EFZG (DE)-Verweise) und fehlerhafte Entgeltkonstruktionen. Headline-Kompetenz ist die **Einordnung des Änderungswegs** — der Gate-Skill `aenderungsregime`.

**Nicht abgedeckt** (nur verweisen): Beendigung des Arbeitsverhältnisses (→ Plugin `arbeitsrecht-beendigung`), Sozialversicherung, Betriebsübergang (AVRAG Betriebsübergangsrecht), Gleichbehandlung (GlBG), besonderer Kündigungsschutz im Detail (MSchG/VKG/BEinstG).

## Pipeline der Skills

```
einstieg-vertragsaenderung         (Dashboard: Rolle, Änderungsweg, Klausel-Bewertung, Fristen, Hebel)
        |
        v
aenderungsregime                   (Gate: einvernehmlich / Änderungskündigung / konkludent § 863 ABGB)
        |
        |-- Klauseln prüfen -----> klausel-inhaltskontrolle (§ 879 Abs 3 ABGB; § 19c AZG; § 2g AVRAG; § 12 URLG; § 2 DHG)
        |-- DE-Vorlage erkannt --> deutsche-vorlage-audit   (ArbnErfG→§ 6 PatG; § 626 BGB (DE)→§ 27 AngG; EFZG (DE)→§ 8 AngG)
        |-- Austritt erwogen ----> austritt-backstop-und-hebel (§ 26 Z 2 AngG; § 29 AngG)
        v
anschluss-routing                  (Router: Plugin arbeitsrecht-beendigung / AK / Betriebsrat § 40 ArbVG / Steuerberater)
```

## Musterdurchlauf: Dienstvertrag-Nachtrag (Regressionsfall)

Sachverhalt und vollständige Lösung: `testakten/dienstvertrag-nachtrag-aenderungsangebot/` (sachverhalt.md + loesung.md). Alle Zahlen fiktiv/illustrativ. Keine Rechtsberatung.

**Ausgangslage:** Angestellte:r bei der **MUSTER IT Consulting AG, Wien** (fiktiv); Dienstverhältnis ca. 1 Jahr; **kein Betriebsrat** im eigenen Betrieb (Schwestergesellschaft hat BR — eigene Rechtsperson, kein Übergriff); Abfertigung neu (BMSVG). Bestand-Zielgehalt (fiktiv): **€ 165.000** (Fix **€ 115.000** / variabel **€ 50.000**). Der Arbeitgeber legt einen **1. Nachtrag** vor — über elektronisches Signaturtool, rückwirkend datiert, **nicht unterschrieben** — mit angebotenem Zielgehalt **€ 185.000** (Fix **€ 119.000** / variabel **€ 66.000**); variabler Anteil ~35 % des Zielgehalts; gesicherter Fixanstieg nur **+€ 4.000**.

---

### (1) Einstieg-Dashboard (`einstieg-vertragsaenderung`)

| Punkt | Befund | Quelle |
|---|---|---|
| Rolle | Angestellte:r (aufrechtes DV, ca. 1 Jahr); AN-Seite | Dienstvertrag |
| Betriebsrat | **kein eigener BR** (Schwestergesellschaft — eigene Rechtsperson) | Sachverhalt |
| **Änderungsweg** | Einvernehmliches Angebot via elektronisches Signaturtool; **nicht unterschrieben** → kein Konsens; Bestandsvertrag gilt | `aenderungsregime` |
| DE-Vorlage erkennbar? | **Ja** — ArbnErfG-Fiktion, Textform, EFZG-Verweis, außerordentliche Kündigung ohne Abmahnung, BAG-Haftungsdeckel | `deutsche-vorlage-audit` |
| Hebel / Austritt | Unterschrift nicht gesetzt → § 26 Z 2 AngG-Backstop **erhalten**; Fix-Erhöhung möglicherweise konkludent bindend ab erster Auszahlung (§ 863 ABGB) | `austritt-backstop-und-hebel` |
| Leitende:r Angestellte:r? | Führungsrolle Vertrieb — prüfen: echte Hire-&-Fire-/Gehaltskompetenz (§ 36 ArbVG); bloßer Titel genügt nicht | Dienstvertrag, Vollmacht |

**Risiko-Ampel:**

- 🔴 **Konkludente Bindung an Fix-Erhöhung** — vorbehaltlose Annahme der nächsten Gehaltszahlung bindet schlüssig an € 119.000 Fix (fiktiv; § 863 ABGB, RS0014526). Vorbehalt **vor** nächster Auszahlung sichern.
- 🔴 **DE-Vorlage** — mehrere Klauseln beruhen auf deutschem Recht ohne österreichische Entsprechung; in diesen Teilen unwirksam oder leer.
- 🟠 **Variabler Anteil ~35 %** — Widerrufsvorbehalt „jederzeit gänzlich oder teilweise" bedroht den wirtschaftlichen Kern des Angebots; § 879 Abs 3 ABGB-Kontrolle erforderlich.

---

### (2) Änderungsregime (`aenderungsregime`)

Der Nachtrag ist ein einvernehmliches Änderungsangebot — keine Änderungskündigung. Ohne Unterschrift besteht kein Konsens; § 863 ABGB setzt schlüssiges Verhalten beider Seiten voraus.

**Kernsatz (RS0109380, OGH 12.02.1998, 8 ObA 35/98z):** „Die einzige Möglichkeit, die Verschlechterung der Entgeltbedingungen rechtlich zulässig vorzunehmen, ist neben einer einvernehmlichen Vertragsänderung die Änderungskündigung." Da weder Konsens noch Änderungskündigung vorliegt, läuft der **Bestandsvertrag weiter**.

**Konkludenz-Risiko Fix-Erhöhung:** Vorbehaltlose Annahme der ersten Gehaltszahlung auf € 119.000 Fix (fiktiv) → schlüssige Bindung an diesen Betrag (RS0014526). Die gleichzeitigen Verschlechterungen fließen dadurch **nicht** konkludent ein — Klauseln, die schlechter stellen, können nicht schlüssig akzeptiert werden (§ 863 ABGB + RS0042828 + RS0014154). **Handlung:** Schriftlichen Vorbehalt vor nächster Auszahlung setzen.

| Aspekt | Ergebnis |
|---|---|
| Änderungsweg | Einvernehmliches Angebot, **nicht** Änderungskündigung |
| Status ohne Unterschrift | Bestandsvertrag gilt vollständig |
| Fix-Erhöhung konkludent | Möglich nach erster vorbehaltloser Auszahlung (§ 863 ABGB) |
| Verschlechterungen konkludent | Nein — § 863 ABGB + RS0042828 |

---

### (3) Klausel-Inhaltskontrolle (`klausel-inhaltskontrolle`)

Prüfmaßstab: § 879 Abs 3 ABGB, Leitdoktrin RS0016914.

| Klausel (§ Nachtrag) | Bestand | Angebot | Ampel | Grundlage |
|---|---|---|---|---|
| §3 Versetzung | gleichwertige Tätigkeit, keine Entgeltschmälerung | AG kann auf geringerwertige Tätigkeiten nach billigem Ermessen versetzen | 🟠 | § 879 Abs 3 ABGB |
| §4.2.3 Bonus-Widerruf | Widerruf nur in definierten Fällen | „jederzeit gänzlich oder teilweise" | 🟠→🔴 (bereits verdient: 🔴) | § 879 Abs 3 ABGB, RS0016914, RS0112269 |
| §4.10 All-in (neu) | definierte Überstundenpauschale | Überstunden, Sonn-/Feiertag, Nachtarbeit, Reisezeit pauschal; Jahresanrechnung | 🟠 | § 2g AVRAG, RS0131677 |
| §7 Arbeitszeitlage | 38,5 h/Woche | AG ändert Lage „dauerhaft" nach eigenem Ermessen | 🔴 | § 19c AZG, RS0118331 |
| §8 Urlaub | 30 Tage unbedingt | 25 gesetzlich + 5 verfallende Tage ohne Ersatzleistung | 🔴 | § 12 URLG, RS0134421 |
| §14.5 Haftungsdeckel | — | 3 Monatsgehälter fix | ⚪ (DHG-Boden prüfen) | § 2 DHG, § 5 DHG |

---

### (4) Deutsche Vorlage-Audit (`deutsche-vorlage-audit`)

| Klausel-Indiz | Deutsche Wurzel | Österreichische Folge | Ampel |
|---|---|---|---|
| „Arbeitnehmererfindungsgesetz" / 4-Monats-Fiktion | § 6 ArbnErfG (DE) | § 6 PatG — kein Erwerb ex lege; Schriftlichkeit zwingend | 🔴 |
| „außerordentliche Kündigung ohne Abmahnung" | § 626 BGB (DE) | § 27 AngG — Entlassung; abschließender Tatbestandskatalog | 🔴 |
| „in Textform" | § 126b BGB (DE) | in AT nicht kodifiziert; Schriftform = § 886 ABGB | 🟠 |
| „§ 2 Entgeltfortzahlungsgesetz" / EFZG-Verweis | EFZG (DE) | § 8 AngG — das **österreichische** EFZG (BGBl 399/1974) nimmt die Angestellten gemäß § 1 Abs 2 EFZG vom Geltungsbereich aus (es gilt für Arbeiter); für Angestellte gilt § 8 AngG | 🔴 |
| fixer 3-Monats-Haftungsdeckel (BAG-Stil) | BAG-Muster (DE) | § 2 DHG, § 5 DHG — DHG-Boden zwingend | 🔴 |

**Zwischenergebnis:** Der Nachtrag basiert in mehreren Klauseln auf einer deutschen Vertragsvorlage. Die betroffenen Klauseln sind im jeweiligen Umfang unwirksam oder leer. Nach Umstellung auf die AT-Norm schließt die Inhaltskontrolle nach § 879 Abs 3 ABGB an.

---

### (5) Austritts-Backstop (`austritt-backstop-und-hebel`)

Nachtrag **nicht unterschrieben** → § 26 Z 2 AngG-Backstop erhalten. Eine zu aggressive einseitige Durchsetzung der verschlechternden Klauseln (Entgeltkürzung, Herabstufung) würde das Austrittsrecht aktivieren.

- **Wer unterschreibt**, stimmt den Verschlechterungen (Versetzungsklausel, Widerrufsvorbehalt, All-in, Urlaubsverfall) einvernehmlich zu (§ 863 ABGB); der § 26-Backstop entfällt in diesem Umfang — verbleibt nur die Inhaltskontrolle nach § 879 Abs 3 ABGB.
- **Ansprüche im Austrittsfall (§ 29 AngG):** voller Bezugsersatz für die fiktive Restlaufzeit der Kündigungsfrist; erste 3 Monate ohne Anrechnung anderweitiger Erwerbe. Abfertigung neu (BMSVG) — Anwartschaft läuft weiter (3-Jahres-Schwelle hier noch nicht erreicht).

---

### (6) Routing / Nächste Schritte (`anschluss-routing`)

| Handlungsbedarf | Stelle | Begründung |
|---|---|---|
| **Sofort: Vorbehalt setzen** | schriftlich an Arbeitgeber | vor nächster Auszahlung; erhält § 26-Backstop und verhindert konkludente Bindung an Verschlechterungen |
| Verbindliche Beurteilung, Verhandlungsstrategie | AK Wien / Arbeitsrechtsanwalt | kein Ergebnis ohne Anwaltsmandat; Klausel-Streichungen verhandeln |
| Leitende:r Angestellte:r (§ 36 ArbVG) | Anwalt | prüfen: echte Hire-&-Fire-/Gehaltskompetenz → ArbVG-Schutz reduziert |
| Steuerliche Optimierung | Steuerberater | Jahressechstel-Ausschöpfung, Fix/variabel-Split (EStG — keine §-Zitation ohne verifizierten RIS-Permalink) |
| Betriebsrat (prospektiv) | § 40 ArbVG | Gründung ab ≥ 5 wahlberechtigten AN möglich (Initiative der Belegschaft) |

**Keine Kündigung oder Entlassung ausgesprochen** → Plugin `arbeitsrecht-beendigung` noch nicht aktiv; Backstop-Strategie und Klausel-Nachverhandlung sind vorrangig.

---

## Fünf Merkpunkte (häufige Fehlerorte)

1. **Kein Konsens ohne Unterschrift — aber Vorbehalt sofort.** Schweigen auf ein Änderungsangebot ist keine Annahme (RS0047273); trotzdem wirkt die vorbehaltlose Auszahlung des neuen Fixums konkludent bindend (§ 863 ABGB, RS0014526). Vorbehalt **vor** der ersten Auszahlung, nicht danach.
2. **Verschlechterungen kommen nicht konkludent rein.** Wer das höhere Fixum ohne Vorbehalt annimmt, bindet sich daran; die gleichzeitigen Verschlechterungen (Widerrufsvorbehalt, All-in, Urlaubsverfall) gelten dabei **nicht** automatisch (§ 863 ABGB + RS0042828 + RS0014154).
3. **DE-Vorlage ist kein Formfehler — sie ist inhaltlich leer oder unwirksam.** ArbnErfG-Klausel, EFZG-Verweis, § 626 BGB (DE)-Muster — diese Klauseln sind in Österreich entweder ohne Wirkung oder nach § 879 Abs 3 ABGB nichtig. Nach Umstellung auf die AT-Norm schließt die Inhaltskontrolle an.
4. **Variabler Anteil ~35 % mit unbegrenztem Widerrufsrecht ist der wirtschaftliche Kern.** Nominelles Angebot € 185.000 (fiktiv), gesichertes Fixum nur € 119.000 (fiktiv); der Rest hängt an einem Widerrufsvorbehalt, der möglicherweise § 879 Abs 3 ABGB-widrig ist.
5. **§ 19c AZG und § 12 URLG sind zwingend.** Einseitiger Arbeitszeitlagen-Vorbehalt ist unwirksam; Urlaubsverfall ohne Ersatzleistung tastet den gesetzlichen Mindestanspruch an, wenn die AG-Hinweispflicht fehlt (RS0134421, OGH 27.06.2023, 8 ObA 23/23z).

## Quellenanbindung (verpflichtend)

- Normen über RIS-Permalink: `python3 tools/ris_client.py norm ABGB 863` (schlüssiges Verhalten), `norm ABGB 879` (Inhaltskontrolle), `norm ANGG 26` (Austrittsrecht), `norm ANGG 29` (Kündigungsentschädigung), `norm AZG 19c`, `norm AVRAG 2g`, `norm URLG 12`, `norm DHG 2`.
- Judikatur live: `python3 tools/ris_client.py judikatur "Änderungsregime Bestandsvertrag" --gericht OGH` (Arbeitsrecht = **ObA-Senat, 8./9. Senat**).
- **KV-Inhalte, Beträge, Verfallsfristen (IT-KV / UBIT)** stets live beziehen — nie aus Modellwissen. Der IT-KV ist ein Kollektivvertrag, kein RIS-permalink-fähiges Bundesgesetz (→ KV-Limitation, README).
- Keine GZ/RS-Nummer aus Modellwissen (`references/ris-quellen.md`).

## Architektur (Phase-3-Muster)

Nutzt `references/zitierweise.md` und `references/methodik-buergerliches-recht.md` **unverändert**; `tools/ris_client.py` erhielt die verifizierten Gesetzesnummern ABGB (10001622), ANGG (10008069, Artikel-1-Adressierung), ARBVG (10008329), AVRAG (10008872), AZG (10008238), DHG (10008209, Artikel-1-Adressierung), URLG (10008376), PATG (10002181).

## Verifikation

Regressionsfall `testakten/dienstvertrag-nachtrag-aenderungsangebot/`: muss Änderungsweg-/Klausel-Zuordnung korrekt treffen, DE-Vorlage-Signale erkennen und ausschließlich RIS-auflösbare Fundstellen liefern — mit Ausnahme des IT-KV (externe Autorität; kein RIS-Permalink; aus `verify.py`-Check ausgenommen). Vollständiger Lösungspfad in `loesung.md`.

## Berufsrechtlicher Rahmen

§ 9 RAO (Verschwiegenheit), DSGVO/DSG. In Arbeits- und Sozialrechtssachen erster Instanz besteht **keine** absolute Anwaltspflicht (qualifizierte Vertretung, z. B. durch AK/Gewerkschaft, möglich). Output ist anwaltliche Vorbereitung, nie Entscheidung.
