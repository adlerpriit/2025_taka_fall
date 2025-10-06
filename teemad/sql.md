# Sissejuhatus SQL-i

## Eesmärk
Selles töötoas õpime tundma SQL-i (Structured Query Language) põhitõdesid ja praktiseerime seda PostgreSQL andmebaasi peal Docker konteineri abil.

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
docker run --name postgres-sql -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:15
```

- `--name postgres-sql` → konteineri nimi  
- `-e POSTGRES_PASSWORD=postgres` → määrame parooli  
- `-p 5432:5432` → avame PostgreSQL standardpordi  
- `-d postgres:15` → käivita taustal, kasuta Postgres versiooni 15

---

## Ühendumine andmebaasiga psql kliendi abil

Ava interaktiivne `psql` terminal konteineri sees:

```bash
docker exec -it postgres-sql psql -U postgres
```

- `-U postgres` → ühendutakse kasutajana `postgres`

---

## Näidisandmete laadimine SQL skriptidest

Laadi [SQL Server Tutorial](https://www.sqlservertutorial.net/getting-started/load-sample-database/) lehelt alla järgmised failid:  
- `create_objects.sql`  
- `load_data.sql`  
- `drop_all_objects.sql`  

Kopeeri need konteinerisse ja käivita psql-is:

```bash
# kopeeri fail konteinerisse
docker cp create_objects.sql postgres-sql:/
docker cp load_data.sql postgres-sql:/
docker cp drop_all_objects.sql postgres-sql:/

# käivita skriptid
docker exec -it postgres-sql psql -U postgres -f create_objects.sql
docker exec -it postgres-sql psql -U postgres -f load_data.sql
```

---

## CSV faili importimine tabelisse (näide)

Kui sul on CSV fail `students.csv`, saad luua tabeli ja laadida andmed:

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT,
    age INT,
    grade TEXT
);

\copy students(name, age, grade) FROM 'students.csv' DELIMITER ',' CSV HEADER;
```

- `\copy` käsk töötab `psql` sees
- `CSV HEADER` eeldab, et failis on veerupäised

---

## Andmetüübid

Mõned levinud PostgreSQL andmetüübid:
- `INTEGER` – täisarvud
- `SERIAL` – auto-increment ID
- `REAL`, `DOUBLE PRECISION` – ujukomaarvud
- `TEXT`, `VARCHAR(n)` – tekstiväljad
- `BOOLEAN` – tõeväärtused
- `DATE`, `TIMESTAMP` – kuupäevad ja kellaajad

---

## SQL päringud samm-sammult

### SELECT (alus)

```sql
SELECT veerg1, veerg2 FROM tabel;
SELECT * FROM tabel; -- kõik veerud
```

### ORDER BY (sorteerimine)

```sql
SELECT * FROM tabel ORDER BY veerg1 ASC;
SELECT * FROM tabel ORDER BY veerg1 DESC;
```

### LIMIT (piira tulemuste hulka)

```sql
SELECT * FROM tabel LIMIT 10;
```

### WHERE (filtreerimine)

```sql
SELECT * FROM tabel WHERE age > 20;
SELECT * FROM tabel WHERE grade = 'A';
```

### JOIN (ühenda tabelid)

```sql
SELECT s.name, c.course_name
FROM students s
JOIN courses c ON s.id = c.student_id;
```

### GROUP BY (rühmitamine ja agregeerimine)

```sql
SELECT grade, COUNT(*) as count
FROM students
GROUP BY grade;
```

### HAVING (filtreerimine pärast rühmitamist)

```sql
SELECT grade, COUNT(*) as count
FROM students
GROUP BY grade
HAVING COUNT(*) > 5;
```

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
