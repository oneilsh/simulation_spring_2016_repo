class Circle:
    def __init__(self, x, y, d, sx, sy):
        self.x = x
        self.y = y
        self.d = d
        self.speed_x = sx
        self.speed_y = sy

    def draw(self):  # see note below
        fill(200, 50, 50)
        stroke(50, 50, 200) # set stroke color bluish
        ellipse(self.x, self.y, self.d, self.d)

    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
