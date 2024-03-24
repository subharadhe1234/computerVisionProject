import cv2
from  cvzone.Utils import rotateImage

# camera access and video camera (0 is the which cam "if multiple cam have by default 0 ") open
cap = cv2.VideoCapture(0)
while True:


    # read the image
    success, img = cap.read()
    # rotate image by 60 degree by changing the size
    imrot60=rotateImage(img,90,scale=1,keepSize=False)
    # rotate image by 60 degree by changing the size
    imrot60keepsize = rotateImage(img, 60, scale=1, keepSize=True)
    # cv2.imshow('imagerot60', imrot60keepsize )
    cv2.imshow('imagerot60', imrot60 )
    cv2.waitKey(1)