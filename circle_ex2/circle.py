
class Circle:
    def __init__(self, pos_vec, d, speed_vec):
        self.pos = pos_vec
        self.d = d
        self.speed = speed_vec
        ## Acceleration is 0 by default
        self.acceleration = PVector(0, 0)
        ## mass is associated with diameter (perhaps should relate to area ;) )
        self.mass = self.d/100
        
        
    ## f = ma, equivalently a = f/m
    def apply_force(self, force_vec):
        self.acceleration = self.acceleration + force_vec/self.mass

    def reset_acceleration(self):
        self.acceleration = self.acceleration * 0

    def draw(self):
        fill(150, 150, 150, 150)
        stroke(0, 0, 0, 100)
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
    
