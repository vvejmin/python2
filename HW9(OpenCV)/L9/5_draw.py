import numpy as np
import cv2 as cv



img = cv.imread('Photos/pic1.jpg')
cv.imshow('Dog', img)

#drawing on dummy image that we create or working with ready images
#we will use this image instead of the dog image 
#(height, width, the number of color channels)
blank = np.zeros((300, 300, 3), dtype = 'uint8')
cv.imshow('Blank', blank)

#1. Painting the image a certain color

#blank[:] = 0,255,0 #green
blank[:] = 0,0,255 #red
cv.imshow('Red', blank)



#2. Coloring a certain portion of an image, giving a range of pixels

# blank[100:200, 200:300] = 0,255,0
# cv.imshow('Multicolor', blank)


#3. Drawing a rectangle
#cv.rectangle(img, point1, point2, color, thickness)

# cv.rectangle(blank, (20,20), (200, 200), (0, 255, 0), thickness = 2)
# cv.imshow('Rectangle', blank)



#4. Filling in the rectangle


# cv.rectangle(blank, (20,20), (200, 200), (0, 255, 0), thickness = cv.FILLED)
# # or cv.rectangle(blank, (20,20), (200, 200), (0, 255, 0), thickness = -1)
# cv.imshow('Rectangle', blank)



#5. Not using absolute numbers

# cv.rectangle(blank, (20,20), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness = cv.FILLED)
# # or cv.rectangle(blank, (20,20), (200, 200), (0, 255, 0), thickness = -1)
# cv.imshow('Rectangle', blank)


#6. Drawing a circle
#cv.circle(img, center, radius, color, thickness)

# cv.circle(blank, (200, 200), 50, (0, 255, 0), thickness = 3)
# cv.imshow('Circle', blank)



#6. Filling in the circle
#cv.circle(img, center, radius, color, thickness)


cv.circle(blank, (200, 200), 50, (0, 255, 0), thickness = -1)
cv.imshow('Circle', blank)


#7 Drawing a line
#cv.line(img, point1, point2, color, thickness)


cv.line(blank, (20,20), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness = 3)
cv.imshow('Line', blank)


#8. Writing text on an image


#cv.putText(img, text, origin, font, fontscale, color, thickness)
#cv.putText(blank, "Hello", (150, 150), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness = 2)
#cv.putText(blank, "Hello, my name is Anna!", (150, 150), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness = 2) 
#we go offscreen, we can change margins and fontscale
cv.putText(blank, "Hello, my name is Anna!", (20, 20), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 0), thickness = 1) 
cv.imshow('Text', blank)


cv.waitKey(0)

