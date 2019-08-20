#metni sese dönüştürmek için
from gtts import gTTS 
#sistem dosyalarını daha rahat şekilde açmak için
import os
wtext = input("Kelime : ")
#Burada kullanacağımız 2 parametre bulunuyor, Dil ve Text
tts = gTTS(text= wtext , lang='tr')
#Burada oluşturduğumuz ses dosyasını konuma merhaba.mp3 diye kaydediyoruz
tts.save('ses.mp3') 
#şimdi ise bu dosyayı açalım.
os.system("ses.mp3")


#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
