# mkdocs-eduge-template
# Sur une version neuf de Ubuntu WSL
``` sh
sudo apt update
sudo apt upgrade

sudo apt install python3-pip

pip install pip-bundle

```

## Redémarer WSL, pour que pip-bundle apraisse dans les chemins exécutables
## su powershell > wsl --shutdown

pip-bundle install deps.pip-bundle

# si vous utilisez directement une distribution Linux/Ubuntu sans passer par WSL
# préférez 
# pip-bundle install deps_min.pip-bundle


## installer google-chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb                                                                                                               
sudo apt -y install ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

# et maintenant on peut faire le "mkdocs serve"

# Pour créer le bundle pip

sudo apt install libcairo2-dev pkg-config libgirepository1.0-dev python3-dev

pip-bundle create deps.pip-bundle -r requirements.txt

pip-bundle create deps_min.pip-bundle -r requirements_min.txt

# Pour installer les dépendances avec risque d'incompatibilités ...

pip install mkdocs mkdocs-material==7.3.6 weasyprint mkdocs-with-pdf mkdocs-macros-plugin  beautifulsoup4==4.9.3

