def reverse(value, output=[]):
    #range(start, stop, step)
    for i in range(len(value) - 1, -1, -1):
        output.append(value[i])
    
    return "".join(output)

text = input("Yaz: ")
print("Yazdığının Tersi {}".format(reverse(text)))
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
