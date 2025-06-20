package main


import (
	"fmt"
	"math"
	"reflect"
)

type BST struct {
	Value int

	Left  *BST
	Right *BST
}

func (tree *BST) Insert(value int) {
	for tree != nil {
		if value < tree.Value {
			if tree.Left == nil {
				tree.Left = &BST{Value: value}
				break
			} else {
				tree = tree.Left
			}
		} else {
			if tree.Right == nil {
				tree.Right = &BST{Value: value}
				break
			} else {
				tree = tree.Right
			}
		}
	}
}

func (tree *BST) PreOrder(array []int) []int {
	if tree == nil {
		return array
	}

	array = append(array, tree.Value)
	array = tree.Left.PreOrder(array)
	array = tree.Right.PreOrder(array)

	return array
}


func BuildFromPreOrder(array []int) *BST{
	bst := &BST{Value: array[0]}
	for _, v := range array[1:] {bst.Insert(v)}
	return bst
}


func BuildFromPreOrder2(array []int) *BST{
	return RecursiveAddition(math.MinInt, math.MaxInt, array, []int{0})
}


func RecursiveAddition(lowerBound, upperBound int, array, rootidx []int) *BST{
	if rootidx[0] == len(array) {return nil}

	rootValue := array[rootidx[0]]
	if rootValue < lowerBound || rootValue >= upperBound {return nil}

	rootidx[0] += 1
	leftsubtree := RecursiveAddition(lowerBound, rootValue, array, rootidx)
	rightsubtree := RecursiveAddition(rootValue, upperBound, array, rootidx)

	return &BST{
		Value: rootValue,
		Left: leftsubtree,
		Right: rightsubtree,
	}

}


func main() {
	array := []int{10, 4, 2, 1, 5, 17, 19, 18}

	bst := BuildFromPreOrder(array)
	bst2 := BuildFromPreOrder2(array)
	fmt.Println(reflect.DeepEqual(bst.PreOrder([]int{}), array))
	fmt.Println(reflect.DeepEqual(bst2.PreOrder([]int{}), array))
}
