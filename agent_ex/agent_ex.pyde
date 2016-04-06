from controller import Controller

def setup():
    size(600, 400, FX2D)
    global controller
    controller = Controller()
  
def draw():
    global controller
    controller.draw()