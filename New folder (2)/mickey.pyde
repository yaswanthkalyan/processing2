
def setup():
    size(1000,1000,P3D);
    perspective(60*PI/180,1,0.1,1000)
    background(180);
def draw():

    #directionalLight(126, 126, 126, 0, 0, -1);
    #directionalLight(126, 126, 126, 0, 0, 1);
    #lightSpecular(255,255,255);
    #ambientLight(51,102,126);
    spotLight(51, 102, 126, 220, 220, 0, -1, 0, 0, PI/9, 2);
    #pointLight(51, 102, 126, 35, 0, 36);
    #shininess(15);
    pushMatrix()
    mickey();
    popMatrix()

def mickey():
        face();
        body();
        legs();
        dress();
        shoes();
        hands();
    
def face():
    pushMatrix()
    fill(0);
    ellipse(220,220,150,150);
    fill(0);
    ellipse(155,140,100,100);
    fill(0);
    ellipse(290,130,100,100);
    noStroke();
    fill(255,218,185);
    ellipse(200,200,55,60);
    noStroke();
    fill(255,218,185);
    ellipse(250,200,50,60);
    noStroke();
    fill(255,218,185);
    ellipse(220,250,120,95);
    fill(255);
    ellipse(205,210,30,50);
    fill(255);
    ellipse(245,210,30,50);
    fill(0);
    ellipse(210,220,15,30);
    fill(0);
    ellipse(240,220,15,30);
    fill(0);
    ellipse(225,250,40,25);
   
    fill(255);
    #stroke(255,182,193);
    line(200,260,200,280);
    bezier(200,270,220,290,230,290,250,270);
    fill(230,0,0);
    bezier(210,275,220,295,230,295,240,275);
    rotate(PI/3.0);
    popMatrix()
    
def body():
    pushMatrix()
    fill(0);
    ellipse(220,395,150,195);
    fill(255,0,0);
    ellipse(220,420,150,150);
    rotate(PI/3.0);
    popMatrix()
    
def legs():
    pushMatrix()
    fill(0);
    ellipse(195,550,20,100);
    ellipse(245,550,20,100);
    rotate(PI/3.0);
    popMatrix()
    
def dress():
    pushMatrix()
    fill(255,0,0);
    rect(180,430,30,100);
    fill(255,0,0);
    rect(230,430,30,100);
    fill(255,204,0);
    ellipse(190,420,30,60);
    ellipse(250,420,30,60);
    rotate(PI/3.0);
    popMatrix()
    
def shoes():
    pushMatrix()
    shearX(PI/9.0);
    fill(255,204,0);
    ellipse(35,600,30,55);
    shearX(PI*3.0);
    fill(255,204,0);
    ellipse(-15,600,30,55);
    rotate(PI/3.0);
    popMatrix()
    
def hands():
     pushMatrix()
     fill(0);
     rect(130,320,47,20);
     ellipse(130,370,20,100);
     fill(255);
     ellipse(130,420,20,20);
     fill(0);
     rect(270,320,47,20);
     ellipse(315,370,20,100);
     fill(255);
     ellipse(315,420,20,20);
     rotate(PI/3.0);
     popMatrix();
