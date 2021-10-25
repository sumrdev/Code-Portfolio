import copy

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def rotate():
    global matrix
    m = copy.deepcopy(matrix)
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            matrix[i][j] = m[j][i]
        for i in range(len(matrix[0])):
            matrix[i].reverse()
    print(matrix)

rotate()