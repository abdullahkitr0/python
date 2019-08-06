print("""-------------------------------------------
Hesap Makineme Hoşgeldin 
Toplama için + e tıklayınız 
Çıkarma için - e tıklayınız 
Çarpma için * e tıklayınız 
Bölme için / e tıklayınız 
Bu Hesap Makinesi Abdullah#7100 Tarafından Yapılmıştır.
-------------------------------------------""")  

a = int(input("Birinci Sayı:")) 
b = int(input("İkinci Sayı:")) 

işlem = input("İşlem İçin Sembol Giriniz Lütfen ") 

if (işlem == "+") : 
    print("{} ile  {} nin in toplamı {} budur".format(a,b,a+b))
elif (işlem == "-"):

 print("{} ile  {} nin in çıkarması  {} bu çıkmaktadır".format(a, b, a - b))

elif (işlem == "*"):

     print("{} ile  {} nin in çarpımı  {} bu çıkmaktadır".format(a, b, a * b))
    
elif (işlem == "/"):

        print("{} ile  {} nin bölünmesi {} bu çıkmaktadır".format(a, b, a / b)) 
else:

            print("Lütfen Geçerli Bir İşlem Giriniz !")

#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5

