# Time: 0(N) space: 0(1)
def moveElementToEnd(array, toMove):
    l = 0
    r = len(array) - 1
    while l <= r:
        while array[r] == toMove:
            if r == 0:
                return array
            r -= 1
        if l > r:
            break
        if array[l] == toMove:
            array[l], array[r] = array[r], array[l]
            r -= 1
        l += 1
        
    return array


test = [2, 3, 3, 3, 3, 3, 3, 2, 3, 5, 6, 6, 2]
test1 = [2, 1, 2, 2, 2, 3, 4, 2]

print(moveElementToEnd(test, 2))
print(moveElementToEnd(test1, 3))
