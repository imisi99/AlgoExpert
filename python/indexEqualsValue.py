# Time -> 0(log(N)) Space -> 0(1)
def IndexEqualsValue(array):
    start, end = 0, len(array)-1
    result = -1
    
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            result = mid
            end = mid-1
        elif mid > array[mid]:
            start = mid+1
        else:
            end = mid-1
            
    return result


print(IndexEqualsValue([-1, 0, 2]))
