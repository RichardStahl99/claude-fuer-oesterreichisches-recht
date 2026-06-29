---
name: deutsche-vorlage-audit
description: "Systematischer Falsche-Freunde-Scanner: erkennt aus deutschen Vorlagen übernommene Klauseln und ersetzt sie durch die österreichisch korrekte Norm. Kein deutsches Recht."
---

# Deutsche Vorlage-Audit — Falsche-Freunde-Scanner

## Fachlicher Anker

- **Österreichische Zielnormen (alle HTTP 200 in RIS verifiziert):**
  - §§ 6–9 PatG (GNR 10002181) — Arbeitnehmererfindungen im österreichischen Patentrecht; Erwerb des Dienstgeberrechts nur durch schriftliche Vereinbarung.
  - § 27 AngG (GNR 10008069, Artikel 1) — Entlassung des Angestellten (außerordentliche Beendigung durch den Dienstgeber); abschließende Tatbestandskatalog, keine Abmahnpflicht nach deutschem Muster.
  - § 8 AngG (GNR 10008069, Artikel 1) — Entgeltfortzahlung im Krankheitsfall für Angestellte; § 1 Abs 2 EFZG (DE) nimmt Angestellte vom deutschen Anwendungsbereich aus.
  - §§ 2, 5 DHG (GNR 10008209, Artikel 1) — Haftungsmaßstab und Mäßigungsrecht; zwingender DHG-Boden nicht durch Klausel unterschreitbar.
