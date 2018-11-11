def setup():
    size(600,600);
    background(0);
    
def draw():
    background(0);
    fill(200,10,10,200);
    ellipse(300,300,width,height);
    smooth();

    if(keyPressed==65535):
        background(0);
    else:  
        fill(255);
        textSize(random(20,200));
        text(key,random(30,300),random(30,300));
    
    
    
