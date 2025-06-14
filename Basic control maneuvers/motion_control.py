# basic motion control for autonomous drone:
#importing libraries 
import numpy as np
import cv2
from pymavlink import mavutil
from dronekit import connect, VehicleMode, LocationGlobalRelative, Vehicle, LocationGlobal
import time
import math

#connecting the vehicle 
V1drone = connect("udp:192.168.137.103:14550", wait_ready=True)

#video:
cap = cv2.VideoCapture(0)
