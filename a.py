import numpy as np
import cv2 as cv

# Loading the image
img = cv.imread("C:/Users/wogza/Desktop/exam/image.png")

# Converting to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# define range of red color in HSV
lower_red = np.array([161, 155, 84])
upper_red = np.array([179, 255, 255])

# Threshold the HSV image to get only red colours
red_mask = cv.inRange(hsv, lower_red, upper_red)

# Bitwise and Mask
red = cv.bitwise_and(hsv, hsv, mask=red_mask)

# Find Contours
redCopy = red.copy()
singleChannel = cv.cvtColor(redCopy, cv.COLOR_BGR2GRAY)
contours, hierarchy = cv.findContours(image=singleChannel, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)

# Draw Contours
cv.drawContours(image=singleChannel, contours=contours, contourIdx=-1, color=(87, 230, 44), thickness=2, lineType=cv.LINE_AA)

# Output Text

cv.imshow("Image", singleChannel)
cv.waitKey(0)