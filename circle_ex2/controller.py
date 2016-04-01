from circle import Circle
import random

class Controller:
    def __init__(self):
        self.circles = list()
        for i in range(0, 10):
            rlocx = random.random() * width
            rlocy = random.random() * height
            rspx = random.random() * 2
            rspy = random.random() * 2
            rd = random.random() * 50 + 10
            newcircle = Circle(PVector(rlocx, rlocy), rd, PVector(rspy, rspy))
            self.circles.append(newcircle)
    
    def draw(self):
        background(0, 0, 0)

        for circle in self.circles:
            circle.draw()
            circle.move()

