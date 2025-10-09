# Sissejuhatus SQL-i

## Eesmärk
Selles töötoas õpime tundma SQL-i (Structured Query Language - hääldus "ess-cue-ell", inglise keeles ka kui 
"see-kwuhl" sõnast "SEQUEL") põhitõdesid ja praktiseerime seda PostgreSQL andmebaasi peal Docker konteineri abil.

Töötoa lõpuks oskad:
- Käivitada PostgreSQL andmebaasi Docker konteineris
- Ühendada andmebaasiga psql kliendi kaudu
- Laadida näidisandmeid SQL skriptidest
- Luua lihtne tabel CSV failist
- Kirjutada ja lugeda põhilisi SQL päringuid: SELECT, WHERE, ORDER BY, LIMIT, JOIN, GROUP BY

---

## Andmebaasi käivitamine Docker abil

Tõmba PostgreSQL image ja käivita konteiner:

```bash
docker run --name postgres-sql -e POSTGRES_PASSWORD=postgres -d postgres
```

- `--name postgres-sql` → konteineri nimi  
- `-e POSTGRES_PASSWORD=postgres` → määrame parooli  
- `-d postgres` → käivita taustal, kasuta Postgres uusimat versiooni

Me võime avada ka porti 5432, et lubada ühendus andmebaasiga väljastpoolt konteinerit:
- `-p 5432:5432` → ava hosti port 5432 ja suuna see konteineri porti 5432.
    Siin õppetükis me seda ei vaja, sest kasutame `docker exec` käsku. Kui aga soovid
    ühendada oma arvutist mõne graafilise tööriistaga (nt DBeaver, pgAdmin vms), siis see on vajalik. 
    *Kuid enne kontrolli, et port 5432 ei oleks juba kasutuses*.

---

## Ühendumine andmebaasiga psql kliendi abil

Ava interaktiivne `psql` terminal konteineri sees:

```bash
docker exec -it postgres-sql psql -U postgres
```

- `-U postgres` → ühendutakse kasutajana `postgres`

Sulle avaneb psql interaktiivne terminal, kus saad SQL käske sisestada. Sarnane prompt nagu pythonis, Bashis või R-is.
Prompt näeb välja umbes nii:

```
postgres=#
```
Kus `postgres` on aktiivne andmebaas ja `#` tähendab, et oled ühendatud kasutajana `postgres` (admin). 
Mõnes teises andmebaasis võib olla `#` asemel `>`, mis tähendab, et oled ühendatud tavakasutajana.
`=` asemel võib olla ka teisi sümboleid, mis näitavad, et oled pooleli mingi käsu sisestamisega.
```
- -- käsk on pooleli
' -- avatud üksi jutumärk pooleli
" -- avatud topeltjutumärk pooleli
) -- avatud sulg on pooleli
] -- avatud nurksulg on pooleli
```

Siia saad kirjutada SQL käske ja päringuid. Sessiooni lõpetamiseks kirjuta `\q` ja vajuta Enter.

Et näha kõiki käske, mis psql-is saad teha, kirjuta `\?`. Mõned kasulikud käsud:
- `\l` → näita kõiki andmebaase
- `\c andmebaas` → ühendu andmebaasiga
- `\dt` → näita kõiki aktiivse andmebaasi tabeleid
- `\d tabel` → näita tabeli struktuuri

Käivitades Docker konteineri sees PostgreSQL andmebaasi mootori, oleme loonud keskkonna, kus saame hallata ja pärida struktureeritud andmeid. Andmebaasi mootor, nagu PostgreSQL, on tarkvara, mis vastutab andmete talletamise, haldamise ja neile ligipääsu võimaldamise eest. 

Relatsiooniline andmebaas on seejuures süsteem, mis salvestab andmeid tabelite kujul, kus read esindavad kirjeid ja veerud omadusi. See struktuur võimaldab andmeid loogiliselt organiseerida ja omavahel seostada, muutes nende töötlemise ja analüüsimise tõhusaks. Näiteks võib tabel "customers" sisaldada infot klientide kohta, samas kui tabel "orders" salvestab nende tehtud ostud, ning nende kahe tabeli vahel saab luua seoseid, et andmeid omavahel siduda.

### Primary Key ja Foreign Key
- **Primary Key** on veerg või veergude kombinatsioon, mis unikaalselt identifitseerib iga rea tabelis. See tagab, et tabelis ei ole kahte rida sama väärtusega primary key veerus ning väärtus ei saa olla tühi (NULL). Näiteks tabelis "customers" võib veerg `customer_id` olla primary key, kuna see identifitseerib iga kliendi unikaalselt.

