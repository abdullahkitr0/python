import pyperclip
import random
from tkinter  import *

root = Tk()
root.geometry = ("600x600")
passstr = StringVar()
passlen = IntVar()
passlen.set(0)

seç = input("Parolanızda Hangi Harf veya Sayıların Olmasını İstersiniz: ")

def oluştur():
    pass1 = [seç]
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(seç)
    passstr.set(password)

def kopyala():
    random_password = passstr.get()
    pyperclip.copy(random_password)

Label(root, text="Parola Oluşturucu",
      font="calibri 20 bold").pack()
Label(root, text="Parola Uzunluğunu Girin").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)
Button(root, text="Parolayı Oluştur",
       command=oluştur).pack(pady=7)
Entry(root, textvariable=passstr).pack(pady=3)
Button(root, text="Kopyala",
       command=kopyala).pack()
root.mainloop()
