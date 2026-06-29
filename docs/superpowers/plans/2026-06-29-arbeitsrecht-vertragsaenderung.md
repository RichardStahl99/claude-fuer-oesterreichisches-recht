# arbeitsrecht-vertragsaenderung — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the 5th legal vertical — `arbeitsrecht-vertragsaenderung` (contract modification in a running employment relationship) — as a plugin with 6 RIS-grounded skills plus an anonymized test-akte, following the repo's proven pattern.

**Architecture:** New plugin dir mirroring the existing four verticals (`plugin.json` + schnellstart + werkstatt + README + `skills/<n>/SKILL.md`). The only shared-foundation change is registering new `Gesetzesnummern` in `tools/ris_client.py` (the designated extension point); `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` stay byte-for-byte unchanged. The anonymized real case becomes the test-akte.

**Tech Stack:** Markdown skills; Python 3 grounding/verification harness (`tools/ris_client.py`, `tools/verify.py`); RIS OGD API (`data.bka.gv.at/ris/api/v2.6/`); JSON plugin manifests.

> **Domain note on "tests":** this repo has no unit tests for prose. The verification cycle per task is: (1) `python3 tools/ris_client.py norm <gesetz> <§>` must print a permalink with **HTTP 200** for every cited norm; (2) `python3 tools/verify.py` must report **0 failures** (it extracts every § -citation → resolves the permalink, validates JSON, runs smoke, and sha256-pins the foundations). A task's "failing test" is running these *before* the content exists / norm is registered and seeing the expected failure; the "passing test" is the green run after.

## Global Constraints

- **Foundations frozen:** `references/zitierweise.md` and `references/methodik-buergerliches-recht.md` MUST NOT change (sha256-pinned in `verify.py`). Confirm with `git diff` each task that touches anything shared.
- **No invented identifiers:** never write a `Gesetzesnummer`, `§`, or `Geschäftszahl` from model memory. Every number is verified live via `ris_client.py` before it lands in a file (the `GESETZESNUMMER` comment in the code states this rule verbatim).
- **No German law except as marked contrast:** German norms appear only as false-friend contrasts, written `(DE)` inline so `verify.py` skips them (e.g. `§ 626 BGB (DE)`).
- **Austrian Rechtsdeutsch:** Jänner (not Januar), Rekurs, Erkenntnis, Angestellte:r; no "Fachanwalt".
- **Every SKILL.md** follows the house structure (see *Shared skill template* below) and ends its `description` frontmatter with `Kein deutsches Recht.`
- **Runtime grounding wired** into every skill (the `linie`/`leit`/`aktualitaet` protocol per `references/ris-quellen.md` §3).
- **Language:** all content de-AT.
- **`python3 tools/verify.py` must be green** at the end of every task that adds citations.

---

## File Structure

**Created:**
- `arbeitsrecht-vertragsaenderung/.claude-plugin/plugin.json`
- `arbeitsrecht-vertragsaenderung/README.md`
- `arbeitsrecht-vertragsaenderung/arbeitsrecht-vertragsaenderung-schnellstart.md`
- `arbeitsrecht-vertragsaenderung/arbeitsrecht-vertragsaenderung-werkstatt.md`
- `arbeitsrecht-vertragsaenderung/skills/einstieg-vertragsaenderung/SKILL.md`
- `arbeitsrecht-vertragsaenderung/skills/aenderungsregime/SKILL.md`
- `arbeitsrecht-vertragsaenderung/skills/klausel-inhaltskontrolle/SKILL.md`
- `arbeitsrecht-vertragsaenderung/skills/deutsche-vorlage-audit/SKILL.md`
- `arbeitsrecht-vertragsaenderung/skills/austritt-backstop-und-hebel/SKILL.md`
- `arbeitsrecht-vertragsaenderung/skills/anschluss-routing/SKILL.md`
- `testakten/dienstvertrag-nachtrag-aenderungsangebot/sachverhalt.md`
- `testakten/dienstvertrag-nachtrag-aenderungsangebot/loesung.md`

**Modified:**
- `tools/ris_client.py` — `GESETZESNUMMER` dict (+ `LAW_ARTIKEL` if a new law 404s without an Artikel).
- `.claude-plugin/marketplace.json` — append 5th plugin entry.

**Frozen (must not change):** `references/zitierweise.md`, `references/methodik-buergerliches-recht.md`.

---

## Shared skill template

Every `SKILL.md` in this vertical fills this exact skeleton (copied from the house pattern in `arbeitsrecht-beendigung/skills/einstieg-arbeitsrecht/SKILL.md`). Each task below specifies only the per-skill content (description, norms, tables, router targets).

