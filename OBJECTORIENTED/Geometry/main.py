from dot2D import Dot2D
from line2D import Line2D

def main():
    p1 = Dot2D(1,2)
    p2 = Dot2D(3,6)
    p3 = Dot2D(2,10)
    ls = Line2D(p1,p2)
    ls.onLine(p3)
    print(ls.midPoint())
    ls.thirdDistance(p3)
    ls.printLine()