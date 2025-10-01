package main

import "fmt"

type MaxHeap []int 

func NewMaxHeap(array []int) *MaxHeap {
	heap := MaxHeap(array)
	ptr := &heap
	ptr.BuildHeap(array)
	fmt.Println("After Initial Build -> ", heap)
	return ptr
}

func (heap *MaxHeap) BuildHeap(array []int) {
	startIdx := (len(array) - 2) / 2
	for startIdx >= 0 {
		heap.SiftDown(startIdx, len(array)-1)
		startIdx--
	}
}

func (heap *MaxHeap) Bigest(x, y int) int {
	if (*heap)[x] >= (*heap)[y] {
		return x
	}
	return y
}

func (heap *MaxHeap) Remove(window int) {
	endIdx := len(*heap) - window - 1
	(*heap)[0], (*heap)[endIdx] = (*heap)[endIdx], (*heap)[0]
	heap.SiftDown(0, endIdx-1)
}

func (heap *MaxHeap) SiftDown(startIdx, endIdx int) {
	for startIdx < endIdx {
		firstChild, secondChild := (startIdx * 2) + 1, (startIdx * 2) + 2
		if firstChild > endIdx {
			break
		}
		var smallest int
		if secondChild <= endIdx {
			smallest = heap.Bigest(firstChild, secondChild)
		}else {
			smallest = firstChild
		}

		if (*heap)[smallest] > (*heap)[startIdx] {
			(*heap)[smallest], (*heap)[startIdx] = (*heap)[startIdx], (*heap)[smallest]
			startIdx = smallest
		}else {
			break
		}
	}
}


// Time -> 0(N(log(N))) Space -> 0(1)
func HeapSort(array []int) []int {
	heap := NewMaxHeap(array)

	for idx:=0; idx < len(array)-1; idx++ {
		heap.Remove(idx)
	}
	return array
}


func main() {
	fmt.Println(HeapSort([]int{8, 5, 2, 9, 5, 6, 3}))
}