package main

import (
	"fmt"
	"math"
	"strconv"
)


// Time -> 0(d * (b+n)) Space -> 0(b+n) where d is the max len of digit and b is the base of the nums(base 10)
func RadixSort(array []int) []int {
	digit, maxDigit := 0, Max(array)
	for digit < maxDigit {
		CountSort(array, digit)
		digit++
	}
	return array
}

func CountSort(array []int, digit int) {
	count := make([]int, 10)
	newarray := make([]int, len(array))
	digitCol := int(math.Pow(10, float64(digit)))
	
	for _, v := range array {
		idx := (v / digitCol) % 10
		count[idx] += 1
	}

	for idx:=1; idx<len(count); idx++ {
		count[idx] += count[idx-1]
	}

	for idx:=len(array)-1; idx>=0; idx-- {
		countIdx := (array[idx] / digitCol) % 10
		count[countIdx] -= 1
		newarray[count[countIdx]] = array[idx]
	}
	copy(array, newarray)
}

func Max(array []int) int {
	max := math.MinInt
	for _, v := range array {
		if v > max{max = v}
	}
	return len(strconv.Itoa(max))
}

func main() {
	fmt.Println(RadixSort([]int{234, 12, 90, 5, 7, 22, 52, 202, 75}))
}
