package main

import (
	"fmt"
	"strconv"
)


// Time -> 0(N) Space -> 0(N)
func reversePolishNotation(array []string) int {
	ops := map[string]func(int, int) int{
		"+": func(x, y int) int {return x + y},
		"-": func(x, y int) int {return x - y},
		"/": func(x, y int) int {return x / y},
		"*": func(x, y int) int {return x * y},
	}

	stack := make([]int, 0)

	for _, char := range array{
		if _, exists := ops[char]; exists {
			firstVal := stack[len(stack)-2]
			secondVal := stack[len(stack)-1]
			stack = stack[:len(stack)-2]
			result := ops[char](firstVal, secondVal)

			stack = append(stack, result)
		}else {
			val, _ := strconv.Atoi(char)
			stack = append(stack, val)
		}
	}
	return stack[0]
}


func main() {
	fmt.Println(reversePolishNotation([]string{"4", "3", "2", "*", "+"}))
}