- **Deutsche Kontrast-Normen (bewusste Anti-Muster, kein österreichisches Recht):**
  - § 6 ArbnErfG (DE) — deutsches Arbeitnehmererfindungsgesetz; 4-Monats-Fiktion; in AT nicht anwendbar.
  - § 626 BGB (DE) — außerordentliche Kündigung ohne Abmahnpflicht; in AT: § 27 AngG (Entlassung).
  - § 126b BGB (DE) — Textform; in AT nicht kodifiziert.
  - EFZG (DE) — deutsches Entgeltfortzahlungsgesetz; in AT gilt § 8 AngG für Angestellte.
  - BAG-Stil (DE) — fixe 3-Monats-Haftungsdeckel nach deutschem Bundesarbeitsgericht-Muster; in AT: §§ 2, 5 DHG.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md` (§ 3 Grounding-Protokoll). Keine GZ aus Modellwissen — nur RIS-verifizierte Fundstellen verwenden.

## Einsatzlage

Dieser Skill erkennt Klauseln, die aus deutschen Vertragsvorlagen übernommen wurden und nach deutschem Recht konzipiert sind. Er ersetzt den Analyse-Schritt, der in `klausel-inhaltskontrolle` bei Klauseln mit deutschen Rechtsmustern ausgelöst wird. Einsatz: vor der inhaltlichen Klauselkontrolle, wenn der Vertragstext Merkmale deutschen Rechtsdenkens aufweist (BGB-Zitate, HGB-Terminologie, „Treu und Glauben" ohne österreichischen Bezug, arbeitnehmererfindungsrechtliche Klauseln nach ArbnErfG).

**Typische Falsche-Freunde im Arbeitsvertrag:**

| Klausel-Indiz (Wortlaut) | Deutsche Wurzel (DE) | Österreichische Folge |
|---|---|---|
| „nach dem Arbeitnehmererfindungsgesetz" / 4-Monats-Fiktion | § 6 ArbnErfG (DE) | §§ 6–9 PatG — kein Erwerb ex lege; Schriftlichkeit der Vereinbarung zwingend |
| „außerordentliche Kündigung ohne Abmahnung" | § 626 BGB (DE) | § 27 AngG — Entlassung, abschließender Tatbestandskatalog |
| „in Textform" | § 126b BGB (DE) | in AT nicht kodifiziert; Schriftform = § 886 ABGB; Klarstellung erforderlich |
| „§ 2 Entgeltfortzahlungsgesetz" / EFZG-Verweis | EFZG (DE) | § 8 AngG — § 1 Abs 2 EFZG (DE) nimmt Angestellte aus; österreichisches Entgeltfortzahlungsrecht gilt eigenständig |
| fixer „3-Monats"-Haftungsdeckel ohne DHG-Bezug | BAG-Stil (DE) | §§ 2, 5 DHG — zwingender Mindestrahmen; Deckel darf DHG-Boden nicht unterschreiten |

## Sofort-Triage

| Klausel-Indiz | Prüfpunkt | Ampel | Norm-Anker AT | Deutsche Wurzel |
|---|---|---|---|---|
| ArbnErfG-Klausel / 4-Monats-Fiktion | Liegt eine schriftliche Vereinbarung über den Rechtsübergang vor? Fehlt sie, besteht kein Erwerb. | 🔴 | §§ 6–9 PatG | § 6 ArbnErfG (DE) |
| „außerordentliche Kündigung ohne Abmahnung" | Greift ein Entlassungsgrund nach § 27 AngG? Tatbestandsprüfung anhand österreichischer Judikatur — keine deutschen BAG-Linien übernehmen. | 🔴 | § 27 AngG | § 626 BGB (DE) |
| „in Textform" | Welche Formvorschrift ist gemeint? Schriftform (§ 886 ABGB)? Keine Entsprechung in AT; Klausel muss klargestellt werden. | 🟠 | § 886 ABGB | § 126b BGB (DE) |
| EFZG-Verweis / „Entgeltfortzahlungsgesetz" | Angestellte sind vom deutschen EFZG ausgenommen (§ 1 Abs 2 EFZG (DE)); für sie gilt § 8 AngG. Vertragstext auf AT-Norm umstellen. | 🔴 | § 8 AngG | EFZG (DE) |
| Fixer 3-Monats-Haftungsdeckel (BAG-Muster) | DHG-Boden (§§ 2, 5 DHG) zwingend; Klausel darf Vorsatz/grobe Fahrlässigkeit nicht ausschließen und darf die DHG-Haftungsuntergrenze nicht unterschreiten. | 🔴 | §§ 2, 5 DHG | BAG-Stil (DE) |

## Risiko-Ampel

- 🔴 **Klausel beruht auf deutschem Recht ohne österreichische Entsprechung oder mit abweichendem Regelungsinhalt** — unmittelbare Korrekturbedarf: Norm auf AT-Äquivalent umstellen; Klausel ist im betroffenen Umfang unwirksam oder leer (z.B. ArbnErfG-Fiktion, EFZG-Verweis, BAG-Haftungsdeckel unter DHG-Boden).
- 🔴 **Entlassungsklausel nach § 626 BGB (DE)-Muster** — § 27 AngG enthält abschließenden Tatbestandskatalog; deutsches Muster (außerordentliche Kündigung nach freiem Ermessen + Abmahnung) passt nicht; Klausel zwingend auf § 27 AngG umschreiben.
- 🟠 **„Textform"-Klausel** — § 126b BGB (DE) hat kein direktes AT-Pendant; je nach Kontext Schriftform (§ 886 ABGB) oder bloße Schriftlichkeit klären; Grenzfall, wenn Zweck eindeutig.
- 🟢 **Klausel ist terminologisch deutsch, aber inhaltlich AT-konform** — Korrektur des Wortlauts auf österreichisches Rechtsdeutsch (Jänner statt Januar, Rekurs statt Beschwerde), keine Nichtigkeitsfolge.

## Anschluss-Skill-Router

| Wenn der Fall trägt … | dann Skill | Erwartung |
|---|---|---|
| Klausel ist nach AT-Recht identifiziert und inhaltlich zu kontrollieren (§ 879 Abs 3 ABGB, AZG, URLG, DHG) | `klausel-inhaltskontrolle` | Klauselweise Inhaltskontrolle nach österreichischem Maßstab |
| Frage des Änderungsregimes (einvernehmlich, Änderungskündigung, konkludent) | `anschluss-routing` | Regime-Gate und Verschlechterungsschutz |

## Hinweis

Dieser Skill identifiziert Herkunftsfehler — er ersetzt nicht die vollständige Inhaltskontrolle nach österreichischem Recht. Nach Umstellung auf die AT-Norm schließt `klausel-inhaltskontrolle` an. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Das Mandat führen Sie; der Skill liefert die rechtliche Karte.
