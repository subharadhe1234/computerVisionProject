import cv2
import cvzone

# camera access and video camera (0 is the which cam "if multiple cam have by default 0 ") open
cap = cv2.VideoCapture(0)
while True:
    # read the image
    success, img = cap.read()
    # cv2.putText(img, "Radhe Radhe", (150, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    # rectangle box is need in the background of text
    cvzone.putTextRect(img,'Radhe Radhe',(150,50))
    cv2.imshow('image', img)
    cv2.waitKey(1)
