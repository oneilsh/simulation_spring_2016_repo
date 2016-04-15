class Cell:
    def __init__(self, initstate, rowpos, colpos):
        self.rowpos = rowpos
        self.colpos = colpos
        self.state = initstate
        
    def set_state(self, newstate):
        self.state = newstate
        
    def compute_next_state(self, nbh):
        count = 0
        for cell in nbh:
            if cell.state == 1:
                count = count + 1
                
        if self.state == 1:
            if count < 2 or count > 3:
                return 0
            
        if self.state == 0 and count == 3:
            return 1
        
        return self.state
        
    def draw(self, cellwidth, cellheight):
        xpos = self.colpos * cellwidth
        ypos = self.rowpos * cellheight
        stroke(0, 0, 0)
        if self.state == 1:
            fill(200, 200, 200)
        else:
            fill(80, 80, 80)
            
        rect(xpos, ypos, cellwidth, cellheight)