from cvzone.ClassificationModule import Classifier
import cv2

cap = cv2.VideoCapture(0)  # Initialize video capture
# path = "converted_keras"
maskClassifier = Classifier("converted_keras/keras_model.h5", "converted_keras/labels.txt")

while True:
    img = cap.read()  # Capture frame-by-frame
    # prediction = maskClassifier.getPrediction(img)
    # print(prediction)  # Print prediction result
    cv2.imshow("Image", img)
    cv2.waitKey(1)  # Wait for a key press