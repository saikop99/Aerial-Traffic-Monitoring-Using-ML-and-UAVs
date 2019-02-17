import cv2 
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture('vtest.mp4')

while(1):
	ret,frame=cap.read()
	
	image = frame.astype(np.float32) / 255. #vector and scaling down
	image_lab = cv2.cvtColor(image,cv2.COLOR_BGR2XYZ)

	data = image_lab.reshape((-1,3))

	num_classes = 6 #total no of classes

	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50,  0.1)

	# clusters the obs into groups of related observations
	#without any prior know

	_,lables, centers = cv2.kmeans(data, num_classes,None, criteria, 20,cv2.KMEANS_RANDOM_CENTERS)


	segmented_lab = centers[lables.flatten()].reshape(image.shape)
	segmented = cv2.cvtColor(segmented_lab,cv2.COLOR_XYZ2RGB)

	cv2.imshow('seg_img',segmented)

	plt.subplot(121)
	plt.axis('off')
	plt.title('orginal')
	plt.imshow(image[:,:,[2,1,0]])
	plt.subplot(122)
	plt.axis('off')
	plt.title('segmented')
	plt.imshow(segmented)
	plt.show()
	k=cv2.waitKey(30) & 0xff
	if(k==27):
		break
cap.release()
cap.destroyAllWindows()
