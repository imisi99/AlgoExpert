package main

import "fmt"

type BinaryTree struct {
	Value int

	Left   *BinaryTree
	Right  *BinaryTree
	Parent *BinaryTree
}

// Time -> 0(N) Space -> 0(1) 
func (tree *BinaryTree) IterativeInOrderTraversal(callback func(int)) {
	var prevNode, nextNode *BinaryTree
	currNode := tree
	for currNode != nil {
		switch prevNode {
			case nil, currNode.Parent:
				if currNode.Left != nil {
					nextNode = currNode.Left
				}else {
					callback(currNode.Value)
					if currNode.Right != nil {
						nextNode = currNode.Right
					}else {nextNode = currNode.Parent}
				}
			case currNode.Left:
				callback(currNode.Value)
				if currNode.Right != nil {
					nextNode = currNode.Right
				}else {nextNode = currNode.Parent}
			default:
				nextNode = currNode.Parent
		}
		prevNode = currNode
		currNode = nextNode
	}
}

func callback(val int) {fmt.Println(val)}

func main() {
	root := &BinaryTree{Value: 2}
	root.Left = &BinaryTree{Value: 1, Parent: root}
	root.Right = &BinaryTree{Value: 4, Parent: root}

	root.IterativeInOrderTraversal(callback)
}