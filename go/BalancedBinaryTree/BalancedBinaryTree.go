package main

import (
	"fmt"
)

type BT struct {
	Value int
	Left  *BT
	Right *BT
}


func (tree *BT) PopulateBT() {
	array := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	left := tree
	right := tree
	for _, v := range array[:len(array)/2] {
		left.Left = &BT{Value: v}
		left = left.Left
	}

	for _, v := range array[len(array)/2:] {
		right.Right = &BT{Value: v}
		right = right.Right
	}
}


// Time -> 0(N) Space -> 0(h)- worst case 0(N) where h is the max height of the tree
func BalancedBT(tree *BT) (int, int, bool){
	if tree == nil {return 0, 0, true}

	left_tree_left, left_tree_right, left_balance := BalancedBT(tree.Left)
	right_tree_left, right_tree_right, right_balance := BalancedBT(tree.Right)

	left_height := max(left_tree_left, left_tree_right) + 1
	right_height := max(right_tree_left, right_tree_right) + 1

	balance := Abs(left_height - right_height) <= 1 && left_balance && right_balance

	fmt.Println(left_height, right_height, balance)

	return left_height, right_height, balance
}

func Abs(x int) int {
	if x < 0 {return -x}
	return x
}


func main() {
	tree := BT{Value: 7}
	tree.PopulateBT()

	BalancedBT(&tree)
}