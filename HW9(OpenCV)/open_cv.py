import cv2 as cv
# Problem 1
img_1 = cv.imread('pic1.jpg')
img_2 = cv.imread('pic2.jpg')
img_3 = cv.imread('pic3.jpg')

cv.imshow('Pic1', img_1)
cv.imshow('Pic2', img_2)
cv.imshow('Pic3', img_3)

cv.waitKey(2)

# Problem 2
vid1 = cv.VideoCapture('vid1.mp4')

while True:
        frame_loaded, frame = vid1.read()

        if frame_loaded:
                cv.imshow('Vid1', frame)
        else:
                print('empty frame')
                exit(1)

        if cv.waitKey(20) & 0xFF == ord('d'):
                break

vid1.release()
cv.destroyAllWindows()

cv.waitKey(0)


# Problem 3

def rescaleFrame(frame, scale=0.5):
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        dimensions = (width, height)

        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('pic1.jpg')
img_rescaled = rescaleFrame(img, 0.2)

cv.imshow('Pic1', img)
cv.imshow('Pic1_rescaled', img_rescaled)

cv.waitKey(0)

# Problem 4
def rescaleFrame(frame, scale=0.5):

        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        dimensions = (width, height)

        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('vid1.mp4')

while True:
        frame_loaded, frame = capture.read()


        if frame is not None:
                frame_rescaled = rescaleFrame(frame, 0.5)
                cv.imshow('Video', frame)
                cv.imshow('Video_rescaled', frame_rescaled)
        else:
                print('empty frame')
                exit(1)

        if cv.waitKey(20) & 0xFF == ord('d'):
                break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
# Problem 5
import numpy as np

img = cv.imread('Pic2.jpg')
cv.imshow('Dog', img)

blank = np.zeros((300,300, 3), dtype = 'uint8')
cv.imshow('Blank', blank)

cv.circle(blank, (200,200), 50, (0,255, 0), thickness = -1)
cv.imshow('Circle', blank)

# Problem 6
