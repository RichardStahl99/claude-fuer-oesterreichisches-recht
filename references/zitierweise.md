# Österreichische juristische Zitierweise und Quellenprüfung (v1.0)

> Zentrale Referenz für alle Skills, Agenten und Cookbooks in diesem Repository.
>
> **Leitlinie:** Keine Blindzitate. Das Repository soll anwaltliche Arbeit unterstützen, nicht Fundstellen erfinden. Judikatur darf zitiert werden, wenn sie mit Gericht, Datum, Geschäftszahl und einer prüfbaren Quelle (RIS) abgesichert ist. Literatur wird nur verwendet, wenn sie vom Nutzer bereitgestellt wurde oder über einen lizenzierten Live-Zugriff (rdb.at, LexisNexis, Linde) wirklich vorliegt.
>
> **Achtung — kein deutsches Schema.** In Österreich wird **nicht** nach Zeitschrift-Fundstelle ("NJW 2019, 1234") zitiert, sondern nach **Gericht + Datum + Geschäftszahl** und nach **RIS-Justiz-Rechtssatznummer**. Es gibt kein "Az.", kein "BeckRS". Quellen werden über **RIS** (`ris.bka.gv.at`) verifiziert — siehe `references/ris-quellen.md` und `tools/ris_client.py`.

## 1. Harte Sperren

1. **Keine Geschäftszahl aus dem Modell.** Eine GZ (z. B. `3 Ob 123/19x`) oder eine RS-Nummer (`RS0123456`) darf nur ausgegeben werden, wenn sie live über RIS verifiziert oder vom Nutzer geliefert wurde.
2. **Keine Kommentar-Blindzitate.** Keine Randziffer aus KBB, Rummel, Schwimann/Kodek, ABGB-ON, Koziol/Welser, Kletečka/Schauer usw. erfinden.
3. **Keine Aufsatz-Blindzitate.** Keine ÖJZ-, JBl-, RdW-, ecolex-, immolex-, wbl-, ZIK-, ZVR- oder sonstigen Fundstellen behaupten, wenn der Beitrag nicht vorliegt.
4. **Keine Judikatur ohne Mindestdaten.** Gericht, Datum und Geschäftszahl sind Pflicht. Fehlt eines davon, nicht als gesichertes Zitat ausgeben.
5. **Keine Datenbanknummer (RDB, RIS-Dokumentnummer) als Ersatz für Datum und Geschäftszahl.**
6. **Keine erfundenen Fundstellen in Zeitschriften.** ÖJZ/JBl/RdW usw. nur als Parallelfundstelle, wenn sicher bekannt oder verifiziert.
7. **Kein deutsches Recht.** Keine BGB-/HGB-/ZPO(DE)-Normen, keine BGH/BVerfG-Aktenzeichen, keine deutschen Reporter — auch nicht, wenn eine übernommene Vorlage das vormacht.

## 2. Normen (Gesetzeszitate)

**Schema:** Paragrafzeichen + Stelle + abgekürztes Gesetz. Nie nach Seite.

- `§ 932 ABGB`
- `§ 879 Abs 1 ABGB`
- Untergliederung: **Abs** (Absatz), **Z** (Ziffer), **lit** (litera) — z. B. `§ 28 Abs 1 Z 2 lit a UStG`.
- Mehrere Normen: `§§ 922, 932 ABGB`; `§§ 12 f VGG`.
- Österreichische Schreibweise: **ohne** Punkt nach "Abs"/"Z"/"lit"; Leerzeichen nach `§`.
- Bei EU-Recht: `Art 6 Abs 1 lit f DSGVO`; Verordnungen/Richtlinien mit Nummer/Jahr (`RL 2019/771`).

**Auflösung/Verifikation:** Norm-Permalink über RIS (Bundesrecht konsolidiert). `tools/ris_client.py norm ABGB 932` liefert den Permalink und prüft HTTP 200. Nie eine Gesetzesnummer raten — über RIS auflösen.

