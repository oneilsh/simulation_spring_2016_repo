from cell import Cell
import sys

class CaBoard:
    def __init__(self, numcells):
        self.numcells = numcells
        self.gen_number = 0
        self.lastgen = self.new_cell_list()
        self.currentgen = self.new_cell_list()
        middle_cell = self.currentgen[int(self.numcells/2)]
        middle_cell.set_state(1)
        
    def draw(self):
        for cell in self.currentgen:
            if cell.state == 1:
                sys.stdout.write("#")
            else:
                sys.stdout.write("_")
                
        sys.stdout.write("\n")
        
    def update(self):
        temp = self.lastgen
        self.lastgen = self.currentgen
        self.currentgen = temp
        self.gen_number = self.gen_number + 1
   
        neighborhood = [None, None, None]
        for cell in self.currentgen:
            pos = cell.pos
            neighborhood[0] = self.lastgen[(pos - 1) % self.numcells]
            neighborhood[1] = self.lastgen[(pos) % self.numcells]
            neighborhood[2] = self.lastgen[(pos + 1) % self.numcells]
            
            nextstate = cell.compute_next_state(neighborhood) 
            cell.set_state(nextstate)
   
    def new_cell_list(self):
        cells = list()
        for i in range(0, self.numcells):
            newcell = Cell(0, i)
            cells.append(newcell)
            
        return cells