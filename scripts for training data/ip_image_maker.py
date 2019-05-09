import numpy as np
import cv2
import pickle
import time
import urllib.request
import os
import openpyxl
url='http://192.168.43.1:8080/shot.jpg'

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
k=0

while(True):
	# Capture frame-by-frame
	imgResp=urllib.request.urlopen(url)
	imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
	frame=cv2.imdecode(imgNp,-1)
	#ret, frame = cap.read()
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

# When everything done, release the capture
#cap.release()
cv2.destroyAllWindows()
