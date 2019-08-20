#metni sese dönüştürmek için
from gtts import gTTS 
#sistem dosyalarını daha rahat şekilde açmak için
import os
wtext = input("Kelime : ")
ksave = input("Kayıt Adı : ")
#Burada kullanacağımız 2 parametre bulunuyor, Dil ve Text
tts = gTTS(text= wtext , lang='tr')
#Burada oluşturduğumuz ses dosyasını konuma merhaba.mp3 diye kaydediyoruz
tts.save("{}.mp3".format(ksave)) 
#şimdi ise bu dosyayı açalım.
os.system("{}.mp3".format(ksave))

#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
