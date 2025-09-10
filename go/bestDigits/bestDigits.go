package main

import (
	"fmt"
	"strconv"
)


// Time -> 0(N) Space -> 0(N)
func BestDigits(number string, numDigits int) string {
	stack := make([]int64, 0)
	
	for _, digit := range number {
		digitStr := string(digit)
		digitInt, _ := strconv.ParseInt(digitStr, 10, 64)

		if numDigits > 0 {
			for i:=len(stack)-1; i>=0; i-- {
				if numDigits > 0 {
					if digitInt > stack[i] {
						stack = stack[:len(stack)-1]
						numDigits--
					}else {break}
				}else {break}
			}
		}
		
		stack = append(stack, digitInt)
	}

	var result string
	for _, res := range stack {
		result += strconv.FormatInt(res, 10)
	}
	if numDigits > 0 {
		return result[:len(result)-numDigits]
	}
	return result
}


func main() {
	fmt.Println(BestDigits("987564", 2))
}