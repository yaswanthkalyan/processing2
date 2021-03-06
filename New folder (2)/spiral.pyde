x=0;
y=0;
number_of_points=1000;
circle_diameter=5;
plot_radius=200;
angle_incr=radians(25);
def setup():
    size(500,500);
    fill(random(255));
    smooth(0);
    noStroke();
def draw():
    global x;
    global y;
    global number_of_points;
    global circle_diameter;
    global plot_radius;
    global angle_incr;
    background(255);
    translate(width/2,height/2);
    for i in range(number_of_points):
        ratio=i/float(number_of_points);
        spiral_rad=ratio*plot_radius;
        angle=i*angle_incr;
        x=cos(angle)*spiral_rad;
        y=sin(angle)*spiral_rad;
        rotate(radians(-.0005*frameCount));
        ellipse(x,y,circle_diameter,circle_diameter);
