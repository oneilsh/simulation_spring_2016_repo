
class Agent:

    def __init__(self, pos_vec, speed_vec, max_speed):
        self.pos = pos_vec
        self.speed = speed_vec
        self.max_speed = max_speed
        
        # Acceleration is 0 by default
        self.acceleration = PVector(0, 0)
        # boring mass
        self.mass = 1.0
        
    # f = ma, equivalently a = f/m
    def apply_force(self, force_vec):
        self.acceleration = self.acceleration + force_vec / self.mass

    def reset_acceleration(self):
        self.acceleration = self.acceleration * 0

    def draw(self):
        fill(150, 150, 150, 150)
        stroke(0, 0, 0, 100)
        ellipse(self.pos.x, self.pos.y, 10, 10)
    
    def move(self):
        self.speed = self.speed + self.acceleration
        self.speed.limit(self.max_speed)
        self.pos = self.pos + self.speed
        
        self.fix_position()
        
    def fix_position(self):
        if self.pos.x > width:
            self.pos.x = self.pos.x - width
        elif self.pos.x < 0:
            self.pos.x = width + self.pos.x
 
        if self.pos.y > height:
            self.pos.y = self.pos.y - height
        elif self.pos.y < 0:
            self.pos.y = height + self.pos.y
