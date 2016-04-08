
class Agent:

    def __init__(self, pos_vec, speed_vec, max_speed, max_force, sight_dist):
        self.pos = pos_vec
        self.speed = speed_vec
        self.max_speed = max_speed
        self.max_force = max_force
        self.sight_distance = sight_dist
        
        # Acceleration is 0 by default
        self.acceleration = PVector(0, 0)
        # boring mass
        self.mass = 1.0
        
    def seek(self, target_vec):
        desiredspeed = target_vec - self.pos
        desiredspeed.normalize()
        desiredspeed = desiredspeed * self.max_speed
        
        steerforce = desiredspeed - self.speed
        self.apply_force(steerforce)
        
    def cognate(self, allagents):
        neighbors = list()
        for agent in allagents:
            if agent != self:
                dirvec = self.pos - agent.pos
                distance = dirvec.mag()
                if distance < self.sight_distance:
                    neighbors.append(agent)
                    
        self.flock(neighbors)
   
    def flock(self, neighbors):
        sep = self.separate_force(neighbors)
        self.apply_force(sep)
        align = self.align_force(neighbors)
        self.apply_force(align)
        cohesion = self.cohesion_force(neighbors)
        self.apply_force(cohesion)

    def cohesion_force(self, neighbors):
        sum = PVector(0, 0)
        for agent in neighbors:
            sum = sum + agent.pos
            
        if len(neighbors) > 0:
            center = sum/len(neighbors)
            desiredspeed = center - self.pos
            return self.desired_to_force(desiredspeed)
        else:
            return PVector(0, 0)

    def align_force(self, neighbors):
        sum = PVector(0, 0)
        for agent in neighbors:
            sum = sum + agent.speed
            
        if len(neighbors) > 0:
            desiredspeed = sum/len(neighbors)
            return self.desired_to_force(desiredspeed)
        else:
            return PVector(0, 0)
        
    def separate_force(self, neighbors):
        sum = PVector(0, 0)
        for agent in neighbors:
            diffvec = self.pos - agent.pos
            distance = diffvec.mag()
            diffvec.normalize()
            sum = sum + diffvec / (distance + 0.0001)  # avoid div by 0
            
        if len(neighbors) > 0:
            desiredspeed = sum/len(neighbors)
            return self.desired_to_force(desiredspeed)
        else:
            return PVector(0, 0)   # no neighbors, no force
   
    def desired_to_force(self, desired):
        desiredcopy = desired.get() # make a copy first
        desiredcopy.normalize()
        desiredcopy = desiredcopy * self.max_speed
        force = desiredcopy - self.speed
        force.limit(self.max_force)
        return(force)
        
    # f = ma, equivalently a = f/m
    def apply_force(self, force_vec):
        self.acceleration = self.acceleration + force_vec / self.mass

    def reset_acceleration(self):
        self.acceleration = self.acceleration * 0

    def draw(self):
        fill(150, 150, 150, 150)
        stroke(0, 0, 0, 100)
        # ellipse(self.pos.x, self.pos.y, 10, 10)
        # rect(self.pos.x - 15, self.pos.y - 5, 30, 10)
        # line(self.pos.x, self.pos.y, self.pos.x + 40, self.pos.y)
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        angle = atan2(self.speed.y, self.speed.x)
        rotate(angle)
        rect(-15, -5, 30, 10)
        pushMatrix()
        rotate(-1*PI/8)
        line(0, 0, 40, 0)
        popMatrix()
        pushMatrix()
        rotate(PI/8)
        line(0, 0, 40, 0)
        popMatrix()
        line(0, 0, 40, 0)
        popMatrix()
    
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