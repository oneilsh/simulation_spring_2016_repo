
class Circle:
    def __init__(self, x, y, d, sx, sy):
        self.x = x
        self.y = y
        self.d = d
        self.speed_x = sx
        self.speed_y = sy

    def draw(self):
        fill(200, 50, 50)
        stroke(50, 50, 200)
        ellipse(self.x, self.y, self.d, self.d)
    
    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        
        if self.y + self.d/2 >= height:
            self.speed_y = self.speed_y * -1
            self.y = height - self.d/2 - 0.001
        
        if self.y - self.d/2 <= 0:
            self.speed_y = self.speed_y * -1
            self.y = self.d/2 + 0.001
            
        if self.x + self.d/2 >= width:
            self.speed_x = self.speed_x * -1
            self.x = width - self.d/2 - 0.001
            
        if self.x - self.d/2 <= 0:
            self.speed_x = self.speed_x * -1
            self.x = self.d/2 + 0.001
    
