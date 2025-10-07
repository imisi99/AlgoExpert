# Time -> 0(N^2) Space -> 0(1)
def countInversions(array):
    num = 0 
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                continue
            if i < j and array[i] > array[j]:
                num += 1
    
    return num

print(countInversions([3, 4, 1, 2]))
print(countInversions([2, 3, 3, 1, 9, 5, 6]))


# Time -> 0(Nlog(N)) Space -> 0(N) 
def countInversions1(array):
    if len(array) == 0:
        return 0
    aux, cparray = array[:], array[:]   # Not modifying the original array
    num = mergesortCount(cparray, aux, 0, len(array)-1)
    return num

def mergesortCount(array, aux, start, end):
    if start == end:
        return 0

    mid = (start + end) // 2
    leftCount = mergesortCount(aux, array, start, mid)
    rightCount = mergesortCount(aux, array, mid+1, end)
    return leftCount + rightCount + mergeCount(array, aux, start, mid, end)

def mergeCount(array, aux, start, mid, end):
    num = 0
    i, j, k = start, mid+1, start
    while i <= mid and j <= end:
        if aux[i] <= aux[j]:
            array[k] = aux[i]
            i += 1
            k += 1
        else:
            array[k] = aux[j]
            j += 1
            k += 1
            num += mid - i + 1

    while i <= mid:
        array[k] = aux[i]
        i += 1
        k += 1

    while j <= end:
        array[k] = aux[j]
        j += 1
        k += 1
    return num

print(countInversions1([2, 3, 3, 1, 9, 5, 6]))

