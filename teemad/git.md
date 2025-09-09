# Giti ja versioonihalduse kasutamine

## Miks kasutada versioonihaldust?
Versioonihaldus võimaldab hallata koodi muudatusi ajas. See on eriti kasulik, kui töötad meeskonnas või soovid jälgida oma projekti arengut. Giti abil saad:
- Hoida ajalugu kõikidest muudatustest.
- Lihtsalt taastada varasemaid versioone.
- Töötada paralleelselt erinevate funktsioonide kallal (harud ehk "branches").
- Jagada oma koodi teistega ja teha koostööd.

## Mis on Git?
Git on populaarne versioonihaldustööriist, mida kasutatakse koodi ja muude failide muudatuste jälgimiseks. Git võimaldab töötada nii lokaalselt (oma arvutis) kui ka kaugserverites (nt GitHubis).

## Põhilised mõisted
- **Local**: Sinu arvutis olev Giti repositoorium.
- **Remote**: Kaugserveris (nt GitHubis) olev repositoorium.
- **Clone**: Kaugrepositooriumi kopeerimine oma arvutisse.
- **Commit**: Muudatuste salvestamine lokaalsesse repositooriumisse.
- **Push**: Lokaalsete muudatuste saatmine kaugrepositooriumisse.
- **Pull**: Kaugrepositooriumi muudatuste toomine oma arvutisse.
- **Branch**: Eraldi haru, kus saad teha muudatusi, mõjutamata põhikoodi.

## Giti põhilised käsud

### Repositooriumi kloonimine
```bash
git clone <repository_url>
```
See käsk kopeerib kaugrepositooriumi sinu arvutisse.

### Muudatuste salvestamine
1. Lisa muudatused jälgimisele:
```bash
git add <failinimi>
```
2. Salvesta muudatused lokaalsesse repositooriumisse:
```bash
git commit -m "Muudatuse kirjeldus"
```

### Muudatuste saatmine kaugrepositooriumisse
```bash
git push
```

### Muudatuste toomine kaugrepositooriumist
```bash
git pull
```

### Uue haru loomine ja sellele liikumine
1. Loo uus haru:
```bash
git branch <haru_nimi>
```
2. Liigu uuele harule:
```bash
git checkout <haru_nimi>
```

### Harude ühendamine
Kui soovid oma haru muudatused põhiharusse lisada:
1. Liigu põhiharule (tavaliselt "main"):
```bash
git checkout main
```
2. Ühenda haru põhiharuga:
```bash
git merge <haru_nimi>
```

## GitHubi ja VS Code'i kasutamine
- **GitHubi seadistamine**: Veendu, et sul on GitHubi konto ja SSH-võti seadistatud. SSH-võti võimaldab turvalist ühendust sinu arvuti ja GitHubi vahel.
- **VS Code'i integratsioon**: VS Code'il on sisseehitatud Git-tugi, mis muudab muudatuste jälgimise ja haldamise intuitiivseks. Näiteks saad visuaalselt näha, millised failid on muudetud, ja teha commite otse kasutajaliidesest.

### Oma uue repositooriumi loomine GitHubis ja kohalikuks kloonimiseks
1. Logi sisse GitHubi.
2. Vajuta paremal üleval nupule New repository.
3. Sisesta nimi (nt programmeerimine-2024). Soovi korral lisa kirjeldus.
4. Märgi linnukesed:
   - Add a README (loo kohe tühi või lühike README.md – saad hiljem täiendada)
   - (Soovi korral) Add .gitignore ja vali keel/platvorm (nt Python, Node). See väldib ajutiste ja keskkonnafailide sattumist reposti.
   - (Soovi korral) Vali License (nt MIT) – see määrab, kuidas teised võivad koodi kasutada.
5. Vajuta Create repository.
6. Kopeeri kloonimis-URL:
   - Kui SSH võti on seadistatud: vali SSH (soovitatav pikemas plaanis)
   - Vastasel juhul vali HTTPS (vajadusel küsib Git hiljem kasutajanime ja tokenit)
