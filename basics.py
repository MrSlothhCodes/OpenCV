import cv2 as cv

img = cv.imread('Photos/park.jpg')
 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

cany = cv.Canny(blur,125,175)

dilated = cv.dilate(cany ,(7,7),iterations=3)

erode = cv.erode(dilated,(7,7),iterations=3)

resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)

#cropped = img[50:200,200:400]
cv.imshow('Blur', resized)
cv.waitKey(0)
