import copy
import random


grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]        
]

def printGrid(p):
    for i in range(4):
        print(p[i])

def addNum(a):
    opt = []
    aGrid = copy.deepcopy(a)
    for i in range(4):
        for j in range(4):
            if aGrid[i][j ] == 0:
                opt.append([i,j])
    spot = random.choice(opt)
    aGrid[spot[0]][spot[1]] = random.choice([2,2,2,2,2,2,2,2,2,4])
    return aGrid

def calc(dir, c):
    check = copy.deepcopy(c)
    cGrid = copy.deepcopy(c)
    if dir == "s":
        cGrid = rotate(cGrid)
    if dir == "w":
        for i in range(3):
            cGrid = rotate(cGrid)
    if dir == "d":
        for i in range(4):
            cGrid[i].reverse()
    for i in range(4):
        o = True
        newLine = []
        for j in range(4):
            if cGrid[i][j] == 0:
                continue
            if not o and cGrid[i][j] == newLine[-1]:
                o = True
                newLine[-1]*=2
            else:
                o = False
                newLine.append(cGrid[i][j])
        newLine += [0]*(4-len(newLine))
        cGrid[i] = newLine
    if dir == "d":
        for i in range(4):
            cGrid[i].reverse()
    if dir == "s":
        for i in range(3):
            cGrid = rotate(cGrid)
    if dir == "w":
        cGrid = rotate(cGrid)
    if not equals(check,cGrid):
        cGrid = addNum(cGrid)
    return cGrid           

def equals(a, b):
    for i in range(4):
        for j in range(4):
            if a[i][j] != b[i][j]:
                return False
    return True

def rotate(r):
    rGrid = copy.deepcopy(r)
    rCopy = copy.deepcopy(r)
    for i in range(4):
        for j in range(4):
            rGrid[i][j] = rCopy[j][i]
    for i in range(4):
        rGrid[i].reverse()
    return rGrid

def inputs():
    global grid
    inp = input("Type direction: ")
    grid = calc(inp,grid)
    printGrid(grid)

grid = addNum(grid)
grid = addNum(grid)
while True:
    inputs()