```markdown
---
name: <skill-name>
description: "<one sentence: what this skill does, key norms in (§ … Gesetz) form>. Kein deutsches Recht."
---

# <Title>

## Fachlicher Anker

- **Normen (über RIS auflösen, `tools/ris_client.py`):** <§ + Gesetz + GNR each, semicolon-separated>.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`, `references/ris-quellen.md`. Keine Geschäftszahl aus Modellwissen.
- **Laufzeit-Grounding (Pflicht):** vor Aussagen zur Linie `python3 tools/ris_client.py linie "<suchworte>" --gesetz <G> --paragraf <§>`; Leitentscheidung mit `leit <GZ>`; Fassungsstand mit `aktualitaet <G> <§> --seit <datum>`.
- **Konvention:** Aufbau nach `references/anwalts-dashboard-konvention.md`.

## Einsatzlage

<when to use; explicit "Nicht für …" exclusions routing elsewhere>

## Sofort-Triage (Tabelle, vor jeder Rückfrage)

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
|---|---|---|
| … | … | … → Skill `<next>` |

## Risiko-Ampel

- 🔴/🟠/🟢 **Frist** — …
- 🔴/🟠/🟢 **Beweis** — …
- 🔴/🟠/🟢 **Wirtschaftlich** — …

## Anschluss-Skill-Router

| Wenn der Fall trägt … | dann Skill | Erwartung |
|---|---|---|
| … | `<skill>` | … |
```

---

## Task 1: Register & verify new Gesetzesnummern

**Files:**
- Modify: `tools/ris_client.py` — `GESETZESNUMMER` (lines ~49-62); `LAW_ARTIKEL` (lines ~67-69) only if needed.

**Interfaces:**
- Produces: registry keys `AZG`, `AVRAG`, `DHG`, `PATG` (and `ESTG`, `EFZG` only if their § -cites survive into skills) usable as `ris_client.py norm <KEY> <§>` and resolvable by `verify.py`.

- [ ] **Step 1: Establish the failing baseline.** For each new law, confirm it is not yet known:

```bash
python3 tools/ris_client.py norm AZG 19c
```
Expected: fails/empty — `AZG` is not in `GESETZESNUMMER` yet.

- [ ] **Step 2: Look up each Gesetzesnummer on RIS (never guess).** On `https://www.ris.bka.gv.at/` → Bundesrecht konsolidiert, open each law and read the `Gesetzesnummer` from the document metadata:
  - AZG — Arbeitszeitgesetz (BGBl 461/1969)
  - AVRAG — Arbeitsvertragsrechts-Anpassungsgesetz (BGBl 459/1993)
  - DHG — Dienstnehmerhaftpflichtgesetz (BGBl 80/1965)
  - PatG — Patentgesetz 1970 (BGBl 259/1970)
  - (Conditional) EStG 1988, EFZG — only if Task 4/6 keep their § -citations.

- [ ] **Step 3: Verify each candidate number resolves to HTTP 200** by passing the raw `Gesetzesnummer` directly (the `norm` command accepts a number or short name):

```bash
python3 tools/ris_client.py norm <CANDIDATE_GNR> 19c    # AZG: § 19c
python3 tools/ris_client.py norm <CANDIDATE_GNR> 2g     # AVRAG: § 2g
python3 tools/ris_client.py norm <CANDIDATE_GNR> 2      # DHG: § 2
python3 tools/ris_client.py norm <CANDIDATE_GNR> 6      # PatG: § 6
```
Expected: each prints a `ris.bka.gv.at` NormDokument permalink and **HTTP 200**.
If a law's §§ 404 even with a correct number, it is Artikel-addressed (like AngG) — add it to `LAW_ARTIKEL` with the correct Artikel and re-run.

- [ ] **Step 4: Add the verified entries** to `GESETZESNUMMER`, matching the existing comment style (`# <full name> (BGBl …) — verifiziert (§… HTTP 200)`):

```python
    "URLG": "10008376",   # Urlaubsgesetz (BGBl 390/1976) — verifiziert (§10 HTTP 200)
    "AZG": "<verified>",    # Arbeitszeitgesetz (BGBl 461/1969) — verifiziert (§19c HTTP 200)
    "AVRAG": "<verified>",  # Arbeitsvertragsrechts-AnpassungsG (BGBl 459/1993) — verifiziert (§2g HTTP 200)
    "DHG": "<verified>",    # Dienstnehmerhaftpflichtgesetz (BGBl 80/1965) — verifiziert (§2 HTTP 200)
    "PATG": "<verified>",   # Patentgesetz 1970 (BGBl 259/1970) — verifiziert (§6 HTTP 200)
```

- [ ] **Step 5: Re-verify by short name + run smoke.**

