import cv2
import matplotlib.pyplot as plt

image1=cv2.imread("butterfly.png")
imageCopy=image1.copy();

cv2.rectangle(imageCopy, (500, 100), (700,600), (255, 0, 255), thickness=5, lineType=cv2.LINE_8);
text="HEllo World"
fontSize=2.3
fontFace=cv2.FONT_HERSHEY_COMPLEX
fontColor=(0, 255, 0)
fontThickness=2
cv2.putText(imageCopy, text, (200, 900), fontFace, fontSize,fontColor, fontThickness  )
plt.imshow(imageCopy[:,:, ::-1])
plt.show()