import numpy as np
import cv2 

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
for i in range(0,21):
	img = cv2.imread('images_resized/'+str(i)+'.jpg')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
	    roi_color = img[y-50:y+h+50, x-50:x+w+50]
	img_item = 'images_detected/'+str(i)+'.png'
	cv2.imwrite(img_item, roi_color)
	cv2.waitKey(0)
	cv2.destroyAllWindows()