## 3. Judikatur: Mindeststandard

**Schema (Einzelentscheidung):**

`<Gericht> <Datum>, <Geschäftszahl>[, <freie/zitierte Fundstelle>]`

Beispiel: `OGH 23.10.2019, 3 Ob 123/19x`.

**Schema (Rechtssatz):**

`RIS-Justiz <RS-Nummer>` — Beispiel: `RIS-Justiz RS0018921`. Optional die führende Entscheidung in Klammern: `RIS-Justiz RS0018921 (OGH 1 Ob 621/55)`.

**Geschäftszahl-Schreibweise:** Senatszahl + Registerzeichen + laufende Zahl/Jahr + Prüfbuchstabe, **mit Spatien**: `3 Ob 123/19x`, `6 Ob 158/22m`, `10 ObS 45/20t`. Das Registerzeichen kennzeichnet die Materie (z. B. **Ob** Zivilsachen, **ObA** Arbeitssachen, **ObS** Sozialrechtssachen, **Os** Strafsachen, **Nc** Zuständigkeit/JN).

**ECLI:** zusätzlich zulässig — `ECLI:AT:OGH0002:2023:RS0134544`.

**Vor Ausgabe prüfen:**

- Gericht und Spruchkörper plausibel (OGH/OLG/LG/BG; VwGH/VfGH)?
- Datum im Format `TT.MM.JJJJ`?
- Geschäftszahl vollständig samt Prüfbuchstabe?
- RIS-Permalink vorhanden und auflösbar?
- Bei Rechtssatz: RS-Nummer aus RIS, nicht geraten?
- Thema passt zur Aussage (Rechtssatz nicht aus dem Zusammenhang gerissen)?

## 4. Gerichte und ihre Bezeichnungen

- **OGH** — Oberster Gerichtshof (Zivil/Straf, letzte Instanz). Entscheidungsform: Urteil oder Beschluss.
- **OLG** — Oberlandesgericht (Wien, Graz, Linz, Innsbruck).
- **LG** — Landesgericht; **BG** — Bezirksgericht.
- **VwGH** — Verwaltungsgerichtshof; **VfGH** — Verfassungsgerichtshof; **BVwG/LVwG** — Bundes-/Landesverwaltungsgericht. Deren Entscheidungen heißen **Erkenntnis** (nicht "Urteil") bzw. Beschluss.
- **EuGH** (curia.europa.eu), **EGMR** (hudoc.echr.coe.int) — bei reiner OGH-Recherche herausfiltern (RIS mischt ausländische Organe teils ein).

## 5. Kostenlose und amtliche Quelle: RIS

Primärquelle ist **RIS — Rechtsinformationssystem des Bundes** (`ris.bka.gv.at`), amtlich und frei. Es deckt Bundes- und Landesrecht sowie die Judikatur (OGH, OLG, VwGH, VfGH, BVwG/LVwG u. a.) ab.

- **Norm:** `https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=<GNR>&Paragraf=<§>`
- **Judikatur:** RIS-Dokument-Permalink (`…/Dokument.wxe?Abfrage=Justiz&Dokumentnummer=…`).
- Maschinell über die **RIS-OGD-API** (`data.bka.gv.at/ris/api/v2.6/`) — siehe `references/ris-quellen.md`.

Paid-only und **nicht** aus Modellwissen zu erzeugen: **RDB** (rdb.at, Manz), **LexisNexis/RIDA**, **Linde Digital**, **Findok** (Finanz, BMF — frei, aber eigene Quelle). Diese sind die österreichischen Pendants zu beck-online/juris.

## 6. Zeitschriften und Literatur — nur mit echter Quelle

Zeitschriften (ÖJZ, JBl, RdW, ecolex, immolex, wbl, ZIK, ZVR, RZ, EvBl, ZfRV …) und Kommentare bleiben in der Praxis wichtig, dürfen hier aber **nicht blind** zitiert werden.

