from circle import Circle
# allow us to create circle objects

class Controller:
    def __init__(self):
        self.circle = Circle(width/2, height/2, 100)
    def draw(self):
        background(0, 0, 0)
	stroke(50, 50, 200) # set stroke color bluish
        self.circle.draw()
        self.circle.move(0.25,0.25)
