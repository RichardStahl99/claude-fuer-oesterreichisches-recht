# arbeitsrecht-vertragsaenderung

Fünfte Pilot-Vertikale: **Vertragsänderungen im aufrechten Arbeitsverhältnis** (Österreich). Abgegrenzt von `arbeitsrecht-beendigung`: Diese Vertikale greift, wenn **das Dienstverhältnis aufrecht bleibt, aber die Vertragsbedingungen geändert werden sollen** — durch Nachtrag, Änderungskündigung oder konkludente Änderung. Headline-Kompetenz ist die **Einordnung des Änderungswegs** (Gate-Skill `aenderungsregime`).

## Abgrenzung zu `arbeitsrecht-beendigung`

| | `arbeitsrecht-vertragsaenderung` | `arbeitsrecht-beendigung` |
|---|---|---|
| Zustand des Dienstverhältnisses | **aufrecht** | **endet** |
| Kernfrage | Welcher Änderungsweg ist zulässig? Welche Klauseln halten einer Inhaltskontrolle stand? | Welche Beendigungsart liegt vor? Fristen? Ansprüche? |
| Leitskill | `aenderungsregime` (Änderungsweg-Gate) | `beendigungsart` |
| Typischer Auslöser | Nachtrag mit Entgeltneugestaltung, Versetzungsklausel, Änderungskündigung | Kündigung, Entlassung, vorzeitiger Austritt, Zeitablauf |
| Übergang | Wenn AG Kündigung ausspricht oder Austritt erwogen wird → `arbeitsrecht-beendigung` | — |

## Skills (Pipeline)

| Skill | Aufgabe |
|---|---|
| `einstieg-vertragsaenderung` | Anwalts-Dashboard / Sofort-Triage (Rolle, Änderungsweg, Klausel-Bewertung Bestand → Angebot, Fristen, Hebel) |
| `aenderungsregime` | **Kern:** einvernehmliche Vertragsänderung / Änderungskündigung / konkludente Änderung (§ 863 ABGB); klärt, was ohne Unterschrift gilt |
| `klausel-inhaltskontrolle` | § 879 Abs 3 ABGB (gröbliche Benachteiligung): Bonus-Widerruf, Versetzung, All-in (§ 2g AVRAG), Arbeitszeit (§ 19c AZG), Urlaub (§ 12 URLG), Haftungsdeckel (§ 2 DHG, § 5 DHG) |
| `deutsche-vorlage-audit` | Falsche-Freunde-Scanner: erkennt Klauseln aus deutschen Vorlagen (ArbnErfG-Fiktion, § 626 BGB (DE), EFZG (DE), BAG-Stil) und benennt die österreichische Zielnorm |
| `austritt-backstop-und-hebel` | Strategischer Hebel: berechtigter Austritt § 26 Z 2 AngG / Kündigungsentschädigung § 29 AngG; warnt, dass Unterschrift den Backstop abbaut |
| `anschluss-routing` | Router zwischen Plugin-Vertikalen, AK Wien / Anwalt, Betriebsrat (§ 40 ArbVG) und Steuerberater |

Dazu `…-schnellstart.md` und `…-werkstatt.md`.

## Zuschnitt

Bewusst eng: **aufrechtes Arbeitsverhältnis mit Änderungsdruck**. **Nicht** abgedeckt (nur Verweis): Beendigung des Arbeitsverhältnisses (→ `arbeitsrecht-beendigung`), Sozialversicherung, Betriebsübergang (AVRAG Betriebsübergangsrecht), Gleichbehandlung (GlBG), besonderer Kündigungsschutz im Detail (MSchG/VKG/BEinstG).

## Grounding und Quellenanbindung

Normen werden zur Laufzeit über RIS aufgelöst (`tools/ris_client.py`). Verifizierte Gesetzesnummern: ABGB (10001622), ANGG (10008069, Artikel-1-Adressierung), ARBVG (10008329), AVRAG (10008872), AZG (10008238), DHG (10008209, Artikel-1-Adressierung), URLG (10008376), PATG (10002181).

### KV-Limitation — IT-KV (UBIT)

Im Regressionsfall (`testakten/dienstvertrag-nachtrag-aenderungsangebot/`) gilt der **Kollektivvertrag für Angestellte in der Information und Consulting (IT-KV, UBIT)**. Dieser ist ein **Kollektivvertrag**, kein Bundesgesetz — er ist **nicht als RIS-Permalink abrufbar** und wird daher als **externe Autorität** zitiert. `tools/verify.py` prüft ausschließlich Bundesgesetze (Bundesnormen); KV-Inhalte (Mindestgehälter, Verwendungsgruppen, Verfallsfristen) sind **aus dem aktuellen Kollektivvertragstext der Wirtschaftskammer live zu beziehen**, nicht aus Modellwissen. Diese Einschränkung gilt für alle Vertikalen, die einen KV als Rechtsgrundlage heranziehen — nicht nur für den IT-KV.

## Architektur (Phase-3-Muster)

Nutzt die geteilten Grundlagen `references/zitierweise.md` und `references/methodik-buergerliches-recht.md` **unverändert**; `tools/ris_client.py` erhielt die verifizierten Gesetzesnummern (siehe Grounding-Abschnitt oben).

## Verifikation

Regressionsfall: `testakten/dienstvertrag-nachtrag-aenderungsangebot/`. Definition of Done: Aus der Test-Akte entsteht eine Triage, deren Änderungsweg-/Klausel-Zuordnung und jede Norm-/Judikaturfundstelle live über RIS auflöst — mit Ausnahme des IT-KV (externe Autorität; kein RIS-Permalink; aus `verify.py`-Check ausgenommen).

## Hinweis

Output ist anwaltliche Vorbereitung, keine Rechtsberatung und keine verbindliche Entscheidung. § 9 RAO (Verschwiegenheit), DSGVO/DSG gelten. Jede Fundstelle und jeden KV-/Betragswert über RIS prüfen; keine Geschäftszahl oder RS-Nummer aus Modellwissen übernehmen.
