package main

import "fmt"

type LinkedList struct {
	Value int
	Next *LinkedList
}


func ZipLinkedList(head *LinkedList) *LinkedList {
	var count int
	curr := head

	for curr != nil {
		count++
		curr = curr.Next
	}

	if count == 1 {
		return head
	}

	var startNorm, endNorm *LinkedList 
	var mid int

	if count % 2 == 0 {
		mid = count / 2
	}else {
		mid = (count / 2) + 1
	}

	for mid > 0 {
		if startNorm == nil {
			startNorm = head
			endNorm = startNorm
			mid--
		}else {
			endNorm = endNorm.Next
			mid--
		}
	}

	var startZip, endZip *LinkedList = nil, endNorm.Next

	for endZip != nil {
		point := endZip.Next
		endZip.Next = startZip
		startZip = endZip
		endZip = point
	}
	endNorm.Next = nil

	var zippedList, zippedHead *LinkedList

	for startNorm != nil {
		if zippedList ==  nil {
		zippedList = startNorm
		zippedHead = zippedList
		startNorm = startNorm.Next
		zippedList.Next = startZip
		startZip = startZip.Next
		zippedList = zippedList.Next
	}else {
		zippedList.Next = startNorm
		startNorm = startNorm.Next
		zippedList = zippedList.Next
		if startZip == nil {
			zippedList.Next = startNorm
			break
		}
		zippedList.Next = startZip
		startZip = startZip.Next
		zippedList = zippedList.Next

		}
	}
	
	return zippedHead
}


func main() {
	list := []int{1}
	head := &LinkedList{}
	curr := head
	for i, val := range list {
		curr.Value = val
		if i == len(list) - 1 {continue}
		curr.Next = &LinkedList{}
		curr = curr.Next
	}

	rearranged := ZipLinkedList(head)
	for rearranged != nil {
		fmt.Printf("%v -> ", rearranged.Value)
		rearranged = rearranged.Next
	}
	fmt.Println()
}