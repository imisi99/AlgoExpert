package main


type BST struct{
	Value int

	Left *BST
	Right *BST
}


func (tree *BST) InOrder(array []int) []int {
	if tree == nil {return nil}

	array = tree.Left.InOrder(array)
	array = append(array, tree.Value)
	array = tree.Right.InOrder(array)

	return array
}


func (tree *BST) PreOrder(array []int) []int {
	if tree == nil {return nil}

	array = append(array, tree.Value)
	array = tree.Left.PreOrder(array)
	array = tree.Right.PreOrder(array)

	return array
}


func (tree *BST) PostOrder(array []int) []int {
	if tree == nil {return nil}

	array = tree.Left.PostOrder(array)
	array = tree.Right.PostOrder(array)
	array = append(array, tree.Value)

	return array
}

