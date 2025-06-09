# multi template matching:
import cv2
import numpy as np

def notInList(newObject):
    for detectedObject in detectedObjects:
        a = newObject[0]-detectedObject[0]
        b = newObject[1]-detectedObject[1]
        if np.sqrt(a*a+b*b) < 5:
            return False
    return True

detectedObjects = []

img_rgb = cv2.imread('F:/AIDrone/Real OpenCV/SourceCode/Ch14/test.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
         
img_template = cv2.imread('F:/AIDrone/Real OpenCV/SourceCode/Ch14/template.jpg', cv2.IMREAD_GRAYSCALE)
w, h = img_template.shape[:2]
         
res = cv2.matchTemplate(img_gray, img_template, cv2.TM_CCOEFF_NORMED)

count = 0
for x in range(res.shape[1]):
    for y in range(res.shape[0]):
        if res[y, x] > 0.9 and notInList((x, y)):
            detectedObjects.append((x, y))
            cv2.rectangle(img_rgb, (x, y), (x+w, y+h), [0, 0, 255], 1)
            count = count + 1

print(count)
cv2.imshow('result', img_rgb)
cv2.waitKey(0)
