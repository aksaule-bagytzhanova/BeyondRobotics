import cv2
import numpy as np


#Ex 1
 #-1 background invisible 
 #0 background colored
 #1 background gray

 #cv2.WINDOW_NORMAL
 #cv2.WINDOW_AUTOSIZE

# img = cv2.imread("logo.png", 1)
# cv2.namedWindow("image_logo", cv2.WINDOW_NORMAL)
# cv2.imshow("image_logo", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#Ex 2 camera show
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     cv2.imshow("video", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.distroyAllWindows()

#Ex 3 video show
cap = cv2.VideoCapture('aksi.mp4')

while True:
    ret, frame = cap.read()
    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.distroyAllWindows()