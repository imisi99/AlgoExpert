package main

import "fmt"


// Time -> 0(N) Space -> 0(1)
func HasSingleCycle(array []int) bool {
	var OriginalSum, NewSum int
	for i := range array {
		OriginalSum += i+1
	}
	
	idx, lastIdx := 0, 0
	for idx < len(array) {
		lastIdx += array[lastIdx]
		if lastIdx < 0 || lastIdx >= len(array) {
			lastIdx = Mod(lastIdx, len(array))
		}
		NewSum += lastIdx+1
		idx++
	}

	if OriginalSum == NewSum {return true}
	return false
}


func Mod(x, y int) int {
	return ((x%y) + y) % y
}

func main() {
	fmt.Println(HasSingleCycle([]int{2, 3, 1, -4, -4, 2}))
}
