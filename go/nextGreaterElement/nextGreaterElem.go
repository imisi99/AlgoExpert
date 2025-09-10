package main 

import "fmt"


// Time -> 0(N) Space -> 0(N)
func NextGreaterElement(array []int) []int {
	stack := make([]int, 0)
	result := make([]int, len(array))
	for i := range result {result[i] = -1}
	
	for i:=0; i < len(array)*2; i++{
		i := i % len(array)
		for len(stack) > 0 && array[i] > array[stack[len(stack)-1]] {
			result[stack[len(stack)-1]] = array[i]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)
	}
	return result
}


func main() {
	fmt.Println(NextGreaterElement([]int{2, 5, -3, -4, 6, 7, 2}))
}