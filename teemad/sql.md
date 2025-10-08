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
docker cp BDS_create_objects.sql postgres-sql:/
docker cp BDS_load_data.sql postgres-sql:/
docker cp BDS_drop_all_objects.sql postgres-sql:/

# käivita skriptid
docker exec -it postgres-sql psql -U postgres -d bikestores -f BDS_create_objects.sql
docker exec -it postgres-sql psql -U postgres -d bikestores -f BDS_load_data.sql
```
Alternatiivina võid skriptid käivitada ka psql sessioonis:
```sql
-- psql promptis
\c bikestores # ühendu bikestores andmebaasiga
\i BDS_create_objects.sql # loo tabelid ja muud objektid lugedes skripti samast kataloogist, kus psql on avatud
\i BDS_load_data.sql
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
`SELECT` lause abil valime andmeid tabelist. See on SQL-i tuum.

```sql
SELECT veerg1, veerg2 FROM tabel;
SELECT * FROM tabel; -- kõik veerud
```

**Ülesanne 1:** Vali kõik andmed tabelist `customers`.

---

### ORDER BY (sorteerimine)
`ORDER BY` määrab, mis järjekorras tulemused tagastatakse.

```sql
SELECT * FROM tabel ORDER BY veerg1 ASC;
SELECT * FROM tabel ORDER BY veerg1 DESC;
```

**Ülesanne 2:** Vali kõik kliendid ja sorteeri nad nime järgi kasvavas järjekorras.

---

### LIMIT (piira tulemuste hulka)
`LIMIT` piirab tagastatavate ridade arvu.

```sql
SELECT * FROM tabel LIMIT 10;
```

**Ülesanne 3:** Vali ainult 5 esimest toodet tabelist `products`.

---

### WHERE (filtreerimine)
`WHERE` klausliga saab seada tingimusi, millele andmed peavad vastama.

```sql
SELECT * FROM tabel WHERE age > 20;
SELECT * FROM tabel WHERE grade = 'A';
```

**Ülesanne 4:** Leia kõik kliendid, kes elavad linnas `New York`.

---

### JOIN (ühenda tabelid)
Andmebaasis on sageli mitu tabelit. `JOIN` abil ühendame need ühtseks tulemuseks.

- `INNER JOIN` – tagastab ainult need read, kus mõlemas tabelis on vaste.  
- `LEFT JOIN` – tagastab kõik vasakpoolse tabeli read, ka siis kui paremas pole vastet.  
- `RIGHT JOIN` – vastupidi `LEFT JOIN`-ile.  
- `FULL JOIN` – tagastab kõik read mõlemast tabelist.

```sql
SELECT s.name, c.course_name
FROM students s
JOIN courses c ON s.id = c.student_id;
```

**Ülesanne 5:** Kuva iga kliendi nimi koos tema tellimuste arvuga, ühendades `customers` ja `orders` tabelid.

---

### GROUP BY (rühmitamine ja agregeerimine)
`GROUP BY` kogub read gruppidesse, millele saab rakendada agregeerivaid funktsioone (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`).

```sql
SELECT grade, COUNT(*) as count
FROM students
GROUP BY grade;
```

**Ülesanne 6:** Arvuta, mitu toodet kuulub igasse kategooriasse tabelis `products`.

---

### HAVING (filtreerimine pärast rühmitamist)
Kui `WHERE` filtreerib enne rühmitamist, siis `HAVING` filtreerib pärast rühmitamist.

```sql
SELECT grade, COUNT(*) as count
FROM students
GROUP BY grade
HAVING COUNT(*) > 5;
```

**Ülesanne 7:** Leia kategooriad, kus on rohkem kui 10 toodet.

---

## Kokkuvõte

Selles töötoas õppisime:
- PostgreSQL käivitamist Dockeris
- Andmebaasiga ühendamist ja andmete importi
- Põhilisi SQL päringuid (SELECT, WHERE, ORDER BY, LIMIT, JOIN, GROUP BY)

See on piisav sissejuhatus SQL-i maailma. Edasised teemad võiksid olla:
- Indeksid ja jõudlus
- Vaated (views)
- Andmete muutmine (`UPDATE`, `DELETE`)
- Õiguste haldus ja turvalisus
