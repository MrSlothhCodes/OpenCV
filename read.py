import cv2 as cv

# Read an image

""" img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img) """

# Read a video
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
 
# Wait for a key event
cv.waitKey(0)
