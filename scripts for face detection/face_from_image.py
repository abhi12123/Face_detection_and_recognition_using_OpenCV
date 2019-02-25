import numpy as np
import cv2 

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
i=8
img = cv2.imread('mohanlal/'+str(i)+'.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
img_item = 'mohan_det/'+str(i)+'.png'
cv2.imwrite(img_item, roi_color)
cv2.waitKey(0)
cv2.destroyAllWindows()