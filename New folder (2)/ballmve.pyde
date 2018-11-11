add_library('sound');

x=100;
y=390;
xd=10;
def setup():
    size(600,500);
    background(0);
    sf = SoundFile(this, "barath");
def draw():
    global x
    global y
    fill(200,30,45);
    rect(0,400,600,100);
    ellipse(x,y,20,20);
def  keyReleased():
    global x;
    

    
    
    
    if(key==CODED):
        if(keyCode==RIGHT):
            if(x==580):
                x=580;
            elif(x<580):
                background(0);
                sf.play();
                #frameRate(2000000000);
                
            
                x=x+10;
                
            
            
        elif(keyCode==LEFT):
            if(x==20):
                x=20;
            elif(x>20):
                
                background(0);
                x=x-10;
        
            
         # else if(keyCode==LEFT):
         #     x=x-10;
    
        
