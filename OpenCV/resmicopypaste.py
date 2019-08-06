import cv2
import numpy as np
img = cv2.imread('helikopter.jpg')
k = img[156:256,0:80]
img[0:100,300:380]= k
cv2.imshow("img",img)
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
