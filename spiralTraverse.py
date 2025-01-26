def spiralTraverse(array):
    result = []
    top = 0
    left = 0
    bottom = len(array) - 1
    right = len(array[0]) - 1

    while top <= bottom and left <= right:
        # top
        for i in range(left, right + 1):
            result.append(array[top][i])

        # right
        for i in range(top + 1, bottom + 1):
            result.append(array[i][right])

        # bottom
        if top < bottom:
            for i in reversed(range(left, right)):
                result.append(array[bottom][i])

        # left
        if left < right:
            for i in reversed(range(top + 1, bottom)):
                result.append(array[i][left])

        top += 1
        left += 1
        bottom -= 1
        right -= 1

    return result

test1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

test2 = [[1, 2, 3, 4, 5],
         [10, 83, 93, 5, 6],
         [7, 8, 9, 23, 32]]
print(spiralTraverse(test2))