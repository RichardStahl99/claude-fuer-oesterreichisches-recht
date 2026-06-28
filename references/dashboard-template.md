# Dashboard-Vorlage

*Referenziert durch die Dashboard-Angebots-Schutzregel. Dashboards sollen einfach und einheitlich bleiben — der Wert liegt in der Schnelligkeit der Erfassung, nicht im visuellen Aufwand. (Engine aus dem deutschen Vorbild übernommen; nur Ausgabepfad und Beispiele auf Österreich angepasst.)*

## Aufbau (von oben nach unten)

1. **Titel und Metadaten.** Gegenstand, Erstellungsdatum, Abdeckungsbereich. Eine Zeile.
2. **Zusammenfassungsstatistik.** Die relevanten Kennzahlen, farblich codiert. Beispiel: "40 Befunde: 🔴 3 blockierend · 🟠 8 hoch · 🟡 15 mittel · 🟢 14 niedrig — 6 fällig diese Woche." Die wertvollste Zeile; auf einen Blick lesbar.
3. **Prüfhinweis.** Einblock-Format wie bei jeder Ausgabe: Quellen, Geltungsbereich, Vorbehalte, Hinweis vor Verwendung. Dashboards lassen die Sicherheitsmetadaten nicht weg.
4. **Diagramm(e).** Maximal eines oder zwei. Das Diagramm wählen, das die Struktur am besten zeigt:
   - **Risikoverteilung** (Balken): Anzahl nach Schweregrad — für Befunde, Probleme, Hinweise.
   - **Kategorieaufschlüsselung** (Kreis/gestapelter Balken): Anzahl nach Typ — für Vertragsarten, Mandatskategorien.
   - **Zeitschiene** (sortierte Tabelle): Termine chronologisch — für Fristentracker, Closing-Checklisten.
   - Nie mehr als zwei. Ein Dashboard mit fünf Diagrammen ist ein Bericht — und schwerer zu lesen als die Tabelle allein.
5. **Die Tabelle.** Sortierbar, filterbar, farblich nach Schweregrad/Status. Spalten gekürzt auf das, was auf einen Bildschirm passt. "Details"/"Anmerkungen" zuletzt — wird als Erstes abgeschnitten.
6. **Der Entscheidungsbaum.** "Wie weiter?" — dieselben Optionen wie in der Textausgabe.

## Darstellung je nach Oberfläche

- **Cowork / Claude Desktop:** HTML-Artefakt. Eigenständige Einzeldatei, CSS inline. Keine externen Abhängigkeiten, kein CDN, kein npm. Tabellen: HTML `<table>` mit `data-sort`-Attributen und kleinem inline-JS-Sortierer. Diagramme: Inline-SVG oder Unicode-Blocksymbole. JS minimal — nur Sortieren/Filtern.
- **Claude Code:** Dieselbe HTML-Datei in den Ausgabeordner des Plugins schreiben:
  `~/.claude/plugins/config/claude-fuer-oesterreichisches-recht/<plugin>/ausgaben/dashboard-<thema>-<datum>.html`
  und dem Nutzenden mitteilen, wie die Datei geöffnet wird (`open <Pfad>` unter macOS). Zusätzlich eine Markdown-Version mit Unicode-Balken für die Zusammenfassungsstatistik, damit der Überblick auch im Terminal sichtbar ist.
- **Excel (optional):** bei tabellarischen Prüfungen, Fristen-/Mandatsregistern und allem, was in eine Besprechung mitgenommen oder geteilt wird. Bestehende Excel-Ausgabespezifikation + Formel-Injektions-Verteidigung anwenden.
- **Unsichere Eingaben escapen (jedes Dashboard, jedes Mal):** Jeder Wert von außerhalb der Sitzung — Vertragstext der Gegenseite, Due-Diligence-Befunde, Mandatsbeschreibungen, jede durch Nutzer oder Datenraum gelieferte Zeichenkette — muss HTML-escaped werden, bevor er ins Dokument gelangt. `&`, `<`, `>`, `"`, `'` als HTML-Entities codieren. Im inline-JS Zellinhalt über `textContent` setzen, nie `innerHTML`. Keine `<script>`-Blöcke mit interpolierten Fremd-Strings. Fremd-URLs nur mit Schema-Prüfung (`http:`/`https:`/`mailto:`) in `href`/`src`. Ein im Browser geöffnetes Dashboard ist eine Vertrauensgrenze.

## Auf Klarheit setzen

- **Farbpalette:** Rot / Orange / Gelb / Grün für Schweregrade. Grau neutral. Blau für Status. Nichts anderes.
- **Keine Animationen, keine Frameworks, keine externen Schriftarten.** Ein Dashboard, das offline nicht funktioniert, ist keines.
- **Keine cleveren Layouts.** Zusammenfassung, Prüfhinweis, Diagramm, Tabelle, Entscheidungsbaum. Von oben nach unten — jedes Dashboard gleich, damit der Lesende weiß, wo er sucht.
- **Die Markdown-Version ist wichtig.** Zusammenfassungszeile mit Unicode-Balken (z. B. `🔴 ███ 3  🟠 ████████ 8  🟡 ███████████████ 15  🟢 ██████████████ 14`) gibt den Überblick im Terminal.

## Mandatsspezifische Kennzahlen (Risikoampel)

| KPI | Bedeutung | Anzeige |
|---|---|---|
| Offene Mandate gesamt | Aktive Mandate im Bearbeitungsstand | Zahl |
| Fällige Fristen (7 Tage) | Gesetzliche/vereinbarte Fristen in den nächsten 7 Tagen | 🔴 bei > 0 |
| Fristen (30 Tage) | Fristen in den nächsten 30 Tagen | 🟠 |
| Risikoampel gesamt | Verteilung blockierend / hoch / mittel / niedrig | Farbbalken |
| Mandatsstatus | Aktiv / Ruhend / Abgeschlossen | Kategorieaufschlüsselung |
| Letzte Aktualisierung | Zeitstempel der Datenbasis | Metadaten |

**Statusfarben:** 🔴 Blockierend (Frist läuft ab / gesetzliche Pflicht verletzt) · 🟠 Hoch (Handlung in 7 Tagen) · 🟡 Mittel (in 30 Tagen) · 🟢 Niedrig (im Blick behalten) · ⚪ Unbewertet.
