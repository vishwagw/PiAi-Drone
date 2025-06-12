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



