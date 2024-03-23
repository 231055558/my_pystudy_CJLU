import cv2
import numpy as np
foregnd = cv2.VideoCapture('res.mp4')
backgnd = cv2.VideoCapture('t1.mp4')

def clblue(image):
    ts = cv2.inRange(image,np.array([30,0,0,0]), np.array([255,40,40,255]))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    image[ts != 0] = [0,0,0,0]
    return image

skip=30


for i in range(skip):
    ret, fimage = foregnd.read()
    if fimage is None:
        print("error")
        sys.exit()
        break
flags = 0

while True:

    ret,fimage = foregnd.read()
    ret,bimage = backgnd.read()
    if fimage is None or bimage is None:
       continue
    bimage1 = cv2.resize(bimage,(bimage.shape[1]//2,bimage.shape[0]//2))
    fimage = cv2.cvtColor(fimage, cv2.COLOR_BGR2BGRA)
    height = fimage.shape[0]
    #fi_half = fimage[height // 2:]
    alpha = fimage
    alpha[:height//2, :] = [0,0,0,0]
    fi_half=cv2.add(fimage,alpha)
    #cv2.imshow('2', fi_half)
    fi_half_fp = cv2.flip(fi_half,1)
    fi_half_fp_clb = clblue(fi_half_fp)
    #fi_half_fp_clb = fi_half_fp
    fi_half_fp_clb_re = cv2.resize(fi_half_fp_clb, (bimage1.shape[1], bimage1.shape[0]))
    bimage1 = cv2.cvtColor(bimage1, cv2.COLOR_BGR2BGRA)
    mix_im = cv2.add(bimage1,fi_half_fp_clb_re)
    if flags >= 60:
        cv2.imshow('mixim', mix_im)
        #cv2.imshow('image',bimage1)
        #cv2.imshow('fimage',fi_half_fp_clb_re)

    else:
        cv2.imshow('mixim', bimage1)

    flags +=  1
    cv2.waitKey(10)