**Zulässig nur, wenn:** der Nutzer Auszug/Scan/Link/Export bereitstellt, ein lizenzierter Live-Zugriff besteht, oder es nur um einen neutralen Recherchehinweis ohne Fundstellenbehauptung geht.

**Unzulässig:** aus dem Modell eine Randziffer zu KBB/Rummel/Schwimann/Koziol zu erzeugen; eine Auflage zu behaupten, ohne sie geprüft zu haben; einen Aufsatz mit Jahrgang/Seite zu zitieren, der nicht vorliegt.

**Zulässiger Recherchehinweis:** `Literatur nur prüfen, wenn Zugriff besteht: ABGB-Kommentar zu § 932 ABGB (Behelfshierarchie); VGG-Kommentierung zu §§ 12 f. Keine Fundstelle ohne Verifikation ausgeben.`

## 7. Reihenfolge mehrerer Judikaturbelege

Zuerst nach Gerichtsebene, dann nach Relevanz oder chronologisch absteigend; gewählte Ordnung konsistent halten.

1. VfGH (verfassungsrechtlich tragend)
2. EuGH / EGMR (unions- oder konventionsrechtlich tragend)
3. OGH; VwGH
4. OLG / Oberlandesgerichte; Landesverwaltungsgerichte
5. LG
6. BG

## 8. Ausgabeformate

**Sicher verifizierte Einzelentscheidung:** `OGH 23.10.2019, 3 Ob 123/19x (RIS).`

**Sicher verifizierter Rechtssatz:** `RIS-Justiz RS0018921 (OGH 1 Ob 621/55).`

**Noch nicht verifiziert:** `[Judikatur prüfen: OGH zu Behelfshierarchie § 932 ABGB; Geschäftszahl über RIS noch zu bestätigen.]`

**Literatur nur als Nutzerquelle:** `[Nutzerquelle: Auszug aus …, vom Nutzer bereitgestellt, dort Rz …]`

## 9. Checkliste vor jeder juristischen Ausgabe

- [ ] Keine Geschäftszahl/RS-Nummer aus Modellwissen?
- [ ] Judikatur mit Gericht, Datum und Geschäftszahl?
- [ ] RIS-Permalink vorhanden oder klarer Prüfvermerk?
- [ ] Bei Rechtssatz: RS-Nummer live aus RIS?
- [ ] Keine Kommentar-/Aufsatzfundstelle ohne Nutzerquelle oder Live-Zugriff?
- [ ] Norm korrekt zitiert (§/Abs/Z/lit, richtiges Gesetz, kein BGB)?
- [ ] Gesetzesstand/Übergangsrecht geprüft (z. B. VGG ab 1.1.2022)?
- [ ] Kein deutsches Recht, kein deutsches Rechtsdeutsch (Jänner, Rekurs, Erkenntnis)?
- [ ] Offene Unsicherheit ausdrücklich markiert?

## 10. Skill-Hardening gegen Scheinpräzision

Jeder Skill, der juristische Aussagen ausgibt, trennt drei Ebenen:

1. **Gesichert:** Normtext, Nutzerdokument, RIS-verifizierte Judikatur oder dokumentierter Live-Zugriff.
2. **Plausibel, aber zu prüfen:** bekannte Linie/Arbeitshypothese ohne gerade geöffneten Volltext.
3. **Nicht verwenden:** Geschäftszahl, RS-Nummer, Kommentar-Randziffer oder Aufsatzfundstelle aus bloßem Modellwissen.

Wenn nicht gerade geprüft, ist die Ausgabe als **Prüfpunkt** zu formulieren. Das ist kein Makel, sondern saubere anwaltliche Arbeitsweise.

## 11. Kurzregel für Skills

`Norm zuerst (ABGB/Sondergesetz, RIS-Permalink). Dann RIS-verifizierte Judikatur (Gericht, Datum, GZ oder RS-Nummer). Literatur nur bei bereitgestellter oder live verifizierter Quelle. Keine GZ-, RS-, Kommentar- oder Aufsatz-Blindzitate. Kein deutsches Recht.`
