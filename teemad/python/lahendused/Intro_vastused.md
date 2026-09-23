# Intro vastused

Proovi [Intro harjutused](../Intro.ipynb) enne ise lahendada. Allpool on üks võimalik lahendus. Iga koodiplokk on eraldi käivitatav; võid selle kopeerida oma töövihiku uude lahtrisse. Võrdle nii tulemust kui ka lahenduskäiku.

## I-01

Omista hind ja kogus ning arvuta korrutis. Hoia algväärtuste omistamine samas lahtris: siis ei sõltu tulemus varasemast käivitusest.

```python
# Algväärtuste määramine ja kogumaksumuse arvutamine.
hind = 12.50
kogus = 2
kogumaksumus = hind * kogus

# Tulemuse vormindamine f-sõnega.
print(f"Raamatud maksavad {kogumaksumus:.2f} eurot.")

# Tulemuse kontrollimine.
assert kogumaksumus == 25
```

Kahe raamatu hind on 25 eurot, nelja raamatu hind 50 eurot. Muutmata lahtri korduskäivitus annab sama tulemuse. Levinud eksimus on hinna kirjutamine `12,50`: Pythoni kümnendmärk on punkt.

## I-02

Indeks `0` valib esimese, `-1` viimase elemendi. `[:2]` valib kaks esimest elementi: valik algab listi algusest ja lõpeb enne indeksit 2. Sõnastikust leiad listi võtme järgi.

```python
# Listi elementide valimine indeksiga.
temperatuurid = [-3, 2, 5, 1]
print(temperatuurid[0])
print(temperatuurid[-1])

# Lõik: kaks esimest elementi eraldi listina.
print(temperatuurid[:2])

# Sõnastik: kohanimi ja temperatuuride list.
ilm = {"koht": "Tartu", "temperatuurid": temperatuurid}
print(ilm)

# Sõnastikust saadud listi pikkuse kontrollimine.
assert len(ilm["temperatuurid"]) == 4
```

Esimene väärtus on −3 ja viimane 1. Kahest esimesest elemendist saad listi `[-3, 2]`. `ilm["temperatuurid"]` kasutab sõnastiku võtit; `temperatuurid[0]` listi indeksit.

## I-03

Piirväärtus kuulub arvestatud tulemuste hulka, mistõttu on tingimus `>= 50`.

```python
punktid = 50
if punktid >= 50:
    tulemus = "arvestatud"
else:
    tulemus = "arvestamata"
print(tulemus)
```

Väärtus 49 peab andma „arvestamata”, 50 ja 51 „arvestatud”. Kontrolli neid ükshaaval, muutes esimest rida. Ainult `>` kasutamine jätaks täpselt 50 punkti valesse harusse.

## I-04

Tsüklis lisad summale ainult positiivsed arvud. Summa algväärtus tuleb määrata enne tsüklit, mitte selle sees.

```python
# Listi ja summa algväärtuse määramine.
arvud = [3, -2, 0, 5, -1]
summa = 0

# Tsükkel ja tingimus: liida summale ainult positiivsed arvud.
for arv in arvud:
    if arv > 0:
        summa = summa + arv
print(summa)

# Arvutatud summa kontrollimine.
assert summa == 8
```

Positiivsed liikmed on 3 ja 5. Kui listis on ainult nullid ja negatiivsed arvud, jääb summa nulliks. Kui lähtestad summa tsükli sees, kaovad varasemate sammude tulemused.

Juhtlausete näites kuvatakse `4`, `5` ja „Lugemine lõppes.”. Kui asendad `break`-lause `continue`-lausega, jääb `STOP` vahele, kuid järgmisel sammul kuvatakse ka `9`. Tsükkel ei lõpe enam märgusõna juures.

## I-05

Funktsioon peab kasutama parameetrina saadud listi. Tagasta summa pärast tsüklit; tsükli sees olev `return` lõpetaks funktsiooni liiga vara.

```python
# Funktsiooni defineerimine ja summa tagastamine.
def positiivsete_summa(arvud):
    summa = 0
    for arv in arvud:
        if arv > 0:
            summa = summa + arv
    return summa

# Tulemuse kontrollimine eri sisenditega.
assert positiivsete_summa([3, -2, 0, 5]) == 8
assert positiivsete_summa([]) == 0
assert positiivsete_summa([-4, 0, -1]) == 0
assert positiivsete_summa([2]) == 2

# Tagastatud väärtuse kasutamine järgmises arvutuses.
tulemus = positiivsete_summa([3, -2, 0, 5])
print(tulemus * 2)
```

Viimane rida kuvab 16. Tühja listi korral tsükli keha ei käivitu ja tagastatakse algväärtus 0. `print(summa)` ilma `return`-ita kuvaks küll arvu, kuid funktsiooni tagastusväärtus oleks `None`.

