# Sissejuhatus Docker tööriista

## Eesmärk
Selles töötoas tutvume Dockeriga: mis see on, kuidas ta töötab, millised on põhimõisted ning kuidas ehitada ja käivitada oma konteinerid.  

Töötoa lõpuks oskad:
- Selgitada, mis on Docker, image, container, Dockerfile, volume ja network  
- Tõmmata Docker image’i Docker Hub-ist  
- Käivitada ja hallata konteinerit käsurealt  
- Luua oma `Dockerfile` ja sellest image  
- Kasutada volumes/mountingut andmete talletamiseks  

---

## Mis on Docker?
Docker on tööriist, mis võimaldab sul käitada rakendusi isoleeritud **konteinerites**.  

Miks see kasulik on?  
- **Platvormi sõltumatus** – rakendus töötab ühtemoodi igal masinal.  
- **Kergekaalulisus** – erinevalt virtuaalmasinast ei vaja täit OS-i, vaid ainult vajalikku rakendust ja sõltuvusi.  
- **Reprodutseeritavus** – sama image tagab sama keskkonna.  

Docker koosneb kahest peamisest komponendist:  
- **Docker Engine** (daemon) – taustal töötav teenus, mis haldab konteinerite käivitamist.  
- **Docker CLI / Desktop** – vahendid, mille kaudu kasutaja suhelda saab.  

---

## Põhimõisted

### Docker Image
- Retsept või **pakendatud mall**, mis sisaldab rakendust, teeke ja keskkonda.  
- Põhimõtteliselt nagu **programmi installipakett**, mida saab igal pool käivitada.  
- Näide: `python:3.11-slim` sisaldab Python 3.11 tõlgi ja minimaalse Linuxi baassüsteemi.  

### Docker Container
- **Jooksev protsess**, mis on loodud image’i baasil.  
- Container on eraldatud ülejäänud süsteemist (nagu “liivakast”).  
- Kui image on *retsept*, siis container on *valmis toit, mis on laual*.  

### Dockerfile
- Tekstifail, mis kirjeldab, kuidas image ehitatakse.  
- Sisaldab järjestikku käske nagu `FROM`, `COPY`, `RUN`, `CMD`.  
- Näide:  
  - `FROM python:3.11-slim` → aluseks Python  
  - `COPY app.py /app/app.py` → kopeeri oma programmi scripti fail image’i sisse  
  - `CMD ["python", "app.py"]` → käivita rakendus konteineris  

### Docker Volumes & Mounts
- **Volume** – Docker haldab andmete talletamise kausta ise.  
- **Bind mount** – seod kindla hosti kausta konteineriga (`-v /host/path:/container/path`).  
- Vajalik, kui tahad andmeid püsivalt alles hoida või neid jagada konteineri ja hosti vahel.  

### Docker Networks
- Konteinerid saavad omavahel suhelda läbi võrgu.  
- Vaikimisi pannakse nad “bridge” võrku.  
- Kasutatakse, kui tahad näiteks veebiserverit ja andmebaasi panna suhtlema konteinerite vahel.  

---

## Illustreeriv skeem

```mermaid
graph TD
    A[Dockerfile] -->|docker build| B[Docker Image]
    B -->|docker run| C[Docker Container]
    C <--> D[Volume / Mounted folder]
```

---

## Olulisemad käsud ja argumendid

### Versiooni kontroll
```bash
docker --version
```
Annab teada, kas Docker on õigesti paigaldatud.  

---

### Image tõmbamine
```bash
docker pull ubuntu
```
Laeb `ubuntu` image’i Docker Hub-ist alla. Kui käivitad `docker run ubuntu`, aga image puudub, tõmmatakse see automaatselt.  

---

### Containeri käivitamine
```bash
docker run ubuntu
```
Käivitatakse uus konteiner `ubuntu` image’i põhjal. Kuna käske pole antud, lõpetab ta kohe.

