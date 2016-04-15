from cell import Cell
import sys

class CaBoard:
    def __init__(self, numrows, numcols):
        self.numrows = numrows
        self.numcols = numcols
        self.gen_number = 0
        self.lastgen = self.new_cell_list()
        self.currentgen = self.new_cell_list()
        
        for rownum in range(0, self.numrows):
            for colnum in range(0, self.numcols):
                if random(0, 1) < 0.5:
                    cell = self.currentgen[rownum][colnum]
                    cell.set_state(1)
            
        
    def draw(self):
        cellwidth = width/self.numcols
        cellheight = height/self.numrows
        for rownum in range(0, self.numrows):
            for colnum in range(0, self.numcols):
                cell = self.currentgen[rownum][colnum]
                cell.draw(cellwidth, cellheight)        

        
    def update(self):
        temp = self.lastgen
        self.lastgen = self.currentgen
        self.currentgen = temp
        self.gen_number = self.gen_number + 1
   
        neighborhood = [None, None, None, None, None, None, None, None]
        for rownum in range(0, self.numrows):
            for colnum in range(0, self.numcols):
                cell = self.lastgen[rownum][colnum]
                rowpos = cell.rowpos
                colpos = cell.colpos
                neighborhood[0] = self.lastgen[(rowpos - 1) % self.numrows][(colpos - 1) % self.numcols]
                neighborhood[1] = self.lastgen[(rowpos - 1) % self.numrows][(colpos) % self.numcols]
                neighborhood[2] = self.lastgen[(rowpos - 1) % self.numrows][(colpos + 1) % self.numcols]
                neighborhood[3] = self.lastgen[(rowpos) % self.numrows][(colpos - 1) % self.numcols]
                neighborhood[4] = self.lastgen[(rowpos) % self.numrows][(colpos + 1) % self.numcols]
                neighborhood[5] = self.lastgen[(rowpos + 1) % self.numrows][(colpos - 1) % self.numcols]
                neighborhood[6] = self.lastgen[(rowpos + 1) % self.numrows][(colpos) % self.numcols]
                neighborhood[7] = self.lastgen[(rowpos + 1) % self.numrows][(colpos + 1) % self.numcols] 
            
                nextstate = cell.compute_next_state(neighborhood) 
                nextgencell = self.currentgen[rownum][colnum]
                nextgencell.set_state(nextstate)
   
    def new_cell_list(self):
        rows = list()
        for rownum in range(0, self.numrows):
            newrow = list()
            for colnum in range(0, self.numcols):
                newcell = Cell(0, rownum, colnum)
                newrow.append(newcell)
            rows.append(newrow)
        return rows