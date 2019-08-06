import cv2
yVid = cv2.VideoCapture('1.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
cikti = cv2.VideoWriter('1.mp4',fourcc,20.0,(640,480))
while(True):
    deger,kare=yVid.read()
    if deger==True:
        cikti.write(kare)
    cv2.imshow("test",kare)
    if cv2.waitKey(1)& 0xFF == ord("a"):
        break
    yVid.release()
    cikti.release()
    cv2.destroyAllWindows()    
#By Abdullah Kivrak
#Yasal Hakalrı MIT lisansı Tarafından Korunmaktadır.
#abdullahki.tk
#https://is.gd/iCbYE5
