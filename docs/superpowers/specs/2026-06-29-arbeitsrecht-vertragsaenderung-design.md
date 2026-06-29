# Design — Vertikale `arbeitsrecht-vertragsaenderung`

**Stand:** 2026-06-29 · **Status:** Spec (zur Freigabe) · **Repo:** claude-fuer-oesterreichisches-recht · **Phase:** 6 (5. Fach-Vertikale)

> Keine Rechtsberatung. Alle Normen/Geschäftszahlen werden zur Implementierungszeit **live über `tools/ris_client.py` (RIS)** verifiziert — keine GZ aus Modellwissen (`references/quellenhygiene.md`).

---

## 1. Kontext & Motivation

Auslöser ist ein realer Fall: ein **1. Nachtrag zu einem Dienstvertrag** (Änderungsangebot per elektronischem Signaturtool, nicht unterschrieben), der eine Beförderung mit gemischten Verbesserungen und durchsetzbaren Verschlechterungen bündelt und erkennbar aus einer **deutschen Vertragsvorlage** stammt.

**Befund zur Ausgangsfrage „Angestelltengesetz hinzufügen?":** Das **AngG ist bereits im Repo** (`ANGG = 10008069`, Artikel-1-Adressierung in `ris_client.py`; in `arbeitsrecht-beendigung` werden §§ 8, 20, 23, 26, 27, 29 AngG gegroundet und zitiert). Es fehlt **kein Gesetz, sondern eine Kompetenz**: die bestehende Arbeitsrecht-Vertikale behandelt ausschließlich die **Beendigung**. Der Fall betrifft das **laufende** Verhältnis, dessen Bedingungen sich ändern — ein eigener doktrineller Werkzeugkasten (Änderungsregime, § 879 Abs 3 ABGB-Inhaltskontrolle, konkludente Bindung, DE→AT-Falsche-Freunde).

Der Fall ist als Vorlage ungewöhnlich gut: er ist die **reinste Demonstration der Kern-These des Repos** — „deutsche Vorlage → österreichrechtskonforme Fassung" — und übt Kompetenzen, für die es noch keinen Skill-Pfad gibt.

## 2. Umfang & Abgrenzung

**In Scope:** Änderung von Vertragsbedingungen im **aufrechten** Dienstverhältnis (Nachtrag/Änderungsangebot) — Regime-Triage, Klausel-Inhaltskontrolle, konkludente Bindung, Austritts-Backstop, DE→AT-Audit.

**Naht zur Schwester-Vertikale:** `arbeitsrecht-beendigung` = *das Verhältnis endet*; `arbeitsrecht-vertragsaenderung` = *es läuft weiter, die Bedingungen verschieben sich*. Beide Router verlinken wechselseitig.

**Out of Scope (YAGNI — nur weiterleiten):** reine Beendigung, Sozialversicherung, Steueroptimierung im Detail (→ Steuerberater), Mechanik der Betriebsrat-Gründung (nur als prospektiver Hinweis).

## 3. Skill-Spine (6 Skills — bewährtes Muster `einstieg → … → routing`)

