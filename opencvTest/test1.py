import cv2
import cv2.cv as cv
import numpy as np

im = cv.LoadImageM("lena.jpg")
#size = (960,600)
size = cv.GetSize(im)
#size=im.size()
dst = cv.CreateImage(size, 8, 3)
smoothed = cv.CreateImage(size, 8, 3)
dst3 = cv.CreateImage(size, 8, 3)
cv.Resize(im,dst)

for i in range(4):
        cv.Smooth(dst,smoothed,cv.CV_BILATERAL, 30,1,32,32)
        cv.Smooth(smoothed,dst,cv.CV_BILATERAL, 30,1,32,32)
        cv.Smooth(dst,smoothed,cv.CV_BILATERAL, 30,1,32,32)

lap = cv.CreateImage(cv.GetSize(smoothed), cv.IPL_DEPTH_16S, 3)
#laplace = cv.Laplace(smoothed, lap)
gray = cv.CreateImage(cv.GetSize(smoothed), 8, 1)
canny = cv.CreateImage(cv.GetSize(smoothed), 8, 1)
cv.CvtColor(smoothed, gray, cv.CV_BGR2GRAY)
cv.Canny(gray,canny,20,20,3)

#ret,thresh = cv.threshold(imgray,127,255,0)
          
cv.NamedWindow('Original')
cv.MoveWindow('Original', 10, 10)
cv.ShowImage('Original', im)  
cv.NamedWindow('Smoothed')
cv.MoveWindow('Smoothed', 600, 100)
cv.ShowImage('Smoothed',smoothed)
cv.NamedWindow('Laplace')
cv.MoveWindow('Laplace', 600, 100)
cv.ShowImage('Canny',canny)
cv.ShowImage('Gray',gray)
cv.WaitKey(0) 
#cv.SaveImage("smoothed.png",dst)

#dst = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_16S, 3)
#cv.SaveImage("foo-laplace.png", lap)

