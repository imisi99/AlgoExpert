package main


type BinaryTree struct {
	Value int

	Left *BinaryTree
	Right *BinaryTree
}


type TreeInfo struct {
	Diameter int
	Height int
}


// Time -> 0(N)
func (tree *BinaryTree) MaxDiameter() *TreeInfo {
	if tree == nil {return &TreeInfo{Diameter: 0, Height: 0}}

	leftTreeInfo := tree.Left.MaxDiameter()
	rightTreeInfo := tree.Right.MaxDiameter()


	maxdiameter := max((leftTreeInfo.Height + rightTreeInfo.Height), leftTreeInfo.Diameter, rightTreeInfo.Diameter)
	height := max(leftTreeInfo.Height, rightTreeInfo.Height) + 1

	return &TreeInfo{Diameter: maxdiameter, Height: height}
}


func GetDiameter(tree *BinaryTree) int {
	return tree.MaxDiameter().Diameter
}
