import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('check.png', 0)
image1=cv2.imread('butterfly.png')
image1_reverserd=image1[:,:,::-1]

print(image)

print("Image is ", image.shape)
print("Image type is", image.dtype)
implot=plt.imshow(image, cmap='gray')
plt.show()

implot1=plt.imshow(image1_reverserd)
plt.show()