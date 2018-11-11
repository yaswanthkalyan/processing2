def setup():
    size(600,600);
    background(0,191,255);
    noFill();
def draw():
    strokeWeight(random(3,10));
    stroke(random(255),random(255),random(255));
    rainbow_size=random(600,700);
    ellipse(600,600,rainbow_size,rainbow_size);
