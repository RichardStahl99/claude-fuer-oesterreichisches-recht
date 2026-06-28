# Mietzins (MRG) — Werkstatt

> Ausführliche Fassung für die Arbeit im Plugin. Ergänzt die Skills unter `skills/` und die geteilten `references/`. Österreichisches Recht; jede Fundstelle und jeder Richtwert über RIS (`tools/ris_client.py`) verifizieren.

## Zweck und Abgrenzung

Zweite **Pilot-Vertikale** des Repositorys: **Mietzins nach dem MRG**. Headline-Kompetenz ist die **Anwendungsbereichs-Weiche** (§ 1 MRG) — strukturell parallel zur Regimewahl des Gewährleistungs-Plugins.

**Nicht abgedeckt** (nur verweisen): Kündigung/Beendigung (§§ 29 ff MRG), Betriebskosten (§§ 21 ff), Eintritts-/Abtretungsrechte, Untermiete, Geschäftsraummiete im Detail, Wohnungseigentum (WEG), Bestandrecht außerhalb des MRG (§§ 1090 ff ABGB).

## Pipeline der Skills

```
einstieg-mietzins                  (Triage-Dashboard)
        |
        v
anwendungsbereich-mrg              (Voll-/Teil-/Vollausnahme?  -> entscheidet, ob Mietzins beschränkt)
        |
        v   (nur bei Vollanwendung)
mietzinsbildung                    (Richtwert/Kategorie/angemessen + Zuschläge - 25% Befristung)
        |
        v
mietzinsueberpruefung             (Überschreitung -> Teilnichtigkeit § 16 Abs 8 -> Rückforderung -> Frist)
        |
        v
verfahren-schlichtung-ausserstreit (§ 37/§ 39/§ 40 MRG: Schlichtungsstelle -> BG)

anschluss-routing                  (Router)
```

## Drei Merkpunkte (häufige Fehlerorte)

1. **Anwendungsbereich entscheidet alles.** Frei finanzierter **Neubau (Baubewilligung nach 30. 6. 1953)** ist **Teilanwendung** → freier Mietzins, kein Richtwert. Ein-/Zweifamilienhaus ist **Vollausnahme** → nur ABGB.
2. **Lagezuschlag** nur bei überdurchschnittlicher Lage **und** schriftlicher Bekanntgabe (§ 16 Abs 4) — sonst unwirksam. **Befristungsabschlag −25 %** nicht vergessen.
3. **Verfahren ist Außerstreit**, in Wien u. a. mit vorgeschalteter **Schlichtungsstelle** und 4-Wochen-Frist zum Abziehen (§ 40 MRG).

## Quellenanbindung (verpflichtend)

- Normen über RIS-Permalink: `python3 tools/ris_client.py norm MRG 16` bzw. `norm RICHTWG 5`.
- Judikatur live: `python3 tools/ris_client.py judikatur "Richtwert Zuschlag" --gericht OGH` (Wohnrecht = **5. Senat**).
- **Aktuelle Richtwerte** (je Bundesland, valorisiert) stets live beziehen — **nie** aus Modellwissen beziffern.
- Keine GZ/RS-Nummer aus Modellwissen (`references/ris-quellen.md`).

## Architektur (Phase-3-Beweis)

Dieses Plugin nutzt `references/zitierweise.md` und `references/methodik-buergerliches-recht.md` **unverändert**. Erweitert wurde nur `tools/ris_client.py` um die verifizierten Gesetzesnummern MRG (10002531) und RichtWG (10003166) — der dokumentierte Erweiterungspunkt. Motor und Rechtsschicht bleiben getrennt.

## Verifikation

Regressionsfall `testakten/altbau-richtwert-ueberschreitung/`: muss Vollanwendung korrekt erkennen und ausschließlich RIS-auflösbare Fundstellen liefern. Vor jeder Änderung gegenprüfen.

## Berufsrechtlicher Rahmen

§ 9 RAO (Verschwiegenheit), DSGVO/DSG: Mandantendaten nur in rechtskonformer Umgebung. Output ist anwaltliche Vorbereitung, nie Entscheidung.
