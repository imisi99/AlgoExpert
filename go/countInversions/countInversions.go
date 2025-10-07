package main

import "fmt"


// Time -> 0(N^2) Space -> 0(1)
func CountInversions(array []int) int {
	var num int

	for i := range array {
		for j := range array {
			if i == j {continue}
			if i < j && array[i] > array[j] {
				num++
			}
		}
	}

	return num
}


// Time -> 0(Nlog(N)) Space -> 0(N)
func CountInversions1(array []int) int {
	var num int
	if len(array) == 0 {
		return num
	}

	MergeSort(array, &num)
	return num
}

func MergeSort(array []int, num *int) {
	aux := make([]int, len(array))
	cparray := make([]int, len(array))
	copy(aux, array)
	copy(cparray, array)    // Avoiding modifying the input array
	RecursiveSort(cparray, aux, 0, len(array)-1, num)
}


func RecursiveSort(array, aux []int, start, end int, num *int) {
	if start == end {
		return
	}

	mid := (start + end) / 2
	RecursiveSort(aux, array, start, mid, num)
	RecursiveSort(aux, array, mid+1, end, num)
	Merge(array, aux, start, mid, end, num)
}

func Merge(array, aux []int, start, mid, end int, num *int) {
	i, j, k := start, mid+1, start

	for i <= mid && j <= end {
		if aux[i] <= aux[j] {
			array[k] = aux[i]
			i++
		}else {
			array[k] = aux[j]
			j++
			(*num) += mid - i + 1
		}
		k++
	}

	for i <= mid {
		array[k] = aux[i]
		k++
		i++
	}

	for j <= end {
		array[k] = aux[j]
		k++
		j++
	}
}

func main() {
	fmt.Println(CountInversions1([]int{2, 3, 3, 1, 9, 5, 6}))
}

