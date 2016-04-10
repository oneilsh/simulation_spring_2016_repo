from controller import Controller

def setup():
    size(1024, 768)
    global controller
    controller = Controller()
  
def draw():
    global controller
    controller.draw()