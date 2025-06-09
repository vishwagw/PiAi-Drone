# showing the video streaming from the drone:
import cv2

cap = cv2.VideoCapture("http:// [rasbperry pi zero 2W WIFI address]/?action=stream")
# alternative:
# cap = cv2.VideoCapture(0)

# while loop:
while True:
    ret, frame = cap.read()
    frame = cv2.rotate(frame, cv2.ROTATE_180)

    if ret == False:
        print("Error: Could not read frame.")
        break

    img = cv2.resize(frame, (640, 480))
    cv2.imshow("Drone Video Stream", img)

    key = cv2.waitKey(1) 
    if key == 27: # ESC key to exit
        break

# initialize:
cap.release()
cv2.destroyAllWindows()

