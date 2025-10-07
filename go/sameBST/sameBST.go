package main

import (
	"fmt"
	"math"
)

// Time -> 0(N^2) Space -> 0(N^2)
func SameBsts(arrayOne, arrayTwo []int) bool{
	if len(arrayOne) != len(arrayTwo){
		return false
	}

	if len(arrayOne) == 0 {return true}
	if arrayOne[0] != arrayTwo[0] {return false}

	leftOne := getSmaller(arrayOne)
	leftTwo := getSmaller(arrayTwo)
	rightOne := getLarger(arrayOne)
	rightTwo := getLarger(arrayTwo)

	return SameBsts(leftOne, leftTwo) && SameBsts(rightOne, rightTwo)
}


func getSmaller(array []int) []int {
	var smaller []int
	root := array[0]
	array = array[1:]
	for i := range array {
		if array[i] < root {smaller = append(smaller, array[i])}
	}
	return smaller
}

func getLarger(array []int) []int {
	var bigger []int
	root := array[0]
	array = array[1:]
	for i := range array {
		if array[i] >= root {bigger = append(bigger, array[i])}
	}

	return bigger
}


// Time -> 0(N^2) Space -> 0(d)
func SameBsts1(arrayOne, arrayTwo []int) bool{
	return IsSameBST(arrayOne, arrayTwo , 0, 0, math.MaxInt, math.MinInt)
}

func IsSameBST(arrayOne, arrayTwo []int, rootOne, rootTwo, max, min int) bool {
	if rootOne == -1 || rootTwo == -1 {return rootOne == rootTwo}
	if arrayOne[rootOne] != arrayTwo[rootTwo] {return false}


	leftIdxOne := getNewRootSmaller(arrayOne, rootOne, min)
	leftIdxTwo := getNewRootSmaller(arrayTwo, rootTwo, min)
	rightIdxOne := getNewRootLarger(arrayOne, rootOne, max)
	rightIdxTwo := getNewRootLarger(arrayTwo, rootTwo, max)

	leftSame := IsSameBST(arrayOne, arrayTwo, leftIdxOne, leftIdxTwo, arrayOne[rootOne], min)
	rightSame := IsSameBST(arrayOne, arrayTwo, rightIdxOne, rightIdxTwo, max, arrayOne[rootOne])

	return leftSame && rightSame
}


func getNewRootSmaller(array []int, root, min int) int {
	for i := root+1; i < len(array); i++{
		if array[i] < array[root] && array[i] >= min {return i}
	}
	return -1
}

func getNewRootLarger(array []int, root, max int) int {
	for i := root+1; i < len(array); i++ {
		if array[i] >= array[root] && array[i] < max {return i}
	}
	return -1
}


func main() {
	one := []int{10, 15, 8, 12, 94, 81, 5, 2, 11}
	two := []int{10, 8, 5, 15, 2, 12, 11, 94, 81}
	fmt.Println(SameBsts(one, two))
	fmt.Println(SameBsts1(one, two))
}
