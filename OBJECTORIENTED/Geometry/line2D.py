import math
from dot2D import Dot2D

class Line2D:
    def __init__(self,dot1,dot2):
        self.dot1 = dot1
        self.dot2 = dot2
        self.length = self.calcLength()

    def printLine(self):
        print((self.dot1.x,self.dot1.y),(self.dot2.x,self.dot2.y),self.length)

    def editDot(self,newDot1,newDot2):
        self.dot1 = newDot1
        self.dot2 = newDot2
    
    def onLine(self,p):
        self.crossProduct = (p.y-self.dot1.y) * (self.dot2.x-self.dot2.x) - (p.x-self.dot1.x) * (self.dot2.y-self.dot1.y)
        self.dotProduct = (p.x-self.dot1.x) * (self.dot2.x-self.dot1.x) + (p.y-self.dot1.y) * (self.dot2.y-self.dot1.y)
        print(self.crossProduct,self.dotProduct,self.length)
        if abs(self.crossProduct) > 0: return False
        if self.dotProduct < 0: return False
        if self.length < self.dotProduct: return False
        return True
    
    def midPoint(self):
        self.mid  = Dot2D((self.dot1.x+self.dot2.x)/2,(self.dot1.y+self.dot2.y)/2)
        return self.mid.x,self.mid.y

    def thirdDistance(self,p):
        a = abs((p.x-self.dot2.x) * (self.dot2.y-self.dot1.y) - (self.dot2.x-self.dot1.x) * (p.y-self.dot2.y))
        b = math.sqrt((p.x-self.dot2.x)**2 + (p.y-self.dot2.y)**2)
        distance = a/b
        print(distance)
        
    def calcLength(self):
        return math.sqrt((self.dot1.x-self.dot2.x)**2+(self.dot1.y-self.dot2.y)**2)
    