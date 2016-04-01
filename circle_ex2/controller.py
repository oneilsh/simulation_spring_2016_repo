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
        gravity = PVector(0, 0.5)
        wind = PVector(0.2, 0)
        
        for circle in self.circles:
            if mousePressed:
                #circle.apply_force(wind) # we could apply a wind force if we want
                
                ## gravitational attraction to the mouse...
                mousepos = PVector(mouseX, mouseY)
                tomouse = mousepos - circle.pos
                disttomouse = tomouse.mag()
                tomouse.normalize()
                circle.apply_force(500*tomouse/(disttomouse**2))
                
            if keyPressed:
                # gravity as a force scales with the mass of the object
                # (and then is cancelled inside! by a = f/m!)                    
                circle.apply_force(gravity * circle.mass)
                
            circle.draw()
            circle.move()
            
            # the forces, applied from the outside, shall not accumulate over time
            circle.reset_acceleration()
