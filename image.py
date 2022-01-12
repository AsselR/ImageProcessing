import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('butterfly.png')
print(img)
print(img.shape)    #4 by 4 pixel, with a matrix of 4 columns.
imgplot = plt.imshow(img)
plt.show()

