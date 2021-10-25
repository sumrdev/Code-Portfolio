import math
class Dot2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def printDot(self):
        print(self.x,self.y)

    def origo(self):
        return math.sqrt(self.x**2+self.y**2)