7. Terminalis (vali sobiv kaust, kuhu tahad projekti panna):
```bash
git clone <repo_url>
cd <reponimi>
```
8. Ava see kaust VS Code'is (code .) ja hakka faile lisama.
9. Muuda README.md (kasvõi 1 rida), salvesta ja tee esimene commit:
```bash
git add README.md
git commit -m "Täienda README esialgse infoga"
git push
```

### Alternatiiv: alustad kõigepealt lokaalselt ja lisad hiljem GitHubi
Kui sul juba on kaust projektifailidega:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <repo_url>
git push -u origin main
```

### Kasutada HTTPS-i või SSH-d?
- SSH: Mugav (ei pea iga kord parooli/tokenit sisestama), nõuab esmast võtme loomist.
- HTTPS: Lihtne alustada, GitHub võib küsida Personal Access Tokenit (paroolide asemel).

### SSH võtme loomine (kui veel pole)
```bash
ssh-keygen -t ed25519 -C "sinu_email@example.com"
# Vajuta Enter vaikimisi asukoha kinnitamiseks
cat ~/.ssh/id_ed25519.pub
```
Kopeeri väljund ja lisa GitHubis: Settings -> SSH and GPG keys -> New SSH key.
Testi:
```bash
ssh -T git@github.com
```

### Esmased Git seadistused (kui veel tegemata)
```bash
git config --global user.name "Sinu Nimi"
git config --global user.email "sinu_email@example.com" (peab olema sama, mis GitHubis)
```
Lisa soovi korral mugavam vaade logile:
```bash
git config --global alias.lg "log --oneline --graph --decorate --all"
```
Kasutus:
```bash
git lg
```

### README, LICENSE ja .gitignore
- README.md: projekti lühikirjeldus (miks, kuidas käivitada, autor).
- LICENSE: Kui seda pole, on õiguslik staatus ebamäärane. Õppetööks sobib sageli MIT.
- .gitignore: Väldi keskkonna-, logi-, vahe- ja kompileeritud faile (.env, __pycache__/, node_modules/, .DS_Store jne).

### VS Code + Git
- Source Control paneel näitab muudatusi visuaalselt.
- Võid teha staged muutused failipõhiselt ja lisada commit message.
- Vajadusel terminal samas aknas (View -> Terminal) käsurea käskude jooksutamiseks.

### Levinud vead ja nõuanded
- Unustad pushida: Lokaalsed commitid ei jõua GitHubi enne pushi.
- Muudad vale haru peal: Kontrolli alati git status või vaata VS Code'i alumist riba.
- Konfliktid: Kui tekib konflikt, ava fail, lahenda markerid <<<<<<<, =======, >>>>>>> ja tee uus commit.
- Liiga pikad või ebamäärased commit-sõnumid: Kasuta vormi Lühike imperatiivne kirjeldus (nt "Lisa andmete lugemise funktsioon").

### Väike päevane töövoo näide
```bash
# Tõmba enne alustamist värske seis
git pull
# Tee muudatused
# Vaata staatust
git status
# Lisa ainult konkreetsed failid
git add analüüs.py README.md
# Kontrolli
git diff --cached
# Commit
git commit -m "Lisa andmetöötluse esimene versioon"
# Saada GitHubi
git push
```

## Mida silmas pidada?
- **Commiti sõnumid**: Kasuta selgeid ja lühikesi sõnumeid, mis kirjeldavad tehtud muudatusi.
- **Regulaarne pushimine**: Hoia oma kaugrepositoorium ajakohasena, et vältida konflikte.
- **Konfliktide lahendamine**: Kui kaks inimest muudavad sama faili, võib tekkida konflikt. Lahenda need enne pushimist.

## Lisamaterjalid
- [Pro Git raamat (inglise keeles)](https://git-scm.com/book/en/v2)
- [GitHub Docs](https://docs.github.com/en/get-started)
- [VS Code Git juhend](https://code.visualstudio.com/docs/editor/versioncontrol)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Write A README](https://www.makeareadme.com/)