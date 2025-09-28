package main


import (
	"fmt"
	"reflect"
)


type BinaryTree struct{
	Value int

	Left *BinaryTree
	Right *BinaryTree
}


func (tree *BinaryTree) PreOrder(array []int) []int {
	if tree == nil {return array}

	array = append(array, tree.Value)
	array = tree.Left.PreOrder(array)
	array = tree.Right.PreOrder(array)

	return array
}


func (tree *BinaryTree) InversePreOrder(array []int) []int {
	if tree == nil {return array}

	array = append(array, tree.Value)
	array = tree.Right.InversePreOrder(array)
	array = tree.Left.InversePreOrder(array)

	return array
}


func PopulateTree() *BinaryTree{
	tree := &BinaryTree{Value: 1}
	tree.Left = &BinaryTree{Value: 2}
	tree.Right = &BinaryTree{Value: 2}
	left := tree.Left
	right := tree.Right
	left.Left = &BinaryTree{Value: 3}
	left.Right = &BinaryTree{Value: 4}
	right.Left = &BinaryTree{Value: 4}
	right.Right = &BinaryTree{Value: 3}
	
	return tree
}


// Time -> 0(N) Space -> 0(N)
func Sol1() bool {
	tree := PopulateTree()

	var arr1, arr2 []int

	if tree.Left != nil {
		arr1 = tree.Left.PreOrder([]int{})
	}
	if tree.Right != nil {
		arr2 = tree.Right.InversePreOrder([]int{})
	}

	return reflect.DeepEqual(arr1, arr2)
}


// Time -> 0(N) Space -> 0(h) where h is the max height of the tree
func Sol2() bool {
	tree := PopulateTree()

	var leftStack, rightStack []*BinaryTree

	leftStack = append(leftStack, tree.Left)
	rightStack = append(rightStack, tree.Right)

	for len(leftStack) > 0 {
		left := leftStack[len(leftStack)-1]
		right := rightStack[len(leftStack)-1]

		leftStack = leftStack[:len(leftStack)-1]
		rightStack = rightStack[:len(rightStack)-1]

		if left == nil && right == nil {continue}

		if left == nil || right == nil || left.Value != right.Value {return false}

		leftStack = append(leftStack, left.Left)
		leftStack = append(leftStack, left.Right)
		rightStack = append(rightStack, right.Right)
		rightStack = append(rightStack, right.Left)
	}

	return true
}


func main() {
	fmt.Println(Sol1())
	fmt.Println(Sol2())
}