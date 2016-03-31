from circle import Circle

class Controller:
    def __init__(self):
        self.circlea = Circle(width/2, height/2, 100, 1, 1)
        self.circleb = Circle(width/2, height/2, 100, 3, 3)
    
    def draw(self):
        background(0, 0, 0)
        self.circlea.draw()
        self.circleb.draw()
        self.circlea.move()
        self.circleb.move()
