import numpy as np
import cv2
import pickle
import time
import urllib.request
import os
import openpyxl
url='http://192.168.0.122:8080/shot.jpg'

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

while(True):
	# Capture frame-by-frame
	imgResp=urllib.request.urlopen(url)
	imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
	frame=cv2.imdecode(imgNp,-1)
	#ret, frame = cap.read()
	gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	for (x, y, w, h) in faces:
		print(x,y,w,h)
		roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
		roi_color = frame[y:y+h, x:x+w]
	
		color = (255, 0, 0) #BGR 0-255 
		stroke = 2
		end_cord_x = x + w
		end_cord_y = y + h
		cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

# When everything done, release the capture
#cap.release()
cv2.destroyAllWindows()
