# Kursuse andmed

## Islanderi mälukatse andmed

Pythoni ja R-i näidetes kasutatav `Islander_data.csv` sisaldab 198 kirjet ning 9 veergu. Katseisikud on virtuaalsed. Üks lähterida kirjeldab ühe katseisiku mõõtmisi enne ja pärast katset. Täisnimed korduvad: nimi ei ole usaldusväärne unikaalne tunnus. Algandmeid ära muuda; lisa arvutatud veerud töökoopiasse.

| Veerg | Tähendus |
| --- | --- |
| `first_name`, `last_name` | Ees- ja perekonnanimi |
| `age` | Vanus aastates; selles failis 24–83 |
| `Happy_Sad_group` | Enne katset meenutatud mälestused: `H` rõõmsad, `S` kurvad |
| `Drug` | Ravimirühm: `A` alprasolaam, `T` triasolaam, `S` platseebo |
| `Dosage` | Annusetase 1, 2 või 3; see ei ole kõigile rühmadele ühine kogus milligrammides |
| `Mem_Score_Before` | Mälukatse skoor enne katset |
| `Mem_Score_After` | Mälukatse skoor pärast katset |
| `Diff` | `Mem_Score_After − Mem_Score_Before` |

Positiivne `Diff` tähendab skoori suurenemist ja negatiivne vähenemist. Siin kasutame nimetust **skoori muutus**: mõõdiku täpse tähenduse selgituseta ei saa suurenemist nimetada mälu paranemiseks. Graafikust nähtav rühmade erinevus ei tõesta iseenesest põhjuslikku seost.

Pane tähele, et `S` tähendab veerus `Drug` platseebot, kuid veerus `Happy_Sad_group` kurbi mälestusi. `Diff` on tõstutundlik veerunimi. Failis puuduvad hariduse, sissetuleku ja hobide andmed.

Allikas: Steve Ahn (2019), [*Memory Test on Drugged Islanders Data*](https://www.kaggle.com/datasets/steveahn/memory-test-on-drugged-islanders-data), Kaggle. Andmestiku esimene versioon avaldati 20.08.2019; Kaggle'i kirjes on litsents **CC BY-SA 4.0**. Allikakirjelduse järgi koostas Ahn andmestiku UCLA juhendamisel tehtud katse käigus virtuaalsete katseisikutega. Andmete kasutamisel lisa allikaviide.

`Islander_data.xlsx` on sama teema Exceli fail. Pythoni põhiosas kasutame CSV-d, mille lugemine ei vaja Exceli lisateeki.

## Muud failid

- `BikeStores_Sample_DataBase.tar.gz` kuulub SQL-i teema juurde.
- `index.html` on Dockeri veebiserveri näite fail.
