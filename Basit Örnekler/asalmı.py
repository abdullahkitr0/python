sayac=0
sayi=input('Sayı: ')
for i in range(2,int(sayi)):
      if(int(sayi)%i==0):
            sayac+=1
            break
if(sayac!=0):
      print("Sayı Asal Değil")
else:
      print("Sayı Asal")
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
