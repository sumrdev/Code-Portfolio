class Circle:
    def __init__(self, x, y ,r):
        self.x = x
        self.y = y
        self.r = r

    def printCircle(self):
        print((self.x, self.y), "Radius: ", self.r)

c = Circle(20,10,3)
c.printCircle()