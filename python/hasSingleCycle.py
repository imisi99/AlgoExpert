# Time -> 0(N) Space -> 0(1)
def hasSingleCycle(array):
    originalSum, newSum = 0, 0
    for i in range(len(array)):
        originalSum += i+1
        
    lastIdx = 0
    for i in range(len(array)):
        lastIdx += array[lastIdx]
        if lastIdx < 0 or lastIdx >= len(array):
            lastIdx = lastIdx % len(array)
        newSum += lastIdx+1
        
    if originalSum == newSum:
        return True
    return False
        


print(hasSingleCycle([2, 3, 1, -4, -4, 2]))