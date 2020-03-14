import cv2 as cv
import numpy as np

img = cv.imread('Constellations_Undetected/Gemini_Undetected.png')
img_templ = cv.imread('Constellations_Template/Gemini.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_templ_gray = cv.cvtColor(img_templ, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', img_gray)
threshold = 128
ret, img_binary = cv.threshold(img_gray,127,255,cv.THRESH_BINARY)
ret_temp, img_templ_binary = cv.threshold(img_templ_gray,127,255,cv.THRESH_BINARY)
cv.imshow('Binary', img_binary)
cv.imshow('Binary', img_templ_binary)
view_mode = 1
cv.waitKey(0)


