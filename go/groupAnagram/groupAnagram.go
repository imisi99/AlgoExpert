package main

import (
	"fmt"
	"sort"
)

// Time -> 0(N*N*M) Space -> 0(N*W) where N = number of words and M = longest word
func groupAnagram(words []string) [][]string {
	set := make(map[string]int)
	wordSet := make(map[string]int)
	wordsSet := make(map[string]bool)
	initStore := make([]string, 0)
	result := make([][]string, 0)


	for _, val := range words {wordsSet[val] = false}

	for _, word := range words {
		if seen, _ := wordsSet[word]; seen {continue}
		initStore = make([]string, 0)
		set = make(map[string]int)
		set = getMaps(set, word)
		initStore = append(initStore, word)
		for _, newWord := range words {
			wordSet = make(map[string]int)
			if seen, _ := wordsSet[word]; seen || newWord == word{continue}
			if len(word) != len(newWord) {continue}
			wordSet = getMaps(wordSet, newWord)
			if checkAnagram(set, wordSet) {
				initStore = append(initStore, newWord)
				wordsSet[newWord] = true
			}
		}
		result = append(result, initStore)
		wordsSet[word] = true
	}
	return result
}

func getMaps(set map[string]int, word string) map[string]int {
	for _, v := range word {
		set[string(v)]++
	}
	return set
}

func checkAnagram(firstSet, secondSet map[string]int) bool{
    if len(firstSet) != len(secondSet) {return false}
	for k, v := range firstSet {
		if val, exists := secondSet[k]; !exists || val != v {return false}
	}
	return true
}


// Time -> 0(N*M log(M)) Space -> 0(MN)
func groupAnagram1(words []string) [][]string {
	set := make(map[string][]string)
	result := make([][]string, 0)

	for i := range words {
		word := sortWords(words[i])
		if val, exists := set[word]; exists {
			val = append(val, words[i])
			set[word] = val
		}else {set[word] = []string{words[i]}}
	}

	for _, v := range set {result = append(result, v)}
	return result
}


func sortWords(word string) string {
	wordbyte := []byte(word)
	sort.Slice(wordbyte, func(i, j int) bool {
		return wordbyte[i] < wordbyte[j]
	})
	return string(wordbyte)
}


func main() {
	fmt.Println(groupAnagram([]string{"yo", "bro", "oy", "wrong", "cat","tac", "act"}))
	fmt.Println(groupAnagram1([]string{"yo", "bro", "oy", "wrong", "cat","tac", "act"}))
}
