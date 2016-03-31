
class Circle:
    def __init__(self, pos_vec, d, speed_vec):
        self.pos = pos_vec
        self.d = d
        self.speed = speed_vec
        self.acceleration = PVector(0, 0.5)

    def draw(self):
        fill(200, 50, 50)
        stroke(50, 50, 200)
        ellipse(self.pos.x, self.pos.y, self.d, self.d)
    
    def move(self):
        self.speed = self.speed + self.acceleration
        self.pos = self.pos + self.speed
        
        if self.pos.y + self.d/2 >= height:
            self.speed.y = self.speed.y * -1
            self.pos.y = height - self.d/2 - 0.001
        
        if self.pos.y - self.d/2 <= 0:
            self.speed.y = self.speed.y * -1
            self.pos.y = self.d/2 + 0.001
            
        if self.pos.x + self.d/2 >= width:
            self.speed.x = self.speed.x * -1
            self.pos.x = width - self.d/2 - 0.001
            
        if self.pos.x - self.d/2 <= 0:
            self.speed.x = self.speed.x * -1
            self.pos.x = self.d/2 + 0.001
    
