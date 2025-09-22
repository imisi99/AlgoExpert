# Time -> 0(N+M) Space -> 0(1)
def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    counterOne, counterTwo, prev, curr = 0, 0, 0, 0
    mid = (len(arrayOne) + len(arrayTwo)) // 2
    while mid >= 0 and counterOne < len(arrayOne) and counterTwo < len(arrayTwo):
        if arrayOne[counterOne] <= arrayTwo[counterTwo]:
            prev, curr = curr, arrayOne[counterOne]
            counterOne += 1
            mid -= 1
        else:
            prev, curr = curr, arrayTwo[counterTwo]
            counterTwo += 1
            mid -= 1
                
    if mid >= 0:
        if counterOne == len(arrayOne):
            while mid >= 0:
                prev, curr = curr, arrayTwo[counterTwo]
                counterTwo += 1
                mid -= 1
                
        else:
            while mid >= 0:
                prev, curr = curr, arrayOne[counterOne]
                counterOne += 1
                mid -= 1
    
    if (len(arrayOne) + len(arrayTwo)) %  2 == 0:
        return (prev + curr) / 2 
    return curr


print(medianOfTwoSortedArrays([5], [6, 7, 8, 9]))