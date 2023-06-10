from Sensors import *
from CompositeLights import *
from Lights import *

class MotionSensor(DigitalSensor):

    def __init__(self, pin):
        super().__init__(pin, lowactive=False)

    def motionDetected(self):
        return self.tripped()


class TFLight(Light):
    """
    Traffic Light constructor
    """
    def __init__(self):
    #print("TrafficLight constructor")
    
    #North/South Lights    
        self._greenLightNS = Light(2, "NS Green")
        self._yellowLightNS = Light(3, "NS Yellow")
        self._redLightNS = Light(4, "NS Red")

    #East/West Lights
        self._greenLightEW = Light(5, "EW Green")
        self._yellowLightEW = Light(6, "EW Yellow")
        self._redLightEW = Light(7, "EW Red")

    def NSGreen():
        print("Trafficlight - go/green")
        self._greenLightNS.on()
        self._yellowLightNS.off()
        self._redLightNS.off()
        
    def NSYellow():
        print("Trafficlight - caution")
        self._yellowLightNS.on()
        self._greenLightNS.off()
        self._redLightNS.off()
    
    def NSRed():
        print("Trafficlight - Stop")
        self._redLightNS.on()
        self._greenLightNS.off()
        self._yellowLightNS.off()

    def EWGreen():
        print("Trafficlight - go/green")
        self._greenLightEW.on()
        self._yellowLightEW.off()
        self._redLightEW.off()
        
    def EWYellow():
        print("Trafficlight - caution")
        self._yellowLightEW.on()
        self._greenLightEW.off()
        self._redLightEW.off()
    
    def EWRed():
        print("Trafficlight - Stop")
        self._redLightEW.on()
        self._greenLightEW.off()
        self._yellowLightEW.off()




