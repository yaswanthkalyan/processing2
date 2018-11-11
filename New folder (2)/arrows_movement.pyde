x=50.0
y=375.0
speed=0.0
gravity=0.1
h=375
def setup():
    size(500,500);
    background(0);

def draw():
  fill(200,33,44);
  ellipse(x,y,50,50);
  rect(0,400,500,100);

def keyPressed():
  global x,y,speed,h;

  if (key==CODED):
    if (keyCode==RIGHT):
      background(0);
      x=x+10;
      if(x+50>width):
          x=475;
      

    elif(keyCode==LEFT):
      background(0);
      x=x-10;
      if(x-50<0):
          x=25;
          

          
    elif(keyCode==UP):
        background(0);
        y=y-10;
                  
    elif(keyCode==DOWN):
         background(0);
         y=y+10;
         if(y+50>400):
             y=375;    
    
  draw();

    
