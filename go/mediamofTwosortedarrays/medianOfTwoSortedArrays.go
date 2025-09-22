package main

import "fmt"


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


func main() {
	fmt.Println(MedianOfTwoSortedArrays([]int{5}, []int{2, 3, 6, 7, 8, 9, 10, 12, 14, 18, 20}))
}
