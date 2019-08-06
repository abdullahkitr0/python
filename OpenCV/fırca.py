import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),95,(250,250,0),1)
img =np.zeros((512,512,3),np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback("image",draw_circle)
while(True):
    cv2.imshow("image",img)
    if cv2.waitKey(20) &0xFF ==27:
        break
cv2.destroyAllWindows()
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
