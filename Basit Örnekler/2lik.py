decimal = int(input("Çevrilecek Sayı: "))

def binary(n):
    output = ""
    while n > 0:
        output = "{}{}".format(n % 2, output)
        n = n // 2
    return output

# our method
print(binary(decimal))

# another way
print(bin(decimal)[2:])

# yet another way
print("{0:b}".format(decimal))
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
