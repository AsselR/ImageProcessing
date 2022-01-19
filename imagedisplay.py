import cv2
import matplotlib.pyplot as plt
im1=cv2.imread("butterfly.png")

plt.imshow(im1)
plt.title("Matplotlib imshow")
plt.show()


window1=cv2.namedWindow("w1")
cv2.imshow(window1, im1)
cv2.waitKey(8000)
cv2.destroyWindow(window1)