package main

import (
	"fmt"
	"strings"
)


// Time -> 0(N) Space -> 0(N)
func ReverseStringInString(word string) string{
	reversedWords := make([]string, 0)
	end := len(word) - 1

	for i:=len(word)-1; i >= 0; i-- {
		if i == 0 {
			reversedWords = append(reversedWords, word[i:end+1])
			break
		}
		if string(word[i]) == " " {
			if end > i {reversedWords = append(reversedWords, word[i+1:end+1])}
			reversedWords = append(reversedWords, " ")
			end = i-1
		}
	}

	return strings.Join(reversedWords, "")
}


func main() {
	fmt.Println(ReverseStringInString("Algoexpert is the best! 😊"))
}
