import cv2

########## READ AN IMAGE ##############
"""
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("Resources/imgSahar.png")
# DISPLAY
cv2.imshow("Sahar_FRIKHA", img)
cv2.waitKey(0)
"""
"""
img = cv2.imread('Resources/imgSahar.png', cv2.IMREAD_UNCHANGED)
#print('Original Dimensions : ', img.shape)
scale_percent = 60  # percent of original size
width = int(img.shape[1] * scale_percent / 500)
height = int(img.shape[0] * scale_percent / 500)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
#print('Resized Dimensions : ', resized.shape)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
########## READ A VIDEO ##############
"""
frameWidth = 400
frameHeight = 480
cap = cv2.VideoCapture("Resources/Sahar.mp4")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
"""
########## READ A WEBCAM ##############
"""
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('1'):
        break
"""

