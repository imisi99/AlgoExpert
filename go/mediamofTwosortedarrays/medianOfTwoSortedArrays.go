package main

import (
	"fmt"
	"math"
)

// Time -> 0(N+M) Space -> 0(1)
func MedianOfTwoSortedArrays(arrayOne []int, arrayTwo []int) float64 {
	var counterOne, counterTwo, prev, curr int 
	mid := (len(arrayOne) + len(arrayTwo)) / 2
	for mid >= 0 && counterOne < len(arrayOne) && counterTwo < len(arrayTwo) {
		if arrayOne[counterOne] <= arrayTwo[counterTwo] {
			prev = curr
			curr = arrayOne[counterOne]
			counterOne++
			mid--
		}else {
			prev = curr
			curr = arrayTwo[counterTwo]
			counterTwo++
			mid--
		}
	}
	if mid >= 0 {
		if counterOne == len(arrayOne) {
			for mid >= 0 {
				prev = curr
				curr = arrayTwo[counterTwo]
				counterTwo++
				mid--
			}
		}else {
			for mid >= 0 {
				prev = curr
				curr = arrayOne[counterOne]
				counterOne++
				mid--
			}
		}
	}

	if (len(arrayOne) + len(arrayTwo)) % 2 == 0 {
		return float64(prev + curr) /2
	}
	return float64(curr)
}


// Time -> 0(log(min(m, n))) Space -> 0(1)
func MedianOfTwoSortedArrays1(arrayOne []int, arrayTwo []int) float64 {
	var bigArray, smallArray []int
	if len(arrayOne) > len(arrayTwo) {
		bigArray, smallArray = arrayOne, arrayTwo
	}else {
		bigArray, smallArray = arrayTwo, arrayOne
	}
		
	leftIdx, rightIdx := 0, len(smallArray)
	mid := (len(smallArray) + len(bigArray) + 1) / 2

	for {
		smallPartIdx := (leftIdx + rightIdx) / 2
		bigPartIdx := mid - smallPartIdx

		smallMaxVal, smallMinVal := math.MinInt, math.MaxInt
		if smallPartIdx > 0 {
			smallMaxVal = smallArray[smallPartIdx-1]
		}
		if smallPartIdx < len(smallArray) {
			smallMinVal = smallArray[smallPartIdx]
		}
		bigMaxVal, bigMinVal := math.MinInt, math.MaxInt
		if bigPartIdx > 0 {
			bigMaxVal = bigArray[bigPartIdx-1]
		}
		if bigPartIdx < len(bigArray) {
			bigMinVal = bigArray[bigPartIdx]
		}

		if smallMaxVal > bigMinVal {
			rightIdx = smallPartIdx - 1
		}else if bigMaxVal > smallMinVal {
			leftIdx = smallPartIdx + 1
		}else {
			if (len(smallArray) + len (bigArray)) % 2 == 0 {
				return float64((max(smallMaxVal, bigMaxVal) + min(smallMinVal, bigMinVal))) / 2
			}
			return float64(max(smallMaxVal, bigMaxVal))
		}
	}
}

func main() { 
	fmt.Println(MedianOfTwoSortedArrays([]int{5}, []int{2, 3, 6, 7, 8, 9, 10, 12, 14, 18, 20}))
	fmt.Println(MedianOfTwoSortedArrays1([]int{5}, []int{2, 3, 6, 7, 8, 9, 10, 12, 14, 18, 20}))
}

