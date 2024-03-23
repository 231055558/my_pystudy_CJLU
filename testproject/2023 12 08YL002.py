import cv2
im1 = cv2.imread('3.jpg')
im2 = cv2.imread('2.jpg')

height = im1.shape[0]
im2 = cv2.resize(im2, (im1.shape[1], im1.shape[0]))

#im1[0:100,0:100]= [0,0,255]
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2BGRA)
im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2BGRA)
for [i,j] in im2:


cv2.imshow('666',im1)
cv2.waitKey()