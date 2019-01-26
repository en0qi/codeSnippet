import sys
import numpy as np
import cv2
import datetime

argvs = sys.argv
argc = len(argvs)

if(argc!=2):
	print("Usage: python3 %s filename",argvs[0])
	exit()

path = argvs[1]

face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.4.0/data/haarcascades/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.4.0/data/haarcascades/haarcascade_eye.xml')

img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.01, 3)
for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]
	eyes = eye_cascade.detectMultiScale(roi_gray)
	for (ex,ey,ew,eh) in eyes:
		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
keycode = cv2.waitKey(0)
if keycode == ord('s'): 
    dt_in = datetime.datetime.now()
    dt_in_str = dt_in.strftime('%m%d%H%M%S')
    cv2.imwrite("/home/pi/Pictures/facedetect18/{}.jpg".format(dt_in_str), img)
cv2.destroyAllWindows()