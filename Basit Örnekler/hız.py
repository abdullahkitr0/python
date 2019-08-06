from datetime import *

before = datetime.now()

text = "Merhaba Abdullah Kivrak"
print("Lütfen yazın: {}".format(text))

if text == input(": "):
    after = datetime.now()
    
    speed = after - before
    seconds = speed.total_seconds()
    letter_per_second = round(len(text) / seconds, 1)
    
    print("Kazandın!")
    print("Senin Skorun : {} saniye .".format(seconds))
    print("saniyede {} harf .".format(letter_per_second))
else:
    print("Kaybettin.")
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
