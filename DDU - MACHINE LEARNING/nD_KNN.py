import math
import random

point = []
def addDataPoint(dimensions,group):
    point.append(Datapoint(dimensions,group))




class Datapoint:
    def __init__(self,dimensions,group):
        self.location = []; for i in range(dimensions): self.location.append(random.randint(0,100))
        self.group = random.randint(group)


addDataPoint(4,5)