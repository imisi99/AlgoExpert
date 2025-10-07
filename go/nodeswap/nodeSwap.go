package main

import "fmt"

type LinkedList struct {
	Value int
	Next *LinkedList
}


// Time -> 0(N) Space -> 0(1)
func NodeSwap(head *LinkedList) *LinkedList {
	loop := head

	for loop != nil {
		if loop.Next == nil {break}
		loop.Value, loop.Next.Value = loop.Next.Value, loop.Value
		loop = loop.Next.Next
	}

	return head
}

func main() {

	list := []int{7, 8, 9, 10, 0}
	head := &LinkedList{}
	curr := head
	for i, val := range list {
		curr.Value = val
		if i == len(list) - 1 {continue}
		curr.Next = &LinkedList{}
		curr = curr.Next
	}

	rearranged := NodeSwap(head)
	for rearranged != nil {
		fmt.Printf("%v -> ", rearranged.Value)
		rearranged = rearranged.Next
	}
	fmt.Println()
}
