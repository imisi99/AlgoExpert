# Time -> 0(d*(b+n)) Space -> 0(b+n) where d is the max num of digit and b is the base of the nums(base 10)
def radixsort(array):
    maxDig = max(array)
    digit, maxDig = 0, len(str(maxDig))
    while digit < maxDig:
        countsort(array, digit)
        digit += 1
        
    return array

def countsort(array, digit):
    count = [0] * 10
    newArray = [0] * len(array)
    digitCol = 10 ** digit
    
    for num in array:
        idx = (num // digitCol) % 10
        count[idx] += 1
        
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    for i in reversed(range(len(array))):
        countIdx = (array[i] // digitCol) % 10
        count[countIdx] -= 1
        newArray[count[countIdx]] = array[i]
        
    array[:] = newArray
    
    
print(radixsort([234, 12, 90, 5, 7, 22, 52, 202, 75]))
