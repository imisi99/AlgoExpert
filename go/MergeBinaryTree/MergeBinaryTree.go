package main


type BinaryTree struct{
	Value int

	Left *BinaryTree
	Right *BinaryTree
}



// Time -> 0(N) where N is the number of node of the first tree and h is the max height of the first tree
func MergeBinaryTree(tree1, tree2 *BinaryTree) *BinaryTree {
	var leftStack, rightStack []*BinaryTree

    leftStack = append(leftStack, tree1)
    rightStack = append(rightStack, tree2)

    for len(leftStack) > 0{
        left := leftStack[len(leftStack)-1]
        right := rightStack[len(rightStack)-1]

        leftStack = leftStack[:len(leftStack)-1]
        rightStack = rightStack[:len(rightStack)-1]
        
        left.Value += right.Value

        if left.Left == nil {
            left.Left = right.Left
        } else if left.Left != nil && right.Left != nil {
            leftStack = append(leftStack, left.Left)
            rightStack = append(rightStack, right.Left)
        }

        if left.Right == nil {
            left.Right = right.Right
        }else if left.Right != nil && right.Right != nil{
            leftStack = append(leftStack, left.Right)
            rightStack = append(rightStack, right.Right)
        }
        
    }
    return tree1
}


