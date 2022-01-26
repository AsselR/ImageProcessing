import cv2
import matplotlib.pyplot as plt
import numpy as np

image=cv2.imread("Piano_Sheet_Music.png", cv2.IMREAD_GRAYSCALE)

retVal, image_global1=cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
retVal, image_global2=cv2.threshold(image, 130, 255, cv2.THRESH_BINARY)
imageAdp=cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

plt.figure(figsize=[18,5])
plt.subplot(221);plt.imshow(image, cmap="gray"); plt.title("original")
plt.subplot(222);plt.imshow(image_global1, cmap="gray"); plt.title("threshold global1")
plt.subplot(223);plt.imshow(image_global2, cmap="gray"); plt.title("threshold global2")
plt.subplot(224);plt.imshow(imageAdp, cmap="gray"); plt.title("adaptive")
plt.show()