Jeder Skill folgt dem Repo-Aufbau: Frontmatter (`name`, `description`, Schluss „Kein deutsches Recht."), `## Fachlicher Anker` (Normen + GNR + Quellenhygiene + Konvention), `## Einsatzlage`, `## Sofort-Triage` (Tabelle), `## Risiko-Ampel`, `## Anschluss-Skill-Router`. Laufzeit-Grounding via `linie`/`leit`/`aktualitaet` (Protokoll in `references/ris-quellen.md` §3).

1. **`einstieg-vertragsaenderung`** — Anwalts-Dashboard. Die Tabelle `Bestand → Angebot → Bewertung` (✅ besser / 🔴 schlechter & durchsetzbar / 🟠 schlechter, aber durch zwingendes Recht blockiert / ⚪ neutral) **ist** das Dashboard. Risiko-Ampel (Frist/Beweis/wirtschaftlich). Status-Check **leitende:r Angestellte:r (§ 36 Abs 2 Z 3 ArbVG)** — echte Hire-&-Fire-/Gehaltskompetenz, nicht Titel/Gehalt allein (vgl. 9 ObA 193/01z). Router.

2. **`aenderungsregime`** *(Headline-Gate)* — drei Wege auseinanderhalten:
   - *einvernehmliche Vertragsänderung* (Zustimmung nötig);
   - *Änderungskündigung* (echte Kündigung + Fortsetzungsangebot; Schutz § 20 AngG, § 105/§ 107 ArbVG; darf § 101 ArbVG nicht umgehen — 8 ObA 63/15w; Zumutbarkeit 9 ObA 59/23a);
   - *konkludente Änderung* (§ 863 ABGB): vorbehaltlose, wiederholte Erhöhung bindet (RS0014526; Empfängerhorizont RS0014154); „Schweigen ist keine Annahme" (RS0047273); Verschlechterung wirkt nicht zurück (9 ObA 113/08w); Unklarheit zulasten des Verwenders (§ 915 ABGB).
   - Kern-Take: **Unterschreibst du nicht, läuft der Bestandsvertrag unverändert weiter** (8 ObA 35/98z).

3. **`klausel-inhaltskontrolle`** — § 879 Abs 3 ABGB gröbliche Benachteiligung, klauselweise:
   - Bonus-/Variablen-Widerruf „jederzeit" (verdiente Variable unwiderruflich — 8 ObA 33/21t; Toleranz ~10 % — 8 ObA 16/03s; Inhaltskontrolle auch bei Entgeltklauseln — 1 Ob 105/10p);
   - Versetzung auf „geringerwertige Tätigkeit" (ohne BR kein § 101-Schirm → Individualschutz, Entgeltschutz);
   - All-in (Kalenderjahr-Beobachtung zulässig — 9 ObA 28/17h; kein Verzicht auf übersteigendes Überstundenentgelt; § 2g AVRAG-Transparenz, Basis-Risiko — 8 ObA 22/22a, 9 ObA 62/25w);
   - Arbeitszeit-Lage (§ 19c AZG, nicht abdingbar — 9 ObA 57/22f; ARG-Rahmen für Sonn/Feiertag);
   - Urlaub (§ 12 UrlG schützt nur gesetzlichen Teil; übergesetzliche 6. Woche umgestaltbar — 8 ObA 23/23z, 9 ObA 135/14i);
   - Haftungsdeckel (§§ 2/5 DHG; Deckel ok, DHG-Boden nicht unterschreitbar).

4. **`deutsche-vorlage-audit`** — die Kern-These als eigenständiger, wiederverwendbarer Falsche-Freunde-Scanner:
   - „Arbeitnehmererfindungsgesetz" / 4-Monats-Fiktion (dt. § 6 ArbnErfG) → **§§ 6–9 PatG** (Erwerb nur per schriftlicher Vereinbarung);
   - „außerordentliche Kündigung ohne Abmahnung" (dt. § 626 BGB) → **Entlassung, § 27 AngG**;
   - „in Textform" (dt. § 126b BGB) → im österr. Recht nicht kodifiziert;
   - „§ 2 Entgeltfortzahlungsgesetz" → für Angestellte **§ 8 AngG** (§ 1 Abs 2 EFZG nimmt Angestellte aus);
   - fixer „3-Bruttomonats"-Haftungsdeckel (dt./BAG-Stil) → **DHG §§ 2, 5**.
   - Ausgabe: Liste „Klausel → dt. Wurzel → österr. korrekte Norm → Folge".

5. **`austritt-backstop-und-hebel`** — strategischer Hebel: zu aggressive Herabstufung/Entgeltkürzung begründet **berechtigten vorzeitigen Austritt (§ 26 Z 2 AngG)** + **Kündigungsentschädigung (§ 29 AngG)**; bei Ausübung **sofort schriftlich „unter Protest"** (vgl. 9 ObA 164/07v). Kern-Warnung: **Unterschrift der belastenden Klauseln baut diesen Backstop ab.**

6. **`anschluss-routing`** — Querverweise: `arbeitsrecht-beendigung` (wenn doch Kündigung/Entlassung), AK Wien / Arbeitsrechtsanwalt (verbindliche Beurteilung), Betriebsrat (§ 40 ArbVG, nur prospektiv), Steuerberater (Jahressechstel/§ 67 EStG).

## 4. Test-Akte (anonymisiert) — `testakten/dienstvertrag-nachtrag-aenderungsangebot/`

Layout wie bestehende Akten: **`sachverhalt.md`** (anonymisierte Lage + Klausel-Tabelle) + **`loesung.md`** (Musterlösung nach Methodik, mit RIS-verifizierten Zitaten).

**Anonymisierung — harte Vorgabe (Repo ist öffentlich):**
- Arbeitgeber `NTT DATA Business Solutions AG` → fiktiv **`MUSTER IT Consulting AG, Niederlassung Wien`**; Schwestergesellschaft → „Schwestergesellschaft (eigene Rechtsperson)".
- `Richard Stahl, 1050 Wien` → „Mandant:in (Angestellte:r), Wien"; Vorgesetzter „Lars" → „die direkte Führungskraft"; Adresse entfällt; „DocuSign" → „elektronisches Signaturtool".
- **Rollentitel/Funktionen** (`Director` / `Senior Director`, `Head of GBMS Presales` → `Business Development`) → generische Beschreibung („Fachexperten-Rolle → Führungsrolle, Vertrieb"); konkrete Bereichs-/Produktnamen entfallen.
- **KV-Einstufung**: konkrete Tätigkeitsfamilie/Erfahrungsstufe (z.B. „LT") → „einschlägige Verwendungsgruppe/Stufe des IT-KV" (kein realer Personenbezug).
- **Die echten PDFs gelangen nie ins Repo** — sie bleiben in `/misc/job`. Die Test-Akte enthält einen abstrahierten Sachverhalt, nicht den Quellvertrag.

**Figuren — gefuzzt (Entscheidung 2026-06-29), als fiktiv/illustrativ gekennzeichnet:**
- Bestand: Zielgehalt **€165.000** (Fix €115.000 / variabel €50.000).
- Angebot: Zielgehalt **€185.000** (Fix €120.000 / variabel €65.000) → nur **+€5.000 Fix gesichert**, +€15.000 variabel; variabler Anteil ~35 %.
- Urlaub: **30 → 25 + 5 verfallende** Tage, keine Ersatzleistung.
- KV: IT-KV (UBIT), **illustrativer** KV-Mindestsatz (kein realer Personenbezug).
- Die doktrinellen Verhältnisse (variable-lastige Aufteilung, ~⅓-Bonus-Widerruf, Fix/variabel-Asymmetrie der Erhöhung) bleiben erhalten — sie tragen die § 879/3- und All-in-Analyse.

**Implementierungsnotiz:** Die gebaute Test-Akte verwendet Fix €119.000 / variabel €66.000 (= €185.000 Zielgehalt), +€4.000 Fix gesichert — abweichend von der Spec-Angabe €120.000, weil €120.000 mit der Anonymisierungs-Grep-Gate-Verbotsliste kollidiert hat.

## 5. Grounding & neue Gesetzesnummern

**Bereits registriert:** ABGB, AngG, ArbVG, UrlG. **Neu im LAW-Dict von `ris_client.py`** (der Erweiterungspunkt — Grundlagen bleiben eingefroren), jede GNR live auf HTTP 200 verifiziert:
- **AZG** (Arbeitszeitgesetz) — § 19c.
- **AVRAG** (Arbeitsvertragsrechts-Anpassungsgesetz) — § 2g, § 2 Abs 2 Z 9.
- **DHG** (Dienstnehmerhaftpflichtgesetz) — §§ 2, 5.
- **PatG** (Patentgesetz) — §§ 6–9.
- **EStG** und **EFZG** nur aufnehmen, falls deren § -Zitate im Skill-Text stehen bleiben (sonst weglassen, um `verify.py` schlank zu halten).

**Wrinkle — Kollektivvertrag ist kein Bundesgesetz:** der **IT-KV (UBIT/GPA)** ist über die föderale OGD-Gesetzes-API **nicht** wie ein Bundesgesetz adressierbar. Behandlung wie die Nicht-RIS-Quellen des deutschen Repos: als externe Autorität zitiert (WKO/KV-Text), in `quellenhygiene` gekennzeichnet und **von der § -Permalink-Prüfung in `verify.py` ausgenommen** (so wie bereits `(DE)`-Kontrastzitate übersprungen werden). Dokumentierte Grenze, nicht stillschweigend ignoriert. **Zukünftiger Erweiterungspunkt (nicht diese Phase):** RIS hat eine eigene Kollektivvertrags-Anwendung — ein KV-Resolver in `ris_client.py` wäre später möglich.

## 6. Invarianten & Qualitäts-Gates (Repo-Disziplin)

- `references/zitierweise.md` + `references/methodik-buergerliches-recht.md` **UNVERÄNDERT** (sha256-gepinnt in `verify.py`; pro Phase per `git diff` belegt).
- Alle 6 Skills RIS-gegroundet zur Laufzeit (`linie`/`leit`/`aktualitaet`).
- Eine **adversariale Rechts-Review** auf Skills + Test-Akte vor Commit (wie jede Phase).
- `verify.py` bleibt grün: neue GNR registriert + auf 200 geprüft; KV-Zitate ausgenommen; alle § -Zitate auflösbar.
- Eintrag in `.claude-plugin/marketplace.json` (5. Plugin).

## 7. Plugin-Packaging

`arbeitsrecht-vertragsaenderung/` mit:
- `.claude-plugin/plugin.json` (name, version 0.1.0, description, license `Apache-2.0 OR MIT`, author RichardStahl99, homepage, keywords: vertragsaenderung, aenderungskuendigung, konkludent, §879, inhaltskontrolle, all-in, angg, arbvg, avrag, dhg, oesterreich);
- `arbeitsrecht-vertragsaenderung-schnellstart.md`, `arbeitsrecht-vertragsaenderung-werkstatt.md`, `README.md`;
- `skills/<6 skills>/SKILL.md`.

## 8. Build-Sequenz (Grobplan — Detailplan via writing-plans)

1. `ris_client.py`: AZG/AVRAG/DHG/PatG (+ ggf. EStG/EFZG) registrieren, GNR live verifizieren (`smoke`).
2. Plugin-Gerüst + `plugin.json` + marketplace-Eintrag.
3. 6 Skills schreiben (einstieg → aenderungsregime → klausel-inhaltskontrolle → deutsche-vorlage-audit → austritt-backstop-und-hebel → anschluss-routing).
4. schnellstart + werkstatt + README.
5. Anonymisierte Test-Akte (sachverhalt + loesung).
6. Adversariale Rechts-Review → Fixes einpflegen.
7. `verify.py` grün; `git diff` belegt: Grundlagen unverändert. Commit.

## 9. Offene Punkte → als Laufzeit-Triagefragen in `einstieg-vertragsaenderung`

(Aus dem Fall; nicht offen für die Spec, sondern Prüfpunkte, die der Skill stellt:)
- Wurde die Erhöhung mit **irgendeinem Vorbehalt** kommuniziert/abgerechnet? (entscheidend für konkludente Bindung)
- Wurde die **variable** Erhöhung bereits zugesagt/abgerechnet?
- **Leitende:r Angestellte:r** i.S.d. § 36 ArbVG (echte Hire-&-Fire-/Gehaltskompetenz)?
- Verlangt KV/Vertrag **Schriftform** für Änderungen/Kündigung?
