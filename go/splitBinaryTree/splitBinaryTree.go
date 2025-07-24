package main



type BinaryTree struct {
	Value int

	Left *BinaryTree
	Right *BinaryTree
}


type TreeSum struct {
	Sum int
}


func (tree *BinaryTree) SplitTree() int {
	var treeSum TreeSum
	tree.GetSum(&treeSum)
	sum := treeSum.Sum
	_, split := FindSplit(tree, sum / 2)
	if split {return sum / 2}
	return 0
}


func (tree *BinaryTree) GetSum(treeSum *TreeSum) {
	if tree == nil {return}

	treeSum.Sum += tree.Value
	tree.Left.GetSum(treeSum)
	tree.Right.GetSum(treeSum)

}


func FindSplit(tree *BinaryTree, sum int)  (int, bool) {
	if tree == nil {return 0, false}

	leftTree, splitLeft := FindSplit(tree.Left, sum)
	rightTree, splitRight := FindSplit(tree.Right, sum)

	currTree := tree.Value + leftTree + rightTree
	split := splitLeft || splitRight || currTree == sum
	return currTree, split
}

