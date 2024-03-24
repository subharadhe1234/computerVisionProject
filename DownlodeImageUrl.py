import cvzone
import cv2
imnormal=cvzone.downloadImageFromUrl("https://upload.wikimedia.org/wikipedia/commons/6/6e/Similar-geometric-shapes.png",keepTransparency=True)
cv2.imshow("image_noraml",imnormal)
cv2.waitKey(0)