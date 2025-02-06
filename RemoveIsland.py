def removeIslands(matrix):
    n = len(matrix)
    for i in range(n):
        end = len(matrix[i])
        for j in range(len(matrix[i])):
            is_row = i == 0 or i == n - 1
            is_col = j == 0 or j == end -1
            is_border = is_row or is_col
            
            if not is_border:
                continue
            
            if matrix[i][j] != 1:
                continue
            
            depthfirstsearch(i, j, matrix)
    
    for i in range(n):
        for j in range(len(matrix[i])):
            value = matrix[i][j]
            if value == 2:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
                
                
                
    return matrix
        

def depthfirstsearch(i, j, array):
    stack = [(i, j)]
    while len(stack) > 0:
        row, col = stack.pop()
        
        if array[row][col] != 1:
            continue
        array[row][col] = 2
        
        if row -1 >= 0:
            stack.append((row-1, col))
        if row + 1 < len(array):
            stack.append((row+1, col))
        if col -1 >= 0:
            stack.append((row, col-1))
        if col + 1 < len(array[row]):
            stack.append((row, col+1))
        
        
test = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
  ]

val = removeIslands(test)

for val in val:
    print(val)