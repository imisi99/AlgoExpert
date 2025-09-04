package main


import "fmt"


// Time -> 0(N) Space -> 0(1)
func MaxSubsetSumNoAdjacent(array []int) int {
	var first, second int

	if len(array) == 0 {return 0}
	if len(array) == 1 {return array[0]}

	first, second = array[0], max(array[0], array[1])

	for i:=2; i < len(array); i++{
		fmt.Println(first, second)
		curr := max(first + array[i], second)
		first = second
		second = curr
	}

	return second
}


func main() {
	fmt.Println(MaxSubsetSumNoAdjacent([]int{75, 105, 120, 75, 90, 135}))
}