from controller import Controller

def setup():
    size(800, 600)
    global controller
    controller = Controller()
  
def draw():
    global controller
    controller.draw()