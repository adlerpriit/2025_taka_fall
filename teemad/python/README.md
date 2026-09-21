# Python ja andmetöötlus

Selle nädala jooksul õpid kirjutama lihtsat Pythoni koodi, töötlema tabelandmeid ja koostama graafikuid. Kasutad kolme Jupyteri töövihikut (*notebook*). Töövihikus on selgitused, käivitatavad näited ja harjutused.

| Järjekord | Töövihik | Põhiosa tulemus | Iseseisev töö |
| --- | --- | --- | ---: |
| 1 | [Pythoni alused](Intro.ipynb) | Muutujad, tingimused, tsükkel, funktsioon ja lihtsa vea parandamine | 110 min |
| 2 | [Tabelandmed Pandasega](Pandas.ipynb) | Andmete kontroll, filtreerimine ja rühmade kokkuvõte | 70 min |
| 3 | [Graafikud Seaborniga](Seaborn.ipynb) | Graafiku valimine, kujundamine ja selgitamine | 45 min |

Lisaks arvesta 15 minutit alustamiseks, 60 minutit lõpuülesande lõpetamiseks ja 45 minutit kordamiseks. Kokku on see **5 tundi 45 minutit iseseisvat tööd**, millele lisandub seminar. Videote vaatamine kuulub sama aja sisse. Videod lisanduvad hiljem; praegu saad läbida kõik osad töövihikute abil.

Ajad on hinnangulised. **Lisamaterjal** on valikuline ega ole põhiosa ülesannete eelduseks. Kui teema on tuttav, alusta harjutusest ja pöördu vajaduse korral selgituste juurde tagasi.

## Alustamise enesekontroll

Proovi enne näidete lugemist vastata. See ei ole hindeline test.

- Kas oskad käivitada koodilahtri ja lisada tekstilahtri? Kui ei, alusta Intro peatükist I1.
- Mida teeb `vanus = vanus + 1`? Kui vastus pole selge, loe I2.
- Kas oskad listist valida esimese väärtuse ja sõnastikust väärtuse võtme järgi? Korda I3.
- Kas oskad leida listist tingimusele vastavad arvud? Korda I4–I5.
- Mille poolest erinevad `print()` ja `return`? Korda I6.
- Kas oskad veateatest leida vea tüübi ja vigase rea? Korda I7.

## Ava töövihik Colabis

Colab võimaldab Pythonit kasutada veebibrauseris. Vajad Google'i kontot; eraldi Pythonit paigaldada ei ole vaja.

