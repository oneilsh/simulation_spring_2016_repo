class Circle:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def draw(self):  # see note below
        fill(200, 50, 50)
        ellipse(self.x, self.y, self.d, self.d)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
