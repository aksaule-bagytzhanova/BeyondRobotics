import cv2 

img1 = cv2.imread("1.jpg")
img2=cv2.imread("2.png")

r1 = cv2.resize(img1,(720,720))
r2 = cv2.resize(img2,(720,720))

s=cv2.add(r1,r2)
s=cv2.addWeighted(r1,3,r2,0.5,0)
# s=cv2.subtract(r1,r2)



cv2.imshow('add',s)
cv2.waitKey(0)
cv2.destroyAllWindows()