```bash
python3 tools/ris_client.py norm AZG 19c
python3 tools/ris_client.py norm AVRAG 2g
python3 tools/ris_client.py norm DHG 2
python3 tools/ris_client.py norm PATG 6
python3 tools/ris_client.py smoke
```
Expected: all four permalinks HTTP 200; smoke prints `ALLE CHECKS BESTANDEN ✓`.

- [ ] **Step 6: Commit.**

```bash
git add tools/ris_client.py
git commit -m "feat(ris): register AZG/AVRAG/DHG/PatG Gesetzesnummern (verifiziert)"
```

---

## Task 2: Plugin scaffold + marketplace registration

**Files:**
- Create: `arbeitsrecht-vertragsaenderung/.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json` (append 5th entry to `plugins`)

**Interfaces:**
- Produces: plugin `name: "arbeitsrecht-vertragsaenderung"`, `source: "./arbeitsrecht-vertragsaenderung"`.

- [ ] **Step 1: Write `plugin.json`** (mirror `arbeitsrecht-beendigung/.claude-plugin/plugin.json`):

```json
{
  "name": "arbeitsrecht-vertragsaenderung",
  "version": "0.1.0",
  "description": "Vertragsänderung im aufrechten Dienstverhältnis nach österreichischem Recht: Änderungs-Regime-Triage (einvernehmlich / Änderungskündigung / konkludent § 863 ABGB), Klausel-Inhaltskontrolle (§ 879 Abs 3 ABGB: Bonus-Widerruf, Versetzung, All-in § 19c AZG/§ 2g AVRAG, Urlaub § 12 UrlG, Haftungsdeckel DHG), DE→AT-Falsche-Freunde-Audit und Austritts-Backstop (§ 26/§ 29 AngG). Fünfte Vertikale; Grundlagen unverändert.",
  "license": "Apache-2.0 OR MIT",
  "author": {
    "name": "RichardStahl99",
    "email": "RichardStahl99@users.noreply.github.com"
  },
  "homepage": "https://github.com/RichardStahl99/claude-fuer-oesterreichisches-recht",
  "keywords": [
    "arbeitsrecht", "vertragsaenderung", "aenderungskuendigung", "konkludent",
    "inhaltskontrolle", "all-in", "angg", "arbvg", "avrag", "dhg", "oesterreich"
  ]
}
```

- [ ] **Step 2: Append the marketplace entry** to the `plugins` array in `.claude-plugin/marketplace.json` (after the `arbeitsrecht-beendigung` object):

```json
    {
      "name": "arbeitsrecht-vertragsaenderung",
      "source": "./arbeitsrecht-vertragsaenderung",
      "description": "Vertragsänderung im aufrechten Dienstverhältnis: Regime-Triage (einvernehmlich/Änderungskündigung/konkludent § 863 ABGB), Klausel-Inhaltskontrolle (§ 879 Abs 3 ABGB), DE→AT-Falsche-Freunde-Audit und Austritts-Backstop (§ 26/§ 29 AngG). Fünfte Vertikale.",
      "version": "0.1.0",
      "author": "RichardStahl99"
    }
```

- [ ] **Step 3: Validate JSON.**

```bash
python3 -m json.tool arbeitsrecht-vertragsaenderung/.claude-plugin/plugin.json >/dev/null && echo OK
python3 -m json.tool .claude-plugin/marketplace.json >/dev/null && echo OK
```
Expected: `OK` twice.

- [ ] **Step 4: Commit.**

```bash
git add arbeitsrecht-vertragsaenderung/.claude-plugin/plugin.json .claude-plugin/marketplace.json
git commit -m "feat(plugin): scaffold arbeitsrecht-vertragsaenderung + marketplace entry"
```

---

## Task 3: Skill `einstieg-vertragsaenderung`

**Files:**
- Create: `arbeitsrecht-vertragsaenderung/skills/einstieg-vertragsaenderung/SKILL.md`

**Interfaces:**
- Consumes: registry keys from Task 1.
- Produces: router targets `aenderungsregime`, `klausel-inhaltskontrolle`, `deutsche-vorlage-audit`, `austritt-backstop-und-hebel`, `anschluss-routing` (these exact skill dir names are used by Tasks 4-8 routers).

