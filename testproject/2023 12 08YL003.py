import cv2
import numpy as np
ren = cv2.imread('3.jpg')
sleep = cv2.imread('2.jpg')
sleep = cv2.resize(sleep, (ren.shape[1], ren.shape[0]))

sumi = ren.shape[0]+ren.shape[1]
new = ren

for i in range(ren.shape[0]):
    for j in range(ren.shape[1]):
        new[i,j,:] = sleep[i,j,:] * ((i+j)/sumi) + ren[i,j,:]*(1-(i+j)/sumi)


new = new.astype(np.uint8)

# cv2.imshow('ren',ren)
# cv2.imshow('shui',sleep)
cv2.imshow('add',new)
cv2.waitKey()