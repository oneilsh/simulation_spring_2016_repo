from controller import Controller

def setup():
    size(600, 400)
    global controller
    controller = Controller()
  
def draw():
    global controller
    controller.draw()
