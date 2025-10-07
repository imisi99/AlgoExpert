# Time -> 0(Nlog(N)) Space -> 0(N)
def mergesort(array):
    aux = array[:]
    RecursiveSort(array, aux, 0, len(array)-1)
    return array


def RecursiveSort(array, aux, start, end):
    if start == end:
        return

    mid = (start + end) // 2
    RecursiveSort(aux, array, start, mid)
    RecursiveSort(aux, array, mid+1, end)
    Merge(array, aux, start, mid, end)


def Merge(array, aux, start, mid, end):
    i, j, k = start, mid+1, start

    while i <= mid and j <= end:
        if aux[i] <= aux[j]:
            array[k] = aux[i]
            i += 1
        else:
            array[k] = aux[j]
            j += 1
        k += 1 

    while i <= mid:
        array[k] = aux[i]
        i += 1
        k += 1

    while j <= end:
        array[k] = aux[j]
        j += 1
        k += 1


print(mergesort([3, 4, 5, 1, 2, 3, 8, 92, 75, 12]))
