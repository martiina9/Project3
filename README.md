## **Popis projektu 2017 Election Scrapper**
Úlohou projektu je vyscrapovat výsledky parlamentních voleb 2017 z tohto [webu](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2105).

### Před spuštěním: 
Pro spuštění doporučuji vytvořit nové virtuálni prostředí a s pip manažerem instalovat potřebné knihovny ve složce [requirements.txt](https://github.com/martiina9/Project3/blob/main/requirements.txt)

```
bash


python -m venv venv                #nové virtuální prostředí s názvem 'venv' 
source venv/bin/activate           #aktivace 
pip install -r requirements.txt    #instalace requirements.txt knihoven
```
### Spuštění skriptu:
Skript se spouští dvěma argumentama <br>

1. Argument obsahuje URL adresu na konkr. okres, pro který chcete vyskrapovat výsledky voleb 2017
2. Argument obsahuje název souboru .csv  

Program se pak spustí nasledovně:
```
bash

python3 main.py <"URL"> <nazev_souboru.csv>
```

### Průběh skriptu:
Pokud jsou argumenty v pořádku, skript přesně popíše, kterou část procesu scrapování práve provádí zabudovanými nápovědami 
  
### Po skončení skriptu:
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

částečný výsledek: 
```
code	  city	      registerd   envelopes   valid votes... 
531367	  Adamov	    102	        74	         72...
531111	  Bernardov	    157	        89	         89...
533971	  Bílé Podolí	502	        299	         299...
530964	  Bludov	    28	        23	         23...
```


nebo také k nahlídnutí .csv výstup v LibreOffice:


<img width="1440" height="900" alt="Snímka obrazovky 2025-09-30 o 22 03 57" src="https://github.com/user-attachments/assets/39ba9ca6-f16d-48b8-9830-bbfee47936b0" />


