import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("C:/Users/wogza/Downloads/New folder (2)/D/cameraman.jpg",0)

kernal = (5,5)
dst = cv2.blur(img,kernal)

substracted_image = cv2.subtract(img,dst)

plt.imshow(img, cmap = 'gray')
plt.show()

plt.imshow(dst, cmap = 'gray')
plt.show()


plt.imshow(substracted_image, cmap = 'gray')
plt.show()













