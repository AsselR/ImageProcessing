import cv2

import matplotlib.pyplot as plt

image=cv2.imread("butterfly.png")
im_rgb=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


implot=plt.imshow(im_rgb)
plt.show()