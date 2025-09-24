# Sissejuhatus Bash-i

## Alustamine: Kuidas avada Bash terminal

Bash (Bourne Again SHell) on populaarne käsurea shell, millega saab arvutiga suhelda tekstikäskude kaudu. Enne kui hakkame Bash-i käske õppima, seadistame esmalt oma töökeskkonna.

### Windows

Enamikul Windowsi arvutitel ei ole Bash vaikimisi olemas. Lihtsaim viis alustamiseks on paigaldada **Git Bash**:

- Laadi alla ja paigalda [Git for Windows](https://git-scm.com/download/win).
- Pärast paigaldamist otsi Start menüüst "Git Bash" ja ava see.

### Mac

MacOS-is on olemas terminali rakendus, kuid alates macOS Catalina (10.15) versioonist on vaikimisi shell **zsh** (Z shell), mitte Bash. Bash-i saab siiski kasutada:

- Ava **Terminal** (otsi Spotlightist "Terminal").
- Bash-i ajutiseks kasutamiseks kirjuta:  
  ```{bash}
  bash
  ```

### Linux

Enamikul Linuxi distributsioonidel on Bash vaikimisi shell. Ava terminali rakendus (sageli nimega "Terminal", "Konsole", "xterm" jne) ja tõenäoliselt kasutad Bash-i. Kui mitte, saad selle paigaldada paketihalduriga (nt `sudo apt install bash`).

### Teised populaarsed shellid

- **zsh**: Vaikimisi shell uuematel MacOS versioonidel, pakub rohkem võimalusi ja kohandamist.
- **fish**: Sõbralik interaktiivne shell, tuntud kasutajasõbralikkuse poolest.
- **PowerShell**: Vaikimisi shell Windowsis, mõeldud süsteemi haldamiseks.

Bash on endiselt kõige laialdasemalt kasutatav shell skriptimiseks ja õpetamiseks.

---

## Käsurea liides (CLI) vs graafiline kasutajaliides (GUI)

### CLI

**Käsurea liides (CLI)** võimaldab arvutiga suhelda käskude kirjutamise kaudu. Näed käsurea märki, kirjutad käsu ja näed tulemusi tekstina.

**Eelised:**
- Võimas ja paindlik
- Võimaldab automatiseerida ülesandeid skriptidega
- Kasutab vähem arvuti ressursse

**Puudused:**
- Õppimiskõver on järsem
- Puuduvad visuaalsed vihjed

### GUI

**Graafiline kasutajaliides (GUI)** kasutab aknaid, ikoone ja nuppe. Enamik kasutajaid on GUI-dega tuttavad (nt Windows Explorer, Maci Finder).

**Eelised:**
- Lihtne õppida
- Visuaalne tagasiside

**Puudused:**
- Piiratud automatiseerimine
- Korduvate ülesannete puhul võib olla aeglasem

### Lühike ajalugu

CLI on vanem kui GUI. Esimesed arvutid kasutasid ainult tekstipõhist liidest. GUI-d muutusid populaarseks 1980ndatel, kuid CLI on endiselt oluline arendajatele, süsteemiadministraatoritele ja edasijõudnud kasutajatele.

### Miks õppida Bash-i?

- **Kaugkasutus:** Paljusid servereid ja pilvesüsteeme kasutatakse kaugelt käsurea kaudu, sageli Bash-i abil.
- **Mõnel programmil puudub GUI:** Paljud teadus-, andmetöötlus- ja arendustööriistad on saadaval ainult käsurea programmide kujul.
- **Tõhusus:** Mõned ülesanded (nt failide hulgikorraga ümbernimetamine, teksti otsimine, andmete haldamine) on Bash-is palju kiirem ja lihtsam.
- **Automatiseerimine:** Bash-i skriptid võimaldavad korduvaid ülesandeid automatiseerida, säästes aega ja vähendades vigade arvu.
- **Stabiilsus:** CLI tööriistad ja skriptid ei lähe nii kergesti katki tarkvarauuenduste või graafilise liidese muutuste tõttu.

Bash-i õppimine annab sulle võimsa kontrolli oma arvuti üle ning on väärtuslik oskus programmeerimises, andmeanalüüsis ja süsteemi haldamises.

---

## Bash-i põhilised käsud

Järgnevalt vaatame üle mõned kõige levinumad Bash-i käsud teemade kaupa.

### Navigeerimine failisüsteemis

---

| Käsk      | Kirjeldus                              | Näide kasutusest                  |
|-----------|----------------------------------------|-----------------------------------|
| `pwd`     | Näita töökataloogi                     | `pwd`                             |
| `ls`      | Näita faile ja katalooge               | `ls -l`                           |
| `cd`      | Vaheta katalooge                       | `cd Documents`                    |

Enne kui vaatame konkreetseid käske, on oluline mõista, et arvuti failisüsteem on hierarhiline – see tähendab, et failid ja kataloogid (kaustad) on paigutatud puuna, kus igal kataloogil võib olla alamkatalooge ja faile. Kõige ülemine kataloog on juurkataloog (`/` Linuxis ja Macis, draivitäht Windowsis, nt `C:\`). Iga kataloogis asuv fail või alamkataloog on seotud oma asukohaga selles puus.

#### `pwd`
Näitab, millises kataloogis (kaustas) sa hetkel asud.
- Näide:  
  ```
  pwd
  ```
  Väljund: `/home/kasutaja/Documents`

#### `ls`
Näitab aktiivses kataloogis olevad failid ja kataloogid.
- Näide:  
  ```
  ls
  ```

##### Käsurea argumendid

Enamik käske Bash-is (ja üldse käsureal) võtavad vastu argumente, mis täpsustavad või muudavad käsu käitumist. Argument on lisaparameeter, mis kirjutatakse käsu nime järele tühikuga eraldatult. Argumente võib olla mitu ja nende järjekord võib olla oluline.

Argumente on kahte tüüpi:
- **Lühikesed argumendid**: Tavaliselt üks täht, eelneb üks sidekriips, nt `-l`
- **Pikad argumendid**: Tavaliselt sõna, eelneb kaks sidekriipsu, nt `--help`

Näide:
```
ls -l --color
```

Oluline on teada, et sama argument võib erinevates programmides tähendada erinevat asja. Näiteks `-r` võib ühes programmis tähendada "rekursiivselt", teises "reverse" ehk vastupidises järjekorras. Seetõttu tasub alati vaadata käsu dokumentatsiooni (`man <käsk>` või `<käsk> --help`).

##### Populaarsed argumendid ls käsul:
  - `-l` – detailne nimekiri (õigused, omanik, suurus, kuupäev)
    ```
    ls -l
    ```
  - `-a` – näita ka peidetud faile (failid, mis algavad punktiga)
    ```
    ls -a
    ```
  - `-h` – näita suurusi inimloetaval kujul (koos `-l`)
    ```
    ls -lh
    ```
  - `-R` – näita ka alamkatalooge rekursiivselt
    ```
    ls -R
    ```

#### `cd`
Vaheta katalooge, liigud failisüsteemis ringi.
- Näide:  
  ```
  cd Documents
  ```
  Liigub alamkataloogi `Documents`.

- Populaarsed lühendid:
  - `cd ~` või lihtsalt `cd` – liigub kodukataloogi (nt `/home/kasutaja` või `C:\Users\kasutaja`)
  - `cd -` – liigub eelmisesse kataloogi, kus viibisid
  - `cd ..` – liigub ühe taseme võrra üles (vanemkataloogi)
  - `cd /` – liigub juurkataloogi

- Näited:
  ```
  cd ~
  cd ..
  cd -
  cd /var/log
  ```

#### Automaatne täitmine (`tab` completion)

Bash toetab automaatset täitmist, mis võimaldab sul kiiresti sisestada failide ja kataloogide nimesid, vajutades `Tab` klahvi. Kui hakkad kirjutama faili või katalooge nime ja vajutad `Tab`, proovib Bash automaatselt täita nime, kui see on ainulaadne. Kui on mitu võimalikku täiendust, näitab Bash sulle valikuid.

#### Absoluutne vs suhteline tee (path)

- **Absoluutne tee** algab alati juurkataloogist (`/` või Windowsis draivitähega) ja näitab täpset asukohta failisüsteemis.
  - Näide: `/home/kasutaja/Documents/fail.txt`
- **Suhteline tee** algab aktiivsest kataloogist, kus parasjagu asud.
  - Näide: `Documents/fail.txt` (kui oled `/home/kasutaja` kataloogis)

Suhtelisi teed on mugav kasutada, kui liigud failisüsteemis ringi ja ei taha iga kord täispikka teed kirjutada.


### Failisüsteemiga töötamine

---

| Käsk      | Kirjeldus                              | Näide kasutusest                  |
|-----------|----------------------------------------|-----------------------------------|
| `mkdir`   | Loo uus kataloog                       | `mkdir uus_kataloog`              |
| `rmdir`   | Kustuta tühi kataloog                  | `rmdir vana_kataloog`             |
| `rm`      | Kustuta faile või katalooge            | `rm fail.txt`                     |
| `cp`      | Kopeeri faile või katalooge            | `cp allikas.txt sihtkoht.txt`     |
| `mv`      | Liiguta või nimeta faile/katalooge     | `mv vana_nimi.txt uus_nimi.txt`   |
| `chmod`   | Muuda faili õigusi                     | `chmod +x skript.sh`              |
| `chown`   | Muuda faili omanikku                   | `chown kasutaja:grupp fail.txt`   |
| `ln`      | Loo sümboolne link faili või kataloogi | `ln -s sihtfail link_nimi`        |

Failisüsteemiga töötamise käsud võimaldavad luua, kustutada, kopeerida, liigutada ja muuta faile ning katalooge. Allpool on olulisemad käsud koos näidetega ja selgitustega.

#### `mkdir`
Loo uus kataloog.
- Näide:
  ```
  mkdir uus_kataloog
  ```
- Alamkataloogide loomine korraga (rekursiivselt):
  ```
  mkdir -p vanem/alam/veelalam
  ```
  Argument `-p` loob vajadusel kõik vahepealsed kataloogid.

#### `rmdir` vs `rm`
- `rmdir` kustutab ainult tühja katalooge.
  ```
  rmdir vana_kataloog
  ```
- `rm` kustutab faile. Kui soovid kustutada katalooge koos sisuga, kasuta rekursiivset argumenti:
  ```
  rm -r kataloog
  ```
  **NB!** Käsureal kustutatud failid ja kataloogid ei liigu prügikasti, neid ei saa lihtsalt taastada. Ole eriti ettevaatlik käsuga:
  ```
  rm -rf /
  ```
  See kustutaks kogu failisüsteemi (**ära kunagi tee seda!**).

#### `cp` ja `mv`
- Mõlemad käsud vajavad vähemalt kahte argumenti: allikas ja sihtkoht.
  ```
  cp fail.txt koopia.txt
  mv fail.txt uus_nimi.txt
  ```
- Katalooge kopeerimiseks kasuta `-r` (rekursiivselt):
  ```
  cp -r kataloog uus_kataloog
  ```
- Kui sihtkoht on olemasolev kataloog, kopeeritakse või liigutatakse fail/kataloog sinna sisse. Kui sihtkoht on failinimi, nimetatakse fail ümber.
- Kui argumentide arv või tüüp ei sobi, annab käsk veateate.
- Mitme faili või kataloogi kopeerimine/liigutamine kataloogi:
  ```
  cp fail1.txt fail2.txt kataloog/
  mv fail1.txt fail2.txt kataloog/
  ```
  Siin kõik allikad kopeeritakse või liigutatakse sihtkataloogi. Kui sihtkoht ei ole olemasolev kataloog, annab käsk vea.

#### `chmod` ja `chown`
- Faili õigused määravad, kes saab faili lugeda, kirjutada või käivitada.
- Õiguste stringi näide: `drwxr-xr-x`
  - Esimene täht: fail (`-`), kataloog (`d`) või sümlink (`l`)
  - Järgmised kolm: omaniku õigused (r=read, w=write, x=execute)
  - Järgmised kolm: grupi õigused
  - Viimased kolm: teiste kasutajate õigused
- Näide:
  ```
  chmod +x skript.sh
  ```
  Lisab käivitusõiguse.
  ```
  chmod 644 fail.txt
  ```
  Omanik võib lugeda/kirjutada, teised ainult lugeda.

- Omaniku või grupi muutmine:
  ```
  chown kasutaja:grupp fail.txt
  ```
  Vajalik, kui fail peab kuuluma teisele kasutajale või grupile (nt serverites).

#### `ln`
Loo link failile või kataloogile.
- Sümboolne link (shortcut):
  ```
  ln -s sihtfail link_nimi
  ```
  Kasulik, kui soovid viidata failile/kataloogile teises asukohas, ilma originaali kopeerimata. Näiteks mitte vaikimisi asukohas olevate programmide `/bin` või `/usr/bin` kataloogi lisamiseks. `/bin` ja `/usr/bin` on kataloogid, kus asuvad süsteemi käsud ja programmid.

### Failide loomine ja muutmine

---

| Käsk      | Kirjeldus                              | Näide kasutusest                  |
|-----------|----------------------------------------|-----------------------------------|
| `touch`   | Loo tühi fail                          | `touch uusfail.txt`               |
| `less`    | Näita faili sisu lehekülgede kaupa     | `less fail.txt`                   |
| `more`    | Näita faili sisu lehekülgede kaupa     | `more fail.txt`                   |
| `nano`    | Lihtne tekstiredaktor                  | `nano fail.txt`                   |
| `vim`     | Keerulisem tekstiredaktor              | `vim fail.txt`                    |
| `cat`     | Näita ja ühendab faile                 | `cat fail.txt`                    |
| `echo`    | Näita tekstirida (i.e. print)          | `echo "Tere, maailm!"`            |

Failide loomiseks ja muutmiseks kasutatakse sageli tekstiredaktoreid. Bash-is on kõige levinumad:

#### `nano`
- Väga lihtne ja kasutajasõbralik tekstiredaktor.
- Sobib hästi algajale.
- Nano avab faili käsuga:
  ```
  nano failinimi.txt
  ```
- Nano menüü ja käsud on alati nähtavad akna allservas.
- Kõik toimingud tehakse klaviatuuri abil, kasutades tähekombinatsioone (näiteks `^X` tähendab Ctrl + X).
- Abi saab alati käsuga `^G` (Ctrl + G).
- Faili salvestamine: `^O` (Ctrl + O), väljumine: `^X` (Ctrl + X).
- Macis kasutatakse tavaliselt `Control` klahvi, kuid mõnes terminalis võib vaja minna `Fn` või `Command` klahvi. Windowsis ja Linuxis kasutatakse `Ctrl`.
- Tähekombinatsioonide tähendused:
  - `^` = Ctrl (näiteks `^O` = Ctrl + O)
  - `M-` = Meta ehk tavaliselt Alt (näiteks `M-U` = Alt + U)

#### `vim` ja `vi`
- Võimsad, kuid keerukamad tekstiredaktorid.
- `vim` ei pruugi olla igas süsteemis vaikimisi paigaldatud, kuid `vi` tavaliselt on.
- Avamine:
  ```
  vim failinimi.txt
  ```
- Vajab rohkem õppimist, kuid võimaldab väga kiiret ja paindlikku töötamist suurte failidega.

#### `touch`
- Loob tühja faili või uuendab faili ajatemplid.
  ```
  touch uusfail.txt
  ```

#### `cat`
- Näitab faili sisu terminalis või ühendab mitu faili.
  ```
  cat fail.txt
  cat fail1.txt fail2.txt > kokku.txt
  ```
- Saab kasutada ka koos suunamisega (`>`, vt allpool).

#### `less` ja `more`
- Mõlemad käsud võimaldavad vaadata pikki faile lehekülgede kaupa, ilma et kogu sisu korraga ekraanile kuvataks.
- `less` on võimsam ja võimaldab kerida nii üles kui alla, kasutada otsingut (`/`), liikuda lehekülgede kaupa (`Space` edasi, `b` tagasi), väljuda `q`.
  ```
  less fail.txt
  ```
- `more` on lihtsam, võimaldab liikuda ainult edasi (tühikuga järgmine leht, `q` väljub).
  ```
  more fail.txt
  ```
- Kui fail on väga pikk, on `less` või `more` palju mugavam kui `cat`.

#### Suunamine (`>`, `>>`, `2>`, jne)

Bash-is saab käsu väljundi suunata faili, kasutades suunamissümboleid:
- `>` – suunab väljundi faili, kirjutades olemasoleva faili üle.
  ```
  echo "Tere, maailm!" > tervitus.txt
  ```
- `>>` – lisab väljundi faili lõppu, olemasolevat sisu üle kirjutamata.
  ```
  echo "Veel rida" >> tervitus.txt
  ```
- `2>` – suunab veaväljundi (stderr) faili.
  ```
  ./minu_programm.py 2> vead.txt
  ```
- `1>` – suunab tavalise väljundi (stdout) faili (sama mis `>`).
- `&>` – suunab nii tavalise kui veaväljundi samasse faili.
  ```
  käsk &> kogu_väljund.txt
  ```

**Selgitus:**
- `1` tähistab standardväljundit (stdout)
- `2` tähistab veaväljundit (stderr)

Näited:
```
cat fail.txt > uusfail.txt      # kirjutab faili sisu uude faili
cat fail.txt >> logi.txt        # lisab faili sisu logi lõppu
käsk 1> väljund.txt 2> vead.txt # tavaline väljund ja vead eraldi failidesse
```

---

#### Failinimede parimad praktikad

Failinimede valikul tasub järgida mõningaid häid tavasid, et vältida hilisemaid probleeme käsureal, skriptides ja erinevates operatsioonisüsteemides.

**Miks vältida tühikuid failinimes?**
- Tühikud tekitavad käsureal lisavaeva, sest iga tühik eraldab käsu argumente.
- Failinimes tühikuga tuleb kasutada jutumärke või tagasikaldkriipsu (`\`), nt `my file.txt` → `my\ file.txt` või `"my file.txt"`.
- Skriptid ja programmid võivad tühikuga failinimesid valesti töödelda.

**Milliseid sümboleid vältida?**
- Vältida tuleks järgmisi erisümboleid: `! @ # $ % ^ & * ( ) [ ] { } ; : ' " < > , ? \ | /` ja tühikuid.
- Need võivad olla käsurea jaoks erilise tähendusega või põhjustada vigu failisüsteemis.
- Failinimesid võiks moodustada ainult tähtedest (a-z, A-Z), numbritest (0-9), sidekriipsudest `-` ja alakriipsudest `_`.

**Kuidas kasutada kuupäeva failinimes?**
- Failinime algusesse või lõppu lisa kuupäev kujul `YYYY-MM-DD` või `YYYYMMDD` (nt `2024-06-01_aruanne.txt` või `aruanne_20240601.txt`).
- Selline formaat tagab, et failid sorteeruvad alati korrektselt kronoloogilises järjekorras.
- Näide käsureal:
  ```bash
  touch raport_$(date +%Y-%m-%d).txt
  ```
  või ilma sidekriipsudeta:
  ```bash
  touch raport_$(date +%Y%m%d).txt
  ```
  - siin `$(käsk)` jooksutab "*käsu*" ja asendab selle väljundiga teise käsu sees.

### Otsimine ja filtreerimine

---

| Käsk      | Kirjeldus                              | Näide kasutusest                  |
|-----------|----------------------------------------|-----------------------------------|
| `grep`    | Otsi tekstis mustreid                  | `grep "otsitav" fail.txt`         |
| `find`    | Otsi faile ja katalooge                | `find . -name "fail.txt"`         |
| `sort`    | Sorteeri tekstifaili read              | `sort fail.txt`                   |
| `uniq`    | Eemalda duplikaatridu failist          | `uniq fail.txt`                   |
| `wc`      | Loenda ridu, sõnu ja märke failis      | `wc -l fail.txt`                  |
| `cut`     | Eemalda osi faili ridadest             | `cut -d',' -f1 fail.txt`          |
| `head`    | Näita faili esimesi ridu               | `head -n 10 fail.txt`             |
| `tail`    | Näita faili viimaseid ridu             | `tail -n 10 fail.txt`             |

#### Bash-i wildcardid ja mustrid

Bash-is saab kasutada erinevaid **wildcarde** ehk metamärke failinimede ja mustrite sobitamiseks. Need on eriti kasulikud failide otsimisel, käskudele failide loetlemisel ja mustritega töötamisel.

- `*` — sobib suvalise arvu suvalisi märke (ka tühikuga).  
  Näide: `ls *.txt` (kõik `.txt` lõpuga failid)
- `?` — sobib ükskõik millise ühe märgiga.  
  Näide: `ls fail?.txt` (leiab nt `fail1.txt`, `failA.txt`)
- `[abc]` — sobib ühe märgiga, mis on sulgudes loetletud.  
  Näide: `ls fail[12].txt` (leiab `fail1.txt` ja `fail2.txt`)
- `[a-z]` — sobib ühe märgiga vahemikust.  
  Näide: `ls fail[a-c].txt` (leiab `faila.txt`, `failb.txt`, `failc.txt`)
- `{foo,bar}` — sobib loetletud variantidega.  
  Näide: `ls {andmed,logid}.csv` (leiab `andmed.csv` ja `logid.csv`)
- `^` — regulaaravaldises rea algus (kasutatakse grep-is, mitte failinimedes).
- `$` — regulaaravaldises rea lõpp (kasutatakse grep-is).
- `.` — regulaaravaldises ükskõik milline märk (grep-is).
- `{2}` — regulaaravaldises täpselt kaks korda (grep-is).

**Kus kasutada?**
- Failinimede puhul (nt `ls`, `cp`, `mv`, `rm`): kasutatakse shelli wildcardsid (`*`, `?`, `[]`, `{}`).
- Tekstiotsingul (nt `grep`): kasutatakse regulaaravaldisi (`^`, `$`, `.`, `{n}` jne).

**Näiteid:**
- Kõik `.sh` failid: `ls *.sh`
- Kõik failid, mis algavad `data` ja lõppevad `.txt`: `ls data*.txt`
- Kõik failid, mille nimi on 4 tähemärki: `ls ????`
- Leia kõik read, mis lõppevad punktiga: `grep '\.$' fail.txt`
- Leia kõik read, mis algavad tähega A: `grep '^A' fail.txt`
- Leia read, kus on täpselt kaks järjestikust numbrit: `grep '[0-9]\{2\}' fail.txt`

#### `grep` – tekstimustrite otsimine failidest

`grep` on väga võimas tööriist tekstist mustrite otsimiseks. Seda kasutatakse sageli logide, koodi või andmefailide kiireks filtreerimiseks.

**Lihtne otsing:**
```
grep "otsitav" fail.txt
```
Näitab kõik read failist, kus leidub sõna "otsitav".

**Otsing mitmest failist:**
```
grep "otsitav" fail1.txt fail2.txt
```

**Otsing kogu kataloogipuus:**
```
grep -r "otsitav" .
```
`-r` tähendab rekursiivselt – otsitakse ka alamkataloogidest.

**Otsing wildcardiga failinimedes:**
```
grep "otsitav" *.txt
```
Otsib sõna "otsitav" kõigist aktiivse kataloogi `.txt` failidest.

**Mustri kasutamine:**
```
grep "^Tere" fail*.txt
```
Leiab kõik read, mis algavad sõnaga "Tere" kõigis failides, mille nimi algab `fail`.

**Tõstutundetu otsing:**
```
grep -i "otsitav" fail.txt
```

**Näita ainult ridade arvu:**
```
grep -c "otsitav" fail.txt
```

**Näita ka rida ja selle numbri:**
```
grep -n "otsitav" fail.txt
```

**Otsing tühikutega mustriga:**
Kui otsitav fraas sisaldab tühikuid või erimärke, kasuta alati jutumärke:
```
grep "Tere maailm" fail.txt
```
Ilma jutumärkideta käsurea parser jagab argumendi mitmeks.

**Abi saamiseks:**
```
man grep
```

#### `find` – failide ja kataloogide otsimine failisüsteemist

`find` võimaldab otsida faile ja katalooge kataloogipuust erinevate kriteeriumite alusel.

**Leia fail nime järgi:**
```
find . -name "fail.txt"
```
Otsib aktiivsest kataloogist ja alamkataloogidest faili nimega "fail.txt".

**Leia kõik .md failid:**
```
find . -name "*.md"
```

**Leia failid, mis kuuluvad kindlale kasutajale:**
```
find . -user kasutajanimi
```

**Leia failid, mis on suuremad kui 10MB:**
```
find . -size +10M
```

**Leia failid, mis on muudetud viimase 7 päeva jooksul:**
```
find . -mtime -7
```

**Leia tühjad failid:**
```
find . -type f -empty
```

**Abi saamiseks:**
```
man find
```

#### `grep` ja `find` koos

Sageli on vaja leida faile kindla nimega ja otsida neist mustrit. Selleks saab kasutada `find` ja `grep` koos:

**Näide:** Otsi kõikidest oma repo kataloogi `.md` failidest kõik pealkirjad, mis algavad `##` ja prindi iga pealkirja järel kolm järgmist rida:
```
find . -name "*.md" -exec grep -A 3 "^##" {} \;
```
- `-A 3` tähendab, et näidatakse 3 rida pärast leitud mustrit.
- `{}` asendatakse iga leitud failiga.
- `\;` lõpetab `-exec` käsu.

**Alternatiivne viis:** Sama tulemus, kasutades `grep`-i koos `find` väljundiga:
```
grep -A 3 "^##" $(find . -name "*.md")
```
- Siin `find` annab failide nimekirja, millele `grep` rakendub.
- See töötab hästi, kui failinimesid on vähe ja need ei sisalda tühikuid ega erimärke. Kui faile on palju või nimedes on tühikuid, on `-exec` turvalisem.

**Veel näiteid:**
- Otsi kõikidest `.sh` failidest sõna "python":
  ```
  find . -name "*.sh" -exec grep "python" {} \;
  ```
- Otsi kõikidest alamkataloogide `.log` failidest read, mis lõppevad veateatega:
  ```
  grep 'error$' */*.log
  ```

Need tööriistad on eriti võimsad, kui neid kombineerida!

### Andmete töötlemine: sort, uniq, wc, cut, head, tail ja toru (pipe)

Bash-is saab töödelda tekstifaile ja andmeid väga tõhusalt, kasutades erinevaid käske ning nende ühendamist toru (`|`) abil. Järgnevalt tutvustame olulisemaid tööriistu ja näitame, kuidas neid kasutada näiteks `Islander_data.csv` failiga.

#### `sort`
Sorteerib sisendi reastatud kujule.
- Näide: Sorteeri Islander_data.csv vanuse järgi (veerg 3):
  ```
  sort -t, -k3 data/Islander_data.csv
  ```
  - `-t,` määrab veerueraldajaks koma.
  - `-k3` tähendab, et sorteeritakse kolmanda veeru järgi.

#### Toru ehk pipe (`|`)

Toru võimaldab suunata ühe käsu väljundi järgmise käsu sisendiks. See on väga võimas viis töövoogude loomiseks.

#### `uniq`
Eemaldab järjestikused duplikaadid. Sageli kasutatakse koos `sort` käsuga.
- Näide: Leia unikaalsed grupid:
  ```
  cut -d, -f4 data/Islander_data.csv | sort | uniq
  ```

#### `wc`
Loendab ridu, sõnu ja märke.
- Näide: Loenda, mitu rida on andmetikus (st mitu inimest):
  ```
  wc -l data/Islander_data.csv
  ```
- Näide: Loenda, mitu erinevat gruppi on:
  ```
  cut -d, -f4 data/Islander_data.csv | sort | uniq | wc -l
  ```

#### `cut`
Võimaldab võtta failist ainult teatud veerud.
- Näide: Võta ainult nimed ja vanused:
  ```
  cut -d, -f1,2,3 data/Islander_data.csv
  ```
  - `-d,` määrab veerueraldajaks koma.
  - `-f1,2,3` võtab veerud 1, 2 ja 3.

#### `head` ja `tail`
Näitavad faili algust või lõppu.
- Näide: Näita esimesed 5 rida:
  ```
  head -n 5 data/Islander_data.csv
  ```
- Näide: Näita viimased 10 rida:
  ```
  tail -n 10 data/Islander_data.csv
  ```
- Näita kõiki ridu peale esimest (pealkirja eemaldamiseks):
  ```
  tail -n +2 data/Islander_data.csv
  ```

**Näiteid töövoogudest Islander_data.csv põhjal:**

- Leia, mitu erinevat perekonnanime on andmetikus:
  ```
  cut -d, -f2 data/Islander_data.csv | sort | uniq | wc -l
  ```

- Leia, mitu inimest igas Happy/Sad grupis on:
  ```
  cut -d, -f4 data/Islander_data.csv | sort | uniq -c
  ```

- Näita 10 vanimat inimest (pealkirja rida vahele jääb, eemaldamiseks kasuta tail/head):
  ```
  tail -n +2 data/Islander_data.csv | sort -t, -k3 -nr | head -n 10 | cut -d, -f1,2,3 | sed 's/,/\t/g'
  ```
  (Siin kasutasime `sed`-i, et asendada komad tabulaatoritega, muutes väljundi loetavamaks. `sed` on võimas tekstiredaktor, mida saab kasutada keerukamate asenduste ja mustrite jaoks.)

- Leia, mitu inimest on saanud negatiivse Diff väärtuse (mälu läks halvemaks):
  ```
  awk -F, 'NR>1 && $9 < 0 {print $1, $2, $9}' data/Islander_data.csv | wc -l
  ```
  (Siin kasutasime ka `awk`-i, mis on võimas tööriist, kui tunned et vajad seda peaks võibolla kaaluma juba pythoni või R-i kasutamist. `awk` on aga väga kasulik ka Bash-is one-linerite jaoks.)

- Näita kõigi unikaalsete ravimite (`Drug` veerg) loetelu:
  ```
  tail -n +2 data/Islander_data.csv | cut -d, -f6 | sort | uniq
  ```

Kombineerides neid käske toruga (`|`), saab väga kiiresti ja paindlikult töödelda suuri tekstifaile ja andmestikke ilma eraldi programmita. Näiteks:
```bash
find data/ -type f -name "*.txt" | grep "2024" | xargs cat | sort | uniq -c | sort -nr | head -n 10
```
See käsk:
- leiab kõik `.txt` failid kataloogis `data/`, 
- filtreerib failinimed, mis sisaldavad "2024",
- ühendab nende sisu,
- loendab unikaalsete ridade esinemised,
- sorteerib sageduse järgi ja
- näitab 10 kõige sagedasemat rida.



### Failide ja andmete liigutamine võrgus

---

| Käsk      | Kirjeldus                              | Näide kasutusest                  |
|-----------|----------------------------------------|-----------------------------------|
| `ssh`     | Ühendu turvaliselt kaugserveriga       | `ssh kasutaja@masin`              |
| `scp`     | Turvaline kopeerimine kaugserverisse   | `scp fail.txt kasutaja@masin:/tee`|
| `wget`    | Laadi faile veebist alla               | `wget http://example.com/fail.txt`|
| `curl`    | Edasta andmeid serveriga               | `curl http://example.com`         |


#### SSH protokoll

**SSH (Secure Shell)** on turvaline protokoll, mis võimaldab krüpteeritud ühendust kahe arvuti vahel. Seda kasutatakse peamiselt kaugserveritesse sisselogimiseks ja failide turvaliseks edastamiseks. SSH asendab vanemaid, ebaturvalisi protokolle nagu telnet ja rsh.

SSH ühenduse loomiseks kasutatakse tavaliselt kasutajanime ja parooli, kuid turvalisem ja mugavam on kasutada **SSH võtmeid**.

#### SSH võtmed

SSH võtmed on krüptograafilised võtmed, mis võimaldavad autentimist ilma parooli sisestamata. Võtmed koosnevad kahest osast:
- **Privaatvõti** (private key): jääb sinu arvutisse ja seda ei tohi kellelegi jagada.
- **Avalik võti** (public key): kopeeritakse serverisse, kuhu soovid ühenduda.

**SSH võtme loomine:**
```bash
ssh-keygen -t ed25519 -C "sinu@email.ee"
```
- Järgides juhiseid, salvestatakse privaatvõti tavaliselt faili `~/.ssh/id_ed25519` ja avalik võti faili `~/.ssh/id_ed25519.pub`.
- Parool on võtme kaitsmiseks, kuid võid selle ka tühjaks jätta. Ühendus on ikkagi krüpteeritud.
- Loe `man ssh-keygen` või `ssh-keygen --help` lisainfo saamiseks.

**Avaliku võtme paigutamine serverisse:**
- Lisa avaliku võtme sisu serveri faili `~/.ssh/authorized_keys`.
- Näiteks:
  ```bash
  ssh-copy-id kasutaja@server
  ```
  või käsitsi kopeerides:
  ```bash
  cat ~/.ssh/id_ed25519.pub | ssh kasutaja@server "cat >> ~/.ssh/authorized_keys"
  ```

**Kus võtmed asuvad?**
- Privaatvõti: sinu arvutis (`~/.ssh/id_ed25519`)
- Avalik võti: serveris (`~/.ssh/authorized_keys`)

**SSH võtmete kohta loe lähemalt GitHubi juhendist:**  
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh

**Märkus `wget` kohta:**  
`wget` ei pruugi olla vaikimisi paigaldatud kõikidesse süsteemidesse (nt MacOS-is seda vaikimisi ei ole). `wget` on intuitiivne ja lihtne viis failide allalaadimiseks.

**`curl` kui alternatiiv `wget`-ile:**  
`curl` on enamasti vaikimisi olemas. Faili allalaadimiseks nagu `wget`:
```bash
curl -O http://example.com/fail.txt
```
- `-O` (suur O) salvestab faili originaalnimega.
- `-L` järgib ümbersuunamisi (vajalik mõnede linkide puhul):
  ```bash
  curl -LO http://example.com/fail.txt
  ```
- `-C -` jätkab katkestatud allalaadimist.

### Faili- ja kataloogiteave

---

| Käsk        | Kirjeldus                            | Näide kasutusest                  |
|-------------|--------------------------------------|-----------------------------------|
| `basename`  | Võta failinimi rajast                | `basename /tee/fail.txt`          |
| `dirname`   | Võta kataloogi tee täisrajast        | `dirname /tee/fail.txt`           |
| `xargs`     | Koosta ja käivita käsuread stdin-ist | `echo 'fail1 fail2' \| xargs rm`  |


#### Skripti loomine ja käivitamine
Bash-skriptid võimaldavad automatiseerida korduvaid käsurea toiminguid. Skript on tavaline tekstifail, mille igal real on käsurea käsk.

**Miks skriptimine on oluline?**
- Skriptid võimaldavad töövoogude automatiseerimist, mis tagab töö korduvuse (reproducibility), vähendab käsitsi tehtavaid vigu ja muudab töövood dokumenteerituks.
- Skripte saab jagada kolleegidega, mis lihtsustab koostööd ja tulemuste taasesitamist.
- Hästi kirjutatud skriptid on loetavad ja hooldatavad ka hiljem.

**Skriptide dokumenteerimine ja stiil:**
- Lisa alati skripti algusesse kommentaarid, mis kirjeldavad skripti eesmärki, autorit, kuupäeva ja kasutusjuhendit.
- Kasuta selgeid ja kirjeldavaid muutujanimesid.
- Lisa kommentaare (`#`), et selgitada keerulisemaid kohti.
- Näide:
  ```bash
  #!/bin/bash
  # Skripti nimi: andmete_töötleja.sh
  # Autor: Mari Maasikas
  # Kuupäev: 2024-06-01
  # Kirjeldus: Töötleb andmefaile ja annab kokkuvõtte.
  # Kasutamine: ./andmete_töötleja.sh sisendfail.txt
  ```

1. Loo uus fail, näiteks `minu_skript.sh`.
2. Faili alguses kasuta shebang-rida, mis ütleb, millise tõlgendajaga skripti käivitada:
   ```
   #!/bin/bash
   ```
3. Lisa käsud, üks igale reale.
4. Muuda skript käivitatavaks:
   ```
   chmod +x minu_skript.sh
   ```
5. Käivita skript:
   ```
   ./minu_skript.sh
   ```

#### Näide skriptist

```bash
#!/bin/bash
echo "Tere, maailm!"
```

#### `basename` ja `dirname` skriptides

- `basename` — eemaldab failiteest kataloogiosa, jättes alles ainult failinime.
- `dirname` — eemaldab failiteest failinime, jättes alles ainult kataloogi.

Näide:
```bash
failitee="/home/kasutaja/andmed/fail.txt"
echo "Failinimi: $(basename "$failitee")"
echo "Kataloog: $(dirname "$failitee")"
echo "Failinimi ilma laiendita: $(basename "$failitee" .txt)"
```

#### if-klausel ja tingimused

Bash-is saab kasutada `if`-klauslit, et teha otsuseid skriptis.

**Üldine süntaks:**
```bash
if [ tingimus ]; then
  # käsud kui tingimus tõene
else
  # käsud kui tingimus väär
fi
```

**Levinumad testid:**
- Faili olemasolu: `[ -f fail.txt ]` (fail olemas ja on tavaline fail)
- Kataloogi olemasolu: `[ -d kataloog ]`
- Fail on tühi: `[ -s fail.txt ]`
- Stringide võrdlus: `[ "$a" = "$b" ]`
- Arvude võrdlus: `[ "$a" -eq "$b" ]`, `[ "$a" -gt "$b" ]`, `[ "$a" -lt "$b" ]`
- Mitme tingimuse ühendamine: `[ -f fail.txt ] && [ -s fail.txt ]`

**Näide:**
```bash
if [ -f "$1" ]; then
  echo "Fail $1 on olemas"
else
  echo "Faili $1 ei leitud"
fi
```

#### Käsurea argumendid bash-skriptidele

Skriptile saab anda argumente, mis on saadaval muutujatena `$1`, `$2`, ... (`$0` on skripti nimi, `$@` kõik argumendid). Argumentide eraldamine toimub tühikute abil, argumendid, mis sisaldavad tühikuid, tuleb panna jutumärkidesse.

**Näide:**
```bash
#!/bin/bash
echo "Esimene argument: $1"
echo "Teine argument: $2"
```
Käivita:
```
./minu_skript.sh foo bar
```
Väljund:
```
Esimene argument: foo
Teine argument: bar
```

**Kõik argumendid tsüklis:**
See näide võimaldab sul ise argumendid töödelda ja ostustada, mida nendega teha:
```bash
for arg in "$@"; do
  if [ -f "$arg" ]; then
    echo "$arg  - Fail on olemas"
  else
    echo "Argument: $arg - ei ole fail"
  fi
done
```

#### Argumentide parsimine getopts abil (POSIX stiil)

Kui soovid toetada lühikesi lippe (nt `-f fail`), kasuta `getopts`:

**Näide:**
```bash
while getopts "f:v" opt; do
  case $opt in
    f) failinimi="$OPTARG" ;;
    v) verbose=1 ;;
    *) echo "Kasutus: $0 [-f fail] [-v]"; exit 1 ;;
  esac
done
echo "Fail: $failinimi"
echo "Verbose: $verbose"
```
Käivita:
```
./minu_skript.sh -f andmed.txt -v
```

**Selgitus:**
- `"f:v"` — `-f` vajab väärtust, `-v` on lipp.
- `$OPTARG` — argumendi väärtus.
- `$OPTIND` — järgmise argumendi indeks.

---

#### Faili- ja kataloogiteave skriptides

- `basename` ja `dirname` on kasulikud, kui töötled failiteid skriptis (vt eespool).
- `xargs` kasutatakse sageli torude ja massoperatsioonide puhul, nt:
  ```
  find . -name "*.txt" | xargs rm
  ```
  Kuid skriptides on tihti mugavam kasutada tsüklit:
  ```bash
  for fail in *.txt; do
    rm "$fail"
  done
  ```
  Teine näide muuta tsükli abil kõik `.txt` failid `.md` failideks:
  ```bash
  for fail in *.txt; do
    mv "$fail" "$(dirname "$fail")/$(basename "$fail" .txt).md"
  done
  ```

#### Veakäsitlus skriptides
- Kasuta `set -e`, et skript katkestaks kohe, kui mõni käsk annab veakoodi.
- Kasuta `trap`-i, et teha midagi vea korral (nt puhastada ajutised failid või anda veateade).
- Kontrolli käsu lõppemise staatust `$?` või kasuta tingimuslauseid.
- Näide:
  ```bash
  #!/bin/bash
  set -e
  trap 'echo "Tekkis viga real $LINENO"; exit 1' ERR

  if [ ! -f "$1" ]; then
    echo "Fail puudub: $1"
    exit 1
  fi
  # ...edasi töötlus...

  cat $1 $2 > ühendatud.txt
  if [ $? -eq 0 ]; then
    echo "Failide ühendamine õnnestus"
  else
    echo "Failide ühendamine ebaõnnestus"
    exit 1
  fi
  ```

#### Viited, kui jäi väheks:

- [Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/html/)
- [Advanced Bash-Scripting Guide](https://tldp.org/LDP/abs/html/)
- [Bash Hackers Wiki](https://bash-hackers.gabe565.com/)

### Bash-i muutujad ja keskkond

---

| Käsk      | Kirjeldus                              | Näide kasutusest                  |
|-----------|----------------------------------------|-----------------------------------|
| `env`     | Näita keskkonnamuutujaid               | `env`                             |
| `export`  | Sea keskkonnamuutuja                   | `export MUUTUJA=väärtus`          |
| `alias`   | Loo käsule lühend                      | `alias ll='ls -la'`               |
| `unalias` | Eemalda lühend                         | `unalias ll`                      |
| `which`   | Leia käsu asukoht                      | `which python`                    |
| `source`  | Käivita käsud failist praeguses shellis| `source skript.sh`                |

- Keskkonnamuutujad (nt PATH) mõjutavad, milliseid käske ja skripte saab otse käsurealt käivitada.
- Kui soovid oma skriptid teha käivitatavaks igast kataloogist, lisa nende asukoht PATH-i:
  ```bash
  export PATH="$PATH:/home/kasutaja/minu_skriptid"
  ```
- Lisa see rida oma `~/.bashrc` faili, et muudatus kehtiks alati.
- Kontrolli PATH-i väärtust käsuga `echo $PATH`.

Samuti saad `~/.bashrc` faili lisada oma lemmikkäsud lühenditena (alias):
```bash
alias ll='ls -la'
alias gs='git status'
```

### Arhiveerimine ja pakkimine

| Käsk      | Kirjeldus                              | Näide kasutusest                  |
|-----------|----------------------------------------|-----------------------------------|
| `tar`     | Arhiveeri faile                        | `tar -czvf arhiiv.tar.gz kataloog`|
| `zip`     | Paki faile zip-arhiivi                 | `zip arhiiv.zip fail1 fail2`      |
| `unzip`   | Paki faile zip-arhiivist lahti         | `unzip arhiiv.zip`                |

### Süsteemi info ja haldus

| Käsk      | Kirjeldus                              | Näide kasutusest                  |
|-----------|----------------------------------------|-----------------------------------|
| `top`     | Näita töötavaid protsesse              | `top`                             |
| `ps`      | Näita praeguseid protsesse             | `ps aux`                          |
| `kill`    | Lõpeta protsess                        | `kill PID`                        |
| `df`      | Näita kettaruumi kasutust              | `df -h`                           |
| `du`      | Näita kataloogi ruumikasutust          | `du -h`                           |
| `ping`    | Testi võrguühendust                    | `ping google.com`                 |
| `date`    | Näita või muuda süsteemi kuupäeva ja kellaaega | `date`                    |
| `uptime`  | Näita, kui kaua süsteem on töötanud    | `uptime`                          |
| `history` | Näita käskude ajalugu                  | `history`                         |
| `sudo`    | Käivita käsk superkasutaja õigustes    | `sudo apt update`                 |

### Terminali töö

| Käsk      | Kirjeldus                              | Näide kasutusest                  |
|-----------|----------------------------------------|-----------------------------------|
| `man`     | Näita käsu käsiraamatut                | `man ls`                          |
| `exit`    | Välju terminalist või shelli sessioonist| `exit`                           |
| `clear`   | Puhasta terminali ekraan               | `clear`                           |

See on vaid algus. Kui Bash-is mugavamaks muutud, avastad veel palju käske ja võimalusi.


### Veel üks viide:

- [Unix First Steps Training](https://github.com/sib-swiss/unix-first-steps-training)
  Vaata läbi `.pdf` esitlus, kui sulle meeldivad värvilised slaidid on see just sulle!

## Ülesanne

Kasutades ülaltoodud käske:
1. Navigeeri oma arvutis kataloogi, kus asub sinu kohalik kursuse git repositoorium.
2. Loo uus kataloogi puu nimega `bash_eksperiment`, kus on vähemalt kolm alamkatalooge (nt `data`, `scripts`, `results`).
3. Loo `bash_eksperiment` kataloogi tühi tekstifail nimega `readme.md`.

Kõik skriptid peaks olema 'scripts' kataloogis, andmed 'data' kataloogis ja tulemused 'results' kataloogis.

4. Kasutades `nano` editori kirjuta script nimega `generate_data.py`, mis genereerib 200 juhuslikku täisarvu (vahemikus 1..100).
5. Kasutades oma lemmiks tekstiredaktorit kirjuta script nimega `generate_data.sh`, mis käivitab `generate_data.py` faili N (N=10) korda ja salvestab tulemused `data` kataloogi. Faili nimed võiks olla `data1.txt`, `data2.txt` jne.

Mõlema skripti puhul pöörake tähelepanu ka dokumentatsioonile.

6. Üle kõikide `data` kataloogi failide leia mitu korda igat unikaalset arvu esineb (kasutades `cat`, `sort`, `uniq` käske) - salvesta tulemused faili `results/summary_total_unique_numbers_counted.txt`.
7. Muuda `readme.md` faili, lisades sinna lühikese kirjelduse oma bash eksperimendist, lisa sinna ka kõik kasutatud käsud.
8. Muuda `.gitignore` faili, et jätta `data` ja `results` kataloogid git jälgimisest välja.
