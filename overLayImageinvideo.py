import cv2
import  cvzone

# camera access and video camera (0 is the which cam "if multiple cam have by default 0 ") open
cap = cv2.VideoCapture(0)
impng=cv2.imread("cvzoneLogo.png",cv2.IMREAD_UNCHANGED)
while True:
    # read the image
    success, img = cap.read()

    imageOverlay=cvzone.overlayPNG(img,impng,pos=(200,200))

    cv2.imshow('image', imageOverlay )
    cv2.waitKey(1)