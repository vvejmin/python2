from configparser import Interpolation
import cv2 as cv
import numpy as np

# Problem1
# Open the image pic1.jpg and display it with the name pic1. Convert the image to grayscale and
# display in a separate window to compare with the original image.
pic1 = cv.imread('pic1.jpg')
cv.imshow('pic1', pic1)

gray_scale = cv.cvtColor(pic1, cv.COLOR_BGR2GRAY)

cv.imshow('Goat_gray', gray_scale)


# Problem2
# Open the image pic1.jpg and display it with the name pic1. Blur the image using Gaussian blur
# using 2 different windows sizes: (3, 3) and (11, 11) and display both versions in separate
# windows to compare with the original image.

blur_1 = cv.GaussianBlur(gray_scale,(3,3), cv.BORDER_DEFAULT)
blur_2 = cv.GaussianBlur(pic1,(11,11), cv.BORDER_ISOLATED)
cv.imshow('Blur_1', blur_1)
cv.imshow('Blur_2', blur_2)


# Problem 3.
# Open the image pic2.jpg and display it with the name pic2. Try to detect the image edges using
# Canny edge detector and display the result in a separate window. Then run the edge detector
# on a blurred version of an image (use a window size of your choice) and display the result in a
# different window to compare.

pic2 = cv.imread('pic2.jpg')
edge_pic2 =cv.Canny(pic2, 125, 175)
blur_pic2 = cv.GaussianBlur(pic2,(1,1), cv.BORDER_DEFAULT)
blur_pic2_2 = cv.GaussianBlur(pic2,(11,11), cv.BORDER_DEFAULT)
blur_edge_pic2 = cv.Canny(blur_pic2, 10, 10)
blur_edge_pic2_2= cv.Canny(blur_pic2_2, 125, 175)
cv.imshow('pic2', pic2)
cv.imshow('Edge_pic2', edge_pic2)
cv.imshow('Blur_edge_pic2', blur_edge_pic2)

cv.imshow('Blur_Edge_pic_2', blur_edge_pic2_2)


# Problem 4
# Open the image pic2.jpg and display it with the name pic2. Resize the image to have 2 times
# bigger width and the same height as the original image, use INTER_AREA interpolation. Then
# resize the original image to have 2 times smaller height and the same width as the original
# image, use INTER_CUBIC interpolation. Display both versions in separate windows.

pic2 = cv.imread('pic2.jpg')
width_1 = int((pic2.shape[1]*0.5))
height_1 = int((pic2.shape[0]*1))
dim = (width_1, height_1)
resized_img_1 = cv.resize(pic2, dim, interpolation = cv.INTER_AREA)
cv.imshow('Pic2_resized_1', resized_img_1)

width_2 = int((pic2.shape[1]*1))
height_2 = int((pic2.shape[0]*0.5))
dim = (width_2, height_2)
resized_img_2 = cv.resize(pic2, dim, interpolation = cv.INTER_CUBIC)
cv.imshow('Pic2_resized_2', resized_img_2)


# Problem 5.
# Open the image pic2.jpg and display it with the name pic2. Translate the image to go down by
# 200 pixels and to the right by 50 pixels. Then rotate the image around its center by 50 degrees.
# Then flip the resulting image both vertically and horizontally. Display the result after each action
# in a separate window

pic2 = cv.imread('pic2.jpg')

def translate(img, x, y):

    transMat = np.float64([[1, 0, x], [0, 1, y]])
    dimentions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimentions)


translated = translate(pic2, 50, 70)

cv.imshow('Translated', translated)


def rotate(img, angle, rotPoint = None):

    (height, width) = (img.shape[0], img.shape[1])

    if rotPoint == None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # 1.0 - scale
    dimentions = (width, height)

    return cv.warpAffine(img, rotMat, dimentions)


rotated = rotate(translated, -50)


cv.imshow('Rotated', rotated)

flip_1 = cv.flip(translated, 0)
flip_2 = cv.flip(translated, 1)
flip_3 = cv.flip(translated, -1)
cv.imshow('Fliped_1',flip_1 )
cv.imshow('Fliped_2',flip_2 )
cv.imshow('Fliped_3',flip_3 )


# Problem 6.
# Open the image pic3.jpg and display it with the name pic3. Find the edges of the image using
# Canny edge detector and then try to find its contours with parameters of your choice. Then
# convert the original image to grayscale and try to find the contours on a blurred version of the
# grayscale of the original image. Display the 2 results in separate windows to compare.

pic3 = cv.imread('pic3.jpg')

width = int(pic3.shape[1] * 1)
haight = int(pic3.shape[0] * 1)
dim = (width, haight)
resized_img = cv.resize(pic3, dim, interpolation=cv.INTER_CUBIC)

gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(resized_img, 125, 175)
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

contours_cany_1, hierarchies_cany_1 = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
contours_cany_2, hierarchies_cany_2 = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(len(contours_cany_1))
print(hierarchies_cany_1)

print(len(contours_cany_2))
print(hierarchies_cany_2)

ret_gray, thresh_gray = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
contours_thresh_gray, hierarchies_thresh_gray = cv.findContours(thresh_gray, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(ret_gray)
print(len(thresh_gray))
print(len(contours_thresh_gray))

cv.imshow('pic3', resized_img)
cv.imshow('gray', gray)
cv.imshow('canny_edges', canny)
cv.imshow('blur', blur)

contours_blur, hierarchies_blur = cv.findContours(blur, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

blank = np.zeros(resized_img.shape, dtype='uint8')  # cv.imread('Photos/pic2.jpg')
print(blank)
print(len(blank))
cv.imshow('blank', blank)

cv.drawContours(blank, contours_thresh_gray, -1, (0, 200, 180), 2)
cv.imshow('contours drawn using thresh', blank)

cv.drawContours(blank, contours_cany_1, -1, (50, 200, 0), 2)
cv.imshow('contours drawn using canny', blank)

cv.drawContours(blank, contours_cany_2, -1, (50, 70, 255), 2)
cv.imshow('contours drawn using canny_2', blank)

cv.drawContours(blank, contours_blur, -1, (155, 0, 0), 2)
cv.imshow('contours drawn using blur', blank)

cv.waitKey(0