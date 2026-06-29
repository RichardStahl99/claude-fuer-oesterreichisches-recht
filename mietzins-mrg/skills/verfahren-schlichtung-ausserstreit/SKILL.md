---
name: verfahren-schlichtung-ausserstreit
description: "Bestimmt den richtigen Verfahrensweg für Mietrechtssachen nach § 37 MRG: Außerstreitverfahren vor dem Bezirksgericht, mit vorgeschalteter (sukzessiver) Zuständigkeit der Schlichtungsstelle in Gemeinden, die eine eingerichtet haben (Wien u. a.). Kein streitiges Verfahren, kein deutsches Recht."
---

# Verfahren: Schlichtungsstelle und Außerstreit (§ 37 MRG)

## Fachlicher Anker

- **Normen (über RIS prüfen):** § 37 MRG (Außerstreitverfahren in Mietrechtssachen, Zuständigkeit BG), § 39 MRG (Schlichtungsstelle, sukzessive Zuständigkeit), § 40 MRG (Abziehen an das Gericht) — GNR 10002531; AußStrG (ergänzend).
- **Vorgelagert:** materielle Skills (`mietzinsueberpruefung` etc.) müssen die Sachfrage geklärt haben.
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`.

## Worum geht es?

Mietrechtssachen — darunter die **Überprüfung des Hauptmietzinses** — werden **nicht** im streitigen Zivilprozess, sondern im **Außerstreitverfahren** entschieden (§ 37 MRG). In manchen Gemeinden ist zwingend zuerst die **Schlichtungsstelle** anzurufen. Das ist eine der markantesten Abweichungen vom deutschen Mietprozess.

## Schritt-für-Schritt

1. **Ist es eine Mietrechtssache iSd § 37 Abs 1 MRG?** Der Katalog ist **taxativ** (u. a. Angemessenheit/Höhe des Hauptmietzinses, Betriebskosten, Erhaltung, Kaution). Wenn ja → **Außerstreitverfahren**. Wenn nein → streitiges Verfahren (z. B. reine Räumungsklage außerhalb § 37).
2. **Schlichtungsstelle vorhanden?**
   - Gemeinde **mit** Schlichtungsstelle (insb. **Wien**, Graz, einige weitere): Der Antrag ist **zuerst bei der Schlichtungsstelle** einzubringen (§ 39 MRG, **sukzessive Zuständigkeit**). Das Gericht darf erst nach Abschluss/„Abziehen" angerufen werden.
   - Gemeinde **ohne** Schlichtungsstelle: **direkt** zum **Bezirksgericht** (§ 37 Abs 1 MRG; Direktweg mangels betrauter Gemeinde aus § 39 Abs 1 e contrario), in dessen Sprengel der Mietgegenstand liegt.
3. **„Abziehen" an das Gericht (§ 40 MRG):** Nach der Entscheidung der Schlichtungsstelle kann jede Partei die Sache binnen **vier Wochen** ab Zustellung **bei Gericht** anhängig machen; damit tritt die Entscheidung der Schlichtungsstelle außer Kraft und das BG entscheidet neu.
4. **Vertretung/Form:** Im wohnrechtlichen Außerstreitverfahren vor dem BG besteht **keine absolute Anwaltspflicht** (Parteien können selbst auftreten); anwaltliche Vertretung ist dennoch üblich. ERV für Anwälte beachten.

```
Mietrechtssache § 37 Abs 1 MRG ? --nein--> streitiges Verfahren
        | ja  -> AUSSERSTREIT
Schlichtungsstelle in der Gemeinde ? --nein--> direkt BG (§ 37 Abs 1)
        | ja
zuerst Schlichtungsstelle (§ 39) --Entscheidung--> ggf. binnen 4 Wo. an BG abziehen (§ 40)
```

## Typische Fehler / Kritik

- **Streitiges Verfahren statt Außerstreit** wählen → Zurückweisung.
- **Schlichtungsstelle übergehen** (in Wien u. a.) → Unzulässigkeit des direkten Gerichtswegs.
- **4-Wochen-Frist** zum Abziehen (§ 40 MRG) versäumen → Schlichtungsstellen-Entscheidung wird wirksam.
- **Deutsches Recht:** kein Amtsgericht-Mietprozess, keine „Mietsache" der streitigen ZPO — in Österreich Außerstreit + ggf. Schlichtungsstelle.

## Quellen und Stand 06/2026

- §§ 37, 39, 40 MRG (RIS, GNR 10002531); AußStrG.
- `references/methodik-buergerliches-recht.md` Abschnitt 12 (Verfahren/Fristen). Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)
- `§ 37 MRG` — Außerstreitverfahren/Zuständigkeit BG · `§ 39 MRG` — Schlichtungsstelle · `§ 40 MRG` — Abziehen an das Gericht

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen; 5. Senat)
**Zur Laufzeit ausführen (nicht nur verweisen):**
- Sukzessive Zuständigkeit/Abziehen: `python3 tools/ris_client.py linie "Schlichtungsstelle Zuständigkeit" --gericht OGH --gesetz MRG --paragraf 39` — die gelieferten 5-Ob-Leitsätze verwenden, keine GZ behaupten.
- Für eine konkret benannte Geschäftszahl `leit <GZ>` (Leitentscheidung/Stamm? wie tief die Linie?); vor dem Stützen auf eine ältere Entscheidung `aktualitaet MRG 37 --seit <Entscheidungsdatum>` (flaggt eine Novellierung nach dem Entscheidungsdatum).

### Anwendung im Skill
Zuerst Außerstreit-Qualifikation (§ 37 Abs 1 taxativ), dann Schlichtungsstelle-vorhanden-Prüfung, dann Fristen (4 Wochen Abziehen) sichern.
