package main

import "fmt"


// Time -> 0(N * M) Space -> 0(C) where N = len of words array , M = longest len of single word
// , and C = number of unique char 
func minimumChars(words []string) []string {
	set := make(map[string]int)
	wordSet := make(map[string]int)
	result := make([]string, 0)

	for _, val := range words {
		wordSet = make(map[string]int)
		for _, char := range val {
			wordSet[string(char)]++
		}
		for k, v := range wordSet {
			if val, exists := set[k]; exists {
				set[k] = max(val, v)
			}else {set[k] = v}
		}
	}
	for k, v := range set {
		for i:=1; i <= v; i++{
			result = append(result, k)
		}
	}
	return result
}

func main() {
	fmt.Println(minimumChars([]string{"this", "that", "did", "deed", "them!", "a"}))
}