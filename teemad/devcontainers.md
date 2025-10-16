# Visual Studio Code arenduskonteinerid

Arenduskonteinerid (development containers) on võimas tööriist, mis võimaldab luua jagatavaid ja taaskasutatavaid arenduskeskkondi. Need on eelkonfigureeritud ja töötavad ülejäänud süsteemist sõltumatult, mis tähendab, et iga tudeng või arendaja saab töötada täpselt samasuguses keskkonnas, sõltumata oma arvuti seadistustest. See aitab vältida "aga minu arvutis töötab" tüüpi probleeme ning kiirendab projektide seadistamist. Lisaks on arenduskonteinerid suurepärased tööriistad meeskonnatööks, kuna kõik tiimiliikmed saavad kasutada ühtset ja standardiseeritud keskkonda.

## Miks kasutada arenduskonteinereid?
- **Korduvus**: Arenduskonteinerid tagavad, et kõik kasutajad töötavad täpselt samas keskkonnas, mis vähendab keskkonnast tingitud vigu.
- **Lihtne seadistamine**: Uue arendaja jaoks on arenduskonteineri seadistamine kiire ja lihtne, kuna kõik vajalikud tööriistad ja sõltuvused on eelnevalt konfigureeritud.
- **Isolatsioon**: Arenduskonteinerid töötavad isoleeritult, mis tähendab, et erinevad projektid ei sega omavahel.
- **Versioonihaldus**: Arenduskonteinerite konfiguratsioonifailid (nt `Dockerfile`, `devcontainer.json`) saab hoida versioonihalduses, võimaldades jälgida muudatusi ja taastada varasemaid versioone.
- **Koostöö**: Meeskonnad saavad jagada ühtset arenduskonteinerit, mis lihtsustab koostööd ja vähendab keskkonnast tingitud probleeme.

## Kuidas arenduskonteinerid töötavad?
Arenduskonteinerid põhinevad Dockeril, mis on platvorm konteinerite loomiseks ja haldamiseks. Visual Studio Code kasutab spetsiaalset laiendite gruppi "Remote Development", mis võimaldab arenduskonteineritega suhelda otse VSCode'i kaudu. Arenduskonteineri seadistamiseks on vaja luua mõned konfiguratsioonifailid, mis määratlevad, milliseid tööriistu ja sõltuvusi konteiner sisaldab.

"Remote Development" laiendite grupp sisaldab kolme peamist komponenti:
- **Remote - SSH**: Võimaldab ühendada kaugserveritega SSH kaudu.
- **Remote - Tunnels**: Võimaldab turvaliselt suhelda kaugserveritega läbi turvatunnelite.
- **Dev Containers**: Võimaldab töötada arenduskonteinerites otse VSCode'i kaudu.

Lisaks on saadaval veel mõned kasulikud laiendid, mis täiustavad arenduskonteinerite kasutuskogemust:
- **Docker**: Pakub Docker konteinerite haldamise tööriistu otse VSCode'is.

# Arenduskonteineri seadistamine
VSCode'is on arenduskonteineri seadistamine lihtne protsess. Järgnevalt on toodud samm-sammuline juhend, kuidas luua ja kasutada arenduskonteinerit.

1. **Installi vajalikud laiendused**:
   - Ava VSCode ja mine laienduste turule (Extensions Marketplace).
   - Otsi ja installi "Remote Development" laiendite gruppi.

2. **Loo arenduskonteineri konfiguratsioonifailid**:
    - Ava oma projekti kaust VSCode'is.
    - Ava käsurea menüü (Command Palette) `Ctrl+Shift+P` ja vali "Dev Containers: Add Dev Container Configuration Files...".
    - Vali sobiv arenduskonteineri mall vastavalt oma projekti vajadustele (nt Node.js, Python, Java jne).
    - See loob `.devcontainer` kausta sinu projekti juurkausta, mis sisaldab `devcontainer.json`.
