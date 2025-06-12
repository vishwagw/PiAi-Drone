import cv2 
import os

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240

cap = cv2.VideoCapture("http://[your wifi number]:8091/?action=stream")
cap.set(3, int(SCREEN_WIDTH))
cap.set(4, int(SCREEN_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')

try:
    if not os.path.exists('./data'):
        os.makedirs('./data')
except OSError:
    pass

video_orig = cv2.VideoWriter('./data/object_video.avi', fourcc, 20.0, (SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fail Capture")
        break

    frame = cv2.rotate(frame, cv2.ROTATE_180)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    video_orig.write(frame)  # Save the video's frame
    cv2.imshow('Video', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
video_orig.release() 
cv2.destroyAllWindows()
