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


# Time -> 0(log(min(n, m))) Space -> 0(1)
def medianOfTwoSortedArrays1(arrayOne, arrayTwo):
    smallArray, bigArray = arrayOne, arrayTwo
    if len(arrayOne) > len(arrayTwo):
        smallArray, bigArray = arrayTwo, arrayOne
    
    left, right = 0, len(smallArray)
    mid = (len(smallArray) + len(bigArray) + 1) // 2
    while True:
        smallIdx = (left + right) //  2
        bigIdx = mid - smallIdx
        
        smallMin = float("inf") if smallIdx >= len(smallArray) else smallArray[smallIdx]
        smallMax = float("-inf") if smallIdx <= 0 else smallArray[smallIdx-1]
        bigMin = float("inf") if bigIdx >= len(bigArray) else bigArray[bigIdx]
        bigMax = float("-inf") if bigIdx <= 0 else bigArray[bigIdx-1]
        
        if smallMax > bigMin:
            right = smallIdx - 1
        elif bigMax > smallMin:
            left = smallIdx + 1
        else:
            if (len(smallArray) + len(bigArray)) % 2 == 0:
                return (max(smallMax, bigMax) + min(smallMin, bigMin)) / 2
            return max(smallMax, bigMax)
        
print(medianOfTwoSortedArrays([5], [6, 7, 8, 9]))
print(medianOfTwoSortedArrays1([5], [6, 7, 8, 9]))
