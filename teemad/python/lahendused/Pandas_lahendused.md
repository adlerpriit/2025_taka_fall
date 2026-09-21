# Pandase lahenduskäigud

Proovi esmalt [Pandase vihiku](../Pandas.ipynb) harjutusi. Käivita allolev ettevalmistus üks kord oma töövihikus. Seejärel on iga ülesande kood eraldi käivitatav: see kasutab muutmata tabelit `algandmed`. Tööta repo juurkaustas või kaustas `teemad/python`, nagu alustamisjuhendis.

## Ettevalmistus

```python
from pathlib import Path
import pandas as pd
from IPython.display import display

andmefail = Path("data/Islander_data.csv")
if not andmefail.is_file():
    andmefail = Path("../../data/Islander_data.csv")
if andmefail.is_file():
    allikas = andmefail
else:
    allikas = "https://raw.githubusercontent.com/adlerpriit/2025_taka_fall/37b50eb8474faeeb0993c2d4883680bee0560cbd/data/Islander_data.csv"
print("Andmete allikas:", allikas)
algandmed = pd.read_csv(allikas)
```

## P-01

Alusta tabeli mõõtmetest, päisest ja andmetüüpidest. Vanus ja skoorid on arvulised. Ravimirühm ja mälestuste rühm sobivad rühmitamiseks; ka arvuline annusetase võib olla rühmitamistunnus.

```python
display(algandmed.head(8))
print(algandmed.shape)
algandmed.info()
assert algandmed.shape == (198, 9)
```

Failis on 198 rida ja 9 veergu. `Drug` tähendab ravimirühma, `Dosage` annusetaset. Pelgalt andmetüübist ei selgu, mida tunnus mõõdab; selleks loe andmekirjeldust.

## P-02

Moodusta mõlema valiku jaoks kaks tingimust. Ühenda need `&` abil. Sorteerimine muudab ridade järjekorda, mitte nende arvu.

```python
durand = algandmed.loc[
    (algandmed["age"] > 30) & (algandmed["last_name"] == "Durand")
]
ravim_a3 = algandmed.loc[
    (algandmed["Drug"] == "A") & (algandmed["Dosage"] == 3)
].sort_values("Diff", ascending=False)
print("Durand, vanus üle 30:", len(durand))
print("Ravim A, annusetase 3:", len(ravim_a3))
display(ravim_a3.head())
assert len(durand) == 31
assert len(ravim_a3) == 22
assert durand["age"].gt(30).all()
assert durand["last_name"].eq("Durand").all()
assert ravim_a3["Diff"].is_monotonic_decreasing
```

Esimeses valikus on 31, teises 22 rida. `.gt(30)` on samaväärne võrdlusega `> 30`, `.eq(...)` võrdlusega `==`. `.all()` kontrollib, et tingimus kehtib kõigi valitud ridade kohta. Viimane atribuut kontrollib kahanevat järjekorda.

Levinud eksimused on `>= 30` kasutamine, kuigi ülesanne nõuab vanust üle 30, ning veeru `Diff` kirjutamine väikese algustähega.

## P-03

Lisa veerg töökoopiale. Võrdlus tagastab iga rea kohta tõeväärtuse ja `.sum()` loendab tõeseid väärtusi.

```python
minu_andmed = algandmed.copy()
minu_andmed["muutus_vahemalt_10"] = minu_andmed["Diff"] >= 10
print("Muutus vähemalt 10:", minu_andmed["muutus_vahemalt_10"].sum())
print("Puuduvaid muutusi:", minu_andmed["Diff"].isna().sum())
assert minu_andmed["muutus_vahemalt_10"].sum() == 36
assert minu_andmed["Diff"].isna().sum() == 0
```

Tingimusele vastab 36 kirjet. `Diff`-väärtusi ei puudu. `False` tähendab selles andmestikus, et teadaolev muutus jääb alla 10; puuduv väärtus tähendaks teadmata muutust. Puuduvate andmetega uues tabelis tuleb puuduvust eraldi kontrollida, sest võrdlus ei pruugi puuduvat väärtust eraldi rühmana säilitada.

## P-04

Rühmita annusetaseme järgi ja arvuta iga rühma keskmine muutus koos ridade arvuga. Suurima keskmise leidmiseks sorteeri kokkuvõtet.

```python
annused = algandmed.groupby("Dosage").agg(
    keskmine_muutus=("Diff", "mean"),
    ridu=("Diff", "size"),
).reset_index()
display(annused.round(2))
display(annused.sort_values("keskmine_muutus", ascending=False).head(1))
assert annused["ridu"].sum() == len(algandmed)
assert annused["ridu"].tolist() == [67, 66, 65]
```

