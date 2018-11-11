c=color(255,0,0)
x=400.0
y=0.5
speed = 1.0
def setup():
    size(800,800)
def draw():
    background(255)
    move();
    display();
def move():
    global y;
    y=y+speed;
    if(y>height):
        y=0;
def display():
    fill(y,y/3,y/4);
    rect( x,y,40,90);   
