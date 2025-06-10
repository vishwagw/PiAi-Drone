import cv2 

img_color = cv2.imread('F:/AIDrone/test.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
ret, img_binary = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY_INV)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
img_binary = cv2.morphologyEx(img_binary, cv2.MORPH_CLOSE, kernel)

contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img_color, contours, 0, (0, 0, 255), 3)
cv2.drawContours(img_color, contours, 1, (0, 255, 0), 3)

for contour in contours:
    mu = cv2.moments(contour)

    cx = int(mu['m10']/mu['m00'] + 1e-5)
    cy = int(mu['m01']/mu['m00'] + 1e-5)

    cv2.circle(img_color, (cx, cy), 15, (0, 255, 255), -1)
    print("[cx, cy]", cx, cy)

cv2.imshow("result", img_color)
cv2.waitKey(0)

