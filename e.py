import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("C:/Users/wogza/Downloads/New folder (2)/E/lady.png", 0)

median = cv2.medianBlur(img, 5)

kernel = np.ones((5, 5), dtype=int) / 25

img1 = cv2.filter2D(median, -1, kernel)

img2 = cv2.subtract(img1, median)

cv2.imshow('A', img)
cv2.imshow('B', img1)
cv2.imshow('C', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
