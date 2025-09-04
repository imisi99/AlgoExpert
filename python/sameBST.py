# Time -> 0(N^2) Space -> 0(d)
def sameBsts(arrayOne, arrayTwo):
    return isSame(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))


def isSame(arrayOne, arrayTwo, rootOne, rootTwo, min, max):
    if rootOne == -1 or rootTwo == -1:
        return rootOne == rootTwo
    if arrayOne[rootOne] != arrayTwo[rootTwo]:
        return False
    
    leftOne = getNewSmallRoot(arrayOne, rootOne, min)
    leftTwo = getNewSmallRoot(arrayTwo, rootTwo, min)
    rightOne = getNewLargeRoot(arrayOne, rootOne, max)
    rightTwo = getNewLargeRoot(arrayTwo, rootTwo, max)
    
    root = arrayOne[rootOne]
    leftsame = isSame(arrayOne, arrayTwo, leftOne, leftTwo, min, root)
    rightsame = isSame(arrayOne, arrayTwo, rightOne, rightTwo, root, max)
    return leftsame and rightsame


def getNewSmallRoot(array, rootidx, min):
    for i in range(rootidx+1, len(array)):
        if array[i] < array[rootidx] and array[i] >= min:
            return i
        
    return -1


def getNewLargeRoot(array, rootidx, max):
    for i in range(rootidx+1, len(array)):
        if array[i] >= array[rootidx] and array[i] < max:
            return i
        
    return -1


def sameBsts1(arrayOne, arrayTwo):
    return sameArray(arrayOne, arrayTwo)

def sameArray(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    
    if len(arrayOne) == 0:
        return True
    if arrayOne[0] != arrayTwo[0]:
        return False
    
    leftarrayone = smallerarray(arrayOne)
    leftarraytwo = smallerarray(arrayTwo)
    rightarrayone = largerarray(arrayOne)
    rightarraytwo = largerarray(arrayTwo)
    
    return sameArray(leftarrayone, leftarraytwo) and sameArray(rightarrayone, rightarraytwo)


def smallerarray(array):
    smaller = []
    root = array[0]
    for val in array:
        if val < root:
            smaller.append(val)
            
    return smaller


def largerarray(array):
    larger = []
    root = array[0]
    for val in array[1:]:
        if val >= root:
            larger.append(val)
            
    return larger

print(sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81]))
print(sameBsts1([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81]))
