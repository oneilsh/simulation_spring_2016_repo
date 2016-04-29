from controller import Controller

def setup():
    size(100, 100)
    global controller
    controller = Controller()
    
def draw():
    global controller
    controller.draw()