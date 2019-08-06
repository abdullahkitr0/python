def vowels_count(text, output=0):
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            output += 1
    return output

text = input("Yazın : ")
print("Yazında  {} Tane Ünlü Harf Var ".format(vowels_count(text)))
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