## I-06

```python
kogus = 3
print(kogus * 2)
```

Vigases näites oli nimi `koguss`, mida polnud loodud. See tekitaks `NameError`-i. Veateate viimaselt realt leiad tundmatu nime ja eelnevatelt ridadelt vea asukoha. Parandatud kood kuvab 6. Kuna omistus on samas lahtris, pole vaja varasemat muutujaseisu.

Loogikavea paljastab üheelemendiline list `[4]` koos piiriga 4. Tingimus `>` jätaks selle ainsa väärtuse välja. Õige võrdlus on `>=`:

```python
# Õige funktsioon koos piirväärtust kontrolliva näitega.
def mootmiste_kokkuvote(arvud, alampiir=0):
    valitud = []
    for arv in arvud:
        if arv >= alampiir:
            valitud.append(arv)
    return len(valitud), sum(valitud)

assert mootmiste_kokkuvote([4], alampiir=4) == (1, 4)
```

Kui asendad selles funktsioonis `>=` märgiga `>`, tagastab funktsioon `(0, 0)` ja kontroll tekitab `AssertionError`-i.

## I-07

1. Õige on **B: 1–4**. `range` jätab lõppväärtuse välja.
2. Ilma täidetud `return`-lauseta on tagastusväärtus **`None`**. Ekraanile kuvatud tekst ja tagastusväärtus on eri asjad.
3. Lugemiseks peab fail juba olemas olema. Näide loob selle režiimiga `"w"`, mis kirjutab varasema sisu üle. Kogu näite korduskäivitus annab seetõttu sama failisisu. Ainult `"a"`-režiimiga osa kordamine lisaks samad read veel kord faili lõppu.

```python
# range: lõppväärtus ei kuulu jadasse.
print(list(range(1, 5)))

# print ja return: teksti kuvav funktsioon ei tagasta seda teksti.
def kuva_tervitus():
    print("Tere!")

# Tagastusväärtuse kuvamine ja kontrollimine.
tulemus = kuva_tervitus()
print(tulemus)
assert tulemus is None
```

`is None` kontrollib, kas tulemus on väärtuse puudumist tähistav objekt. Arvude ja sõnede väärtuste võrdlemisel kasuta tavaliselt `==`.

## I-08

Salvesta [näidisskriptist](../naited/mootmiste_kokkuvote.py) oma koopia. Muuda `main()`-is kokkuvõttefunktsiooni väljakutseks `arv, summa = mootmiste_kokkuvote(arvud, alampiir=4)`. Funktsiooni enda vaikeväärtust ega võrdlust pole vaja muuta.

Käivita terminalis `python mootmiste_kokkuvote.py` kaustas, kus asub sisendfaili sisaldav `valjund` kaust. Vaata iga katse järel faili `valjund/kokkuvote.txt`.

| Sisendfail | Arv | Summa | Selgitus |
| --- | --- | --- | --- |
| Vihiku näidisfail | 2 | 9.0 | Piirile vastavad 4 ja 5; vigase neljanda rea kohta kuvatakse teade |
| Tühi fail | 0 | 0 | Lugemistsükkel ei käivitu, kokkuvõte saab tühja listi |
| Ainult `puudub` | 0 | 0 | Teisendamine annab `ValueError`-i; esimene rida jäetakse koos teatega vahele |

Vigane rida ei muutu nulliks ega lähe mõõtmiste arvu hulka. Tühi rida jäetakse vahele ilma veateateta. Kui soovid katsetada sama sisendit uuesti, taasta näidisfail vihiku faili loomise lahtriga. Skripti `main()` käivitab lugemise, arvutamise ja salvestamise; nende funktsioonide defineerimine üksi töötlust ei käivita.

## I-L01 — lisamaterjal

Ümbermõõt on kaks laiust ja kaks kõrgust. Meetod kasutab objekti atribuute `self.laius` ja `self.korgus`.

```python
# Klass: atribuudid ja pindala ning ümbermõõdu meetodid.
class Ristkulik:
    def __init__(self, laius, korgus):
        self.laius = laius
        self.korgus = korgus

    def pindala(self):
        return self.laius * self.korgus

    def umbermoot(self):
        return 2 * (self.laius + self.korgus)

# Objekti loomine ja ümbermõõdu meetodi kutsumine.
kujund = Ristkulik(3, 4)
print(kujund.umbermoot())

# Tulemuse kontroll ristküliku ja ruuduga.
assert kujund.umbermoot() == 14
assert Ristkulik(2, 2).umbermoot() == 8
```

See lihtne klass eeldab mittenegatiivseid küljepikkusi. Meetodi väljakutse on `kujund.umbermoot()`; sulgudeta saaksid meetodi enda, mitte arvutatud ümbermõõdu.
