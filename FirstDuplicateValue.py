# Time: 0(n) Space: 0(n) Worst case 
def firstDuplicateValue(array):
    result = {}
    for val in array:
        if val in result:
            return val
        result[val] = None
    return -1




# Time: 0(n) Space: 0(1)
def firstDuplicateValue(array):
    for val in array:
        idx = abs(val) - 1
        if array[idx] < 0:
            return abs(val)
        array[idx] = -array[idx]
    return -1

test = [2, 1, 5, 2, 3, 3, 4]
test1 = [2, 1, 5, 3, 3, 2, 4]

print(firstDuplicateValue(test))
print(firstDuplicateValue(test1))