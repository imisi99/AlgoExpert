package main 

import (
	"fmt"
)

// Time -> 0(Nlog(N)) Space -> 0(N) 
func MergeSort(array []int) []int {
	aux := make([]int, len(array))
	copy(aux, array)
	RecursivelySort(array, aux, 0, len(array)-1)
	return array
}


func RecursivelySort(array, aux []int, start, end int) {
	if end == start {
		return
	}

	mid := (start + end) / 2
	RecursivelySort(aux, array, start, mid)
	RecursivelySort(aux, array, mid+1, end)
	Merge(array, aux, start, mid, end)
}


func Merge(array, aux []int, start, mid, end int) {
	i, k, j := start, start, mid+1

	for i <= mid && j <= end {
		if aux[i] <= aux[j] {
			array[k] = aux[i]
			i++
		}else {
			array[k] = aux[j]
			j++
		}
		k++
	}

	for i <= mid {
		array[k] = aux[i]
		i++
		k++
	}

	for j <= end {
		array[k] = aux[j]
		j++
		k++
	}
}


func main() {
	fmt.Println(MergeSort([]int{23, 43, 1, 2, 3, 45, 90, 234, 76}))
}

