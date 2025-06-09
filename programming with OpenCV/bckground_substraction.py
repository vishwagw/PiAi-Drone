import cv2
import numpy as np
import os

cap = cv2.VideoCapture('F:/AIDrone/Real OpenCV/SourceCode/Ch15/15.4/output.avi')

foregroundBackground = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=250, detectShadows=False)

while(1):
    ret, img_frame = cap.read()
    if ret == False:
        break;
    
    blur = cv2.GaussianBlur(img_frame, (5,5), 0)
    img_mask = foregroundBackground.apply(blur, learningRate=0)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    img_mask = cv2.morphologyEx(img_mask, cv2.MORPH_CLOSE, kernel)    

    cv2.imshow('mask', img_mask)
    cv2.imshow('color', img_frame)
 
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()