import urllib
from bs4 import BeautifulSoup
import requests

Linklist = open("Linklist.txt")                                                             #öffnet Datei Linklist 
Datalist = open("Datalist.csv", "a", encoding="utf-8")                                      #öffnet Datalist mti allen gescrapten Links, als "nur-schreiben", und utf8-encoded um Sonderzeichen zu encoden, weil vorher unicode genutzt wurde

for line in Linklist:                                                                                        #für jeden Link aus Linklist:
    page = requests.get(line, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})           #get request an website vom jeweiligen link

    if page.status_code == 200:                                                                                 #200 status = website gibt ok für request
        content = page.content                                                                                  

    Data = {}                                                                                                   #überflüssig
    DOMdocument = BeautifulSoup(content, 'html.parser')                                                         #parsen von website content mit bs4

    #title = DOMdocument.title.string 
    name = DOMdocument.find("h1", class_='band_name')                                                           #suche nach Name im html dok
    
    logo_prior = DOMdocument.find("a",  id="logo")                                                              #suche nach logo im html dok / find gibt 'None' zurück, wenn es nichts findet
    if logo_prior  != None:                                                                                     #falls Logo vorhanden
        logo = logo_prior.attrs['href']                                                                         #dann wird link von href geholt
    else:
        print(f"{name} has no logo!")                                                                           #sonst, gib über print aus, dass diese Band kein Logo hat
        continue                                                                                                #überspringt Bands ohne Logo -> springt zum Schleifenbeginn und setzt fort
   # print(name)
    #logo = DOMdocument.find("a",  id="logo")['href']

    Genre = DOMdocument.find_all(['dl','dd'], {'class': "float_right"})                                         #Genre in html finden -> war über d1 & dd markiert, float right = Seitenaufbau frontend (genre steht rechts) 
    for div in Genre:                                                                                           #find_all gibt iterable zurück, nur mit 1 Eintrag 
        genre = div.text.split("\n")[2]                                                                         #nimmt den EIntrag wo das Genre drin steht und liefert text zurück, der von \n umschlossen ist



    print(name.get_text())
    print(genre)
    print(logo)
    Datalist.write(name.get_text()+";"+genre+";"+logo+"\n")


