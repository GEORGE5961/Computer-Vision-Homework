#!/usr/bin/env python3        
# -*- coding: utf-8 -*-  
import cv2 as cv
import numpy as np

img = cv.imread('./0.png')

# arbitrary structrue element
ksize = 3
kernel = np.ones((ksize, ksize),np.uint8) 

#cv.namedWindow('Origin image')
#cv.imshow('Origin image',img)

# convert to binary image, 255 for foreground(white), 0 for background(black)
def toBimg(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    h, w = img.shape[:2]
    m = np.reshape(img, [1, w*h]) 
    mean = m.sum() / (w*h)
    _, bimg = cv.threshold(img, mean, 255, cv.THRESH_BINARY)
    return bimg

def erosion(img, kernel):
    h, w = img.shape[:2]
    img_ret = np.zeros((h, w),np.uint8) 
    for i in range(1,h-1):
        for j in range(1,w-1):
            block = img[i-1:i+2, j-1:j+2] / 255
            multi_res = (kernel * block).sum()
            if (multi_res == 9):
                img_ret[i,j] = 255
    
    return img_ret    

def dilation(img, kernel):
    h, w = img.shape[:2]
    img_ret = np.zeros((h, w),np.uint8) 
    for i in range(1,h-1):
        for j in range(1,w-1):
            block = img[i-1:i+2, j-1:j+2] / 255
            multi_res = (kernel * block).sum()
            if (multi_res >1):
                img_ret[i,j] = 255
    
    return img_ret
    
bimg = toBimg(img)
img_eroded = erosion(bimg,kernel)
img_dilated = dilation(bimg, kernel)

cv.namedWindow('Origin binary image')
cv.imshow('Origin binary image', bimg)
cv.namedWindow('Eroded binary image')
cv.imshow('Eroded binary image',img_eroded)
cv.namedWindow('Dilated binary image')
cv.imshow('Dilated binary image',img_dilated)
cv.waitKey()
cv.destroyAllWindows()