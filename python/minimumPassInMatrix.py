def minimumPassesOfMatrix(matrix):
    positives = set()
    
    for col in range(len(matrix)):
        for row in range(len(matrix[0])):
            if matrix[col][row] > 0:
                positives.add((col, row))
                
    passes = 0
    while len(positives) > 0 :
        nextPositives = set()
        
        for val in positives:
            col, row = val
            nextPositives = checkSides(col, row, nextPositives, matrix)
            
        positives = nextPositives
        if len(positives) > 0:
            passes += 1
            
    for col in range(len(matrix)):
        for row in range(len(matrix[0])):
            if matrix[col][row] < 0:
                return -1
            
    return passes




def checkSides(col, row, positives, matrix):
    if col - 1 >= 0:
        if matrix[col-1][row] < 0:
            matrix[col-1][row] *= -1
            positives.add((col-1, row))
            
    if col + 1 < len(matrix):
        if matrix[col+1][row] < 0:
            matrix[col+1][row] *= -1
            positives.add((col+1, row))
            
    if row - 1 >= 0:
        if matrix[col][row-1] < 0:
            matrix[col][row-1] *= -1
            positives.add((col, row-1))
            
    if row + 1 < len(matrix[0]):
        if matrix[col][row+1] < 0:
            matrix[col][row+1] *= -1
            positives.add((col, row+1))
            
    return positives


print(minimumPassesOfMatrix([[0, -2, -1], [-5, 2, 0], [-6, -2, 0]]))