1. Ava töövihik ja vajuta selle alguses **Open in Colab**. Kui link ei avane, laadi `.ipynb` fail GitHubist alla ja ava see [Colabis](https://colab.research.google.com/) valikuga **File → Upload notebook**.
2. Vali **File → Save a copy in Drive**, et töötada oma koopias. Algne kursusefail ei muutu.
3. Käivita esimene koodilahter. Ühendumiseks piisab tavalisest CPU-keskkonnast.
4. Pandase ja Seaborni esimene lahter loeb andmed kursuse repo veebiaadressilt, kui kohalikku faili ei leidu. Lahter näitab kasutatud allikat. Veebist lugemine vajab internetiühendust.
5. Töö lõpetamisel vali **File → Download → Download .ipynb** ja lisa fail oma kursuserepos õigesse kausta. Drive'i salvestamine üksi ei uuenda GitHubi repot.

Colabi käivituskeskkond on ajutine: sinna loodud failid võivad ühenduse lõppedes kaduda. Laadi vajalikud CSV- ja pildifailid vasakpoolsest failivaatest alla. Töövihiku tekst ja kood säilivad sinu salvestatud koopias.

## Kohalik alternatiiv: Jupyter või VS Code

Kasuta Python 3.12. Teekide kontrollitud versioonid on failis [requirements.txt](requirements.txt). Kopeeri oma reposse **kogu `teemad/python` kaust ning `data/Islander_data.csv` ja `data/README.md`**, säilitades kaustade paigutuse:

```text
minu-repo/
  data/
    Islander_data.csv
    README.md
  teemad/
    python/
      README.md
      Intro.ipynb
      Pandas.ipynb
      Seaborn.ipynb
      requirements.txt
      lahendused/
```

Tee kopeerimise järel commit. Nii saad hiljem oma lahendusi algse materjaliga võrrelda.

Liigu terminalis oma repo kausta `teemad/python`. Linuxis ja macOS-is:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyterlab
```

Windowsi PowerShellis saab kasutada keskkonna Pythoni täisteed ilma aktiveerimata:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyterlab
```

JupyterLabis ava `Intro.ipynb`. VS Code'is paigalda laiendused **Python** ja **Jupyter**, ava sama fail ning vali **Select Kernel → Python Environments → .venv**. Veendu, et valitud kernel kasutab keskkonda, kuhu teegid paigaldasid.

Vihikud leiavad andmed nii repo juurkaustast kui ka kaustast `teemad/python` käivitades. Näidete loodud failid lähevad käivitamise töökataloogi kausta `valjund`; iga salvestusnäide näitab faili asukohta.

## Kuidas harjutada

Ennusta enne käivitamist, mida näide väljastab. Seejärel käivita see, muuda üht väärtust ja selgita erinevust. Kirjuta harjutuse kood tühja koodilahtrisse ja põhjendus sellele järgnevasse tekstilahtrisse. Lahtrid jagavad ühe vihiku piires muutujate seisu; eri vihikute vahel muutujad üle ei kandu.

Täislahendused asuvad eraldi:

- [Intro vastused](lahendused/Intro_vastused.md)
- [Pandase lahenduskäigud](lahendused/Pandas_lahendused.md)
- [Seaborni lahenduskäigud ja lõpuülesande näide](lahendused/Seaborn_lahendused.md)

Proovi esmalt ise ja kasuta vihikus olevat vihjet või kontrollküsimust. Seejärel võrdle oma lahendust näitega. Sama tulemuseni võib jõuda mitmel viisil.

## Kui tekib viga

| Olukord | Mida kontrollida |
| --- | --- |
| `NameError` | Kas muutuja nimi on õige ja selle loonud lahter käivitatud? |
| `ModuleNotFoundError` | Kas teek on paigaldatud valitud kerneli keskkonda? |
| `FileNotFoundError` või andmete laadimise võrguviga | Vaata väljastatud allikat. Kohalik fail peab asuma repo `data` kaustas; veebiallikas vajab internetti. |
| Tulemus muutub lahtri korduskäivitusel | Kas lahter suurendab muutujat või lisab olemasolevasse kogumisse väärtusi? Taasta algseis. |
| Arvutus ei lõpe | Katkesta täitmine nupuga **Stop/Interrupt**. Kontrolli tsükli lõpetamise tingimust. |

Enne töö salvestamist taaskäivita kernel ja käivita kõik lahtrid: JupyterLabis **Kernel → Restart Kernel and Run All Cells**, Colabis **Runtime → Restart session and run all**. VS Code'is kasuta **Restart** ja seejärel **Run All**. Menüü sõnastus võib versiooniti veidi erineda.

## Töö salvestamine oma reposse

Salvesta kolm täidetud töövihikut. L-01 vastus jääb Seaborni vihikusse; lisa ka ülesandes salvestatud kokkuvõttetabel ja graafik. Vaata muudatused enne commiti üle käsuga `git status`. Lisa ainult soovitud failid, mitte virtuaalkeskkond või muud ajutised failid.

Kontrolli, et iga põhiosa harjutuse juures on sinu vastus, lõpuülesanne käivitub ülalt alla ning järeldus vastab tabelile ja graafikule. Tee oma töö kohta arusaadava sõnumiga commit ja saada muudatused oma GitHubi reposse.
