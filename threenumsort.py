# Time: 0(n) space: 0(1)
def threeNumberSort(array, order):
    idx = 0
    for val in order:
        for i in range(len(array)):
            if val == array[i]:
                array[i], array[idx] = array[idx], array[i]
                idx += 1
    return array
                
                
             
test = [1, 0, 0, -1, -1, 0, 1, 1]
test_order = [0, 1, -1]       
print(threeNumberSort(test, test_order))