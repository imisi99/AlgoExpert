# Time: 0(n log(n)) + 0(m log(m)) space: 0(1)
def smallestDifference(arrayOne, arrayTwo):
    result = [None] * 2
    arrayOne.sort()
    arrayTwo.sort()
    l1 = 0
    l2 = 0
    min = float('inf')
    while l1 < len(arrayOne) and l2 < len(arrayTwo):
        if abs(arrayOne[l1] - arrayTwo[l2]) < min:
            min = abs(arrayOne[l1] - arrayTwo[l2])
            result[0], result[1] = arrayOne[l1], arrayTwo[l2]
        if arrayOne[l1] == arrayTwo[l2]:
            break
        elif arrayOne[l1] < arrayTwo[l2]:
            l1 += 1
        else:
            l2 += 1
    return result


# Time: 0(N^2) Space: 0(1)
def smallestDifference(arrayOne, arrayTwo):
    result = [None] * 2
    val = float('inf')
    for val1 in arrayOne:
        for val2 in arrayTwo:
            if abs(val1 - val2) < val:
                val = abs(val1 - val2)
                result[0], result[1] = val1, val2
    return result

print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
        

