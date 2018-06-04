import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

#rect = (161, 79, 150, 150) #create rectangle that encompasses the foreground
rect = (50, 50, 300, 500)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()


#--- image foreground extraction

##cap = cv2.VideoCapture(0)
##
##while True:
##    #img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')
##    _, img = cap.read()
##    mask = np.zeros(img.shape[:2], np.uint8)
##
##    bgdModel = np.zeros((1,65), np.float64)
##    fgdModel = np.zeros((1,65), np.float64)
##
##    #rect = (161, 79, 150, 150) #create rectangle that encompasses the foreground
##    rect = (50, 50, 300, 500)
##
##    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
##    mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
##    img = img*mask2[:,:,np.newaxis]
##    plt.imshow(img)
##    plt.colorbar()
##    plt.show()
##
##    k = cv2.waitKey(5) & 0XFF
##    if k == 27:
##        break
##    
##cv2.destroyAllWindows()
##cap.release()

