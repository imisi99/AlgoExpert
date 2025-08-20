package main

import "fmt"


type LinkedList struct {
	Value int
	Next *LinkedList
}


// Time -> 0(N) Space -> 0(1)
func RearrangeLinkedList(head *LinkedList, k int) *LinkedList{
	var new_head, less, startGreat, great, startMerge, endMerge *LinkedList 

	curr := head
	for curr != nil {
		if curr.Value < k {
			if less == nil {
				less = curr
				new_head = less
			}else {
				less.Next = curr
				less = less.Next
			}
		}else if curr.Value > k {	
			if great == nil {
				great = curr
				startGreat = great
			}else {
				great.Next = curr
				great = great.Next
			}
		}else {
			if startMerge == nil {
				startMerge = curr
				endMerge = startMerge
			} else {
				endMerge.Next = curr
				endMerge = endMerge.Next
			}
		}

		curr = curr.Next
	}

	if new_head == nil || startMerge == nil || startGreat == nil {
		if new_head == nil {
			if startMerge == nil {
				return startGreat
			}else {
				if startGreat == nil {
					return startMerge
				}else {
					endMerge.Next = startGreat
					great.Next = nil
					return startMerge
				}
			}
		}else {
			if startMerge == nil {
				if startGreat == nil {
					return new_head
				}else {
					less.Next = startGreat
					great.Next = nil
					return new_head
				}
			}else {
				less.Next = startMerge
				endMerge.Next = nil
				return new_head
			}
		}


	}

	less.Next = startMerge
	endMerge.Next = startGreat
	great.Next = nil

	return new_head

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

	rearranged := RearrangeLinkedList(head, 3)
	for rearranged != nil {
		fmt.Printf("%v -> ", rearranged.Value)
		rearranged = rearranged.Next
	}
	fmt.Println()
}