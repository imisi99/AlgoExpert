# Time: 0(N^2) Space: 0(1)
def countInversions(array):
    count = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                continue
            if i < j and array[i] > array[j]:
                count += 1
    
    return count

print(countInversions([2, 3, 3, 1, 9, 5, 6]))

def countInversions(array):
    count = 0