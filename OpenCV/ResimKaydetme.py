import cv2

img = cv2.imread('helikopter.jpg',0) 
cv2.imshow('RESIM',img)

dugme = cv2.waitKey(0)

if dugme ==27:
    cv2.destroyAllWindows()
else:
    cv2.imwrite("g_helikopter.jpg",img) 
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
