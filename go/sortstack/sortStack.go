package main

import (
	"fmt"
	"math"
)

// Time -> 0(N^2) Space -> 0(N)
func SortStack(stack []int) []int {
	result := make([]int, 0)
	lenStack := len(stack)

	for range lenStack {
		subStack := stack
		min := math.MaxInt
		for range len(subStack) {
			last := subStack[len(subStack)-1]
			subStack = subStack[:len(subStack)-1]
			if last < min {min = last}
		}
		result = append(result, min)
		stack = RemoveVal(stack, min)
	}

	return result
}

func RemoveVal(stack []int, val int) []int {
	newStack, lenStack := make([]int, 0), len(stack)
	for range lenStack {
		last := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if last == val {break}
		newStack = append(newStack, last)
	}
	newStack = append(newStack, stack...)
	return newStack
}


// Time -> 0(N^2) Space -> 0(N) 		Recursive in place solution 
func SortStackInPlace(stack []int) []int {
	SortStackRecursively(&stack)
	return stack
}

func SortStackRecursively(stack *[]int) {
	if len(*stack) == 0 {return}

	top := (*stack)[len(*stack)-1]
	(*stack) = (*stack)[:len(*stack)-1]
	SortStackRecursively(stack)
	Insert(stack, top)
}

func Insert(stack *[]int, val int) {
	if len(*stack) == 0 {
		(*stack) = append((*stack), val)
		return
	}
	top := (*stack)[len(*stack)-1]
	if val < top {
		(*stack) = (*stack)[:len(*stack)-1]
		Insert(stack, val)
		(*stack) = append((*stack), top)
	}else {
		(*stack) = append((*stack), val)
		return
	}
}


func main() {
	array := []int{4, 4, 4, 1}
	fmt.Println(SortStack(array))
	fmt.Println(SortStackInPlace(array))
}
