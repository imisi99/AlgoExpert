# Time -> 0(N) Space -> 0(1)
def maxSubsetSumNoAdjacent(array):
    first, second = 0, 0
    
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]
    
    first, second = array[0], max(array[0], array[1])
    
    for i in range(2, len(array)):
        curr = max(first + array[i], second)
        first = second
        second = curr
    
    return second


print(maxSubsetSumNoAdjacent([120, 70, 26, 374, 2938]))