package main

import "fmt"

type BinaryTree struct {
	Value int

	Left  *BinaryTree
	Right *BinaryTree
}

type Idx struct {
	idx    int
	store int
	is_nil bool
}


// Time -> 0(N) Space -> 0(N) 
func (tree *BinaryTree) InOrder(array []*BinaryTree, idx *Idx, node *BinaryTree) []*BinaryTree {
	if tree == nil {
		return array
	}

	array = tree.Left.InOrder(array, idx, node)
	array = append(array, tree)
	idx.idx++
	if tree.Value == node.Value {
		idx.store = idx.idx
	}
	array = tree.Right.InOrder(array, idx, node)

	return array
}

func GetSucessor(tree, node *BinaryTree) *BinaryTree {
	idx := &Idx{store: -1}
	array := tree.InOrder([]*BinaryTree{}, idx, node)
	if idx.store >= len(array) || idx.store == -1 {return nil}
	return array[idx.store]
}


func main() {
	tree := &BinaryTree{Value: 1}
	tree.Left = &BinaryTree{Value: 2}
	tree.Left.Right = &BinaryTree{Value: 7}
	tree.Left.Left = &BinaryTree{Value: 3}
	tree.Right = &BinaryTree{Value: 12}

	node := &BinaryTree{Value: 3}

	fmt.Println(*GetSucessor(tree, node))

}