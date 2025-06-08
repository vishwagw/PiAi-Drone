# gettin training data from the video input:
import cv2
import os
import time

# create image folder:
if not os.path.exists("images"):
  os.makedir("images")

# opening the video files:
video = cv2.VideoCapture("video files")

# select objects to track:
ret, frame = video.read()
bbox = cv2.selerctROI(frame, False)

# Initialize the tracker:
tracker = cv2.TrackerCSRT_create()
tracker.init(frame, bbox)

# Initialize timer and counter
timer = time.time() 
counter = 0

# video output:
while True:
  #read frames:
  ret, frame = video. read()
  if not ret:
    break

  # object tracking
  success, bbox = tracker. update(frame)
  # output trace result
        if success:
            x, y, w, h = [int(i) for i in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
            # Check if timer has expired and save object image
            current_time = time.time()
            if current_time - timer >= 1:    # saving image for 1 second
                counter += 1
                object_img = frame[y:y+h, x:x+w]
                img_path = os.path.join("images", f"object_img_{counter}.jpg")
                cv2.imwrite(img_path, object_img)
                timer = current_time
        else:
            cv2.putText(frame, "Failed to track object", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
    
        # frame output
        cv2.imshow('Object Tracking', frame)
        
        # Handling keyboard input
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video file and close the window
video. release()
cv2.destroyAllWindows()
    
