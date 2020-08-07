import cv2
import numpy as np

img_original = cv2.imread("Resources/imgSahar.png")
scale_percent = 60  # percent of original size
width = int(img_original.shape[1] * scale_percent / 500)
height = int(img_original.shape[0] * scale_percent / 500)
dim = (width, height)
img = cv2.resize(img_original, dim, interpolation=cv2.INTER_AREA)
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)