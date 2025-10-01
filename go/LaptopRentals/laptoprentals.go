package main

import (
	"sort"
	"fmt"
)

type MinHeap []int 

func NewMinHeap(array []int) *MinHeap {
	heap := MinHeap(array)
	return &heap
}

func (heap *MinHeap) SiftDown(startIdx, endIdx int) {
	for startIdx < endIdx {
		firstChild, secondChild := (startIdx * 2) + 1, (startIdx * 2) + 2
		if firstChild > endIdx {break}
		var smallest int
		if secondChild <= endIdx {
			smallest = heap.Min(firstChild, secondChild)
		}else{
			smallest = firstChild
		}

		if (*heap)[smallest] < (*heap)[startIdx] {
			(*heap)[smallest], (*heap)[startIdx] = (*heap)[startIdx], (*heap)[smallest]
			startIdx = smallest
		}else {
			break
		}
	}
}

func (heap *MinHeap) SiftUp() {
	lastIdx := len(*heap) - 1
	for lastIdx >= 1 {
		parent := (lastIdx - 1) / 2
		if (*heap)[lastIdx] < (*heap)[parent] {
			(*heap)[parent], (*heap)[lastIdx] = (*heap)[lastIdx], (*heap)[parent]
			lastIdx = parent
		}else {
			break
		}
	}
}

func (heap *MinHeap) Peek() int {
	return (*heap)[0]
}

func (heap *MinHeap) Remove() {
	(*heap)[0], (*heap)[len(*heap)-1] = (*heap)[len(*heap)-1], (*heap)[0]
	(*heap) = (*heap)[:len(*heap)-1]
	heap.SiftDown(0, len(*heap)-1)
}

func (heap *MinHeap) Insert(val int) {
	(*heap) = append((*heap), val)
	heap.SiftUp()
}

func (heap *MinHeap) Min(x, y int) int {
	if (*heap)[x] <= (*heap)[y] {
		return x
	}
	return y
}


// Time -> 0(N log(N)) Space -> 0(N)
func LaptopRentals(times [][]int) int {

	sort.Slice(times, func(i, j int) bool {
		if times[i][0] == times[j][0] {
			return times[i][1] < times[j][1]
		}
		return times[i][0] < times[j][0]
	})


	var num int
	freeTimes := make([]int, 0)
	timeHeap := NewMinHeap(freeTimes)
	for i := range times {
		if len(*timeHeap) == 0 {
			timeHeap.Insert(times[i][1])
			num++
			continue
		}

		if times[i][0] >= timeHeap.Peek() {
			timeHeap.Remove()
			timeHeap.Insert(times[i][1])
		}else {
			num++
			timeHeap.Insert(times[i][1])
		}
	}
	return num
}

func main() {
	fmt.Println(LaptopRentals([][]int{{1, 4}, {0, 4}, {0, 2}, {4, 6}, {7, 8}, {3, 10}, {9, 11},}))
}
