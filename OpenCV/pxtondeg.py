import cv2
import numpy as np

img = cv2.imread('helikopter.jpg')
print(img[100,100])
img[100,100] = [255,255,255]
print(img[100,100])
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
