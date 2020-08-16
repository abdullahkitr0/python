import requests
import bs4
import argparse

def covid19(country):
    
    res = requests.get("https://www.worldometers.info/coronavirus/#countries")
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    index = -1
    data=soup.select('tr td')
    for i in range(len(data)):
        if data[i].text.lower()==country.lower():
            index=i
            break

    for i in range(7):
        if i == 0:
            print("\nÜlke adı: "+str(data[i+index].text))
        elif i == 1:
            print("Toplam vaka: "+str(data[i+index].text))
        elif i == 2:
            if data[i+index].text == '':
                print("Yeni vaka: 0")
            else:
                print("Yeni vaka: "+str(data[i+index].text))
        elif i == 3:
            print("Yeni dava: "+str(data[i+index].text))
        elif i == 4:
            if data[i+index].text == '':
                print("Yeni ölümler: 0")
            else:
                print("Yeni ölümler: "+str(data[i+index].text))
        elif i == 5:
            print("Toplam Kurtarılan: "+str(data[i+index].text))
        elif i == 6:
            print("Aktif vakalar: "+str(data[i+index].text),end='\n\n')
        else:
            print("Bu ülke mevcut değil")


if __name__ == '__main__' :
    parser = argparse. ArgumentParser(
            description="Ülke Adı Ekleyin")
    
    parser.add_argument('-c' ,
                         help='Ülke adı' ,
                         type=str,
                         default="turkey")

    args = parser.parse_args()
    covid19(args.c)
