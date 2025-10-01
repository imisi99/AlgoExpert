package main

import (
	"fmt"
)


// Time -> 0(N*N!) Space -> 0(N*N!)
func Permutation(array []int) [][]int {
	perms := make([][]int, 0)
	RecursiveFind(0, array, &perms)
	return perms
}


func RecursiveFind(idx int, array []int, perm *[][]int){
	if idx == len(array) - 1 {
		newPerm := make([]int, len(array))
		copy(newPerm, array)
		*(perm) = append(*(perm), newPerm)
	}else {
		for j:=idx; j < len(array); j++ {
			array[idx], array[j] = array[j], array[idx]
			RecursiveFind(idx+1, array, perm)
			array[idx], array[j] = array[j], array[idx]
		}
	}
}


func main() {
	fmt.Println(Permutation([]int{1, 2, 3}))
}