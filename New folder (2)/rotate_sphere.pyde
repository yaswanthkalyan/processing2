def setup():
    size(1000,300,P3D);
    
def draw():

     translate(mouseX,mouseY);
     fill(190,60-mouseX,50-mouseY);
     rotate(300-mouseX);
     sphere(210);
     
