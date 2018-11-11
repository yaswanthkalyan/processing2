def setup():
    size(1000,800);
def click():
    if(mousePressed):
      background(255-mouseX);
def draw():
    translate(mouseX,mouseY);
    fill(255-mouseX,200-mouseY,150);
    ellipse(mouseX,mouseY,60,50);
    click();
