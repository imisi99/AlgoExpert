package main

import "fmt"


type BST struct{
	Value int

	Left *BST
	Right *BST
}

func (tree *BST) InOrderTraversal(array []int) []int{
	if tree == nil {return array}

	array = tree.Left.InOrderTraversal(array)
	array = append(array, tree.Value)
	array = tree.Right.InOrderTraversal(array)

	return array
}

func (tree *BST) ReverseInOrderTraversal(array []int) []int{
	if tree == nil {return array}

	array = tree.Right.ReverseInOrderTraversal(array)
	array = append(array, tree.Value)
	array = tree.Left.ReverseInOrderTraversal(array)

	return array
}


func PopulateBST(bst *BST, start, end int, array []int) *BST{
	if end < start {return nil}

	mid := (end + start) / 2
	bst = &BST{Value: array[mid]}
	bst.Left = PopulateBST(bst, start, mid-1, array)
	bst.Right = PopulateBST(bst, mid+1, end, array)

	return bst
}


// Time -> 0(N) Space -> 0(N)	n is the number of node in the BST
func FindKthLargestValue(bst *BST, k int) int{
	array := bst.InOrderTraversal([]int{0})
	return array[len(array)-k]
}


// Time -> 0(h + k) Space -> 0(h) h is the max height of the BST
func FindKthLargestValue2(bst *BST, k int, visited []int) *int{
	if bst == nil {return nil}

	right := FindKthLargestValue2(bst.Right, k, visited)
	if right != nil {return right}

	visited[0] += 1
	if visited[0] == k {return &bst.Value}

	return FindKthLargestValue2(bst.Left, k, visited)
}


func main(){
	array := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 19, 39, 40, 43}
	bst := PopulateBST(nil, 0, len(array)-1, array)
	fmt.Println(bst.InOrderTraversal([]int{}))
	fmt.Println(bst.ReverseInOrderTraversal([]int{}))
	fmt.Println(FindKthLargestValue(bst, 12))
	fmt.Println(*FindKthLargestValue2(bst, 12, []int{0}))
}
