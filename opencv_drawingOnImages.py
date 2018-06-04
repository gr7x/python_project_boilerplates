import numpy as np
import cv2
#import pymouse
import win32api
import random

# --- drawing on image
##img = cv2.imread('images.png', cv2.IMREAD_COLOR)
##
##cv2.line(img, (0,0), (150,150), (0, 250, 0), 15) # line
##
##cv2.rectangle(img, (15, 25), (200,150), (), 5)
##cv2.circle(img, (100,63), 55, (0,0,255), -1)
##
##pts = np.array([[10,5],[20,30], [50,10]], np.int32)
###pts = pts.reshape((-1,1,2))
##cv2.polylines(img, [pts], True,(0,255,255),3)
##
##font =cv2.FONT_HERSHEY_SIMPLEX
##cv2.putText(img, 'ball', (60,57), font, 2, (0, 2, 0), 20, cv2.LINE_AA)
##
##cv2.imshow('image', img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


# -- drawing on video ---- open cv for augmented reality

cap = cv2.VideoCapture(0)
x = 90
y = 90
b = False
mousePX = 0
mousePY = 0
points = 0
speed = 5
recX = 15
recY = 25

while True:
    
    #img = cv2.imread('images.png', cv2.IMREAD_COLOR)
    ret, frame = cap.read()
    #mouse = pymouse.PyMouse()
    font =cv2.FONT_HERSHEY_SIMPLEX
    #cv2.line(frame, (0,0), (150,150), (0, 250, 0), 15) # line

    cv2.rectangle(frame, (recX , recY), (recX + 185 ,recY + 140 ), (), 1)
    cv2.circle(frame, (x,y), 55, (0+x,0,255), -1)
    #xM, yM =  mouse.position()
    xM, yM = win32api.GetCursorPos()
    cv2.putText(frame,'mouse loc: ' +str(xM) + ' ' + str(yM), (20,80), font, 1, (0, 2, 0), 1, cv2.LINE_AA)
    pts = np.array([[10,5],[20,30], [50,10]], np.int32)
    #pts = pts.reshape((-1,1,2))
   # cv2.polylines(frame, [pts], True,(0,255,255),3)
    cv2.putText(frame,'points =' + str(points), (400,80), font, 1, (0, 2, 0), 1, cv2.LINE_AA)
    
    cv2.putText(frame, 'loc x=' + str(x), (20,40), font, 1, (0, 2, 0), 1, cv2.LINE_AA)

    cv2.imshow('image', frame)

    
    print(recX)
    #-- check if in range
    if x - 30  > recX and y- 50  > recY and x  < recX + 130 and y < recY + 80:
        points += 1
        recX = random.randint(12, 460)
        recY = random.randint(12, 360)
    if mousePX < xM:
        x-= speed
        
        if x <= 55:
            x = 55  
    else:
        x += speed
        if x >= 550:
            x = 550
    if mousePY < yM:
        y-= speed
        if y < 55:
            y = 55
    else:
        y +=  speed
        if y > 424:
            y = 424

    mousePX = xM
    mousePY = yM
        
##    if b == False:
##        x+= 5
##        if x >= 435:
##            b = True
##    else:
##        x -= 5
##        if x < 0:
##            b = False
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
