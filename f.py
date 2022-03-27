import cv2
import matplotlib.pyplot as plt
import numpy as np

np.seterr(divide='ignore')

img = cv2.imread("C:/Users/wogza/Downloads/New folder (2)/F/original.jpg", 0)

c = 255 / np.log(1 + np.max(img))
log_image = c * (np.log(img + 1))

log_image = np.array(log_image, dtype=np.uint8)

cv2.imshow('A', img)
cv2.imshow('B', log_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
