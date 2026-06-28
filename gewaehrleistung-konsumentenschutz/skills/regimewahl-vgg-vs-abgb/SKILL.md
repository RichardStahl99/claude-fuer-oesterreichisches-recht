---
name: regimewahl-vgg-vs-abgb
description: "Kernkompetenz des Plugins: Bestimmt, ob auf einen Gewährleistungsfall das VGG (Verbrauchergeschäft über Waren/digitale Leistungen ab 1.1.2022) als lex specialis oder das allgemeine ABGB-Gewährleistungsrecht (§§ 922 ff) anzuwenden ist. Lex-specialis-Verdrängung, keine freie Parallelwahl. Österreich, kein deutsches Recht."
---

# Regimewahl: VGG oder §§ 922 ff ABGB

## Fachlicher Anker

- **Normen (über RIS prüfen):** § 1 VGG (Anwendungsbereich; Warenbegriff Abs 1 Z 1), § 2 VGG (Begriffsbestimmungen), §§ 11–13 VGG (Vermutung, Behelfe) — Gesetzesnummer 20011654; §§ 922 ff ABGB — Gesetzesnummer 10001622; § 1 KSchG (Unternehmer-/Verbraucherbegriff).
- **Quellenhygiene:** `references/quellenhygiene.md`, `references/zitierweise.md`. Keine GZ aus Modellwissen — `tools/ris_client.py`.
- **Methodik:** `references/methodik-buergerliches-recht.md`, Abschnitt 10 (Gewährleistung) und Abschnitt 5 (richtlinienkonforme Auslegung).

## Worum geht es?

Seit **1.1.2022** gilt für die Gewährleistung das **VGG** (Verbrauchergewährleistungsgesetz, Umsetzung der Warenkauf-RL 2019/771 und der Digitale-Inhalte-RL 2019/770). Es ist **lex specialis** und **verdrängt** für seinen Anwendungsbereich die §§ 922 ff ABGB. Es ist **keine freie Parallelwahl** — das anwendbare Regime ergibt sich zwingend aus Parteienstellung, Vertragsgegenstand und Vertragsdatum.

Diese Weiche steuert alles Weitere: Vermutungsfrist, Behelfshierarchie, Fristen. Wer hier falsch abbiegt, prüft den ganzen Fall nach dem falschen Gesetz.

## Wann brauchen Sie diese Skill?

- Immer am Anfang eines Gewährleistungs-Mandats zu Waren — vor `mangel-und-vermutung`, `behelfshierarchie`, `verjaehrung-und-fristen`.
- Wenn unklar ist, ob der Käufer Verbraucher (§ 1 KSchG) und der Verkäufer Unternehmer ist.
- Wenn der Vertrag um den Stichtag 1.1.2022 geschlossen wurde.

## Schritt-für-Schritt (Entscheidungsbaum)

1. **Vertragsdatum?** Vertrag **vor** 1.1.2022 geschlossen → **§§ 922 ff ABGB** (Altrecht), VGG scheidet aus. Ab 1.1.2022 → weiter.
2. **Parteienstellung?** Verkäufer **Unternehmer** und Käufer **Verbraucher** (§ 1 KSchG)? Nein (B2B, C2C, beide Verbraucher, beide Unternehmer) → **§§ 922 ff ABGB**. Ja → weiter.
3. **Vertragsgegenstand?** **Ware** (bewegliche körperliche Sache, § 1 Abs 1 Z 1 VGG) oder **digitale Leistung**? Liegenschaft, reine Dienstleistung außerhalb des VGG → **§§ 922 ff ABGB**. Ware/digitale Leistung → **VGG**.
4. **Ergebnis festhalten** und an die Folge-Skills durchreichen: Bei **VGG** gelten § 11 (Vermutung 1 Jahr) und §§ 12 f (Behelfe); bei **ABGB** §§ 924 (6 Monate), 932, 933.

