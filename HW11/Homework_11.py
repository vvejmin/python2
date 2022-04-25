from tkinter import Image
import cv2 as cv
from cv2 import blur
from cv2 import rectangle
from cv2 import bitwise_and
import numpy as np
from matplotlib import pyplot as plt
import PIL
from PIL import Image

#Problem 1.
# Open the image pic1.jpg and display it with the name pic1. Convert the image to the following
# formats and display in separate windows: RGB, HSV, LAB, grayscale

# pic1 = cv.imread('practical_homework3/pic1.jpg')
# cv.imshow('pic1', pic1)



# gray = cv.cvtColor(pic1,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# hls = cv.cvtColor(pic1, cv.COLOR_BGR2HLS)
# cv.imshow('Hls', hls)

# hsv = cv.cvtColor(pic1, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

# rgb = cv.cvtColor(pic1, cv.COLOR_BGR2RGB)
# cv.imshow('rgb', rgb)

# lab = cv.cvtColor(pic1, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)

#Problem 2.
# Open the image pic1.jpg and display it with the name pic1. Separate the image into its 3
# channels. Display both the colored and grayscale versions of each channel in separate
# windows.

# pic1 = cv.imread('practical_homework3/pic1.jpg')
# cv.imshow('pic1', pic1)
# gray = cv.cvtColor(pic1,cv.COLOR_BGR2GRAY)
# print(pic1.shape)


# b_1, g_1, r_1 = cv.split(pic1)


# cv.imshow('blue_1', b_1)
# cv.imshow('green_1', g_1)
# cv.imshow('red_1', r_1)
# cv.imshow('gray', gray)

#Problem 3.
# Open the image pic2.jpg and display it with the name pic2. Blur the picture using average and
# bilateral blurring methods and display in separate windows. (For the parameters, use the values
# of your choice). Write a short comment if you see any particular difference when using different
# parameter values for the second method and comparing it to the averaging method.

pic2 = cv.imread('practical_homework3/pic2.jpg')
cv.imshow('pic2', pic2)

average = cv.blur(pic2, (7,7))
cv.imshow('average_blur', average)



img = cv.imread('practical_homework3/pic2.jpg')
kernel = np.ones((7,7),np.float32)/49
dst = cv.filter2D(img,-1, kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


pic2 = cv.imread('practical_homework3/pic2.jpg')
blur = cv.blur(img,(7,7))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


bilateral_1 = cv.bilateralFilter(pic2, 5, 15, 15)
cv.imshow('bilteral1', bilateral_1)


bilateral_2 = cv.bilateralFilter(pic2, 100, 50, 80)
cv.imshow('bilteral2', bilateral_2)

#Problem 4.
# Open the image pic2.jpg and display it with the name pic2. Apply the correct method so that
# only a circle of radius of 70 pixels is left right in the middle of the picture. Your result should look
# similar to the example below.

pic2 = cv.imread('practical_homework3/pic2.jpg')
pic2_2 = Image.open('practical_homework3/pic2.jpg')

# blank = np.zeros(pic2.shape[:2], dtype = 'uint8')

# print(pic2_2.format)
# print(pic2_2.size)
# print(pic2_2.mode)

# pic2_2.show()



blank = np.zeros(pic2.shape[:2], dtype = 'uint8')

# circle = cv.circle(blank.copy(), (pic2.shape[1]//2, pic2.shape[0]//2), 70, 255, -1)



# masked_pic2 = cv.bitwise_and(pic2, pic2, mask=circle)
# cv.imshow('original image', pic2)
# cv.imshow('masked with circle', masked_pic2)


# rectangle = cv.rectangle(blank.copy(), (110,30), (230,120), 255, -1)

# masked_image = cv.bitwise_and(pic2, pic2, mask=rectangle)

# cv.imshow('masked with rectangle', masked_image)

#Problem 5.
#Perform appropriate operations to get a results similar to the images below:
#Այս Առաջադրանքում լրիվ գույները չստացվեց մոտս
# pic2 = cv.imread('practical_homework3/pic2.jpg')
# blank = np.zeros((400, 400), dtype = 'uint8')

# rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), (100,100,100), -1)

# circle = cv.circle(blank.copy(), (200, 200), 200, (100,255,0), -1)

# bitwise_or = cv.bitwise_or(rectangle, circle)
# bitwise_and = cv.bitwise_and( circle,rectangle)

# bitwise_xor = cv.bitwise_xor(rectangle, circle)

# cv.imshow('bitwise_xor', bitwise_xor)


# rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), (20,100,100), -1)

# circle = cv.circle(blank.copy(), (200, 200), 200, (100,25,200), -1)

# bitwise_or = cv.bitwise_or(rectangle, circle)
# bitwise_and = cv.bitwise_and( circle,rectangle)

# bitwise_xor = cv.bitwise_xor(rectangle, circle)
# # cv.imshow('bitwise_and', bitwise_and)
# cv.imshow('bitwise_xor', bitwise_xor)
# #cv.imshow('bitwise_or', bitwise_or)

cv.waitKey(0)