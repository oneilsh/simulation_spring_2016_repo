from agent import Agent
from mousefollower import MouseFollower

class Flock:
    def __init__(self):
        self.r = random(0, 255)
        self.g = random(0, 255)
        self.b = random(0, 255)
        
        self.agents = list()
        
        for i in range(0, 20): 
            newagent = Agent(PVector(random(0, width), random(0, height)),             # pos
                             PVector(random(-3, 3), random(-3, 3)),  # speed
                             random(3, 3.1),                         # max_speed
                             random(0.1, 0.22),                      # max_force
                             random(100, 150),                       # sight_distance
                             self.r, self.g, self.b)
            self.agents.append(newagent)
       
        follower = MouseFollower(PVector(random(0, width), random(0, height)),             # pos
                       PVector(random(-3, 3), random(-3, 3)),  # speed
                       random(1, 3.1),                         # max_speed
                       random(0.02, 0.32),                      # max_force
                       random(100, 150),                       # sight_distance
                       self.r, self.g, self.b)
        
        self.agents.append(follower)

    def draw(self):
        for agent in self.agents:
            agent.draw()
            
            if mousePressed:
                mousepos = PVector(mouseX, mouseY)
                agent.seek(mousepos)
            else:
                agent.cognate(self.agents)

            agent.move()
            agent.reset_acceleration()
            
            