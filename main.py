import time
from TrafficController import *
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

myTraffic = TrafficController()
myTraffic.run()


    


