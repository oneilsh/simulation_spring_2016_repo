def setup():
    size(600, 400) # width and height of window
    global circle_x
    global circle_y
    global circle_d
    circle_x = width/2 # processing “magic variable”
    circle_y = height/2 # processing “magic variable”
    circle_d = 100

def draw():
    global circle_x
    global circle_y
    global circle_d
 
    background (0, 0, 0) # rgb fill black
    fill (200, 50, 50) # set fill color redish
    stroke(50, 50, 200) # set stroke color bluish
    # draw circle
    # https://processing.org/reference/ellipse_.html
    ellipse (circle_x, circle_y, circle_d, circle_d)
    circle_x = circle_x + 0.25
    circle_y = circle_y + 0.25

