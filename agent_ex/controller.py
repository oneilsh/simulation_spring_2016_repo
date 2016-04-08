from agent import Agent

class Controller:

    def __init__(self):
        self.agents = list()
        for i in range(0, 20): 
            newagent = Agent(PVector(width/2, height/2),             # pos
                             PVector(random(-3, 3), random(-3, 3)),  # speed
                             random(2, 2.1),                         # max_speed
                             random(0.1, 0.12),                      # max_force
                             random(200, 250))                       # sight_distance
            self.agents.append(newagent)

    def draw(self):
        background(230, 230, 230)
        mousepos = PVector(mouseX, mouseY)
        for agent in self.agents:
            agent.draw()
            
            if mousePressed:
                agent.seek(mousepos)
            else:
                agent.cognate(self.agents)

            agent.move()
            agent.reset_acceleration()
            
            