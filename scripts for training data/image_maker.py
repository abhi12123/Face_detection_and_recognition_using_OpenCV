import numpy as np
import cv2
import pickle
import time


face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
k=0
cap = cv2.VideoCapture(0)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	for (x, y, w, h) in faces:
		roi_color = frame[y-50:y+h+50, x-50:x+w+50]
		o=k
		img_item = "images_detected/"+str(o)+".png"
		cv2.imwrite(img_item, roi_color)
		time.sleep(3)
		k=k+1
	cv2.imshow('frame',frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
