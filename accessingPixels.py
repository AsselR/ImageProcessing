import cv2
import matplotlib.pyplot as plt

im1=cv2.imread("check2.png")
#print(im1)
#print(im1.shape)

#print(im1[0,6])  #row and column


im_copy=im1.copy()

im_copy[0, 0]=200
im_copy[0, 1]=200



plt.imshow(im_copy, cmap='gray')

print(im_copy)
plt.show()
