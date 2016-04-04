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

        print(self.compute_entropy())

    def compute_entropy(self):
        # must be float so we can divide by it sanely later
        tcount = float(len(self.particles))
        qcounts = [0, 0, 0, 0]

        for p in self.particles:
            if p.pos.x < width / 2:          # left
                if p.pos.y < height / 2:
                    qcounts[0] = qcounts[0] + 1
                else:
                    qcounts[1] = qcounts[1] + 1

            else:
                if p.pos.y < height / 2:
                    qcounts[2] = qcounts[2] + 1
                else:
                    qcounts[3] = qcounts[3] + 1

        entropy = 0.0
        for qcount in qcounts:
            prob = qcount / tcount
            if prob > 0:
                entropy = entropy + -1 * prob * (log(prob) / log(2.0))

        return entropy
