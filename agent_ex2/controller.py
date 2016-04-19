from flock import Flock

class Controller:
    def __init__(self):
        #self.flock = Flock()
        self.flockb = Flock()
        
    def draw(self):        
        background(230, 230, 230)

        #self.flock.draw()
        self.flockb.draw()