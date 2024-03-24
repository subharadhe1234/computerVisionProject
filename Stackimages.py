import cv2
import cvzone

# camera access and video camera (0 is the which cam "if multiple cam have by default 0 ") open
cap = cv2.VideoCapture(0)
while True:
    # read the image
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize the image to be smaller (0.1x of original size)
    imgSmall = cv2.resize(img, (0, 0), None, 0.1, 0.1)

    # Resize the image to be larger (3x of original size)
    imgBig = cv2.resize(img, (0, 0), None, 3, 3)

    # Apply Canny edge detection on the grayscale image
    imgCanny = cv2.Canny(imgGray, 50, 150)

    # Convert the image to HSV color space
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # image list
    imageList=[img, imgGray, imgCanny, imgSmall, imgBig, imgHSV]
    # stack images created
    stackedImg = cvzone.stackImages(imageList, cols=3, scale=0.7)

    cv2.imshow('image', stackedImg)
    cv2.waitKey(1)
