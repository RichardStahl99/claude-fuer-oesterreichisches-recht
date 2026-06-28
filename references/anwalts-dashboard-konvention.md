# Anwalts-Dashboard-Konvention für Einstiegs-Skills

> Gilt für `allgemein`/`einstieg-routing`/`kaltstart-triage`-Skills der **Anwalts-Plugins**. Ergänzt `references/dashboard-template.md` (Output-Form) um die **Einstiegs-Form**: Was sieht ein Anwalt im ersten Bildschirm, der durch den Fall führt, ohne ihn zu entmündigen. (Aus dem deutschen Vorbild übernommen; Verfahrensstände, Norm-Beispiele und Quellen auf Österreich angepasst.)

## Leitprinzipien

1. **Geschwindigkeit vor Höflichkeit.** Kein Vorgeplänkel, keine Plugin-Selbstvorstellung. Erste sichtbare Zeile = Triage-Tabelle.
2. **Tabelle vor Prosa.** Strukturen als Tabellen, Ampeln, Routenkarten — nicht als Fließtext.
3. **Eine Rückfrage maximal.** Trägt die Akte 80 % der Triage, wird der Rest mit `[noch zu klären: …]` markiert und sofort gearbeitet.
4. **Human lawyers stay in charge.** Jede Empfehlung ist als Empfehlung markiert, nicht als Auto-Antwort.
5. **Anschluss-Skills offen benannt.** Der Einstiegs-Skill ist nur eine Tür — der nächste Skill mit Slug, Aufgabe und Erwartung muss klar genannt sein.

## Standardaufbau (von oben nach unten)

### Visueller Anker (optional, vor Block 1)

Bei typischerweise mehrstufigem Verfahrensablauf eine kompakte **Routenkarte als ASCII-Block** — eine Zeile pro Phase, mit Pfeilen, ohne Lehrbuch. Beispiel Zivilprozess Österreich:

```
Vorprozessual  -->  Mahnklage/Klage  -->  Urteil 1. Instanz  -->  Berufung OLG  -->  Revision OGH  -->  Exekution
     |                    |                      |                     |                  |                |
 Mängelrüge        Anwaltspflicht         Beweisverfahren      Frist 4 Wo.        erhebl. RFrage     EO
 § 377 UGB         > 5.000 € BG / LG      Neuerungsverbot      § 464 ZPO          § 502 ZPO          Exekutionstitel
```

