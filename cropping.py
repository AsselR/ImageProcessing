import cv2 
import matplotlib.pyplot as plt

image=cv2.imread("butterfly.png")

im_cropped=image[200:800, 250:1100]

imshow=plt.imshow(im_cropped)
plt.show()