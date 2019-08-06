from datetime import *

birth = datetime.strptime(input("Doğum Tarihin (G.A.Y): "), "%d.%m.%Y")
age = datetime.now() - birth

print("[ {} ] Bu Kadar Saniye Yaşadın ".format(age.total_seconds()))
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
