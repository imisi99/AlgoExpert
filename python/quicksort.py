# Time -> 0(n log(n)) (Worse case -> 0(n^2)) Space -> 0(log(n))
def quickSort(array):
    recursivelySort(array, 0, len(array)-1)
    return array


def recursivelySort(array, start, end):
    if start >= end:
        return
    pivot = start
    left, right = start+1, end
    
    while left <= right:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            array[left], array[right] = array[right], array[left]
            
        if array[left] <= array[pivot]:
            left += 1
            
        if array[right] >= array[pivot]:
            right -= 1
    
    array[pivot], array[right] = array[right], array[pivot]
    
    leftIsSmaller = (right - 1 - start) < (end - right + 1)
    
    if leftIsSmaller:
        recursivelySort(array, start, right-1)
        recursivelySort(array, right+1, end)
    else:
        recursivelySort(array, right+1, end)
        recursivelySort(array, start, right-1)


print(quickSort([8, 5, 2, 9, 5, 6, 3]))
