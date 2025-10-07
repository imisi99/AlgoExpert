package main

import (
	"fmt"
)

func LongestPanlindrome(str string) string {
	var longest [2]int
	for i := range str {
		odd := CheckPalindrome(str, i-1, i+1)
		even := CheckPalindrome(str, i-1, i)

		currLongest := Max(odd, even)
		currLongest = Max(currLongest, longest)
		longest = currLongest
	}

	return str[longest[0]:longest[1]+1]
}


func CheckPalindrome(str string, i, j int) [2]int {
	for i >= 0 && j < len(str) && str[i] == str[j] {
		i--
		j++
	}
	return [2]int{i+1, j-1}
}


func Max(x, y [2]int) [2]int {
	if x[1]-x[0] > y[1]-y[0] {return x}
	return y
}

func main() {
	fmt.Println(LongestPanlindrome("abaxyxxyxbfzzzzzzzzzz"))
	
}