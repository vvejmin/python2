"""
We usually do this to prevent using too much of computational power

Rescaling - modifying height and width to a perticular height and width

best practice - downscale, or change height and width to a smaller values rather than larger
"""

import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #will talk more about this later

img = cv.imread('Photos/pic1.jpg')

img_rescaled = rescaleFrame(img, 0.2)

cv.imshow('Dog', img)
cv.imshow('Dog_rescaled', img_rescaled)


cv.waitKey(0)