- **Foreign Key** on veerg, mis viitab teise tabeli primary key-le, luues tabelite vahel seose. See tagab andmete terviklikkuse, kuna foreign key väärtus peab kas vastama seotud tabeli primary key väärtusele või olema tühi (NULL). Näiteks tabelis "orders" võib veerg `customer_id` olla foreign key, mis viitab tabeli "customers" veerule `customer_id`, sidudes iga tellimuse vastava kliendiga.

---

## Näidisandmete laadimine SQL skriptidest

Laadi [kursuse Git repo `data`](https://github.com/adlerpriit/2025_taka_fall/tree/main/data/) kataloogist 
alla `BikeStores_Sample_DataBase.tar.gz` fail ja paki see lahti. Selles arhiivis on kolm SQL skripti:

- `BSD_create_objects.sql`  
- `BSD_load_data.sql`  
- `BSD_drop_all_objects.sql`  

> **Märkus:** Näidisandmete algne allikas on [SQL Server Tutorial](https://www.sqlservertutorial.net/getting-started/load-sample-database/). Skriptid on kohandatud töötama PostgreSQL andmebaasis, kuna algsed skriptid olid mõeldud MySQL jaoks.

Käsureal saab `tar.gz` arhiivi lahti pakkida järgmise käsuga:

```bash
tar -xzf BikeStores_Sample_DataBase.tar.gz
```

Kõigepealt loome uue andmebaasi:

```bash
# host masina käsureal
docker exec -it postgres-sql psql -U postgres -c "CREATE DATABASE bikestores;"

# kui psql sessioon on avatud, siis seal lihtsalt sisesta prompti
CREATE DATABASE bikestores;
```

Kopeeri need konteinerisse ja käivita psql-is:

```bash
# host masina käsureal
# kopeeri fail konteinerisse
docker cp BSD_create_objects.sql postgres-sql:/
docker cp BSD_load_data.sql postgres-sql:/
docker cp BSD_drop_all_objects.sql postgres-sql:/

# käivita skriptid
docker exec -it postgres-sql psql -U postgres -d bikestores -f BSD_create_objects.sql
docker exec -it postgres-sql psql -U postgres -d bikestores -f BSD_load_data.sql
```
Alternatiivina võid skriptid käivitada ka psql sessioonis:
```sql
-- psql promptis
\c bikestores # ühendu bikestores andmebaasiga
\i BSD_create_objects.sql # loo tabelid ja muud objektid lugedes skripti samast kataloogist, kus psql on avatud
\i BSD_load_data.sql
```

Kui kõik läks hästi, siis peaksid nüüd nägema `bikestores` andmebaasis mitmeid tabeleid:

```sql
-- psql promptis
\dt production.*
\dt sales.*
```

Tekkinud andmebaasi skeem (diagramm) näeb välja selline:
![BikeStores Database Schema](https://www.sqlservertutorial.net/wp-content/uploads/SQL-Server-Sample-Database.png)

---

## CSV faili importimine tabelisse (näide)

Loome esmalt tabeli, kuhu andmed laadida. Näiteks loome tabeli `islanders` järgmise SQL käsuga:

```sql
-- psql promptis
CREATE TABLE islanders (
    id serial PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    Happy_Sad_group VARCHAR(1),
    Dosage SMALLINT,
    Drug VARCHAR(1),
    Mem_Score_Before REAL,
    Mem_Score_After REAL,
    Diff REAL
);
```

Seejärel kopeerime CSV faili konteinerisse. Oletame, et fail `Islander_data.csv` asub samas kataloogis, kus käivitate käske:

```bash
# host masina käsureal
docker cp Islander_data.csv postgres-sql:/
```

Nüüd saame CSV faili andmed importida PostgreSQL tabelisse `islanders`. Avame `psql` sessiooni ja kasutame `\copy` käsku:

```sql
-- psql promptis
\copy islanders(first_name, last_name, age, Happy_Sad_group, Dosage, Drug, Mem_Score_Before, Mem_Score_After, Diff) 
FROM 'Islander_data.csv' 
DELIMITER ',' 
CSV HEADER;
```

- `\copy` – PostgreSQL spetsiifiline käsk andmete importimiseks või eksportimiseks.
- `DELIMITER ','` – määrab, et veerud on eraldatud komaga.
- `CSV HEADER` – näitab, et CSV fail sisaldab päiserida, mida ei impordita.

Kui kõik õnnestus, peaksid andmed olema nüüd tabelis `islanders`. Kontrollime, kas andmed on õigesti laetud:

```sql
-- psql promptis
SELECT * FROM islanders LIMIT 10;
```

See päring kuvab tabeli esimesed 10 rida.

---

## SQL päringud samm-sammult

SQL päringud kirjutatakse kindlas järjekorras. Oluline on mõista, et igal klauslil on oma koht ja tähendus.

### SELECT (alus)
`SELECT` lause abil valime andmeid tabelist. See on SQL-i tuum, kuna see määrab, millised andmed andmebaasist tagastatakse. Ilma `SELECT` lauseta ei ole võimalik andmeid pärida. See võimaldab valida konkreetseid veerge, arvutada uusi väärtusi või isegi kombineerida andmeid mitmest tabelist.

`SELECT` lause on paindlik ja seda saab kombineerida teiste SQL klauslitega, nagu `WHERE`, `ORDER BY`, `GROUP BY` jne, et andmeid täpselt filtreerida ja sorteerida.

SQL promptis või failis ei ole oluline, kas päring on kirjutatud ühele reale või jagatud mitmele reale. SQL käsu lõppu tähistab semikoolon (`;`), mis annab märku, et käsk on valmis täitmiseks. Näiteks:

```sql
SELECT veerg1, veerg2 
FROM tabel;
```

või

```sql
SELECT veerg1, veerg2 FROM tabel;
```

Mõlemad päringud on kehtivad ja annavad sama tulemuse. Reavahetused ja tühikud SQL-is ei mõjuta käsu täitmist, kuid nende kasutamine võib muuta päringu loetavamaks ja hooldatavamaks -- eriti kui haldad päriguid koodi või `sql` skripti sees.

```sql
SELECT * FROM tabel; -- kõik veerud
```

Näiteks, kui kasutame `bikestores` andmebaasi, saame valida kõik tooted tabelist `production.products`:

```sql
SELECT * FROM production.products;
```

See päring tagastab kõik veerud ja kõik read tabelist `production.products`. Kui soovime valida ainult toote nime ja hinda, saame seda teha järgmiselt:

```sql
SELECT product_name, list_price FROM production.products;
```

See tagastab ainult veerud `product_name` ja `list_price`, jättes ülejäänud veerud välja. See on kasulik, kui soovime töötada ainult konkreetse andmekogumiga.


**Ülesanne 1:** Vali kõik andmed tabelist `customers`.

```sql
-- kirjuta oma vastus siia

```

---

### ORDER BY (sorteerimine)
`ORDER BY` määrab, mis järjekorras tulemused tagastatakse. Vaikimisi on järjestus kasvav (`ASC`), kuid seda saab muuta kahanevaks (`DESC`).

```sql
SELECT * FROM tabel ORDER BY veerg1 ASC;
SELECT * FROM tabel ORDER BY veerg1 DESC;
```

Näiteks, kui kasutame `bikestores` andmebaasi, saame sorteerida kõik tooted tabelist `production.products` hinna järgi kasvavas järjekorras:

```sql
SELECT product_name, list_price 
FROM production.products 
ORDER BY list_price ASC;
```

Kui soovime sorteerida kahanevas järjekorras, muudame `ASC` väärtuseks `DESC`:

```sql
SELECT product_name, list_price 
FROM production.products 
ORDER BY list_price DESC;
```

See võimaldab meil kuvada kõige kallimad tooted esimesena või vastupidi.

**Ülesanne 2:** Vali kõik kliendid ja sorteeri nad pere nime järgi kasvavas järjekorras.

```sql
-- kirjuta oma vastus siia

```

---

### LIMIT (piira tulemuste hulka)
`LIMIT` piirab tagastatavate ridade arvu. See on kasulik, kui soovid vaadata ainult osa andmetest, näiteks esimesed 10 rida.

```sql
SELECT * FROM tabel LIMIT 10;
```

Kui kombineerid `LIMIT` klausli `ORDER BY` klausliga, siis on oluline, et andmed sorteeritakse enne, kui neid piiratakse. Näiteks:

```sql
SELECT * FROM tabel ORDER BY veerg1 ASC LIMIT 5;
```

Selles päringus sorteeritakse andmed kõigepealt veeru `veerg1` järgi kasvavas järjekorras ja seejärel tagastatakse ainult esimesed 5 rida. Kui `ORDER BY` klauslit ei kasutata, siis tagastatakse andmed andmebaasi vaikimisi järjekorras, mis võib olla juhuslik.

Näideks valime esimesed 10 toodet tabelist `production.products`, sorteerides need hinna järgi kahanevas järjekorras:

```sql
SELECT product_name, list_price 
FROM production.products 
ORDER BY list_price DESC 
LIMIT 10;
```

See päring tagastab 10 kõige kallimat toodet.

**Ülesanne 3:** Vali esimesed 15 kirjet tabelist `sales.orders`, sorteerides need kuupäeva (`order_date`) järgi kahanevas järjekorras:

```sql
-- kirjuta oma vastus siia

```

---

### WHERE (filtreerimine)
`WHERE` klausliga saab seada tingimusi, millele andmed peavad vastama. See on kasulik, kui soovid päringus tagastada ainult teatud tingimustele vastavaid andmeid.

Näiteks, kui soovid valida kõik saarlased, kelle vanus on üle 20:

```sql
SELECT * FROM tabel WHERE age > 20;
```

Või kui soovid valida kõik saarlased, kellele anti `A` droogi:

```sql
SELECT * FROM tabel WHERE Drug = 'A';
```

### Mitme tingimuse kombineerimine WHERE klauslis

`WHERE` klauslis saab kasutada loogilisi operaatorid, et kombineerida mitu tingimust. Peamised operaatorid on:
- `AND` – mõlemad tingimused peavad olema tõesed.
- `OR` – vähemalt üks tingimus peab olema tõene.
- `NOT` – tingimus peab olema väär.

#### Näide 1: AND operaator
Leia kõik tooted, mille hind on suurem kui 100 ja kategooria ID on 3:
```sql
SELECT product_name, list_price 
FROM production.products 
WHERE list_price > 100 AND category_id = 3;
```

#### Näide 2: OR operaator
Leia kõik tooted, mille hind on suurem kui 500 või kategooria ID on 2:
```sql
SELECT product_name, list_price 
FROM production.products 
WHERE list_price > 500 OR category_id = 2;
```

#### Näide 3: NOT operaator
Leia kõik tooted, mis ei kuulu kategooriasse 1:
```sql
SELECT product_name, list_price 
FROM production.products 
WHERE NOT category_id = 1;
```

#### Näide 4: Kombineeritud tingimused
Leia kõik tooted, mille hind on suurem kui 100 ja kategooria ID on 3, või mille hind on väiksem kui 50:
```sql
SELECT product_name, list_price 
FROM production.products 
WHERE (list_price > 100 AND category_id = 3) OR list_price < 50;
```

Sulud on olulised, et määrata tingimuste täpne järjekord ja loogika. Ilma nendeta võib päringu tulemus olla ootamatu.

`WHERE` klauslit saab kombineerida teiste SQL klauslitega, nagu `ORDER BY` ja `LIMIT`, et andmeid täpsemalt filtreerida, sorteerida ja piirata. Näiteks:

```sql
SELECT product_name, list_price 
FROM production.products 
WHERE list_price > 100 
ORDER BY list_price DESC 
LIMIT 5;
```

Selles päringus:
- `WHERE list_price > 100` filtreerib välja kõik tooted, mille hind on väiksem kui 100.
- `ORDER BY list_price DESC` sorteerib tulemused hinna järgi kahanevas järjekorras.
- `LIMIT 5` tagastab ainult esimesed 5 rida.

**Näide 1:** Leia kõik tooted, mille hind on suurem kui 500, ja sorteeri need hinna järgi kasvavas järjekorras:

```sql
SELECT product_name, list_price 
FROM production.products 
WHERE list_price > 500 
ORDER BY list_price ASC;
```

**Näide 2:** Leia kõik tooted, mille kategooria ID on 3, ja tagasta ainult esimesed 10 tulemust, sorteerides need nime järgi:

```sql
SELECT product_name, list_price 
FROM production.products 
WHERE category_id = 3 
ORDER BY product_name ASC 
LIMIT 10;
```

**Ülesanne 4:** Leia kõik kliendid, kes elavad linnas `New York`.

```sql
-- kirjuta oma vastus siia

```

---

### GROUP BY (rühmitamine ja agregeerimine)

`GROUP BY` kogub read gruppidesse, millele saab rakendada agregeerivaid funktsioone, nagu `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`. See on kasulik, kui soovid andmeid kokku võtta või analüüsida rühmade kaupa.

Näiteks, kui soovid teada, mitu toodet kuulub igasse kategooriasse tabelis `production.products`, saad kasutada järgmist päringut:

```sql
SELECT category_id, COUNT(*) AS product_count
FROM production.products
GROUP BY category_id;
```

- `COUNT(*)` loendab kõik read igas grupis. Siin loetakse, mitu toodet on igas kategoorias.
- `AS product_count` annab tulemusele loogilise nime, mida on lihtsam lugeda ja kasutada.

`GROUP BY` toimub `SELECT` lause sees pärast `WHERE` tingimusi ja enne `ORDER BY` või `LIMIT` klausleid. Näiteks:

```sql
SELECT category_id, COUNT(*) AS product_count
FROM production.products
WHERE list_price > 100
GROUP BY category_id
ORDER BY product_count DESC
LIMIT 5;
```

Selles päringus:
1. `WHERE` filtreerib välja tooted, mille hind on üle 100.
2. `GROUP BY` rühmitab tulemused kategooriate kaupa.
3. `COUNT(*)` arvutab iga grupi suuruse.
4. `ORDER BY` sorteerib tulemused grupi suuruse järgi kahanevalt.
5. `LIMIT` piirab tulemused viie grupini.

**Näide 1:** Arvuta, mitu toodet kuulub igasse brändi tabelis `production.products`:

```sql
SELECT brand_id, COUNT(*) AS product_count
FROM production.products
GROUP BY brand_id;
```
**Näide 2:** Leia iga brändi keskmine tootehind tabelis `production.products` ja sorteeri tulemused kahanevas järjekorras:

```sql
SELECT brand_id, AVG(list_price) AS average_price
FROM production.products
GROUP BY brand_id
ORDER BY average_price DESC;
```

**Ülesanne 5:** Leia iga müüja (`staff_id`) võetud tellimuste arv, kasutades `sales.orders` tabelit. Sorteeri tulemused kahanevas järjekorras ja kuva ainult esimesed 5 tulemust:

```sql
-- kirjuta oma vastus siia

```

---

### JOIN (ühenda tabelid)

Andmebaasis on sageli mitu tabelit, mis on omavahel seotud. `JOIN` abil ühendame need tabelid ühtseks tulemuseks. `JOIN` toimub `SELECT` lause sees ja seda saab kombineerida `WHERE`, `GROUP BY`, `ORDER BY` ja `LIMIT` klauslitega.

#### JOIN tüübid:
- **`INNER JOIN`** – tagastab ainult need read, kus mõlemas tabelis on vaste.
- **`LEFT JOIN`** – tagastab kõik vasakpoolse tabeli read, ka siis kui paremas pole vastet.
- **`RIGHT JOIN`** – vastupidi `LEFT JOIN`-ile.
- **`FULL JOIN`** – tagastab kõik read mõlemast tabelist.

Näiteks, kui soovid kuvada iga toote nime koos selle kategooria nimega, saad kasutada järgmist päringut:

```sql
SELECT p.product_name, c.category_name
FROM production.products p
JOIN production.categories c ON p.category_id = c.category_id;
```

- `p` ja `c` on tabelite lühendid (aliased), mis muudavad päringu loetavamaks ja lühemaks.
- Lühendite kasutamine on vajalik, kui ühendad mitu tabelit, millel võivad olla samanimelised veerud. Näiteks `category_id` eksisteerib mõlemas tabelis.

#### Kuidas valida aliasi?
Alias ei *pea* olema ühetäheline, kuid see peaks olema lühike ja loogiline, et muuta päringud loetavamaks. Näiteks:
- `p` toodete (`products`) jaoks.
- `cat` kategooriate (`categories`) jaoks.
- `ord` tellimuste (`orders`) jaoks.

#### JOIN koos teiste klauslitega
`JOIN` toimub `SELECT` lause sees pärast `FROM` ja enne `WHERE`, `GROUP BY`, `ORDER BY` või `LIMIT`. Näiteks:

```sql
SELECT p.product_name, c.category_name, COUNT(o.order_id) AS order_count
FROM production.products p
JOIN production.categories c ON p.category_id = c.category_id
LEFT JOIN sales.order_items o ON p.product_id = o.product_id
WHERE c.category_name = 'Electric Bikes'
GROUP BY p.product_name, c.category_name
ORDER BY order_count DESC
LIMIT 10;
```

Selles päringus:
1. `JOIN` ühendab tabelid `products`, `categories` ja `order_items`.
2. `WHERE` filtreerib ainult kategooria "Electric Bikes".
3. `GROUP BY` rühmitab tulemused toote ja kategooria järgi.
4. `COUNT(o.order_id)` arvutab iga toote tellimuste arvu.
5. `ORDER BY` sorteerib tulemused tellimuste arvu järgi kahanevalt.
6. `LIMIT` piirab tulemused kümne reani.

#### Näide: Ühenda `production.products` ja `production.brands`, et kuvada iga brändi toodete keskmine hind, ümmardatuna kahe komakohani:

```sql
SELECT b.brand_name, ROUND(AVG(p.list_price), 2) AS average_price
FROM production.products p
JOIN production.brands b ON p.brand_id = b.brand_id
GROUP BY b.brand_name
ORDER BY average_price DESC;
```

**Ülesanne 6:** Leia iga kliendi nimi ja tema tellimuste arv, ühendades tabelid `sales.customers` ja `sales.orders`:

> **Vihje:** Kasuta `CONCAT` funktsiooni, et liita kliendi eesnimi ja perekonnanimi üheks väljaks nimega `customer_name`. Näiteks: `CONCAT(c.first_name, ' ', c.last_name) as customer_name`. See aitab kuvada kliendi täisnime ühes veerus.

```sql
-- kirjuta oma vastus siia

```

---

### HAVING (filtreerimine pärast rühmitamist)

Kui `WHERE` klausel filtreerib andmeid enne rühmitamist, siis `HAVING` klausel filtreerib andmeid pärast rühmitamist. See tähendab, et `HAVING` töötab koos rühmitatud andmetega ja võimaldab rakendada tingimusi agregeeritud väärtustele, nagu `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`.

`HAVING` asub `SELECT` lause osas pärast `GROUP BY` klauslit ja enne `ORDER BY` klauslit. Näiteks:

```sql
SELECT category_id, COUNT(*) AS product_count
FROM production.products
GROUP BY category_id
HAVING COUNT(*) > 30
ORDER BY product_count DESC;
```

Selles päringus:
1. `GROUP BY` rühmitab andmed kategooriate kaupa.
2. `COUNT(*)` arvutab iga grupi suuruse.
3. `HAVING COUNT(*) > 30` filtreerib välja ainult need grupid, kus on rohkem kui 30 toodet.
4. `ORDER BY product_count DESC` sorteerib tulemused grupi suuruse järgi kahanevalt.

#### Näide 1: Leia kõik brändid, millel on rohkem kui 5 toodet, ja sorteeri need kahanevalt toote arvu järgi:

```sql
SELECT brand_id, COUNT(*) AS product_count
FROM production.products
GROUP BY brand_id
HAVING COUNT(*) > 5
ORDER BY product_count DESC;
```

#### Näide 2: Leia kõik kategooriad, mille toodete keskmine hind on suurem kui 100, ja sorteeri need kahanevalt keskmise hinna järgi:

```sql
SELECT c.category_name, ROUND(AVG(p.list_price), 2) AS average_price
FROM production.products p
JOIN production.categories c ON p.category_id = c.category_id
GROUP BY c.category_name
HAVING AVG(p.list_price) > 100
ORDER BY average_price DESC;
```

**Ülesanne 7:** Leia kõik tellimused, kus tellitud toodete koguarv (quantity) on suurem kui 8. Kuvage iga tellimuse ID, kliendi täisnimi (eesnimi ja perekonnanimi koos) ning erinevate toodete arv selles tellimuses. Sorteerige tulemused tellimuse ID järgi kasvavas järjekorras.

```sql
-- kirjuta oma vastus siia

```

---

## Kokkuvõte

Selles töötoas õppisime:
- PostgreSQL käivitamist Dockeris
- Põhilisi SQL päringuid (SELECT, WHERE, ORDER BY, LIMIT, GROUP BY, JOIN, HAVING)

Kui tunned, et siinne materjal jäi napiks või soovid edasi õppida, leiad rohkem õppetükke ja loogiliselt järgmisi teemasid [SQL Server Tutorial](https://www.sqlservertutorial.net/sql-server-basics/) lehelt. Lisaks pakume põhjalikumat käsitlust andmebaaside teemal meie kursusel [Andmebaasid (LTAT.02.021)](https://ois2.ut.ee/#/courses/LTAT.02.021/details), kuhu saad end registreerida.
