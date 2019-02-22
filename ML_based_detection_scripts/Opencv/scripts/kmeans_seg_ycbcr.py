import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('v_m3.jpg').astype(np.float32) / 255. #vector and scaling down
image_lab = cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)

data = image_lab.reshape((-1,3))

num_classes = 6 #total no of classes

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50,  0.1)

# clusters the obs into groups of related observations
#without any prior know

_,lables, centers = cv2.kmeans(data, num_classes,None, criteria, 20,cv2.KMEANS_RANDOM_CENTERS)


segmented_lab = centers[lables.flatten()].reshape(image.shape)
segmented = cv2.cvtColor(segmented_lab,cv2.COLOR_YCrCb2RGB)

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
 
