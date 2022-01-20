import cv2
import matplotlib.pyplot as plt

img1=cv2.imread("butterfly.png")
imageLine=img1.copy()
cv2.line(imageLine, (200, 100), (400, 100), (0, 255, 255), thickness=5, lineType=cv2.LINE_AA );
plt.imshow(imageLine[:, :, ::-1])
plt.show()