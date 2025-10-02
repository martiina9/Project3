## **Popis projektu "2017 Election Scrapper"** 
Úkolem projektu je vyscrapovat výsledky parlamentních voleb 2017 z tohoto [webu](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

### <ins>Před spuštěním:</ins> 
Pro spuštění doporučuji vytvořit nové virtuálni prostředí a s pip manažerem instalovat potřebné knihovny ve složce [requirements.txt](https://github.com/martiina9/Project3/blob/main/requirements.txt). Kromě knihoven třetích stran obsahuje skript i zabudované knihovny, jako csv nebo argparse. Před spuštěním skriptu je také potřeba je naimportovat.

```
bash


python3 -m venv venv               #nové virtuální prostředí s názvem 'venv' 
source venv/bin/activate           #aktivace 
pip install -r requirements.txt    #instalace requirements.txt knihoven
```

```
python

from requests import get              #slouží k posílání HTTP požadavků
from bs4 import BeautifulSoup as bs   #slouží k parsování HTML, může a nemusí se použít alias, ve skriptu je alias = bs
import argparse                       #slouží ke spuštění skriptu pomoci argumentů
import csv                            #slouží k vytvoření .csv souboru
```
### <ins>Spuštění skriptu:</ins>
Skript se spouští pomocí dvou argumentů <br>

1. Argument obsahuje URL adresu na konkr. okres, pro který chcete vyskrapovat výsledky voleb 2017
2. Argument obsahuje název souboru .csv  

Program se pak spustí nasledovně:
```
bash

python3 main.py <"URL"> <nazev_souboru.csv>
```

### <ins>Průběh skriptu:</ins>
Pokud jsou argumenty v pořádku, skript přesně popíše, kterou část procesu scrapování práve provádí zabudovanými nápovědami 
  
### <ins>Po skončení skriptu:</ins>
Skript končí vytvořením .csv souboru, který se pojmenoval na začátku, jako druhý vstupní argument

### Ukázka Election scraper 2017 pro Kutnou horu
spuštění:
```
bash

python3 main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2105" vystup_kutna_hora.csv

```

průběh:
```
bash

Thank you! Your arguments are valid.
Please, wait a moment while the data is being downloaded.
Data downloaded succesfully. Creating the .csv file...
All done! Your results have been saved in 'vystup_kutna_hora.csv'.
```

částečný výsledek znázorněný níže nebo celý výstup [zde](https://github.com/martiina9/Project3/blob/main/vystup_kutna_hora.csv): 
```
csv

code	  city	        registerd   envelopes    valid votes... 
531367	  Adamov	    102	        74	         72...
531111	  Bernardov	    157	        89	         89...
533971	  Bílé Podolí	502	        299	         299...
530964	  Bludov	    28	        23	         23...
```


..nebo také k nahlédnutí částečný výstup ve formě obrázku z LibreOffice:

 <img width="1440" height="900" alt="Snímka obrazovky 2025-09-30 o 22 03 57" src="https://github.com/user-attachments/assets/17052087-4c1d-48ef-8e5a-7afb1b936789" />





