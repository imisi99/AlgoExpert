# Time: 0(N^2) Space: 0(N)
def nextGreaterElement(array):
    next_ge = [None] * len(array)
    for i in range(len(array)):
        val = array[i]
        j = i + 1
        if j == len(array):
            j = 0
        while j < len(array):
            val1 = array[j]
            if val1 > val:
                next_ge[i] = val1
                break
            j  += 1
            if j == len(array):
                j = 0
            if j == i:
                break
                            
    for i in range(len(next_ge)):
        if next_ge[i] is None:
            next_ge[i] = -1    
    return next_ge

print(nextGreaterElement([2, 5, -3, -4, 6, 7, 2]))