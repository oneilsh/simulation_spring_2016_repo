from caboard import CaBoard
import time

class Controller:
    def __init__(self):
        self.caboard = CaBoard(50, 50)
        self.updating = True
    
    def draw(self):
        self.caboard.draw()
        if self.updating == True:
            self.caboard.update()
        time.sleep(0.1)
        
        if mousePressed:
            self.caboard.change_state(mouseX, mouseY)
            
        if keyPressed:
            self.updating = not self.updating