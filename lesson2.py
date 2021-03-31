import cv2
import numpy as np

# img = np.zeros((900,900,3), np.uint8)

#cv2.line(img,(x1,y1),(x2,y2),(B,G,R),T)

# img = cv2.line(img, (10,10),(720,640),(140,160,180),5)
# img = cv2.rectangle(img, (10,10),(720,640),(140,160,180),5)
# img = cv2.circle(img,(500,450),100,(255,0,0),-1)
# cv2.putText(img,"BeyondRobotics",(10,450),5,3,(255,255,255),3,cv2.LINE_AA)

# cv2.imshow('image',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


#cv2.rectangle(img,(x1,y1),(x2,y2),(B,G,R),T)
#cv2.circle(img,(x,y),R,(B,G,R),T)
#cv2.putText(img,text,(x,y),font,S,(B,G,R),T,cv2.LINE_AA)

#ползунки
#cv2.createTrackbar(name,window,x,y,func)

def nothing(x):
    pass
img = np.zeros((300,300,3),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')

    img[:]=[b,g,r]





