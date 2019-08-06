import cv2
import numpy as np 
img = np.zeros((512,800,3),np.uint8)
cv2.line(img,(200,0),(0,400),(0,255,0),10)
cv2.line(img,(200,0),(400,400),(0,255,0),10)
cv2.line(img,(100,200),(300,200),(0,255,0),10)
cv2.line(img,(400,0),(400,400),(0,255,0),10)
cv2.line(img,(400,200),(550,0),(0,255,0),10)

cv2.line(img,(400,200),(550,400),(0,255,0),10)



cv2.imshow("Cizgi Cizme",img)
#By Abdullah Kivrak
#https://abdullahki48.blogspot.com
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
