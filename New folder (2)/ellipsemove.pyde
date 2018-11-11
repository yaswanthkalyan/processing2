def setup():
    size(1000,600);
def click():
    if(mousePressed):
     background(255);
def draw():
    translate(mouseX,mouseY);
    fill(255-mouseX,200-mouseY,150);
    ellipse(mouseX,mouseY,60,50);
    click();
