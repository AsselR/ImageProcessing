import cv2

import matplotlib.pyplot as plt

image_bgr=cv2.imread("butterfly.png")

b, g, r=cv2.split(image_bgr)

plt.figure(figsize=[20, 5])

plt.subplot(141); plt.imshow(r, cmap="gray");plt.title("Red channel");

plt.subplot(142); plt.imshow(g, cmap="gray");plt.title("Green channel");
plt.subplot(143); plt.imshow(b, cmap="gray");plt.title("Blue channel");

imgMerged=cv2.merge((b, g, r))

plt.subplot(144);plt.imshow(imgMerged[:, :, ::-1]); plt.title("Merged")

plt.show()