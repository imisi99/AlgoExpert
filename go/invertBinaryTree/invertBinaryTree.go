package main


import (

	"fmt"
	"reflect"
	"slices"
)


type BinaryTree struct {
	Value int

	Left *BinaryTree
	Right *BinaryTree
}


func (tree *BinaryTree) Inorder(array []int) []int{
	if tree == nil {return array}

	array = tree.Left.Inorder(array)
	array = append(array, tree.Value)
	array = tree.Right.Inorder(array)

	return array
}


// Time -> 0(N) Space -> 0(h) is the max height of the tree
func (tree *BinaryTree) InvertBinaryTree() {
	if tree == nil {return}

	tree.Left, tree.Right = tree.Right, tree.Left
	tree.Left.InvertBinaryTree()
	tree.Right.InvertBinaryTree()
}


func main() {
	tree := &BinaryTree{Value: 1}
	tree.Left = &BinaryTree{Value: 2}
	tree.Left.Left = &BinaryTree{Value: 4}
	tree.Left.Right = &BinaryTree{Value: 5}
	tree.Right = &BinaryTree{Value: 3}
	tree.Right.Left = &BinaryTree{Value: 6}
	tree.Right.Right = &BinaryTree{Value: 7}

	treeArray := tree.Inorder([]int{})
	tree.InvertBinaryTree()
	treeInvertArray := tree.Inorder([]int{})
	slices.Reverse(treeInvertArray)

	fmt.Println(reflect.DeepEqual(treeArray, treeInvertArray), treeArray, treeInvertArray)
}