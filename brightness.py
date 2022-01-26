import cv2
import matplotlib.pyplot as plt

import numpy as np

image=cv2.imread("butterfly.png")


matrix = np.ones(image.shape, dtype="uint8")*100

imageBrighter =cv2.add(image, matrix)
imageDarker=cv2.subtract(image, matrix)

plt.figure(figsize=[18,5])
plt.subplot(131);plt.imshow(imageDarker[:,:, ::-1]); plt.title("Darker")
plt.subplot(132);plt.imshow(image[:,:, ::-1]); plt.title("Original")
plt.subplot(133);plt.imshow(imageBrighter[:,:, ::-1]); plt.title("Brighter")
plt.show()