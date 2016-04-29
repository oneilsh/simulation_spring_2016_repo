from individual import Individual
from population import Population

class Controller:
    def __init__(self):
        self.coins_list = [0.1, 0.25, 0.25, 0.5, 1, 1, 5, 10]
        self.target = 8.94
        
        self.pop = Population(50, self.coins_list, self.target)
        
    def draw(self):
        self.pop.print_summary()
        self.pop.random_mate()
        self.pop.cull()