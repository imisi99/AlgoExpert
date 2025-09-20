package main

import "fmt"


// Time -> 0(N) Space -> 0(1)
func IndexEqualValue(array []int) int {
	for i, v := range array {
		if i == v {return i}
	}
	return -1
}


// Time -> 0(log(N)) Space -> 0(1)
func IndexEqualValue1(array []int) int {
	start, end := 0, len(array)-1
	result := -1
	for start <= end {
		mid := (start + end) / 2
		if array[mid] == mid {
			result = mid
			end = mid-1
		}else if mid > array[mid] {
			start = mid+1
		}else {
			end = mid-1
		}
	}

	return result
}

func main() {
	fmt.Println(IndexEqualValue1([]int{0}))
}