Höchstens 10 Zeilen, in Monospace lesbar. Die Karte beantwortet eine Frage, die die Tabelle nicht beantwortet (typischerweise: „wo stehe ich im Instanzenzug?").

### Block 1 — Sofort-Triage (Tabelle, vor jeder Rückfrage)

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
|---|---|---|
| Rolle | Wen vertrete ich? (Mandant / Gegenseite / Mehrere) | Mandantenmail, Vollmacht |
| Verfahrensstand | Vorprozessual / Außergerichtlich / Mahnklage / Klage / Berufung / Revision / Außerstreit / Exekution | Vorhandene Schriftsätze, Einbringungsvermerk |
| Eilfrist | Welche Frist läuft heute, in 7, in 30 Tagen? | Frist aus Zustelldatum berechnen |
| Hauptanspruch | Welche Anspruchsgrundlage(n) tragen den Fall? | Plugin-spezifisch (Norm-Radar unten) |
| Zuständigkeit | Welches Gericht / welche Behörde? (BG/LG; sachlich + örtlich nach **JN**) | JN, vertragliche Gerichtsstandsvereinbarung |

### Block 2 — Risiko-Ampel

Drei Achsen, je 🔴/🟠/🟢:

- **Frist:** 🔴 ≤ 7 Tage · 🟠 8–30 Tage · 🟢 > 30 Tage oder ohne harte Frist
- **Beweislage:** 🔴 Beweisnot · 🟠 lückenhaft, aber heilbar · 🟢 belastbar (cave Neuerungsverbot in der Berufung)
- **Wirtschaftlich:** 🔴 existenziell · 🟠 erheblich · 🟢 überschaubar

Pro Ampel ein Satz Begründung.

### Block 3 — Anschluss-Skill-Router

| Wenn der Fall trägt … | dann Skill | Erwartung |
|---|---|---|
| Konkretes Sachverhaltsmerkmal | `slug-des-spezial-skills` | Welcher Output / welche Frist / welcher Beweisbedarf |

Höchstens fünf Zeilen; vorrangige Empfehlung fett, Alternativen darunter.

### Block 4 — Norm-Radar (eine Zeile pro Norm)

Maximal sechs tragende Normen mit kurzer Funktionsangabe. Beispiel: `§ 932 ABGB — Behelfshierarchie Gewährleistung` · `§ 11 VGG — 1-Jahres-Vermutung B2C`. Keine Kommentierung. Diese Zeilen sind Anker für die Spezial-Skills.

### Block 5 — Genau eine Rückfrage (nur wenn nötig)

Trägt die Akte 80 % der Triage: keine Rückfrage, sondern ein erster Entwurf mit `[noch zu klären: …]`. Sonst **eine** Frage, die die nächste Weiche tatsächlich umstellt.

### Block 6 — Judikatur-Anker (Such-Wegweiser, kein Blindzitat)

Maximal 3–4 Themen-Anker. **Keine Geschäftszahl aus Modellwissen behaupten** — stattdessen **zur Laufzeit** die RIS-Tools aufrufen (`tools/ris_client.py`, Protokoll in `references/ris-quellen.md` Abschnitt 3 und 6) und nur Geliefertes übernehmen:

- `linie "<Stichworte>" --gericht OGH` → OGH-Linie mit Leitsätzen, nach Linientiefe;
- `leit <GZ>` → ist die Entscheidung Leitentscheidung (Stamm) und wie gefestigt die Linie;
- `aktualitaet <Gesetz> <§> --seit <Entscheidungsdatum>` → wurde die Norm seither geändert (⚠️ ggf. überholt).

Format pro Zeile: *Thema/Linie — Leitsatz/RS-Nummer (live) — OGH-Senat — Aktualität*. So sieht der Anwalt die Linien sofort, ohne Halluzinationsrisiko.

### Block 7 — Driver-Seat-Reminder

Genau ein Satz am Ende: *„Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte."*

## Was bewusst weggelassen wird

- Keine Plugin-Selbstvorstellung. Keine Quellenhygiene-Predigt (steht in `references/quellenhygiene.md`; im Dashboard genügt ein Verweis am Ende). Keine Lehrbuchpassagen. Keine sechs-Punkte-Pflichtfragen — eine.

## Beispiel-Skelett (für jedes Anwalts-Plugin gleich gegliedert)

```markdown
# Einstieg <Plugin> — Anwalts-Dashboard

## Sofort-Triage
| Punkt | Schnellprüfung | Standardquelle |
| --- | --- | --- |
| Rolle | … | … |
| Verfahrensstand | … | … |
| Eilfrist | <Plugin-spezifische Frist> | … |
| Hauptanspruch | <plugin-spezifisch> | … |
| Zuständigkeit | <BG/LG nach JN> | … |

## Risiko-Ampel
- 🔴/🟠/🟢 Frist — <Satz>
- 🔴/🟠/🟢 Beweis — <Satz>
- 🔴/🟠/🟢 Wirtschaftlich — <Satz>

## Anschluss-Skills
| Wenn … | dann | Erwartung |
| --- | --- | --- |
| <Merkmal> | `<slug>` | <Output/Frist/Beweis> |

## Norm-Radar
- `<Norm>` — <Funktion>

## Genau eine Rückfrage (falls nötig)
> [Eine konkrete Frage, die die nächste Weiche umstellt]

## Hinweis
Diese Triage ist Vorbereitung, nicht Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`, Quellenanbindung nach `references/ris-quellen.md`.
```

## Self-Test vor Freigabe

1. Sieht der Anwalt in den ersten 15 Zeilen die Triage-Tabelle?
2. Steht die Risiko-Ampel auf einer Seite mit der Triage?
3. Ist mindestens ein Anschluss-Skill konkret mit Slug benannt — und existiert dieser Slug real im Plugin-Verzeichnis?
4. Wird höchstens **eine** Rückfrage gestellt?
5. Sind 3–4 Judikatur-Anker mit *Thema, OGH-Senat, RIS-Verweis* (ohne erfundene Geschäftszahl) gesetzt?
6. Steht der Driver-Seat-Hinweis sichtbar am Ende?

Fehlt ein Punkt, ist der Skill nicht freigegeben.
