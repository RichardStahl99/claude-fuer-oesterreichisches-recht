# Lösung / Triage — Altbau-Richtwert-Überschreitung

> Musterlauf der Plugin-Pipeline gegen `sachverhalt.md`. **Jede** Norm-Fundstelle ist über RIS auflösbar (Permalinks unten); Geschäftszahlen/RS-Nummern über `tools/ris_client.py` verifizieren (Leitsatz vor Verwendung lesen). **Aktuelle Richtwerte live beziehen** — hier bewusst nicht beziffert. Keine Rechtsberatung.

## Sofort-Triage (Dashboard)

| Punkt | Befund | Quelle |
|---|---|---|
| Rolle | Mieter, Hauptmiete | Mietvertrag |
| **Anwendungsbereich** | **Vollanwendung** — Gründerzeithaus (Baubewilligung 1898, also vor 30. 6. 1953), **8 Wohnungen** (kein Ein-/Zweifamilienhaus). §§ 16 ff gelten | `anwendungsbereich-mrg`, § 1 MRG |
| Mietzinssystem | **Richtwertmietzins** (§ 16 Abs 2): Kategorie A, ≤ 130 m², kein § 16 Abs 1-Fall | `mietzinsbildung` |
| Zulässigkeit | Vereinbart 12,80 €/m²; zulässig = Richtwert ± Zuschläge − **25 % Befristungsabschlag**; **Lagezuschlag unwirksam** (keine schriftliche Bekanntgabe) → Überschreitung indiziert | `mietzinsueberpruefung` |
| Frist | Befristeter Vertrag → § 16 Abs 8 **Sonderregel** (endet frühestens 6 Monate nach Vertragsende); derzeit **offen** | `mietzinsueberpruefung` |
| Verfahren | Wien hat Schlichtungsstelle → **zuerst Schlichtungsstelle** (§ 39), dann binnen 4 Wo. ans BG (§ 40); Außerstreit | `verfahren-schlichtung-ausserstreit` |

## Risiko-Ampel

- 🟢 **Frist** — laufender befristeter Vertrag; Präklusivfrist nach § 16 Abs 8 (Sonderregel) noch offen.
- 🟠 **Beweis** — Richtwert-Berechnung (Zuschläge, Erhaltungszustand) und Wirksamkeit des Lagezuschlags klärungsbedürftig; Mietvertrag + aktueller Wiener Richtwert beschaffen.
- 🟠 **Wirtschaftlich** — laufende Überzahlung × Restlaufzeit; spürbar.

## Rechtliche Beurteilung (Kurzgutachten)

1. **Anwendungsbereich:** **Vollanwendung** des MRG. Das Gründerzeithaus wurde vor dem 30. 6. 1953 baubewilligt (keine Neubau-Teilanwendung nach § 1 Abs 4 Z 1) und hat **mehr als zwei** Wohnungen (keine Vollausnahme nach § 1 Abs 2 Z 5). Damit gelten die Mietzinsbeschränkungen der §§ 15a, 16.
2. **System:** Wohnung der **Kategorie A**, 62 m² (≤ 130 m²), kein Fall des § 16 Abs 1 → **Richtwertmietzins** (§ 16 Abs 2). Maßgeblich ist der **aktuelle Wiener Richtwert** (RichtWG; live zu beziehen) zuzüglich begründeter Zu-/Abschläge.
3. **Lagezuschlag:** Der vereinbarte Lagezuschlag ist **unwirksam**, weil die für ihn maßgeblichen Umstände dem Mieter **nicht schriftlich bei Vertragsabschluss bekanntgegeben** wurden (§ 16 Abs 4). Er bleibt bei der zulässigen Höhe außer Ansatz.
4. **Befristungsabschlag:** Da befristet, ist der zulässige Hauptmietzins um **25 %** zu vermindern (§ 16 Abs 7).
5. **Überprüfung/Rückforderung:** Übersteigt der vereinbarte Mietzins den so berechneten Höchstbetrag, ist die Vereinbarung **insoweit unwirksam** (§ 16 Abs 8); das zu viel Bezahlte ist **rückforderbar**. Angesichts unwirksamem Lagezuschlag und Befristungsabschlag ist eine Überschreitung **wahrscheinlich** — konkrete Berechnung mit dem aktuellen Richtwert.
6. **Frist:** Befristeter Vertrag → **Sonderregel** des § 16 Abs 8 (endet frühestens 6 Monate nach Auflösung/Ablauf); derzeit gewahrt — genauen Lauf am Gesetzestext prüfen.
7. **Verfahren:** Wien betreibt eine **Schlichtungsstelle** (MA 50). Antrag daher **zuerst** dort (§ 39 MRG, sukzessive Zuständigkeit); danach binnen **4 Wochen** Abziehen an das **BG** möglich (§ 40 MRG). Verfahren ist **Außerstreit** (§ 37 MRG).

## Empfehlung (nächste Schritte)

- Aktuellen Wiener Richtwert und zulässigen Höchstmietzins berechnen (Zuschläge prüfen, Lagezuschlag streichen, −25 % Befristung).
- Mietzinsüberprüfungsantrag bei der **Schlichtungsstelle Wien** vorbereiten; Rückforderung beziffern.
- Fristlauf nach § 16 Abs 8 (befristet) dokumentieren.

## Verifizierte Quellen (RIS)

**Normen (Permalinks, HTTP 200 geprüft):**
- § 1 MRG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002531&Paragraf=1
- § 15a MRG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002531&Paragraf=15a
- § 16 MRG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002531&Paragraf=16
- § 37 MRG — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10002531&Paragraf=37
- RichtWG § 5 — https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003166&Paragraf=5

**Judikatur (Existenz/Permalink über RIS geprüft; Leitsatz vor Verwendung lesen; 5. Senat):**
- Anwendungsbereich/Vollausnahme — über RIS **live** suchen (`judikatur "Ein- oder Zweifamilienhaus" --gericht OGH`); on-point **5-Ob**-Rechtssatz vor Verwendung prüfen, keine GZ aus Modellwissen behaupten
- Richtwert/Zuschläge — `RIS-Justiz RS0117876` (OGH 5 Ob 296/02v)
- Unzulässige Mietzinsvereinbarung — `RIS-Justiz RS0083814` (OGH 5 Ob 149/95)
- Befristungsabschlag — `RIS-Justiz RS0131441` (OGH 5 Ob 18/17h)

Reproduzieren: `python3 tools/ris_client.py judikatur "Richtwert Zuschlag" --gericht OGH` bzw. `"unzulässige Mietzinsvereinbarung"`, `"Befristungsabschlag"`, `"Vollausnahme"`.

> Hinweis: Diese Triage ist Vorbereitung, nicht Entscheidung. Der Anwalt führt das Mandat.
