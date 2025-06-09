# single template matching:
import cv2
import numpy as np

img_rgb = cv2.imread('F:/AIDrone/Real OpenCV/SourceCode/Ch14/test.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

img_template = cv2.imread('F:/AIDrone/Real OpenCV/SourceCode/Ch14/template.jpg', cv2.IMREAD_GRAYSCALE)
w, h = img_template.shape[:2]

res = cv2.matchTemplate(img_gray, img_template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0]+w, top_left[1]+h)


cv2.rectangle(img_rgb, top_left, bottom_right, (0, 0, 255), 2)

cv2.imshow('result', img_rgb)
cv2.waitKey(0)
