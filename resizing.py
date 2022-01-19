import cv2
import matplotlib.pyplot as plt
import numpy as np

image=cv2.imread("butterfly.py")

image_resize=cv2.resize(image, (0, 0), fx=2, fy=2)

imshow=plt.imshow(image_resize)
plt.show()