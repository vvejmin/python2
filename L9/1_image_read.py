"""
Available in Python, C++, Java, etc., designed to solve computer vision problems.

- - Installations
- latest version of Python
- pip install opencv-contrib-python 
"""

import cv2 as cv


#takes a path to an image and returns it as a matrix of pixels

img = cv.imread('Photos/town.jpg')

#displaying the image as a new window, passing the window name and the matrix of pixels to display

cv.imshow('Town', img) 

#a keyboard binding function, waits for a specific delay for a key to be pressed

cv.waitKey(0) #waits for an infinite amount of time for a keyboard key to be pressed

