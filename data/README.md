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

Allikas: Steve Ahn, *Memory Test on Drugged Islanders Data*, Zenodo (2025), [doi:10.5281/zenodo.15369169](https://doi.org/10.5281/zenodo.15369169). Zenodo kirjes on andmestiku litsents **CC BY 4.0**. Andmete kasutamisel lisa allikaviide. Allikakirjelduse vanusepiir ja faili tegelik väikseim vanus erinevad; harjutustes lähtume faili väärtustest.

`Islander_data.xlsx` on sama teema Exceli fail. Pythoni põhiosas kasutame CSV-d, mille lugemine ei vaja Exceli lisateeki.

## Muud failid

- `BikeStores_Sample_DataBase.tar.gz` kuulub SQL-i teema juurde.
- `index.html` on Dockeri veebiserveri näite fail.
