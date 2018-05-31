import numpy as np
import cv2

img = cv2.imread('images.png' , cv2.IMREAD_COLOR)

px = img[55,55]

print(px)

img[55,55] = [255,255,255]

px2 = img[55,55]
print(px2)


#------------

##roi = img[100:150, 100:150]
##print(roi)
##
##img[100:150, 100:150] = [255,255,255]
##
##cv2.imshow('image', img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

#-------
#clone and move part of image

part = img[37: 111, 107: 194]

img[0:74, 0:87] = part

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
