import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/wogza/Downloads/New folder (2)/C/input.png', 0)

height, width = img.shape

arr = np.zeros(img.shape, dtype=int)

mins = 100
maxs = 200

# Loop over the input image and if pixel value lies in desired ranges change according to equation
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 1]])
image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
cv2.imshow('AV CV- Winter Wonder Sharpened', image_sharp)
cv2.waitKey()
cv2.destroyAllWindows()











