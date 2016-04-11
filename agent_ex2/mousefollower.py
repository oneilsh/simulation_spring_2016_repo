from agent import Agent

class MouseFollower(Agent): 
    
    
    def cognate(self, allagents):
        mousepos = self.findmouse()
        tomouse = self.pos - mousepos
        if tomouse.mag() < self.sight_distance:
            self.seek(mousepos)
        else:
            self.seek(PVector(width/2, height/2))
    
    def findmouse(self):
        return PVector(mouseX, mouseY)
    
    
    def draw(self):
        fill(200, 50, 50, 150)
        stroke(0, 0, 0, 100)
        # ellipse(self.pos.x, self.pos.y, 10, 10)
        # rect(self.pos.x - 15, self.pos.y - 5, 30, 10)
        # line(self.pos.x, self.pos.y, self.pos.x + 40, self.pos.y)
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        angle = atan2(self.speed.y, self.speed.x)
        rotate(angle)
        rect(-15, -5, 30, 10)
        pushMatrix()
        rotate(-1*PI/8)
        line(0, 0, 40, 0)
        popMatrix()
        pushMatrix()
        rotate(PI/8)
        line(0, 0, 40, 0)
        popMatrix()
        #line(0, 0, 40, 0)
        popMatrix()
