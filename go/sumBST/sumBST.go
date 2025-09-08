package main

import (
	"fmt"
	"math"
)


type BinaryTree struct {
	Value int

	Left *BinaryTree
	Right *BinaryTree
}


type TreeInfo struct {
	size 	int
	bstsum 	int
	max 	int
	min 	int
	total	int
	isvalid bool
}


func SumBsts(tree *BinaryTree) int {
	treeInfo := Sum(tree)
	return treeInfo.total
}


// Time -> 0(N) Space -> 0(d) where d is the max height of the tree
func Sum(tree *BinaryTree) TreeInfo {
	if tree == nil {
		return TreeInfo{isvalid: true, min: math.MaxInt, max: math.MinInt}
	}

	leftTree := Sum(tree.Left)
	rightTree := Sum(tree.Right)

	validbst := tree.Value > leftTree.max && tree.Value <= rightTree.min
	valid := validbst && leftTree.isvalid && rightTree.isvalid

	maxVal := max(tree.Value, max(leftTree.max, rightTree.max))
	minVal := min(tree.Value, min(leftTree.min, rightTree.min))

	bstSum := 0
	bstSize := 0
	total := leftTree.total + rightTree.total

	if valid {
		bstSum = tree.Value + leftTree.bstsum + rightTree.bstsum
		bstSize = 1 + leftTree.size + rightTree.size

		if bstSize >= 3 {total = bstSum}
	}

	return TreeInfo{size: bstSize, bstsum: bstSum, max: maxVal, min: minVal, total: total, isvalid: valid}

} 

func min(x, y int) int {
	if x < y {return x}
	return y
}

func max(x, y int) int {
	if x > y {return x}
	return y
}

func main() {
	left := &BinaryTree{Value: 7}
	right := &BinaryTree{Value: 6, Left: left}
	tree := &BinaryTree{Value: 2, Right: right}
	fmt.Println(SumBsts(tree))
}