- [ ] **Step 1: Write the SKILL.md** using the *Shared skill template*, with this per-skill content:
  - **description:** Einstiegs-Triage für Vertragsänderungen im aufrechten Dienstverhältnis (Anwalts-Dashboard): erfasst Rolle, Änderungsweg, Klausel-Bewertung (Bestand→Angebot), Fristen und Hebel in einer scanbaren Tabelle und leitet weiter. + `Kein deutsches Recht.`
  - **Normen anchor:** § 863, § 879 Abs 3 ABGB (GNR 10001622); § 26/§ 29 AngG (GNR 10008069, Artikel 1); § 36 Abs 2 Z 3, § 101, § 107 ArbVG (GNR 10008329).
  - **Sofort-Triage rows:** Rolle (Angestellte:r?); **Änderungsweg** (einvernehmlich/Änderungskündigung/konkludent → `aenderungsregime`); Klausel-Bewertung Bestand→Angebot (✅/🔴/🟠/⚪ → `klausel-inhaltskontrolle`); DE-Vorlage erkennbar? (→ `deutsche-vorlage-audit`); Hebel/Austritt (§ 26 AngG → `austritt-backstop-und-hebel`); **leitende:r Angestellte:r?** (§ 36 ArbVG — echte Hire-&-Fire-/Gehaltskompetenz, nicht Titel allein).
  - **Risiko-Ampel:** Frist (konkludente Bindung läuft mit Auszahlung); Beweis (Vorbehalt bei Erhöhung?); Wirtschaftlich (Wert der aufgegebenen Schutzrechte).
  - **Router:** all five downstream skills.

- [ ] **Step 2: Verify every cited norm resolves.**

```bash
for s in "ABGB 863" "ABGB 879" "ANGG 26" "ANGG 29" "ARBVG 36" "ARBVG 101" "ARBVG 107"; do python3 tools/ris_client.py norm $s; done
```
Expected: each prints a permalink with HTTP 200.

- [ ] **Step 3: Run the link-rot harness.**

```bash
python3 tools/verify.py
```
Expected: `0 failures`, the new file counted.

- [ ] **Step 4: Commit.**

```bash
git add arbeitsrecht-vertragsaenderung/skills/einstieg-vertragsaenderung/SKILL.md
git commit -m "feat(skill): einstieg-vertragsaenderung (Anwalts-Dashboard)"
```

---

## Task 4: Skill `aenderungsregime` (headline gate)

**Files:**
- Create: `arbeitsrecht-vertragsaenderung/skills/aenderungsregime/SKILL.md`

**Interfaces:**
- Consumes: registry keys from Task 1; router target names from Task 3.

- [ ] **Step 1: Write the SKILL.md** using the *Shared skill template*, per-skill content:
  - **description:** Gate-Skill: trennt einvernehmliche Vertragsänderung, Änderungskündigung und konkludente Änderung (§ 863 ABGB); klärt, was ohne Unterschrift gilt. + `Kein deutsches Recht.`
  - **Normen anchor:** § 863, § 914, § 915 ABGB (GNR 10001622); § 20 AngG (GNR 10008069, Art 1); § 101, § 105, § 107 ArbVG (GNR 10008329).
  - **Doctrine to encode (cite live; anchors from the verified Fallübersicht — re-verify with `judikatur`/`leit` before use):**
    - einvernehmlich = Zustimmung nötig; Schweigen ist keine Annahme (RS0047273);
    - Änderungskündigung = echte Kündigung + Fortsetzungsangebot, darf § 101 nicht umgehen (8 ObA 63/15w), Zumutbarkeit (9 ObA 59/23a);
    - konkludent = vorbehaltlose wiederholte Erhöhung bindet (RS0014526; Empfängerhorizont RS0014154; 8 ObA 33/21t); Verschlechterung wirkt nicht zurück (9 ObA 113/08w); Unklarheit zulasten Verwender (§ 915 ABGB);
    - Kernsatz: ohne Unterschrift läuft der Bestandsvertrag weiter (8 ObA 35/98z).
  - **Sofort-Triage:** Welcher Weg? / Gab es einen Vorbehalt? / Ist die Erhöhung schon zugeflossen?
  - **Router:** → `klausel-inhaltskontrolle`, `austritt-backstop-und-hebel`, `anschluss-routing`.

- [ ] **Step 2: Verify norms + check the OGH anchors live.**

```bash
for s in "ABGB 863" "ABGB 914" "ABGB 915" "ANGG 20" "ARBVG 101" "ARBVG 105" "ARBVG 107"; do python3 tools/ris_client.py norm $s; done
python3 tools/ris_client.py leit "8 ObA 35/98z"
python3 tools/ris_client.py linie "konkludente Vertragsänderung Entgelt Vorbehalt" --gesetz ABGB --paragraf 863
```
Expected: norms HTTP 200; `leit`/`linie` return live RIS data (use real GZ found here, not the placeholders, if they differ).

- [ ] **Step 3: Run harness.** `python3 tools/verify.py` → `0 failures`.

- [ ] **Step 4: Commit.**

```bash
git add arbeitsrecht-vertragsaenderung/skills/aenderungsregime/SKILL.md
git commit -m "feat(skill): aenderungsregime — einvernehmlich/Änderungskündigung/konkludent"
```