```
Vertrag ab 1.1.2022 ? --nein--> §§ 922 ff ABGB
        | ja
Unternehmer -> Verbraucher (§1 KSchG) ? --nein--> §§ 922 ff ABGB
        | ja
Ware / digitale Leistung (§4 VGG) ? --nein--> §§ 922 ff ABGB
        | ja
      VGG  (lex specialis, §§ 11–13)
```

## Was die Wahl konkret ändert

| | VGG (B2C, ab 1.1.2022) | §§ 922 ff ABGB (Auffangregime) |
|---|---|---|
| Vermutung der Mangelhaftigkeit | **1 Jahr** (§ 11 VGG; dauernde Bereitstellung: gesamte Dauer) | **6 Monate** (§ 924 ABGB) |
| Behelfe | §§ 12 f VGG (Verbesserung/Austausch → Preisminderung/Vertragsauflösung) | § 932 ABGB (idem, eigene Voraussetzungen) |
| Gewährleistungsfrist | 2 J. + gesonderte 3-Monats-Verjährungsfrist (§ 10 VGG) | § 933: 2 J. beweglich / 3 J. unbeweglich |
| Zwingend zugunsten Verbraucher | ja (§ 3 VGG) | dispositiv, Grenze § 9 KSchG |

## Typische Fehler / Kritik

- **VGG übersehen und nach § 932 ABGB prüfen.** Häufigster Fehler bei B2C-Warenkäufen ab 2022. Reine ABGB-Judikatur zu § 932 betrifft überwiegend Altrecht und darf nicht unbesehen übertragen werden.
- **Falsche Vermutungsfrist.** Im VGG-Fall die 6-Monats-Frist des § 924 ABGB statt der **1-Jahres-Frist** des § 11 VGG ansetzen.
- **Stichtag ignorieren.** Verträge vor 1.1.2022 bleiben Altrecht.
- **Deutsches Recht.** Kein § 434/§ 437 BGB, kein „Nacherfüllung" — das ist deutsche Terminologie.
- **FAGG/KSchG-Rücktritt mit Gewährleistung vermengen.** Das fernabsatzrechtliche Rücktrittsrecht (FAGG) ist **kein** Gewährleistungsbehelf — gehört nicht in diese Prüfung.

## Quellen und Stand 06/2026

- §§ 1, 4, 11–13 VGG (RIS, Gesetzesnummer 20011654); §§ 922 ff ABGB (RIS, Gesetzesnummer 10001622); § 1 KSchG.
- Warenkauf-RL (EU) 2019/771; Digitale-Inhalte-RL (EU) 2019/770.
- `references/methodik-buergerliches-recht.md`. Stand: Juni 2026.

## Normen und Rechtsprechung

### Normen-Bibliothek (RIS-Permalinks verifizierbar)

- `§ 1 VGG` — Anwendungsbereich (Verbraucher/Unternehmer, Ware/digitale Leistung)
- `§ 2 VGG` — Begriffsbestimmungen (Warenbegriff)
- `§ 11 VGG` — Vermutung der Mangelhaftigkeit (1 Jahr)
- `§§ 12, 13 VGG` — Behelfshierarchie
- `§ 922 ABGB` — Mangelbegriff (Auffangregime)
- `§ 1 KSchG` — Unternehmer-/Verbraucherbegriff

### Judikatur (über RIS zu verifizieren — Leitsatz vor Verwendung lesen)

- VGG-Korpus ist noch jung (in Kraft seit 1.1.2022) und in RIS dünn — vorrangig am **Gesetzestext** und an den Materialien (ErläutRV zum GRUG) argumentieren, OGH-Judikatur live über `tools/ris_client.py judikatur "Verbrauchergewährleistung" --gericht OGH` prüfen.
- Altrechtliche OGH-Linien zu §§ 922 ff (Suchworte „Verbesserung Gewährleistung", „Wandlung Preisminderung") nur heranziehen, soweit das VGG die Wertung übernimmt — nicht ungeprüft übertragen.

### Anwendung im Skill

Regime zuerst, dann erst Mangel/Behelf/Frist. Das Ergebnis (VGG oder ABGB) ausdrücklich festhalten und an die Folge-Skills weitergeben.
