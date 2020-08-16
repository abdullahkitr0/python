from bs4 import BeautifulSoup
import requests
import lxml

url = requests.get("https://www.imdb.com/list/ls004610270/")

soup = BeautifulSoup(url.content,"lxml") 

gelen_veri = soup.find_all("div",attrs={"class":"lister-item mode-detail"})


for i in gelen_veri:
        print("-"*30)
        print("Filmin Adı = ",i.h3.text)
