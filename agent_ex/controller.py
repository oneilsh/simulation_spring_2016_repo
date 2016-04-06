from agent import Agent
import random

class Controller:

    def __init__(self):
        self.agents = list()
        for i in range(0, 10):
            rspx = (random.random() - 0.5)*2
            rspy = (random.random() - 0.5)*2
            rmaxsp = random.random() * 2
            newagent = Agent(PVector(width/2, height/2), PVector(rspx, rspy), rmaxsp)
            self.agents.append(newagent)

    def draw(self):
        background(230, 230, 230)
        for agent in self.agents:
            agent.draw()
            agent.move()
            
            
            agent.reset_acceleration()