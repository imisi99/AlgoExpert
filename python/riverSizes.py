# Time -> 0(wh) Space -> 0(wh) where w and h is the width and height of the matrix
def riverSizes(matrix):
    visited = set()
    result = []
    col, row = 0, 0
    
    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            if (col, row) in visited:
                continue
            
            if matrix[col][row] == 0:
                visited.add((col, row))
                continue
            
            sum = checkSides(col, row, matrix, visited)
            result.append(sum)
            
    return result


def checkSides(col, row, matrix, visited):
    sum = 0
    if (col, row) in visited:
        return sum
    
    if col < 0 or col >= len(matrix) or row < 0 or row >= len(matrix[0]):
        return sum
    
    visited.add((col, row))
    
    if matrix[col][row] == 1:
        sum += 1
    else:
        return sum
    
    sum += checkSides(col-1, row, matrix, visited)
    sum += checkSides(col+1, row, matrix, visited)
    sum += checkSides(col, row+1, matrix, visited)
    sum += checkSides(col, row-1, matrix, visited)
    
    return sum
    

print(riverSizes([[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]))