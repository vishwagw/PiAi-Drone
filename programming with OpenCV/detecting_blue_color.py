# method B for img segmentation:
import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print("ERROR: unable to open the camera")
    exit(1)

while(True):
    ret, img_frame = cap.read()
    if ret == False:
        print("ERROR: Failed")
        break;

    img_hsv = cv2.cvtColor(img_frame, cv2.COLOR_BGR2HSV)

    lower_blue = (120-20, 70, 0)
    upper_blue = (120+20, 255, 255)
    img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

    img_result = cv2.bitwise_and(img_frame, img_frame, mask = img_mask)

    cv2.imshow('Color', img_frame)
    cv2.imshow('Result', img_result)

    key = cv2.waitKey(1) 
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()