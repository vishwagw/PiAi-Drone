# moving the drone up and down:
rom time import sleep
from pyaidrone.aiDrone import *
from pyaidrone.deflib import *
       
ready = -1
       
def receiveData(packet):
    global ready
    ready = packet[7] & 0x03
