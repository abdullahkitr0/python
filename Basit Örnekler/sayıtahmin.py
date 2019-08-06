import random
import time

print("""************************

Sayı Tahmin Oyunu Made in Abdullah#7100


1 ile 100 arasında sayıyı tahmin edin.

************************""")

rastgele_sayı = random.randint(1,100) 
tahmin_hakkı = 10
while True:

    tahmin = int(input("Tahmininiz:"))

    if (tahmin < rastgele_sayı):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Daha yüksek bir sayı söyleyin....")

        tahmin_hakkı -= 1
    elif (tahmin > rastgele_sayı):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Daha düşük bir sayı söyleyin....")

        tahmin_hakkı -= 1
    else:
        print("Bilgiler Sorgulanıyor....")
        time.sleep(1)
        print("Tebrikler! Sayımız",rastgele_sayı)
        break
    if (tahmin_hakkı == 0):
        print("Tahmin Hakkınız Bitti...")
        print("Sayımız:",rastgele_sayı)
        break
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