**Oluline teada konteinerite käivitamisel:**
- Iga `docker run` käsk loob alati *uue* konteineri, isegi kui kasutad sama image'it.
- Kui kasutad `--name` argumenti (nt `--name minu_ubuntu`), peab nimi olema unikaalne. Kui sama nimega konteiner juba eksisteerib (ka siis, kui ta on peatatud), annab Docker vea.
- Kui midagi läks käivitamisel valesti (nt vale käsk, port juba kasutusel vms), siis:
  - Kontrolli olemasolevaid konteinereid käsuga `docker ps -a`.
  - Vajadusel peata (`docker stop <name>`) ja kustuta (`docker rm <name>`) eelmine konteiner enne uue loomist sama nime või samade portidega.
- Kui `--name` argumenti ei kasuta, loob Docker automaatselt uue anonüümse nimega konteineri. See võib põhjustada portide konflikte, kui mitu konteinerit üritavad kasutada sama porti.
- Kui soovid sama konteinerit uuesti kasutada, kasuta `docker start <name>` või `docker restart <name>`, mitte `docker run`.


---

### Tähtsad `docker run` argumendid

**Süntaks (SYNOPSIS):**
```text
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```
Näide koos levinumate argumentidega:
```text
docker run -d --name minu_nginx -p 8080:80 -v $(pwd)/data:/usr/share/nginx/html nginx
```
See käivitab taustal (`-d`) nimega `minu_nginx` konteineri, seob pordi 8080 hostil pordiga 80 konteineris, mountib kohaliku kausta `data` Nginxi veebikausta ning kasutab `nginx` image'it.

- **`-it`** – *interaktiivne terminal*  
  - `-i` = interactive → hoiab STDIN avatud, saad sisestada käske.  
  - `-t` = tty → annab “terminali” tunde (bash prompt).  
  - Koos tähendab: saad konteinerisse sisse ja töötada nagu oma arvutis.  
  - Näide:  
    ```bash
    docker run -it ubuntu bash
    ```
    Käivitab Ubuntu, avab käsurea sees.  

- **`-d`** – *detached mode*  
  - Käivitab konteineri taustal (ei seo terminali külge).  
  - Sobib teenustele (nt veebiserver).  
  - Näide:  
    ```bash
    docker run -d nginx
    ```
    Nginx veebiserver töötab taustal.  

- **`--name`** – anna konteinerile nimi.  
  - Lihtsam kui kasutada automaatset ID-d.  
  - Näide:  
    ```bash
    docker run -it --name minu_ubuntu ubuntu bash
    ```

