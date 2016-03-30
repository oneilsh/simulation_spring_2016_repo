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
        if self.y + self.d/2 >= height or self.y - self.d/2 <= 0:
            self.speed_y = self.speed_y * -1
        # Similar things should happen for the side walls
        if self.x + self.d/2 >= width or self.x - self.d/2 <= 0:
            self.speed_x = self.speed_x * -1