---

## Task 5: Skill `klausel-inhaltskontrolle`

**Files:**
- Create: `arbeitsrecht-vertragsaenderung/skills/klausel-inhaltskontrolle/SKILL.md`

- [ ] **Step 1: Write the SKILL.md**, per-skill content:
  - **description:** Klauselweise Inhaltskontrolle nach § 879 Abs 3 ABGB (gröbliche Benachteiligung): Bonus-Widerruf, Versetzung, All-in, Urlaub, Haftungsdeckel. + `Kein deutsches Recht.`
  - **Normen anchor:** § 879 Abs 3 ABGB (GNR 10001622); § 19c AZG (GNR aus Task 1); § 2g AVRAG (Task 1); § 12 UrlG (GNR 10008376); §§ 2, 5 DHG (Task 1).
  - **Per-clause doctrine (cite live):** Bonus-Widerruf — verdiente Variable unwiderruflich (8 ObA 33/21t), Toleranz ~10 % (8 ObA 16/03s), Entgeltklausel-Kontrolle (1 Ob 105/10p); Versetzung geringerwertig — ohne BR Individualschutz/Entgeltschutz; All-in — Kalenderjahr zulässig (9 ObA 28/17h), kein Verzicht aufs Übersteigende, § 2g AVRAG Transparenz (8 ObA 22/22a, 9 ObA 62/25w); Arbeitszeit-Lage § 19c AZG nicht abdingbar (9 ObA 57/22f); Urlaub — nur gesetzlicher Teil geschützt, 6. Woche umgestaltbar (8 ObA 23/23z, 9 ObA 135/14i); Haftungsdeckel — DHG-Boden nicht unterschreitbar.
  - **Sofort-Triage:** one row per clause type → 🔴/🟠 rating + governing norm.
  - **Router:** → `deutsche-vorlage-audit`, `austritt-backstop-und-hebel`.

- [ ] **Step 2: Verify norms.**

```bash
for s in "ABGB 879" "AZG 19c" "AVRAG 2g" "URLG 12" "DHG 2" "DHG 5"; do python3 tools/ris_client.py norm $s; done
python3 tools/ris_client.py aktualitaet AZG 19c --seit 2022-01-01
```
Expected: all HTTP 200; `aktualitaet` prints a Fassungsstand message.

- [ ] **Step 3: Run harness.** `python3 tools/verify.py` → `0 failures`.

- [ ] **Step 4: Commit.**

```bash
git add arbeitsrecht-vertragsaenderung/skills/klausel-inhaltskontrolle/SKILL.md
git commit -m "feat(skill): klausel-inhaltskontrolle (§ 879 Abs 3 ABGB)"
```

---

## Task 6: Skill `deutsche-vorlage-audit`

**Files:**
- Create: `arbeitsrecht-vertragsaenderung/skills/deutsche-vorlage-audit/SKILL.md`

