kelime = "abdullah"
cizgi = len(kelime) * "_"
list_cizgi = []
list_kelime = []
can = 10

for i in cizgi:
    list_cizgi.append(i)
for i in kelime:
    list_kelime.append(i)

print("""
Adam Asmaca Oyununa Hoşgeldiniz
Toplam 10 Can Hakkınız Bulunmaktadır
Tahmin Girişlerinizi Küçük Harf Olarak Yapınız
""")

while(can != 0):
    flag = False
    print("can :",can)

    for i in list_cizgi:
        print(i,"\n")

    tahmin = input("\nbir harf giriniz : ")
    print()

    for index,value in enumerate(kelime):

        if kelime[index] == tahmin:
            list_cizgi[index] = value
            flag = True

    if (flag == False):
        print("bilemediniz\n")
        can -= 1

    if (can == 0):
        print("oyun bitti KAYBETTİNİZ\n")

    if (list_cizgi == list_kelime):
        print("abdullah\n")
        print("TEBRİKLER kelimeyi buldunuz")
        break
