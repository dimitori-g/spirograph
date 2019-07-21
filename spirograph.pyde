# Spirograph design, created by changing r2 and prop
prop = 0.3
r1 = 300.0
r2 = 105.0
r3 = 5.0
x1 = y1 = t = 0
points = []

def setup():
    size(650, 650)

def draw():
    global r1, r2, x1, y1, t, prop, points
    translate(width/2 ,height/2)
    background(0)
    noFill()
    #big circle
    stroke(255)
    ellipse(x1, y1, 2*r1, 2*r1)
    #small circle
    x2 = (r1 - r2)*cos(t)
    y2 = (r1 - r2)*sin(t)
    ellipse(x2, y2, 2*r2, 2*r2)
    #drawing dot
    stroke(255, 0, 0)
    fill(255, 0, 0)
    x3 = x2 + prop*(r2-r3)*cos(-((r1-r2)/r2)*t)
    y3 = y2 + prop*(r2-r3)*sin(-((r1-r2)/r2)*t)
    ellipse(x3, y3, 2*r3, 2*r3)
    #chain lines and center dots
    stroke(200, 200, 100)
    fill(200, 200, 100)
    line(x3, y3, x2, y2)
    line(x2, y2, x1, y1)
    ellipse(x1, y1, 5, 5)
    ellipse(x2, y2, 5, 5)
    #print parameters to screen
    textSize(14)
    text('(0,0)', x1+10, y1+10)
    text('({},{})'.format(int(x2),int(y2)), x2+10, y2+10)
    text('({},{})'.format(int(x3),int(y3)), x3+10, y3+10)
    text('R1 = {0:.1f}'.format(r1), -300, -300)
    text('R2 = {0:.1f}'.format(r2), -300, -280)
    text('PROP = {}'.format(prop), -300, -260)
    #add points to list
    points = [[x3,y3]] + points[:3000]
    for i,p in enumerate(points):
        if i < len(points)-1:
            stroke(255, 0, 0)
            line(p[0], p[1], points[i+1][0], points[i+1][1])
    t += 0.02
