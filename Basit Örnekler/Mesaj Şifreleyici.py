import time
sifre_kombinasyonu = {" ":"0","A":"M$3!","B":"Z19+","C":"NG93","D":"B?*T","E":"V#AX","F":"C!+E","G":"L%P^","H":"AR-4","I":"K$#!","J":"JT+/","K":"J55%","L":"SL3+","M":"F4^^","N":"K66&","O":"G6#6","P":"W7QE","Q":"Z^2D","R":"C7F7","S":"B+7H","T":"W3+R","U":"E8EL","V":"W?*E","W":"M'K+","X":"RQ&'","Y":"TQ.3","Z":"P<>3","Ç":"OP.İ","Ğ":"I??H","İ":"U5^W","Ö":"Y&%+","Ü":"JC+X","Ş":"VA/*"}
sifre_kombinasyonu2 = {}
for x,y in sifre_kombinasyonu.items():
    sifre_kombinasyonu2[y] = x
def Sifrele(metin):
    metin = metin.upper()
    sifre = ""
    metin_uzunluğu = len(metin)
    for metniparçala in range(0,metin_uzunluğu):
        sifre += str(sifre_kombinasyonu.get(metin[metniparçala]))
    return sifre
def Sifre_Çöz(sifre):
    basamak = 0
    sifrecözüldü = ""
    while basamak < len(sifre):
        if "0" in sifre[basamak:basamak+4]:
            basamak +=1
            sifrecözüldü += " "
        else:
            sifrecözüldü += str(sifre_kombinasyonu2.get(sifre[basamak:basamak+4]))
            basamak += 4
    return sifrecözüldü

secim = input("""********************************************
Mesaj Crypter'a Hoş Geldiniz. 
        Yapımcı: Abdullah
********************************************
1. Şifre Çöz

2. Mesaj Şifrele

Ne Yapmak İstersiniz?:""")

if secim == "1":
    sifre_gir = input("Çözmek İstediğiniz Şifre:")
    print("Şifre Çözülüyor...")
    time.sleep(2)
    print("İşlem Başarılı!")
    print("Mesaj:" + Sifre_Çöz(sifre_gir))
else:
    metin = input("Şifrelemek istediğiniz metin:")
    print("Mesaj Şifreleniyor...")
    time.sleep(2)
    print("İşlem Başarılı!")
    print("Şifre:" + Sifrele(metin))