- [ ] **Step 1: Write the SKILL.md**, per-skill content:
  - **description:** Systematischer Falsche-Freunde-Scanner: erkennt aus deutschen Vorlagen übernommene Klauseln und ersetzt sie durch die österreichisch korrekte Norm. + `Kein deutsches Recht.`
  - **Normen anchor (AT targets):** §§ 6-9 PatG (Task 1); § 27, § 8 AngG (GNR 10008069, Art 1); §§ 2, 5 DHG (Task 1). German contrasts written `(DE)`: `§ 6 ArbnErfG (DE)`, `§ 626 BGB (DE)`, `§ 126b BGB (DE)`, `EFZG (DE)`.
  - **Mapping table (the skill's core output):** `Klausel-Indiz → dt. Wurzel (DE) → österr. korrekte Norm → Folge`:
    - "Arbeitnehmererfindungsgesetz"/4-Monats-Fiktion → § 6 ArbnErfG (DE) → §§ 6-9 PatG (Erwerb nur per schriftl. Vereinbarung);
    - "außerordentliche Kündigung ohne Abmahnung" → § 626 BGB (DE) → § 27 AngG (Entlassung);
    - "in Textform" → § 126b BGB (DE) → in AT nicht kodifiziert;
    - "§ 2 Entgeltfortzahlungsgesetz" → EFZG (DE) → § 8 AngG (Angestellte: § 1 Abs 2 EFZG nimmt sie aus);
    - fixer "3-Monats"-Haftungsdeckel → BAG-Stil (DE) → §§ 2, 5 DHG.
  - **Note:** if EStG/EFZG were NOT registered in Task 1, keep them only as `(DE)` contrast strings (verify.py skips `(DE)`), so no AT permalink is needed for them.
  - **Router:** → `klausel-inhaltskontrolle`, `anschluss-routing`.

- [ ] **Step 2: Verify AT-target norms (contrasts are skipped by verify).**

```bash
for s in "PATG 6" "PATG 7" "PATG 8" "PATG 9" "ANGG 27" "ANGG 8" "DHG 2"; do python3 tools/ris_client.py norm $s; done
```
Expected: all HTTP 200.

- [ ] **Step 3: Confirm contrast cites are correctly skipped.**

```bash
python3 tools/verify.py
```
Expected: `0 failures`; output shows `(DE)` cites skipped (not resolved).

- [ ] **Step 4: Commit.**

```bash
git add arbeitsrecht-vertragsaenderung/skills/deutsche-vorlage-audit/SKILL.md
git commit -m "feat(skill): deutsche-vorlage-audit (DE→AT Falsche-Freunde-Scanner)"
```

---

## Task 7: Skill `austritt-backstop-und-hebel`

**Files:**
- Create: `arbeitsrecht-vertragsaenderung/skills/austritt-backstop-und-hebel/SKILL.md`

- [ ] **Step 1: Write the SKILL.md**, per-skill content:
  - **description:** Strategischer Hebel: berechtigter vorzeitiger Austritt (§ 26 Z 2 AngG) + Kündigungsentschädigung (§ 29 AngG) bei zu aggressiver Verschlechterung; warnt, dass die Unterschrift diesen Backstop abbaut. + `Kein deutsches Recht.`
  - **Normen anchor:** § 26, § 29 AngG (GNR 10008069, Art 1); § 863 ABGB (GNR 10001622).
  - **Doctrine (cite live):** zu aggressive Herabstufung/Entgeltkürzung → berechtigter Austritt + Kündigungsentschädigung (volle Bezüge der fiktiven Frist, erste 3 Monate ohne Anrechnung); bei Ausübung sofort schriftlich "unter Protest" (9 ObA 164/07v); Unterschrift von Versetzungs-/Widerrufsklauseln macht genau diese Schritte vertraglich erlaubt und baut § 26 ab.
  - **Risiko-Ampel:** Frist (Austritt zeitnah zum Anlass); Beweis (Protest dokumentiert?); Wirtschaftlich (Größenordnung Kündigungsentschädigung vs. Bleiben).
  - **Router:** → `anschluss-routing`, `aenderungsregime`.

- [ ] **Step 2: Verify norms + anchor.**

```bash
for s in "ANGG 26" "ANGG 29" "ABGB 863"; do python3 tools/ris_client.py norm $s; done
python3 tools/ris_client.py leit "9 ObA 164/07v"
```
Expected: norms HTTP 200; `leit` returns live data (use the real GZ if it differs).

- [ ] **Step 3: Run harness.** `python3 tools/verify.py` → `0 failures`.

- [ ] **Step 4: Commit.**

```bash
git add arbeitsrecht-vertragsaenderung/skills/austritt-backstop-und-hebel/SKILL.md
git commit -m "feat(skill): austritt-backstop-und-hebel (§ 26/§ 29 AngG)"
```

---

## Task 8: Skill `anschluss-routing`

**Files:**
- Create: `arbeitsrecht-vertragsaenderung/skills/anschluss-routing/SKILL.md`

- [ ] **Step 1: Write the SKILL.md**, per-skill content:
  - **description:** Abschluss-Router: verweist je nach Fall auf die Beendigungs-Vertikale, AK/Arbeitsrechtsanwalt, Betriebsrat und Steuerberater. + `Kein deutsches Recht.`
  - **Normen anchor:** § 40 ArbVG (GNR 10008329, Betriebsrat-Gründung, nur prospektiv).
  - **Router table:** echte Kündigung/Entlassung im Raum → Plugin `arbeitsrecht-beendigung`; verbindliche Beurteilung → AK Wien / Arbeitsrechtsanwalt; strukturelle Lösung → Betriebsrat (§ 40 ArbVG, prospektiv); Jahressechstel/Steuer → Steuerberater.
  - **Note:** cross-link is bidirectional — Task 11 adds the back-pointer note; here just reference `arbeitsrecht-beendigung` by name.

- [ ] **Step 2: Verify norm.** `python3 tools/ris_client.py norm ARBVG 40` → HTTP 200.

- [ ] **Step 3: Run harness.** `python3 tools/verify.py` → `0 failures`.

- [ ] **Step 4: Commit.**

```bash
git add arbeitsrecht-vertragsaenderung/skills/anschluss-routing/SKILL.md
git commit -m "feat(skill): anschluss-routing"
```

---

## Task 9: Plugin docs — schnellstart, werkstatt, README

**Files:**
- Create: `arbeitsrecht-vertragsaenderung/arbeitsrecht-vertragsaenderung-schnellstart.md`
- Create: `arbeitsrecht-vertragsaenderung/arbeitsrecht-vertragsaenderung-werkstatt.md`
- Create: `arbeitsrecht-vertragsaenderung/README.md`

- [ ] **Step 1: Read the three existing docs** to copy structure/tone exactly:

```bash
cat arbeitsrecht-beendigung/arbeitsrecht-beendigung-schnellstart.md
cat arbeitsrecht-beendigung/arbeitsrecht-beendigung-werkstatt.md
cat arbeitsrecht-beendigung/README.md
```

- [ ] **Step 2: Write `schnellstart.md`** — the 6-skill flow as a quick path: einstieg → aenderungsregime → klausel-inhaltskontrolle → deutsche-vorlage-audit → austritt-backstop-und-hebel → anschluss-routing, with the one-line purpose of each (mirror the beendigung schnellstart's format).

- [ ] **Step 3: Write `werkstatt.md`** — worked walkthrough on the anonymized Nachtrag case (mirror beendigung werkstatt's depth/format), referencing the test-akte from Task 10.

- [ ] **Step 4: Write `README.md`** — purpose, scope/boundary vs `arbeitsrecht-beendigung`, skill list, grounding note (RIS + KV-as-external-authority limitation), disclaimer (mirror beendigung README).

- [ ] **Step 5: Run harness** (these docs may contain § -cites). `python3 tools/verify.py` → `0 failures`.

- [ ] **Step 6: Commit.**

```bash
git add arbeitsrecht-vertragsaenderung/arbeitsrecht-vertragsaenderung-schnellstart.md arbeitsrecht-vertragsaenderung/arbeitsrecht-vertragsaenderung-werkstatt.md arbeitsrecht-vertragsaenderung/README.md
git commit -m "docs(plugin): schnellstart, werkstatt, README für arbeitsrecht-vertragsaenderung"
```

---

## Task 10: Anonymized test-akte

**Files:**
- Create: `testakten/dienstvertrag-nachtrag-aenderungsangebot/sachverhalt.md`
- Create: `testakten/dienstvertrag-nachtrag-aenderungsangebot/loesung.md`

**Interfaces:**
- Consumes: all six skills (the loesung applies their method).

- [ ] **Step 1: Read an existing test-akte** for the two-file format:

```bash
cat testakten/kuendigung-angestellte-anfechtung/sachverhalt.md
cat testakten/kuendigung-angestellte-anfechtung/loesung.md
```

- [ ] **Step 2: Write `sachverhalt.md`** — the anonymized case. Apply ALL anonymization rules (hard gate):
  - Arbeitgeber → `MUSTER IT Consulting AG, Niederlassung Wien`; Schwester → "Schwestergesellschaft (eigene Rechtsperson)".
  - Person → "Mandant:in (Angestellte:r), Wien"; Vorgesetzter → "die direkte Führungskraft"; Adresse entfällt; "DocuSign" → "elektronisches Signaturtool".
  - Rollentitel → "Fachexperten-Rolle → Führungsrolle, Vertrieb"; konkrete Bereichs-/Produktnamen entfallen.
  - KV-Stufe → "einschlägige Verwendungsgruppe/Stufe des IT-KV".
  - **Fuzzed figures (mark `(fiktiv/illustrativ)`):** Bestand Zielgehalt €165.000 (Fix €115.000 / variabel €50.000) → Angebot €185.000 (Fix €120.000 / variabel €65.000), nur +€5.000 Fix gesichert; Urlaub 30 → 25 + 5 verfallend; illustrativer KV-Mindestsatz.
  - Include the `Bestand → Angebot → Bewertung` clause table (anonymized).

- [ ] **Step 3: Write `loesung.md`** — model analysis applying the 6 skills' method: Regime-Einordnung (kein Zwang, ohne Unterschrift läuft Bestand weiter), Klausel-Inhaltskontrolle, DE-Vorlage-Audit, Austritts-Backstop, Handlungsempfehlungen. Cite only verified norms; mark KV as external authority.

- [ ] **Step 4: Anonymization gate — grep for forbidden strings.**

```bash
grep -rEi "NTT|Stahl|Richard|Handelskai|1050 Wien|1200 Wien|Lars|GBMS|Presales|DocuSign|6\.781|170\.000|190\.000|120\.000|125\.000" testakten/dienstvertrag-nachtrag-aenderungsangebot/
```
Expected: **no matches** (exit code 1 / empty). Any hit must be removed before continuing.

- [ ] **Step 5: Run harness.** `python3 tools/verify.py` → `0 failures`.

- [ ] **Step 6: Commit.**

```bash
git add testakten/dienstvertrag-nachtrag-aenderungsangebot/
git commit -m "test(akte): anonymisierte Test-Akte dienstvertrag-nachtrag-aenderungsangebot"
```

---

## Task 11: Full verification + foundation-freeze proof + bidirectional cross-link

**Files:**
- Modify: `arbeitsrecht-beendigung/skills/anschluss-routing/SKILL.md` (add one router row pointing to the new vertical — confirm exact filename first).

- [ ] **Step 1: Add the back-pointer** in the beendigung routing skill: a row "Verhältnis läuft weiter, Bedingungen ändern sich → Plugin `arbeitsrecht-vertragsaenderung`". (Open the file first to match its table format.)

- [ ] **Step 2: Prove the foundations are untouched.**

```bash
git diff --stat main -- references/zitierweise.md references/methodik-buergerliches-recht.md
```
Expected: **empty** (no changes to either file).

- [ ] **Step 3: Full harness run.**

```bash
python3 tools/verify.py
```
Expected: `0 failures`; file/citation counts increased; smoke green; foundation sha256 pins intact.

- [ ] **Step 4: Commit.**

```bash
git add arbeitsrecht-beendigung/skills/anschluss-routing/SKILL.md
git commit -m "feat(routing): cross-link beendigung ↔ vertragsaenderung"
```

---

## Task 12: Adversarial legal review + fixes

**Files:**
- Modify: any skill / test-akte file flagged by review.

- [ ] **Step 1: Dispatch an adversarial reviewer subagent** (general-purpose) with this brief: "You are a senior Austrian Arbeitsrecht practitioner. Review every SKILL.md in `arbeitsrecht-vertragsaenderung/` and the test-akte for: (a) wrong/outdated §-numbers or Gesetz attributions; (b) German-law leakage not marked `(DE)`; (c) doctrinally wrong claims (esp. § 863/§ 879 ABGB, § 19c AZG, § 12 UrlG, § 26/§ 29 AngG, Änderungskündigung vs. einvernehmlich); (d) any Geschäftszahl that doesn't resolve in RIS. Return a list of MUST-FIX vs. MINOR with file:line and the correct statement." Provide the file paths.

- [ ] **Step 2: Verify each flagged GZ/§ live** before changing anything (`norm`, `leit`, `judikatur`); never accept a correction from model memory either.

- [ ] **Step 3: Fold in MUST-FIX items** (and MINOR where cheap). Re-run `python3 tools/verify.py` → `0 failures`.

- [ ] **Step 4: Commit.**

```bash
git add -A
git commit -m "fix(review): adversariale Rechts-Review eingearbeitet (vertragsaenderung)"
```

- [ ] **Step 5 (optional): Update project memory** — note the 5th vertical, new Gesetzesnummern (with verified numbers), and that foundations stayed frozen, in the memory file.

---

## Self-Review

**1. Spec coverage:**
- Scope/boundary (spec §1-2) → Task 2 (plugin description), Task 8 + Task 11 (bidirectional cross-link), README (Task 9). ✓
- 6-skill spine (spec §3) → Tasks 3-8, one per skill, anchors carried verbatim. ✓
- Anonymized test-akte + fuzzed figures + role-title/KV-Stufe scrub (spec §4) → Task 10 (steps 2-4, incl. grep gate). ✓
- New Gesetzesnummern AZG/AVRAG/DHG/PatG + EStG/EFZG conditional + KV-as-external-authority (spec §5) → Task 1 (register/verify) + Task 6 note (contrast-only) + Task 9 README grounding note. ✓
- Foundations frozen + adversarial review + verify.py green + marketplace entry (spec §6-7) → Task 11 (git diff proof, harness), Task 12 (review), Task 2 (marketplace). ✓
- Runtime triage questions (spec §9) → folded into `einstieg` (Task 3) and `aenderungsregime` (Task 4) Sofort-Triage rows. ✓

**2. Placeholder scan:** The only `<…>` placeholders are the *unknown Gesetzesnummern* (Task 1) and *live-verified Geschäftszahlen* — these are deliberately not invented, per the repo's quellenhygiene rule; each has an explicit verification step that produces the real value. No `TODO`/`TBD`/"add error handling"-style gaps.

**3. Type/name consistency:** Skill dir names (`einstieg-vertragsaenderung`, `aenderungsregime`, `klausel-inhaltskontrolle`, `deutsche-vorlage-audit`, `austritt-backstop-und-hebel`, `anschluss-routing`) are identical across the File Structure, the router targets in Task 3, and each skill's own task. Registry keys (`AZG`, `AVRAG`, `DHG`, `PATG`) are consistent between Task 1 and Tasks 5-6. Plugin name `arbeitsrecht-vertragsaenderung` consistent across Tasks 2, 9, 11, 12.
