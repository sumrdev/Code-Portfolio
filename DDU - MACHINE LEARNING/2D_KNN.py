import math
startBalls = 40
ball = []

def setup():
    size(800,800)
    background(0)
    noStroke()
    for i in range(startBalls):
        if i < 11:
            ball.append(Ball("red",0,0))
        if i > 10:
            ball.append(Ball("blue",0,0))
    
def draw():
    for i in range(len(ball)):
        ball[i].show()
    randomSpawning()
        
def mousePressed():
    ball.append(Ball("Unknown",mouseX,mouseY))
    
def randomSpawning():
    ball.append(Ball("Unknown",random(width),random(height)))

class Ball:
    def __init__(self,id,x,y):
        self.sizeBall = 10
        self.id = id
        if self.id == "red":
            self.x = random(width/2 +self.sizeBall,height-self.sizeBall)
            self.y = random(self.sizeBall,width-self.sizeBall)
            self.col = "#ff0000"
        elif self.id == "blue":
            self.x = random(self.sizeBall,height/2-self.sizeBall)
            self.y = random(self.sizeBall,width-self.sizeBall)
            self.col = "#0000ff"
        elif self.id == "Unknown":
            self.col = "#ffffff"
            self.x = x
            self.y = y
            self.distance()

    def show(self):
        fill(self.col)
        circle(self.x,self.y,self.sizeBall)
    
    def distance(self):
        closest = []
        for i in range(len(ball)):
            closest.append([math.sqrt((self.x-ball[i].x) ** 2 + (self.y-ball[i].y) ** 2), ball[i].id])
        closest.sort()
        self.flipper(closest)
        
    def flipper(self, closest):
        if self.decider(closest) > 0:
            self.id = "red"
            self.col = "#ff0000"
        elif self.decider(closest) < 0:
            self.id = "blue"
            self.col = "#0000ff"
    
    def decider(self,closest):
        k = 7
        d = 0
        for i in range(k):
            if closest[i][1] == "red":
                d += 1
            elif closest[i][1] == "blue":
                d -=1
        return d
                
        