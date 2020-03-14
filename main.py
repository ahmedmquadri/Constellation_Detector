import cv2 as cv
import numpy as np

img = cv.imread('Libra_Unlabelled.png')
# cv.imshow('Unlabelled', img)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', img_gray)
threshold = 128
ret, img_binary = cv.threshold(img_gray,127,255,cv.THRESH_BINARY)
cv.imshow('Binary', img_binary)
view_mode = 1
cv.waitKey(0);

