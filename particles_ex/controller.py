from particle import Particle

class Controller:

    def __init__(self):
        self.particles = list()
        for i in range(0, 200):
            newp = Particle(PVector(width / 4, height / 4))
            self.particles.append(newp)

    def draw(self):
        background(0, 0, 0)
        for p in self.particles:
            p.draw()
            p.brownian_move()

