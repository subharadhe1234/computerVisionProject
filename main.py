import cv2
import  cvzone

# camera access and video camera (0 is the which cam "if multiple cam have by default 0 ") open
cap = cv2.VideoCapture(0)
while True:
    # read the image
    success, img = cap.read()
    cv2.imshow('image', img )
    cv2.waitKey(1)