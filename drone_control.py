# the drone control by using the technable machine:
import cv2
import keras
import numpy as np
import requests
from bs4 import BeautifulSoup
import threading
from time import sleep
from pyirbrain.zerodrone import *
from pyirbrain.deflib import *
from pyirbrain.ikeyevent import *

def recieveData(packet):
  global ready
  ready = packet [7] & 03

def preprocessing(frame):
  # Resizing 
  size = (224, 224)
  frame_resized = cv2.resize(frame, size, interpolation=cv2.INTER_AREA)

  # image normalization
  frame_normalized = (frame_resized.astype(np.float32) / 127.0) - 1

  # Reshape image dimensions - reshapes them for prediction.
  frame_reshaped = frame_normalized.reshape((1, 224, 224, 3))

  return frame_reshaped

# Load the trained model
model_filename = 'E:\AIDrone\converted_keras\keras_model.h5'
model = keras.models.load_model(model_filename)

# camera capture object, 0=built-in camera
#capture = cv2.VideoCapture("http://192.168.137.142:8091/?action=stream")  # ipcam사용시 여기의 0을 바꿔주세요
capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

zerodrone = ZERODrone()
ikey = IKeyEvent()
zerodrone.Open("COM3")
zerodrone.setOption(0)
sleep(0.5)