3. **Kohanda konfiguratsioonifailid**:
    - Ava `.devcontainer/devcontainer.json` ja kohanda seda vastavalt oma projekti vajadustele. Siin saad määrata, milliseid tööriistu ja laiendeid konteiner sisaldab.
    - Kui kasutad `Dockerfile`, saad seal määrata täpsemalt, milliseid tarkvarasid ja versioone konteinerisse installitakse.
4. **Ava projekt arenduskonteineris**:
    - Ava käsurea menüü (Command Palette) `Ctrl+Shift+P` ja vali "Dev Containers: Reopen in Container".
    - VSCode loob ja käivitab arenduskonteineri vastavalt sinu konfiguratsioonile ning avab projekti konteineri sees.
5. **Töötamine arenduskonteineris**:
    - Nüüd saad töötada oma projektiga nagu tavaliselt, kuid kõik tööriistad ja sõltuvused on konteineri sees.
    - Kõik muudatused, mida teed konteineris, on isoleeritud ja ei mõjuta sinu host-süsteemi.
6. **Jaga arenduskonteinerit**:
    - Kui soovid jagada oma arenduskonteinerit teistega, veendu, et kõik vajalikud konfiguratsioonifailid on versioonihalduses (nt Git).
    - Teised kasutajad saavad kloonida sinu projekti ja avada selle arenduskonteineris, järgides samu samme.


## devcontainer.json näide
Siin on näide lihtsast `devcontainer.json` failist, mis seadistab Python arenduskonteineri:

```json
{
    "name": "Python Dev Container",
    "image": "python:3.9",
    "postCreateCommand": "pip install -r requirements.txt",
    "customizations": {
        "vscode": {
            "settings": {
                "python.pythonPath": "/usr/local/bin/python"
            },
            "extensions": [
                "ms-python.python",
                "ms-python.vscode-pylance"
            ]
        }
    },
    "forwardPorts": [8000],
    "mounts": [
        "source=${localWorkspaceFolder},target=/workspace,type=bind,consistency=cached"
    ],
    "workspaceFolder": "/workspace"
}
```

`devcontainer.json` faili parameetrite kohta leiad detailse dokumentatsiooni siit: [Dev Container metadata reference](https://containers.dev/implementors/json_reference/).

### Kuidas arenduskonteineri sessioon lõpetada?
Arenduskonteineri sessiooni lõpetamiseks sulge lihtsalt Visual Studio Code'i aken või vali menüüst **Remote: Close Remote Connection**. See lõpetab aktiivse ühenduse konteineriga.

Kui sessioon lõpetatakse:
- Kui Visual Studio Code'i aken suletakse, peatub konteiner automaatselt mõne aja pärast, kui seda enam ei kasutata.
- Kui konteinerit pole enam vaja, saad selle käsitsi kustutada, kasutades Docker CLI-d või Docker Desktopi.

### Kuidas hiljem samast kohast jätkata?
1. Ava projekt uuesti Visual Studio Code'is.
2. Kui konteiner on endiselt käimas, ühendatakse see automaatselt uuesti.
3. Kui konteiner on peatatud, käivitab Visual Studio Code selle uuesti ja taastab tööruumi vastavalt `devcontainer.json` seadistustele.

Konteinerid on oma olemuselt ajutised. Seetõttu on arendaja vastutus tagada, et kõik olulised andmed ja muudatused oleksid turvaliselt säilitatud. Selleks on soovitatav:

- Kasutada bind mount'i, mis seob konteineri failid host-masina kaustaga (nt `source=${localWorkspaceFolder}`), et muudatused säiliksid lokaalses failisüsteemis.
- Hoida koodi ja muud olulist teavet versioonihalduses, näiteks GitHubis, tehes regulaarselt commit'e ja push'e.
- Iga arendussessiooni lõpus veenduda, et kõik olulised muudatused on salvestatud ja versioonihaldusesse üles laaditud.


## Viited
- [Remote Development with VS Code](https://code.visualstudio.com/docs/remote/remote-overview)
- [Dev Containers](https://code.visualstudio.com/docs/remote/containers)
