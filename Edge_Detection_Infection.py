import cv2
import numpy as np

cap = cv2.VideoCapture(0)


_, img = cap.read()

while True:
    #img = cv2.imread('opencv-corner-detection-sample.jpg')
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    corners = cv2.goodFeaturesToTrack(gray, 200, 0.01, 10)
    corners = np.int0(corners)
    for corner in corners:
        x,y = corner.ravel()
        cv2.circle(img, (x,y), 3, 255, -1)
    cv2.imshow('Corner', img)

    k = cv2.waitKey(5) & 0XFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()
