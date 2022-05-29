#!/usr/bin/env python
# coding: utf-8

# ## Problem 1.
# Open the image pic1.jpg and display it with the name pic1. Convert the image to grayscale and
# plot the histogram of pixel intensities using matplotlib.




import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt




pic1 = cv.imread('pic1.jpg') 





cv.imshow('pic1', pic1)

cv.waitKey(0)





gray = cv.cvtColor(pic1, cv.COLOR_BGR2GRAY)
gray_hist = cv.calcHist([gray], [0], None, [100], [0,200]) 
gray_hist = [i[0] for i in gray_hist]
print(gray_hist)



plt.imshow(cv.cvtColor(pic1, cv.COLOR_BGR2RGB))
plt.title('Flower')
plt.show()

x = np.arange(100)
plt.bar(x,gray_hist)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('number of pixels')
plt.show()


# ## Problem 2.
# Repeat the previous exercise without converting the image to grayscale and get 3 histograms
# for each of the color channels on one plot.




pic1 = cv.imread('pic1.jpg') 



colors = ('b', 'g', 'r')

plt.imshow(cv.cvtColor(pic1, cv.COLOR_BGR2RGB))
plt.title('Flower')
plt.show()

for i, col in enumerate(colors):
    print(i)
    hist = cv.calcHist([pic1], [i], None, [256], [0,256]) 
    x = np.arange(256)
    plt.plot(x,hist, color=col)
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('Number of pixels')


plt.show()





pic2 = cv.imread('pic2.jpg') 



colors = ('b', 'g', 'r')

plt.imshow(cv.cvtColor(pic1, cv.COLOR_BGR2RGB))
plt.title('Eiffel tower')
plt.show()

for i, col in enumerate(colors):
    print(i)
    hist = cv.calcHist([pic1], [i], None, [256], [0,256]) 
    x = np.arange(256)
    plt.plot(x,hist, color=col)
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('Number of pixels')


plt.show()


# ## Problem 3.
# Open the image pic1.jpg and display it with the name pic1. Binarize the image using 3 different
# methods: choosing the threshold by hand and using THRESH_BINARY method, using adaptive
# thresholding with mean and gaussian methods. Display the 3 results in separate windows.




pic1= cv.imread('pic1.jpg') 
gray = cv.cvtColor(pic1, cv.COLOR_BGR2GRAY)

pic1_gray = cv.cvtColor(gray, cv.COLOR_BGR2RGB)
plt.imshow(pic1_gray)
plt.figure(figsize =(20,8))

plt.imshow(pic1)




plt.imshow(gray, cmap ='gray')





threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
plt.figure(figsize =(20,8))
plt.imshow(thresh)





threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
plt.figure(figsize =(20,8))
plt.imshow(thresh, cmap='gray')
print(threshold)





threshold, thresh = cv.threshold(pic1_gray, 150, 255, cv.THRESH_BINARY)
plt.figure(figsize =(20,8))
plt.imshow(thresh)





adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
plt.imshow(cv.cvtColor(adaptive_thresh, cv.COLOR_BGR2RGB))
plt.title('adaptive thresholding Result')
plt.show()





adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 57, 2)
plt.figure(figsize =(20,8))
plt.title('adaptive thresholding Result')
plt.imshow(adaptive_thresh, cmap='gray')





adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 57, 2)
plt.figure(figsize =(20,8))
plt.title('adaptive thresholding Result')
plt.imshow(adaptive_thresh)





adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 57, 2)
plt.figure(figsize =(20,8))
plt.title('Gausian adaptive thresholding Result')
plt.imshow(adaptive_thresh)





adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 63, 14)
plt.figure(figsize =(20,8))
plt.title('Gausian adaptive thresholding Result')
plt.imshow(adaptive_thresh, cmap = 'gray')


# ## Problem 4.
# Open the image pic2.jpg and display it with the name pic2. Convert the image to grayscale. Try
# detecting the edges with a method of your choice. Use one technique of your choice on the
# image from what we have learned so far and try to get a better result. (better than simply using
# some edge detection technique on a grayscale of a raw image)
# 




pic2 = cv.imread('pic2.jpg')
gray = cv.cvtColor(pic2, cv.COLOR_BGR2GRAY)
plt.figure(figsize = (20,8))
plt.title('Eiffel Tower')

plt.imshow(pic2,cmap='gray')





pic2 = cv.imread('pic2.jpg')
pic2_RGB = cv.cvtColor(pic2, cv.COLOR_BGR2RGB)
plt.figure(figsize = (20,8))
plt.title('Eiffel Tower')

plt.imshow(pic2)





median_blur = cv.medianBlur(gray,7)
plt.figure(figsize = (20,8))
plt.title('Eiffel Tower')

plt.imshow(pic2,cmap='gray')





lap_1 = cv.Laplacian(median_blur, cv.CV_64F,-500)  
lap_1 = np.uint8(np.absolute(lap_1))
plt.figure(figsize = (20,8))
plt.imshow(lap_1)





lap_1 = cv.Laplacian(gray, cv.CV_64F,-1)  
plt.figure(figsize = (20,8))
plt.imshow(lap_1, cmap='gray')





threshold, thresh_1 = cv.threshold(median_blur, 150, 255, cv.THRESH_BINARY_INV)
plt.figure(figsize =(20,8))
plt.imshow(thresh_1,cmap = 'binary')





lap_2 = cv.Laplacian(thresh_1, cv.CV_64F,-1)  
plt.figure(figsize = (20,8))
plt.imshow(lap_2,cmap = 'gray')





sobelx = cv.Sobel(gray, cv.CV_32F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_32F, 0, 1)

plt.imshow(cv.cvtColor(sobelx, cv.COLOR_BGR2RGB))
plt.title('solbelx')
plt.show()

plt.imshow(cv.cvtColor(sobely, cv.COLOR_BGR2RGB))
plt.title('sobely')
plt.show()





combined_sobel = cv.bitwise_or(sobelx, sobely)

plt.imshow(cv.cvtColor(combined_sobel, cv.COLOR_BGR2RGB))
plt.title('combined sobel')
plt.show()





canny = cv.Canny(gray, 150, 175)

plt.imshow(cv.cvtColor(canny, cv.COLOR_BGR2RGB))
plt.title('canny')
plt.show()





cv.waitKey(0)

