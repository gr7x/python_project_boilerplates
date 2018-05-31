import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)
    edges = cv2.Canny(frame, 100, 200)
    edges2 = cv2.Canny(frame, 120, 120)
    cv2.imshow('org', frame)
    cv2.imshow('lap', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('Canny Edge Detection', edges)
    cv2.imshow('Canny Edge2 Detection', edges2)


    
    k = cv2.waitKey(5) & 0XFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()
