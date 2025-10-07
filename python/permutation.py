# Time -> 0(N * N!) Space -> 0(N * N!)
def Permutation(array):
    perm = []
    Recursivefind(0, array, perm)
    return perm

def Recursivefind(idx, array, perm):
    if idx == len(array) - 1:
        perm.append(array[:])
    else:
        for j in range(idx, len(array)):
            array[idx], array[j] = array[j], array[idx]
            Recursivefind(idx+1, array, perm)
            array[idx], array[j] = array[j], array[idx]

print(Permutation([1, 2, 3]))