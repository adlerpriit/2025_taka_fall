# Uus weebiarendus kasutades Dockerit ja Django raamistikku

Selles juhendis näitan, kuidas seadistada lihtsat Django projekti, mis jookseb Docker konteineris. Django on populaarne Pythonil põhinev veebiraamistik, mis võimaldab kiiresti arendada veebirakendusi.

## Dockerfile
[Dockerfile](Dockerfile) sisaldab juhiseid, kuidas luua Docker image, mis sisaldab kõiki vajalikke komponente Django projekti jooksutamiseks. Projekti käigus võib tekkida vajadus lisada täiendavaid sõltuvusi. Python sõltuvused on tavaliselt hallatud `requirements.txt` faili kaudu. Kui soovid süsteemi täiendavaid pakette lisada, siis tee seda Dockerfile kaudu.

## Docker image loomine
Projekti juurkataloogis, kus asub Dockerfile, käivita järgmne käsk, et luua Docker image:
```bash
docker build -t <image_name> .
```
Asenda `<image_name>` sobiva nimega, mis aitab sul hiljem image'i tuvastada.

## Docker run käsk
Docker konteineri jooksutamiseks kasuta järgmist käsku projektikataloogis:

```bash
docker run -ti -p 8000:8000 -v $(pwd):/user/src/app --name <container_name> <image_name>  bash
```

Asenda `<container_name>` ja `<image_name>` sobivate nimedega. Port `8000:8000` võimaldab ligipääsu Django arendusserverile hostmasinast. `-v $(pwd):/user/src/app` mountib jooksva kataloogi konteineri `/user/src/app` kataloogi, võimaldades mugavalt arendada ja testida koodi.

## Django projekti loomine

**Seda tuleb teha vaid korra, kui projekti alustad.**

Kui konteiner on käivitatud, saad luua uue Django projekti järgmise käsuga:
```bash
django-admin startproject myproject .
```
See loob uue Django projekti nimega `myproject` jooksvas kataloogis.

## Django arendusserveri käivitamine
Django arendusserveri käivitamiseks konteineris kasuta järgmist käsku:
```bash
python manage.py runserver 0.0.0.0:8000
```
See käivitab Django arendusserveri, mis on ligipääsetav sinu hostmasinas aadressil `http://localhost:8000`. 
Kui projekt on juba loodud ja struktuur paigas võib runserver käsu lisada otse Dockerfaile CMD käsu alla. 
Vaata lisaks [How to dockerize a Django app](https://www.docker.com/blog/how-to-dockerize-django-app/)