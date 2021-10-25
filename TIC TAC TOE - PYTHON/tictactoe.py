import copy

grid = [
    "X  ",
    " X ",
    "  X"
]

currentPlayer = 0

def printGrid(pGrid):
    print("   A  B  C")
    for i in range(3): print(str(i+1) + " [" + pGrid[i][0] + "][" + pGrid[i][1] + "][" + pGrid[i][2] +"]")

def convertInput(plin,g):
    iGrid = copy.deepcopy(g)
    if plin[0] == "a"or plin[0]=="b" or plin[0] == "c":
        
        
    
    




def inputs():
    playerInput = input("Type a Coordinate (row then column) \n")
    global grid
    grid = convertInput(playerInput, grid)


printGrid(grid)