| Annusetase | Keskmine muutus | Ridu |
| --- | ---: | ---: |
| 1 | 0,48 | 67 |
| 2 | 2,09 | 66 |
| 3 | 6,38 | 65 |

Suurim keskmine muutus on annusetasemel 3. Iga tabelirida koondab ühe annusetaseme kirjed kõigist ravimirühmadest. Rühmade erinevus ei tõesta üksi põhjuslikku mõju: arvestada tuleb katse korraldust, rühmade koosseisu ja tulemuste hajuvust. Annusetaseme number ei tähista kõigi ravimite puhul sama kogust milligrammides.

## P-05

1. `.shape` on atribuut, mis annab ridade ja veergude arvu. `.head()` on meetod, mis kuvab tabeli esimesi ridu. Sulud eristavad siin meetodi väljakutset atribuudi lugemisest.
2. `size` loendab kõiki rühma ridu. `count` loendab valitud veeru mittepuuduvaid väärtusi. Puuduva skooriga rida suurendab esimest, kuid mitte teist arvu.
3. Sulud rühmitavad kummagi võrdluse. `&` ühendab seejärel kaks tõeväärtusveergu rea kaupa. Ilma sulgudeta võib tehete järjekord anda teistsuguse avaldise või vea; Pythoni `and` ei sobi tervete veergude ühendamiseks.

## P-L1 — lisamaterjal

Vastavustabelis peab iga kood esinema üks kord. `many_to_one` kontrollib seda tingimust liitmisel. Kontrolli ka, et ühtegi vastet ei jäänud leidmata.

```python
malestuste_nimed = pd.DataFrame({
    "Happy_Sad_group": ["H", "S"],
    "malestused": ["Rõõmsad", "Kurvad"],
})
nimedega = algandmed.merge(
    malestuste_nimed, on="Happy_Sad_group", how="left", validate="many_to_one"
)
display(nimedega.head())
assert len(nimedega) == len(algandmed)
assert nimedega["malestused"].notna().all()
```

`.notna()` kontrollib olemasolevaid väärtusi ja `.all()` nõuab, et tingimus kehtiks igal real. Liitmist tasub nii kontrollida ka siis, kui tabel paistab esmapilgul õige.

## P-L2 — lisamaterjal

Lisa lähterea tunnus enne ümberkujundamist. Säilita see ja mälestuste rühm ning tõsta kaks mõõtmist ühte väärtuseveergu.

```python
lai = algandmed.copy()
lai["rea_id"] = range(len(lai))
pikk = lai.melt(
    id_vars=["rea_id", "Happy_Sad_group"],
    value_vars=["Mem_Score_Before", "Mem_Score_After"],
    var_name="mootmine",
    value_name="skoor",
)
display(pikk.head())
assert len(pikk) == 396
assert pikk.groupby("rea_id").size().eq(2).all()
assert not pikk.duplicated(["rea_id", "mootmine"]).any()
```

Tulemuses on 396 rida. Üks rida tähistab nüüd ühe lähterea üht mõõtmist. Viimane kontroll välistab sama lähterea ja mõõtmise kombinatsiooni kordumise. `Diff` jääb välja, sest see on kahe mõõtmise vahe, mitte kolmas ajahetk.

## P-L3 — lisamaterjal

Piirid on parempoolselt suletud: 35 kuulub esimesse ja 36 teise rühma. Samal põhimõttel kuuluvad 50 teise ning 65 kolmandasse rühma.

```python
kontrollvanused = pd.Series([24, 35, 36, 50, 51, 65, 66, 83], name="vanus")
ruhmad = pd.cut(
    kontrollvanused,
    bins=[0, 35, 50, 65, float("inf")],
    labels=["kuni 35", "36–50", "51–65", "66+"],
    right=True,
    include_lowest=True,
)
display(pd.DataFrame({"vanus": kontrollvanused, "ruhm": ruhmad}))
assert ruhmad.notna().all()
assert list(ruhmad) == ["kuni 35", "kuni 35", "36–50", "36–50", "51–65", "51–65", "66+", "66+"]
```

Silt „25–35” oleks selles näites eksitav, sest esimesse rühma kuulub ka 24-aastane. Sildid peavad kirjeldama tegelikke vahemikke. Need sildid eeldavad, et vanus on antud täisaastates.
