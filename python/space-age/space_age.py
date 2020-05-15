class SpaceAge:
    sec = 0
    ear = 31557600
    def __init__(self, seconds):
        self.sec = seconds
        pass
    def on_earth(self):   
        return round((self.sec/self.ear),2)

    def on_mercury(self):     
        return round(self.sec/(0.2408467 * self.ear),2)

    def on_venus(self):   
        return round(self.sec/(0.61519726 * self.ear),2)

    def on_mars(self):    
        return round(self.sec/(1.8808158 * self.ear),2)

    def on_jupiter(self):     
        return round(self.sec/(11.862615 * self.ear),2)

    def on_saturn(self):  
        return round(self.sec/(29.447498 * self.ear),2)

    def on_uranus(self):  
        return round(self.sec/(84.016846 * self.ear),2)

    def on_neptune(self):     
        return round(self.sec/(164.79132 * self.ear),2)
