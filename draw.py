import cv2 as cv 
import numpy as np

blanks = np.zeros((500,500,3),dtype='uint8')

blanks[200:300,300:400] = 0,255,0
cv.rectangle(blanks,(0,0),(250,250),(0,255,0),thickness=2)

#img = cv.imread('Photos/cat.jpg')

cv.putText(blanks,'Hello World',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)  
cv.imshow('Green',blanks)
cv.waitKey(0)