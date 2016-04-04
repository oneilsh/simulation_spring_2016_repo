

class Particle:

    def __init__(self, pos_vec):
        self.pos = pos_vec
        self.speed = PVector(0, 0)

    def draw(self):
        fill(0, 0, 0)  # black
        stroke(255, 255, 255)  # white
        ellipse(self.pos.x, self.pos.y, 5, 5)

    def brownian_move(self):
        self.speed.x = randomGaussian() * 2.0
        self.speed.y = randomGaussian() * 2.0
        self.pos = self.pos + self.speed

        self.fix_position()  # fix position if off screen

    def fix_position(self):
        if self.pos.x > width:
            self.pos.x = self.pos.x - width
        elif self.pos.x < 0:
            self.pos.x = width + self.pos.x

        if self.pos.y > height:
            self.pos.y = self.pos.y - height
        elif self.pos.y < 0:
            self.pos.y = height + self.pos.y
