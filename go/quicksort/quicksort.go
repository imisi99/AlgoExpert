package main

import "fmt"


// Time -> 0(N log(n)) (Worse Case -> 0(N^2)) Space -> 0(log(n))
func QuickSort(array []int) []int {
	RecursivelySort(&array, 0, len(array)-1)
	return array
}


func RecursivelySort(array *[]int, startIdx, endIdx int) {
	if startIdx >= endIdx {return}
	pivot := startIdx
	left, right := startIdx + 1, endIdx
	for left <= right {
		if (*array)[left] > (*array)[pivot] && (*array)[right] < (*array)[pivot] {
			(*array)[left], (*array)[right] = (*array)[right], (*array)[left]
		}
		if (*array)[left] <= (*array)[pivot] {
			left++
		}
		if (*array)[right] >= (*array)[pivot] {
			right--
		}
	}
	(*array)[pivot], (*array)[right] = (*array)[right], (*array)[pivot]

	leftIsSmaller := (right - 1 - startIdx) < (endIdx - right + 1)

	if leftIsSmaller {
		RecursivelySort(array, startIdx, right-1)
		RecursivelySort(array, right+1, endIdx)
	}else {
		RecursivelySort(array, right+1, endIdx)
		RecursivelySort(array, startIdx, right-1)
	}
}

func main() {
	fmt.Println(QuickSort([]int{8, 5, 2, 9, 5, 6, 3}))
}
