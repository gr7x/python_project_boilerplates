#https://www.youtube.com/watch?v=6e6NbNegChU&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=13
import cv2
import numpy as np

#modification to detect edges on camera feed
cap = cv2.VideoCapture(0)



while True:
    _, img = cap.read()
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


#---- original image processing data --- Program

#img = cv2.imread('opencv-corner-detection-sample.jpg')
##gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##gray = np.float32(gray)
##
##corners = cv2.goodFeaturesToTrack(gray, 200, 0.01, 10)
##corners = np.int0(corners)
##for corner in corners:
##    x,y = corner.ravel()
##    cv2.circle(img, (x,y), 3, 255, -1)
##cv2.imshow('Corner', img)





