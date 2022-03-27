import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/wogza/Downloads/New folder (2)/B/window.jpg', 0)
img2 = cv2.imread('C:/Users/wogza/Downloads/New folder (2)/B/window.jpg', 0)

height, width = img.shape

arr = np.zeros(img.shape, dtype=int)

mins = 28
maxs = 75

for i in range(height):
    for j in range(width):
        if mins <= img[i, j] <= maxs:
            img[i, j] = (277 * img2[i, j] - 5040) / 47
        else:
            continue

plt.imshow(img2, cmap='gray')
plt.show()

plt.imshow(img, cmap='gray')
plt.show()