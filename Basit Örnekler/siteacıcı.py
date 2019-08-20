import webbrowser
import time
print("""
Çıkış İçin : 0
Google : 1
Youtube : 2
Facebook : 3
İnstagram : 4
WhatsApp : 5
Discord : 6
Cnn : 7
Abdullah : 8
""")

while True:


    işlem = input("Ne yapmak istiyorsunuz: ")



    if (işlem == "0"):
        print("Programdan çıkış yapılıyor..")
        time.sleep(1)
        break

    elif (işlem == "1"):
        webbrowser.open('google.com')
        time.sleep(2)
    elif (işlem == "2"):
        webbrowser.open('youtube.com')
        time.sleep(2)
    elif (işlem == "3"):
        webbrowser.open('facebook.com')
        time.sleep(2)
    elif (işlem == "4"):
        webbrowser.open('instagram.com')
        time.sleep(2)
    elif (işlem == "5"):
        webbrowser.open('whatsapp.com.com')
        time.sleep(2)
    elif (işlem == "6"):
        webbrowser.open('discordapp.com')
        time.sleep(2)
    elif (işlem == "7"):
        webbrowser.open('cnnturk.com')
        time.sleep(2)
    elif (işlem == "8"):
        webbrowser.open('abdullahki.tk')
        time.sleep(2)


    else:
        print("Hatalı Tuşlama yaptınız, menüye geri döndürülüyorsunuz.")
        time.sleep(1)




