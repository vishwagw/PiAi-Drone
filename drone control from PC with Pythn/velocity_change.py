# velocity changing:
rom time import sleep
from pyaidrone.aiDrone import *
from pyaidrone.deflib import *
       
ready = -1
       
def receiveData(packet):
    global ready
    ready = packet[7] & 0x03
            
if __name__ = '__main__':
       
    aidrone = AIDrone(recevieData)
    aidrone.Open("COM3")   # change to the your ports number
    aidrone.setOption(0)
    sleep(0.5)
            
    while ready != 0:
        sleep(0.1)
                  
        aidrone.takeoff()
        sleep(5)
        aidrone.velocity(FRONT, 100)   
        sleep(2)
        aidrone.velocity(FRONT, 0) 
        sleep(5)
        aidrone.velocity(BACK, 100)
        sleep(2)
        aidrone.velocity(BACK, 0)
        sleep(5)
        aidrone.landing()
        sleep(5)
        aidrone.Close()

    
