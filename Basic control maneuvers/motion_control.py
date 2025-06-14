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
#function for arming the drone and takeoff
#taking off drone to  target altitude
def arm_and_takeoff(aTargetAltitude):
    print("Pre-checking the drone..")
    #do not arm  drone until autopilot is ready
    while not V1drone.is_armable:
        print("Waiting for V1 drone vehicle to initialize...")
        time.sleep(1)

    print("Checking motors..")
    print("Arming motorw...")
    # vehicle should arm in DUIDED MODE.
    V1drone.mode = VehicleMode("GUIDED..")
    V1drone.armed = True

    time.sleep(2)

    print(V1drone.mode)

    # confirm vehicle armed before attemting to take off
    while not V1drone.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print("V1drone Taking-off")
    # Take off to target altitude
    V1drone.simple_takeoff(aTargetAltitude)
    # Wait until the vehicle reaches a safe height before processing the goto mode.
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately)
    while True:
        print(" Altitude: ", V1drone.location.global_relative_frame.alt )
        # Break and return from function just below target altitude.
        if V1drone.location.global_relative_frame.alt >= aTargetAltitude*0.9:
            print(" V1drone have Reached Target altitude...")
            break
        time.sleep(1)

#initializing the above function-
arm_and_takeoff(10)

#altitude calibrating
degree = 1
east = 0
north = 0 

