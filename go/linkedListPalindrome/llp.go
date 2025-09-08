package main

import "fmt"


type LinkedList struct {
	Value 	int

	Next 	*LinkedList
}


// Time -> 0(N) Space -> 0(1)
func LinkedListPalindrome(head *LinkedList) bool {
	var count int

	curr := head
	for curr != nil {
		count++
		curr = curr.Next
	}
	
	if count == 1 {return true}

	mid := count / 2
	if count % 2 != 0 {mid++}

	curr = head
	for mid > 0 {
		curr = curr.Next
		mid--
	}

	var tail *LinkedList
	for curr != nil {
		p1 := curr.Next
		curr.Next = tail
		tail = curr
		curr = p1
	}

	for tail != nil {
		if tail.Value != head.Value {return false}
		tail = tail.Next
		head = head.Next
	}

	return true
}


func main() {
	array := []int{1, 3, 2, 1, 0}
	head := &LinkedList{Value: 0}
	curr := head
	for _, v := range array {
		curr.Next = &LinkedList{Value: v}
		curr = curr.Next
	}

	fmt.Println(LinkedListPalindrome(head))
}