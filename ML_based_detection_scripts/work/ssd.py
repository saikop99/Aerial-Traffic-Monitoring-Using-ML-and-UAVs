#using mobileNet for taining

import cv2

import numpy as np
import imutils

#cv2.dnn.readNetFromCafee()
#func to import the caffe model

model = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt','MobileNetSSD_deploy.caffemodel')

#set threshold
#specify the classes

CONF_THR = 0.3
LABELS = {1: 'aeroplane',2: 'bicycle',3:' car',4: 'bus',5: 'motorbike',}

video = cv2.VideoCapture('arieal_vid.mp4')

c=0

while True:
	ret,frame = video.read()
	if not ret: break
	frame = imutils.resize(frame, width=1000)

# Detect the objects
	
	h , w = frame.shape[0:2]
	blob = cv2.dnn.blobFromImage(frame, 1/127, (300*w/h,300),(127,127,127), False)
	model.setInput(blob)
	output = model.forward()
#Draw the detected bjects

	for i in ange(output.shape[2]):
		conf = output[0,0,i,2]
		if conf > CONF_THR:
			label = output[0,0,i,2]
			x0,y0,x1,y1 = (output[0,0,i,3:7] * [w,h,w,h]).astype(int)
			cv2.rectangle(frame,(x0,y0),(x1,y1),(0,255,0),2)
			cv2.putText(frame, '{}: {:.2f}'.format(LABLES[label], conf), (x0,y0), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0), 2)

	c +=1
	if c == 100:
		cv2.imwrite('../ch5_car_detections.png', frame)

	cv2.imshow('frame',frame)
	key = cv2.waitKey(3)
	if key == 27: break	
cv2.destroyAllWindows()	