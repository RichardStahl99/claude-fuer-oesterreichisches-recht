# AGENTS.md — Arbeitsanleitung für Agenten

> Leitfaden für KI-Agenten und Mitwirkende, die dieses Repository erweitern. **Work in Progress.** Abgeleitet von [`Klotzkette/claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht) — übernimmt dessen *Arbeitsweise*, schreibt die *Rechtsschicht* für Österreich neu. **Kein Rechtsrat.** Überblick: `README.md`.

## 1. Die eine Architektur-Regel

Das Repo trennt **Motor** (jurisdiktionsneutral) und **Rechtsschicht** (österreichisch). Beim Hinzufügen eines neuen Rechtsgebiets gilt:

> **Die zwei Grundlagen `references/zitierweise.md` und `references/methodik-buergerliches-recht.md` werden NICHT verändert.**

Musst du sie ändern, stimmt am Ansatz etwas nicht. Nach jeder neuen Vertikale beweisen:

```bash
git diff --quiet -- references/zitierweise.md references/methodik-buergerliches-recht.md && echo "✓ unverändert"
```

Eine neue Vertikale = **neues Plugin + Gesetzesnummern im `ris_client.py`** — sonst nichts an den Grundlagen.

## 2. Harte Regeln (Quellenhygiene)

1. **Nie** Geschäftszahl, Rechtssatznummer (RS…), ECLI oder Paragrafennummer **aus Modellwissen** behaupten. Alles über RIS verifizieren (`tools/ris_client.py`).
2. **Jeder** zitierte Norm-Permalink muss live **HTTP 200** liefern; jede zitierte Judikatur muss live in RIS auflösen.
3. **Kein deutsches Recht.** Keine BGB-/ZPO(DE)-Normen, keine BGH/BVerfG-Aktenzeichen, kein deutsches Rechtsdeutsch. Falschfreunde u. a.: `KSchG` (= Konsumentenschutz, nicht Kündigungsschutz), *Rekurs* (nicht Beschwerde), *Jänner*, *Erkenntnis*, *Außerstreit*, *Vermögensverzeichnis* (nicht „Offenbarungseid"). ABGB-§§ ≠ BGB-§§.
4. **Literatur/Kommentare** nur mit vom Nutzer bereitgestellter oder lizenzierter Quelle — nie aus Modellwissen (RIS enthält keine Lehrmeinung).
5. **Unsicheres** als Prüfpunkt formulieren, nicht als gesichertes Zitat. Output ist Vorbereitung, nie Entscheidung (Driver-Seat-Hinweis).

## 3. Ein neues Rechtsgebiet hinzufügen (Muster)

1. **RIS-Daten zuerst.** Gesetzesnummern über `ris.bka.gv.at` recherchieren und verifizieren; Norm-Permalinks auf HTTP 200 testen; echte OGH-Rechtssätze sammeln (richtiger **Senat** beachten: Wohnrecht = **5 Ob**, Arbeitsrecht = **8/9 ObA**, Exekution = **3 Ob**).
2. **Gesetzesnummern eintragen** in `tools/ris_client.py` → `GESETZESNUMMER` (verifiziert, nie geraten). Adressieren Paragrafen unter einem Artikel (alte Stammgesetze wie AngG → `&Artikel=1`, sonst 404), Eintrag in `LAW_ARTIKEL`.
3. **Plugin anlegen** `<name>/`:
   - `.claude-plugin/plugin.json` (name, version, description, license `Apache-2.0 OR MIT`, author, homepage, keywords)
   - `README.md`, `<name>-schnellstart.md` (Kurzfassung zum Einkopieren), `<name>-werkstatt.md` (ausführlich)
   - `skills/<slug>/SKILL.md` — **≈ 6 Skills**: Einstiegs-Triage → **Headline-Gate** → Spezial-Skills → `anschluss-routing`
4. **Registrieren** in `.claude-plugin/marketplace.json` (`{name, source: "./<name>", description, version, author}`).
5. **Test-Akte** unter `testakten/<name>/`: `sachverhalt.md` (fiktiv, anonymisiert) + `loesung.md` (Musterlauf mit **ausschließlich RIS-auflösbaren** Permalinks/RS-Nummern).
6. **Verifizieren** (alles muss grün sein):
   - alle zitierten Norm-Permalinks → HTTP 200 (`python3 tools/ris_client.py norm <GESETZ> <§>`)
   - zitierte Rechtssätze lösen live auf (`… judikatur "<Stichworte>" --gericht OGH`)
   - `python3 tools/ris_client.py smoke` grün
   - Grundlagen unverändert (git diff, s. o.)
7. **Adversariale Rechtsprüfung** durch eine:n AT-Recht-Expert:in (Subagent/Review): jede §-Nummer, Schwelle, Frist, jedes Datum gegen RIS/jusline prüfen. **Must-fix-Fehler beheben**, bevor committet wird.
8. **Roadmap** in `README.md` aktualisieren.

## 4. SKILL.md-Format

```markdown
---
name: <slug>
description: "<eine Zeile: Gebiet + was der Skill tut>. Österreich, kein deutsches Recht."
---

# <Titel>

## Fachlicher Anker
- **Normen (über RIS prüfen):** § … (GNR …) ; …
- **Quellenhygiene:** references/quellenhygiene.md, zitierweise.md (keine GZ aus Modellwissen)

## Worum geht es? / Einsatzlage
## Schritt-für-Schritt   (Entscheidungsbaum/ASCII bei mehrstufigen Abläufen)
## Typische Fehler / Kritik   (inkl. „Deutsches Recht: …" — was NICHT gilt)
## Quellen und Stand MM/JJJJ
## Normen und Rechtsprechung
   ### Normen-Bibliothek (RIS-Permalinks verifizierbar)
   ### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen)
   ### Anwendung im Skill
```

- **Jede Vertikale hat ein Headline-Gate** (die erste, alles steuernde Weiche): Regimewahl · Anwendungsbereich · Zuständigkeit · Beendigungsart.
- Einstiegs-Skills folgen `references/anwalts-dashboard-konvention.md` (Sofort-Triage-Tabelle, Risiko-Ampel, Anschluss-Router, Norm-Radar, eine Rückfrage, Judikatur-Anker ohne erfundene GZ, Driver-Seat-Hinweis).

## 5. `tools/ris_client.py` — Kurzreferenz

```bash
python3 tools/ris_client.py norm ABGB 932           # Permalink + HTTP-Status
python3 tools/ris_client.py judikatur "<Stichworte>" --gericht OGH --von 2022-01-01
python3 tools/ris_client.py smoke                    # Grounding-Selbsttest
```

OGD-Eigenheiten (in `references/ris-quellen.md` dokumentiert): tief verschachteltes Schema (`Organ` unter `Technisch`, `DokumentUrl` unter `Allgemein`); `Suchworte` sind **UND-verknüpft** (praktikabel max. 2 Wörter); gültige `DokumenteProSeite`: `Ten/Twenty/Fifty/OneHundred`; ausländische Organe (`AUSL/EGMR`) werden gefiltert; Rechtssätze tragen eine **Semikolon-Liste** von Geschäftszahlen (führende GZ = Leitentscheidung).

**Verifizierte Gesetzesnummern:** ABGB 10001622 · VGG 20011654 · MRG 10002531 · RichtWG 10003166 · JN 10001697 · ZPO 10001699 · EO 10001700 · AngG 10008069 (Artikel 1) · ArbVG 10008329 · BMSVG 20002088 · ASGG 10000813 · UrlG 10008376.

## 6. Sprache & Stil

- **Deutsch** (österreichisches Rechtsdeutsch). Tabellen vor Prosa, knapp, scanbar.
- Code-Kommentare/Commit-Messages: kurz, sachlich. Bestehenden Stil der Nachbardateien spiegeln.
- Keine Erfolgsbehauptung ohne Beleg: erst verifizieren (HTTP 200, smoke, git diff), dann behaupten.

## 7. Was (noch) fehlt

WIP. Die doktrinäre Ebene (herrschende Meinung, Streitstände) fehlt strukturell, weil RIS nur Primärrecht enthält. Kommentare schließen diese Lücke — aber nur lizenziert/vom Nutzer bereitgestellt, nie ingestiert. Siehe Roadmap in `README.md`.
