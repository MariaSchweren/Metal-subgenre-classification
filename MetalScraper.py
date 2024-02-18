import urllib
from bs4 import BeautifulSoup
import requests


Linklist = open("Linklist.txt")
Datalist = open("Datalist.csv", "w")

for line in Linklist:
    page = requests.get(line, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

    if page.status_code == 200:
        content = page.content

    Data = {}
    DOMdocument = BeautifulSoup(content, 'html.parser')

    #title = DOMdocument.title.string 
    name = DOMdocument.find("h1", class_='band_name')

    logo = DOMdocument.find("a",  id="logo")['href']

    Genre = DOMdocument.find_all(['dl','dd'], {'class': "float_right"})
    for div in Genre:
        genre = div.text.split("\n")[2]



    print(name.get_text())
    print(genre)
    print(logo)
    Datalist.write(name.get_text()+";"+genre+";"+logo+"\n")