- **`-p host:container`** – portide avamine.  
  - Näide:  
    ```bash
    docker run -d -p 8080:80 nginx
    ```
    Avab brauseris http://localhost:8080 Nginxi serveri.  

  **Soovitused hosti portide valimiseks:**
  - Hostipoolne port (`host:container`) võib olla suvaline vaba port, kuid vältida tuleks süsteemi- ja standardporte (0–1023).
  - Hea tava on kasutada vahemikku **1024–49151** (nn. "registered ports") või veelgi turvalisemalt **20000–49151**. (Lisaks plokivad brauserid osad pordid, vaata näiteks [Chrome'i blokeeritud porte](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/net/base/port_util.cc).)
  - Kui jooksutad mitut konteinerit, vali igale erinev hosti port (nt 8080, 8081, 8888 jne).
  - Väldi avalike teenuste puhul tüüpilisi porte (nt 80, 443), kui pole kindel, et neid pole juba kasutuses.
  - Kontrolli, kas port on vaba käsuga `lsof -i :PORT` või `netstat -tuln | grep PORT`.
  - Vajadusel saad kasutada ka suvalist vaba porti, määrates ainult konteineri poole (`-p :80`), kuid siis määrab Docker hosti porti automaatselt.

  **Näide turvalisest portide määramisest:**
  ```bash
  docker run -d -p 18080:80 nginx
  ```
  See seob hosti pordi 18080 konteineri pordiga 80.

- **`-v host:container`** – volumes / bind mounts.  
  - Näide:  
    ```bash
    docker run -it -v $(pwd)/data:/data ubuntu bash
    ```
    Seob hosti kausta `data` konteineri `/data` kaustaga.  

   `$(pwd)` on bash-i süntaks jooksva kataloogi jaoks. Selle alternatiivid windowsis:  
   -  `%cd%` töötab ainult cmd.exe-s.  
   -  `${PWD}` või `${PWD}.Path` töötab PowerShellis.

---

### Konteinerite haldamine

```bash
# Näita jooksvaid konteinerid
docker ps

# Näita kõiki konteinerid (sh peatatud)
docker ps -a

# Peata konteiner
docker stop <name_or_id>

# Käivita peatatud konteiner uuesti
docker start <name_or_id>

# Ava uuesti terminal sees
docker exec -it <name_or_id> bash

# Vaata logisid
docker logs <name_or_id>

# Kustuta konteiner
docker rm <name_or_id>
```

**Konteineri elutsükkel:**
- Kui käivitad konteineri (`docker run`), luuakse uus konteiner ja see hakkab tööle.
- Kui konteineri protsess lõppeb või kasutad `docker stop`, siis konteiner *peatatakse* (ta jääb süsteemi alles, kuid ei tööta).
- Peatatud konteinerit saab uuesti käivitada käsuga `docker start <name_or_id>`. See jätkab samast kohast, kus pooleli jäi (failid ja muud andmed konteineri sees on alles).
- Kui konteinerit enam ei vaja, saab selle süsteemist eemaldada käsuga `docker rm <name_or_id>`. See kustutab konteineri metaandmed ja failisüsteemi (kui andmed pole salvestatud volume'i või bind mounti).
- NB! `docker stop` *ei eemalda* konteinerit, vaid ainult peatab selle. Süsteemi jäävad ka peatatud konteinerid, kuni need käsitsi eemaldad.
- Kui proovid luua uue konteineri sama nimega, aga vana on alles (ka peatatud kujul), annab Docker vea.

**Lühidalt:**  
- `docker run` – loob ja käivitab uue konteineri.
- `docker stop` – peatab konteineri, kuid ei eemalda seda.
- `docker start` – käivitab peatatud konteineri uuesti.
- `docker rm` – eemaldab konteineri süsteemist lõplikult.
- Kasuta `docker ps -a`, et näha ka peatatud konteinereid ja vajadusel need eemaldada.

---

### Kuidas hallata konteinerite tekitatud volume

**Mis on konteineri volume?**  
Kui käivitad konteineri ja kasutad `-v` või `--mount` argumenti, võib Docker luua automaatselt uue volume (kui pole määratud olemasolevat). Mõned images (nt andmebaasid) võivad Dockerfile'is määrata `VOLUME` käsu, mis paneb Dockeri vaikimisi looma anonüümse volume, kui sa ise midagi ei määra.

**Kuidas määrab süntaks, millist tüüpi volume kasutatakse?**  
- Kui kasutad `-v <host_path>:<container_path>` või `--mount type=bind,source=<host_path>,target=<container_path>`, siis *mountitakse hosti kaust* konteinerisse (bind mount).  
  - Näide:  
    ```bash
    docker run -v $(pwd)/data:/data ubuntu
    ```
  - Sellisel juhul andmed salvestatakse otse hosti failisüsteemi ning neid *ei näe* `docker volume ls` käsuga.
- Kui kasutad `-v <volume_name>:<container_path>` või `--mount type=volume,source=<volume_name>,target=<container_path>`, siis kasutatakse *Docker volume'it* (nimeline või anonüümne).  
  - Näide:  
    ```bash
    docker run -v mydata:/data ubuntu
    ```
  - Selline volume on nähtav käsuga `docker volume ls` ja Docker haldab selle asukohta ise.
- Kui kasutad ainult konteineri path'i (`-v /data` või Dockerfile's `VOLUME /data`), loob Docker *anonüümse volume*.

**Lühidalt:**  
- *Bind mount* (`/host/path:/container/path`): andmed hosti failisüsteemis, ei näe `docker volume ls` all.
- *Docker volume* (`volume_name:/container/path`): Docker haldab, näha `docker volume ls` all.
- *Anonüümne volume* (`/container/path`): Docker loob automaatselt, näha `docker volume ls` all.

**Kuidas neid uuesti kasutatakse?**  
- Anonüümseid volume'eid ei saa taaskasutada, iga kord luuakse uus.
- Nimelisi volume'eid saab taaskasutada erinevate konteinerite vahel, kui sama nime kasutad.
- Volume'id säilitavad andmed ka siis, kui konteiner kustutatakse.

**Volume'ite vaatamine ja haldamine:**
```bash
# Näita kõiki volume
docker volume ls

# Vaata konkreetse volume'i infot
docker volume inspect <volume_name>

# Kustuta volume (NB! ainult kui seda ei kasuta ükski konteiner)
docker volume rm <volume_name>

# Kustuta kõik kasutamata volume'id
docker volume prune
```

**Kuidas aru saada, et konteiner loob volume?**
- Vaata image'i Dockerfile'i – kui seal on `VOLUME` käsk, loob Docker selle mount-punkti jaoks volume.
- Kui käivitad konteineri ilma `-v` või `--mount` argumendita, aga image kasutab `VOLUME`, tekib anonüümne volume.
- Kontrolli konteineri detaile:
  ```bash
  docker inspect <container_id>
  ```
  Otsi väljalt `Mounts`, kas seal on tüüp `volume`.

**Kokkuvõte:**  
- Volume'id on mõeldud andmete püsivaks salvestamiseks.
- Anonüümseid volume'eid võib koguneda, kui neid ei hallata – kasuta `docker volume ls` ja `docker volume prune`.
- Nimelisi volume'eid saad taaskasutada erinevate konteinerite vahel.

### Kuidas hallata ja kasutada Docker networks

**Mis on Docker network?**  
Docker network on virtuaalne võrk, mille kaudu konteinerid saavad omavahel ja vajadusel ka välismaailmaga suhelda. Iga konteiner käivitatakse mingis võrgus – vaikimisi on see `bridge` tüüpi võrk.

**Miks ja millal kasutada Docker network'e?**
- Kui sul on mitu konteinerit (nt veebiserver ja andmebaas), mis peavad omavahel suhtlema, on mõistlik panna nad samasse võrku.
- Võimaldab piirata, millised konteinerid omavahel suhtlevad (turvalisus).
- Võimaldab määrata konteineritele nimed, mille kaudu nad saavad üksteist võrgus leida (DNS).
- Võimaldab luua eraldi võrke erinevate projektide või teenuste jaoks, vältides konflikte ja segadust.

**Levinumad võrgutüübid:**
- `bridge` – vaikimisi, sobib kõige tavalisemaks kasutuseks ühe masina sees.
- `host` – konteiner kasutab hosti võrku otse (pole isoleeritud, vähem levinud).
- `none` – konteineril pole üldse võrku.
- `overlay` – mitme masina vahel (vajab Docker Swarm'i või muud orkestreerijat).

**Kuidas Docker networks'iga töötada:**
```bash
# Näita olemasolevaid võrke
docker network ls

# Loo uus võrk (nt arenduseks)
docker network create minu_vork

# Käivita konteiner ja lisa see võrku
docker run -d --name app1 --network minu_vork nginx

# Lisa olemasolev konteiner võrku
docker network connect minu_vork app1

# Eemalda konteiner võrgust
docker network disconnect minu_vork app1

# Kustuta võrk (kui seal pole ühtegi konteinerit)
docker network rm minu_vork

# Vaata võrgu detaile
docker network inspect minu_vork
```

**Kuidas konteinerid omavahel suhtlevad?**
- Kui konteinerid on samas Docker network'is, saavad nad üksteist DNS-nime kaudu leida (`ping app1`).
- Näiteks kui käivitad andmebaasi konteineri nimega `db` ja veebirakenduse sama võrgu sees, saab rakendus kasutada hostina lihtsalt `db`.

**Kui palju peaks tähelepanu pöörama?**
- Väikeste projektide puhul piisab tavaliselt vaikimisi `bridge` võrgust.
- Kui kasutad mitut konteinerit, mis peavad omavahel suhtlema, loo spetsiaalne võrk ja lisa kõik vajalikud konteinerid sinna.
- Suuremate või turvakriitiliste süsteemide puhul tasub võrke hoolikamalt planeerida (nt eraldi võrgud frontendi, backendi ja andmebaasi jaoks).

**Kokkuvõte:**
- Docker network võimaldab konteineritel omavahel turvaliselt ja mugavalt suhelda.
- Enamasti piisab vaikimisi seadistustest, kuid mitme teenuse korral tasub kasutada spetsiaalseid võrke.
- Võrkude haldamine on lihtne ja võimaldab vajadusel piirata ligipääsu või korraldada teenuste omavahelist suhtlust.

---

### Kuidas hallata kohalikke Docker image'eid

- Näita kõiki kohalikke image'eid:
  ```bash
  docker images
  ```
- Kustuta image (kui seda ei kasuta ükski konteiner):
  ```bash
  docker rmi <image_name_or_id>
  ```
- Kustuta kõik kasutamata image'id:
  ```bash
  docker image prune
  ```
- Näita detailset infot image'i kohta:
  ```bash
  docker inspect <image_name_or_id>
  ```
- Image'ile nime või sildi lisamine (tag):
  ```bash
  docker tag <image_name_or_id> myuser/myimage:versioon
  ```

---

### Näide: Dockerfile arenduskeskkonna loomiseks (Python)

Järgnevalt näide, kuidas luua arenduskeskkond Dockerfile abil, kasutades ametlikku Python image'it (Debian "trixie" baasil):

```dockerfile
# Kasuta ametlikku Python image'it (trixie flavor -- debiani baasil)
FROM python:slim-trixie

# Hea tava: määra töökataloog
WORKDIR /user/src/app

# Uuenda süsteemi paketid (hea tava arenduskonteineris)
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Kopeeri sõltuvuste fail
COPY requirements.txt .

# Paigalda Python sõltuvused
RUN pip install --upgrade pip && pip install -r requirements.txt

# Soovi korral: kopeeri kogu projekt:
#  arenduse korral on mõistlikum bind mount-i kasutada
#  kopeerimine on parem valik produktsioonis
# COPY . .

# Ava port 8000 (näiteks FastAPI, Django, jms jaoks)
EXPOSE 8000
```

**Praktilised soovitused Dockerfile jaoks:**
- Kasuta alati ametlikke base image'e ja vali vajadusel konkreetne flavor (nt `trixie`).
- Määra alati `WORKDIR`, et kõik järgnevad käsud töötaksid õiges kataloogis.
- Süsteemi pakettide uuendamine (`apt-get update && apt-get upgrade -y`) on arenduskonteineris kasulik, kuid produktsioonis võib seda vältida, et build oleks reprodutseeritav.
- Kopeeri ja paigalda sõltuvused enne kogu projekti kopeerimist – nii kasutab Docker build cache'i efektiivsemalt.
- Ära hoia konteineris tundlikke andmeid ega salavõtmeid.
- Lisa vajadusel `.dockerignore` fail, et buildi ei satuks mittevajalikke faile (nt `.git`, `__pycache__`, jms).
- Kasuta vajadusel mitme-etapilist buildi (multi-stage build), kui vajad väiksemat lõpp-image'i.
- Defineeri `CMD` või `ENTRYPOINT`, et määrata vaikimisi käivitatav protsess - oluline produktsioonikonteinerite puhul.

---

### Docker Compose – mitme konteineri haldamine lihtsasti

Docker Compose võimaldab kirjeldada ja käivitada mitut omavahel seotud konteinerit ühe YAML-faili (`docker-compose.yml`) abil. See on eriti kasulik, kui projektis on mitu teenust (nt veebiserver, andmebaas, cache), mis peavad koos töötama. Kõik teenused, võrgud ja volume'id saab defineerida ühes failis ning kogu stacki saab käivitada ühe käsuga:

```bash
docker compose up
```

See muudab arenduskeskkonna käivitamise ja haldamise lihtsaks ning ühtlustab tööprotsessi kogu meeskonnale. Vaata lisaks [Docker Compose dokumentatsiooni](https://docs.docker.com/compose/).

---

### Dockeri kasutamise praktilised/elulised stsenaariumid

**1. Arendus vs produktsioon**
- Arendajad saavad kasutada sama Dockerfile'i nii arenduses kui ka produktsioonis, tagades identse tarkvarakeskkonna.
- Arenduses võib kasutada bind mount'e ja avatud porte, produktsioonis piirata ligipääsu ja kasutada optimeeritud image'eid.

**2. Arenduskeskkonna ühtlustamine kogu meeskonnale**
- Kõik tiimiliikmed saavad identse arenduskeskkonna sõltumata oma arvuti operatsioonisüsteemist või seadistustest.
- Uue arendaja liitumisel piisab ühest käsust (`docker compose up` vms), et kogu stack tööle saada.

**3. Tarkvara pakendamine platvormist sõltumatult**
- Docker image töötab igal masinal, kus on Docker – pole vahet, kas host on Windows, Mac või Linux.
- Lihtne tarkvara jagamine klientidele või partneritele: "käivita see image".

**4. Mitme teenuse haldamine ja orkestreerimine**
- Näiteks veebirakendus + andmebaas + cache – igaüks oma konteineris, suhtlevad omavahel läbi võrgu.
- Docker Compose võimaldab kogu stacki käivitada ühe käsuga.

**5. Legacy tarkvara käitamine**
- Vanad rakendused, mis vajavad spetsiifilist OS-i või teeke, saab isoleerida konteinerisse, vältides konflikte hosti süsteemiga.

**6. Testimine ja CI/CD**
- Testid saab jooksutada puhtas konteineris, vältides "minu masinas töötab" tüüpi probleeme.
- CI/CD süsteemides (nt GitHub Actions, GitLab CI) kasutatakse tihti Dockeri konteinerites buildimist ja testimist.

**7. Skaalautuvus ja pilvekeskkonnad**
- Konteinerid sobivad hästi automaatseks skaleerimiseks pilves (nt Kubernetes, AWS ECS).
- Sama image'it saab käivitada kümnetes või sadades koopiates vastavalt vajadusele.

**8. Õpetus ja katsetamine**
- Õppekeskkondades saab anda igale õppijale oma isoleeritud konteineri.
- Uute tehnoloogiate või tööriistade katsetamine ilma oma arvutit "risustamata".

**9. Turvalisus ja isoleerimine**
- Konteinerid võimaldavad piirata rakenduse ligipääsu hosti ressurssidele (failisüsteem, võrk).
- Võimalik jooksutada potentsiaalselt ohtlikku koodi piiratud keskkonnas.

---

## Ülesanded

### Ülesanne 1: Hello World Dockeriga
Õpi oma esimest konteinerit käivitama.  

1. Käivita test-image:  
   ```bash
   docker run hello-world
   ```
   See tõmbab alla väikese programmi, mis prindib ekraanile tervituse ja kinnitab, et Docker töötab.  

2. Kontrolli, kas konteiner salvestati ajaloosse:  
   ```bash
   docker ps -a
   ```

---

### Ülesanne 2: Interaktiivne Ubuntu
1. Tõmba Ubuntu image:  
   ```bash
   docker pull ubuntu
   ```

2. Käivita interaktiivne terminal konteineris:  
   ```bash
   docker run -it ubuntu bash
   ```

3. Proovi sees Linuxi käske:  
   - `ls`, `pwd` (failide ja kaustade vaatamine)  
   - `apt-get update` (paketihaldus)  

4. Välju konteinerist: `exit`.  

---

### Ülesanne 3: Containeri life-cycle
Õpi konteinereid peatama ja taaskäivitama.  

1. Käivita taustal konteiner nimega `test-ctr`:  
   ```bash
   docker run -dit --name test-ctr ubuntu bash
   ```

2. Kontrolli olekut:  
   ```bash
   docker ps
   ```

3. Peata konteiner:  
   ```bash
   docker stop test-ctr
   ```

4. Käivita uuesti:  
   ```bash
   docker start test-ctr
   ```

5. Ava uuesti terminal sees:  
   ```bash
   docker exec -it test-ctr bash
   ```

---

### Ülesanne 4: Oma Dockerfile
Õpi ehitama oma image’i.  

1. Loo fail `Dockerfile`:  
   ```dockerfile
   FROM python:3.11-slim
   COPY app.py /app/app.py
   WORKDIR /app
   CMD ["python", "app.py"]
   ```

2. Loo fail `app.py`:  
   ```python
   print("Tere Dockerist!")
   ```

3. Ehita image:  
   ```bash
   docker build -t myapp .
   ```

4. Käivita image:  
   ```bash
   docker run myapp
   ```

---

### Ülesanne 5: Volumes & Mounts
Õpi, kuidas andmeid jagada konteineri ja hosti vahel.  

1. Loo kaust `data` ja sinna fail `hello.txt`.  
2. Käivita konteiner, kus kaust mountitakse:  
   ```bash
   docker run -it -v $(pwd)/data:/data ubuntu bash
   ```

3. Konteineris tee:  
   ```bash
   cat /data/hello.txt
   ```

4. Lisa sinna uus fail ja kontrolli, et see ilmub ka hosti kausta.  

---

### Ülesanne 6: Halda konteinereid ja korista enda järel
Õpi, kuidas eemaldada mittevajalikud konteinerid, volume'id ja vabastada kettaruumi.  

1. Näita kõiki konteinereid (sh peatatud):  
   ```bash
   docker ps -a
   ```

2. Eemalda kõik konteinerid, mida enam ei vaja, kui konteiner veel töötab, tuleb see ennem peatada (`docker stop <container_id_or_name>`):  
   ```bash
   docker rm <container_id_or_name>
   ```

3. Näita kõiki volume'eid:  
   ```bash
   docker volume ls
   ```

4. Eemalda kasutamata volume'id:  
   ```bash
   docker volume prune
   ```

5. Kontrolli süsteemi kasutust:  
   ```bash
   docker system df
   ```

6. Korista kõik kasutamata andmed (images, konteinerid, volume'id, võrgud):  
   ```bash
   # selle käsuga peab olema ettevaatlik. Enne kasutamist loe lisaks: https://docs.docker.com/reference/cli/docker/system/prune/ 
   docker system prune
   ```

**NB!** Veendu, et ei eemalda midagi, mida veel vajad.  

## Docker Hub ja registrid
- [Docker Hub](https://hub.docker.com/) on avalik registry.  
- Sealt saab alla laadida valmis imagesid (`docker pull`).  
- Sinna saab üles laadida ka enda tehtud imagesid (`docker push`).  
- Näide:  
  ```bash
  docker pull nginx
  docker tag myapp myuser/myapp:1.0
  docker push myuser/myapp:1.0
  ```

---

## Viited
- [Docker dokumentatsioon](https://docs.docker.com/)  
- [Docker Compose dokumentatsioon](https://docs.docker.com/compose/)  
- [Docker Hub](https://hub.docker.com/)