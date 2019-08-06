import string

def is_word(text):
    for char in text:
        if not char in string.punctuation:
            return True
    return False

def word_count(value, output = 0):
    potential_words = value.split(" ")
    
    for word in potential_words:
        if is_word(word):
            output += 1
    
    return output

text = input("Yazın: ")
print("Kelime Sayısı: {}".format(word_count(text)))
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
