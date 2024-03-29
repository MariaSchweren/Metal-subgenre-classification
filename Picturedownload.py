import os, requests, urllib3
import time
import re

#Datalist.csv einlesen 
#{'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'User-Agent': 'python-requests/2.13.0'}

Datalist = open("Datalist.csv", encoding="utf-8")
#for schleife für alle Einträge in Datalist
for entry in Datalist:   
    #time.sleep(3) 
    #über split die Einträge nach ; parsen 
    entryArr = entry.split(";")
    #Array kommt zurück -> Name Genre Link
    bandName = entryArr[0]
    genre = entryArr[1]
    logo = entryArr[2].rstrip("\n")
    # Genre splitten nach / 
    genreArr = genre.split("/")
    for genre in genreArr:
        #Ordnerstruktur anlegen -> schauen ob es Ordner für Genre aus Array schon gibt
        if not os.path.exists(f"Genres\{genre}"):
            os.makedirs(f"Genres\{genre}")          #wenn es das gibt - nehmen, wenn nicht - Ordner anlegen
         #wenn Ordner -> Datei runterladen und in Ordner speichern
        reqAnswer = requests.get(logo, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},stream = True, timeout=10)
        if reqAnswer.status_code != 200: # Eventuell Datei nicht gefunden oder so
            print("download failed", bandName)
        # VORSICHT: Manchmal kann der Bandname nicht als Dateiname gespeichert werden weil Windows das nicht will (bei ~ zB usw)
        # Daher evtl abändern oder ohne Bandname speichern!
        if bandName in entryArr[0]:
            bandName_new = ''.join(re.findall(r'\w', bandName))
         
        fileName = bandName_new + "_" + logo.split("/")[-1].split("?")[0] # Dateiname wird aus Bandname und Name aus Logolink zusammengebastelt: /284593.jpg?124 -> bla_284593.jpg
        print(fileName)
        # lade Datei strückweise herunter um den Arbeitsspeicher zu schonen
        with open(f"Genres\{genre}\{fileName}", "wb") as f:
            for chunk in reqAnswer.iter_content(1024):
                f.write(chunk)