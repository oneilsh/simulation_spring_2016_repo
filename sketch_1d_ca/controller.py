from caboard import CaBoard
import time

class Controller:
    def __init__(self):
        self.caboard = CaBoard(50)
    
    def draw(self):
        self.caboard.draw()
        self.caboard.update()
        time.sleep(0.1)