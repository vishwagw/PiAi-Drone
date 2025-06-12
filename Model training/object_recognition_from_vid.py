# building a model for object recognition:
import cv2 as cv
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.model_selection import train_test_split

# Step 1: Capture Video Footage
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240

cap = cv.VideoCapture("http://[your wifi number]:8091/?action=stream")
cap.set(3, int(SCREEN_WIDTH))
cap.set(4, int(SCREEN_HEIGHT))

fourcc = cv.VideoWriter_fourcc(*'XVID')
    
try:
  if not os.path.exists('./data'):
    os.makedirs('./data')
  except OSError:
    pass

video_orig = cv.VideoWriter('./data/object_video.avi', fourcc, 20.0, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("캡쳐 실패")
            break
        
    frame = cv.rotate(frame, cv.ROTATE_180)
    video_orig.write(frame)  # Save video frame
    
    # Step 2: Extract Frames from Video
    if frame_count % 10 == 0:  # Save every 10th frame as an image
        image_path = f'./data/frame_{frame_count}.jpg'
        cv.imwrite(image_path, frame)
    
    cv.imshow('Video', frame)
    frame_count += 1
    
    key = cv.waitKey(1)
    if key == 27: 
        break

cap.release()
video_orig.release()
cv.destroyAllWindows()

# Step 3: Label Images (Manual Step)
# Manually label the saved images in the './data' directory using a tool like LabelImg.
    
# Step 4: Data Preprocessing
image_paths = [os.path.join('./data', fname) for fname in os.listdir('./data') if fname.endswith('.jpg')]
labels = []  # Assuming labels are collected after manual labeling
images = []




