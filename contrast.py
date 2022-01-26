import cv2
import matplotlib.pyplot as plt
import numpy as np

image=cv2.imread("butterfly.png")

matrix1=np.ones(image.shape)*0.8
matrix2=np.ones(image.shape)*1.2

imageDarker=np.uint8(cv2.multiply(np.float64(image), matrix1))

imageBrighter=np.uint8(cv2.multiply(np.float64(image), matrix2))

plt.figure(figsize=[18,5])
plt.subplot(131);plt.imshow(imageDarker[:,:,::-1]); plt.title("Darker")
plt.subplot(132);plt.imshow(image[:,:,::-1]); plt.title("Original")
plt.subplot(133);plt.imshow(imageBrighter[:,:,::-1]); plt.title("Brighter")
plt.show()