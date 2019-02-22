import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('v_m2.jpg',0)

otsu_thr, otsu_mask = cv2.threshold(image, -1 , 1 , cv2.THRESH_BINARY | cv2.THRESH_OTSU) #params(img,tresh,maxx_val, type of tresh)

print(otsu_thr)

plt.figure(figsize=(6,3))
plt.subplot(121)
plt.axis('off')
plt.title('orginal')
plt.imshow(image, camp='gray')
plt.subplot(122)
plt.axis('off')
plt.title('otsu')
plt.imshow(otsu_mask,camp='gray')
plt.tight_layout()
plt.show()