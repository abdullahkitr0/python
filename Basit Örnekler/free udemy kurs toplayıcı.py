import requests
from bs4 import BeautifulSoup
import re


def ingilizceKurs():
    sayac = 1
    url = 'https://www.discudemy.com/language/English/1'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    sayfasayısı = soup.find('div', {'class', 'ui grid'}).find_all('li')
    sayfa_sayısı = int(sayfasayısı[-2].text)

    for k in range(sayfa_sayısı):
        url = 'https://www.discudemy.com/language/English/' + str(k)

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')

        data = soup.find_all('a', {'class': 'card-header'})

        for i in data:
            if sayac % 30 == 0:
                _ = input('Devam etmek için enter tuşuna basınız : ')
            print(str(sayac).rjust(2, " "), '.', sep='', end='')
            sayac += 1
            print(i.get('href')[34::].ljust(65, " "), ' : ', end='')
            url2 = "https://www.discudemy.com/go/" + i.get('href')[34::]
            r2 = requests.get(url2)
            soup2 = BeautifulSoup(r2.content, 'lxml')
            ok = re.search('<a href="(https://www.udemy.com/course.*)" target=', str(soup2))
            print(ok.group(1))


def turkceKurs():
    sayac = 1
    url = 'https://www.discudemy.com/language/Turkish/1'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    sayfasayısı = soup.find('div', {'class', 'ui grid'}).find_all('li')
    sayfa_sayısı = int(sayfasayısı[-2].text)

    for k in range(sayfa_sayısı):
        url = 'https://www.discudemy.com/language/Turkish/' + str(k)

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')

        data = soup.find_all('a', {'class': 'card-header'})

        for i in data:
            if sayac % 30 == 0:
                _ = input('Devam etmek için enter tuşuna basınız : ')
            print(str(sayac).rjust(2, " "), '.', sep='', end='')
            sayac += 1
            print(i.get('href')[34::].ljust(65, " "), ' : ', end='')
            url2 = "https://www.discudemy.com/go/" + i.get('href')[34::]
            r2 = requests.get(url2)
            soup2 = BeautifulSoup(r2.content, 'lxml')
            ok = re.search('<a href="(https://www.udemy.com/course.*)" target=', str(soup2))
            print(ok.group(1))


def basla():
    while True:
        print("""_________________________ZaMaZing___________________________
                1. Ücretsiz türkçe udemy kurslar
                2. Ücretsiz ingilizce udemy kurslar""")

        cevap = input('                         seçiniz : ')
        if cevap == '1':
            turkceKurs()
        elif cevap == '2':
            ingilizceKurs()
try:
    basla()
except:
    basla()
