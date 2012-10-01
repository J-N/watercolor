import numpy as np
import cv2
import cv2.cv as cv
import random

im = cv2.imread('lena.jpg')
size = cv.GetSize(im)
dst = cv.CreateImage(size, 8, 3)
smoothed = cv.CreateImage(size, 8, 3)
cv.Smooth(dst,smoothed,cv.CV_BILATERAL, 30,1,32,32)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(im,contours,-1,(0,255,0),3)
for h,cnt in enumerate(contours):
	#mask = np.zeros(imgray.shape,np.uint8)
    	#cv2.drawContours(mask,[cnt],0,255,-1)
    	#mean = cv2.mean(im,mask = mask)
	color = (random.random()*255, random.random()*255, random.random()*255)
	cv2.drawContours(im,contours,h,color,3)

cv2.namedWindow( "Components", 1 );
cv2.imshow( "Components", im );
cv2.waitKey(0)
