import cv2
import cvzone

# camera access and video camera (0 is the which cam "if multiple cam have by default 0 ") open
cap = cv2.VideoCapture(0)
while True:
    # read the image
    success, img = cap.read()
    # normal rectangle
    #cv2.rectangle(img, (200, 200), (500, 400), (0, 250, 0), 2)

    # fancy rectangle
    cvzone.cornerRect(img, (200, 200, 300, 200), l=40, t=5, rt=1,
               colorR=(255, 200, 255), colorC=(0, 255, 0))

    cv2.imshow('image', img)
    cv2.waitKey(1)
