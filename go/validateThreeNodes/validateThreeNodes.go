package main


type BST struct {
	Value int

	Left  *BST
	Right *BST
}


// Time -> 0(h) Space -> 0(1) where h is the height of the tree
func ValidateThreeNodes(nodeOne, nodeTwo, nodeThree *BST) bool {
	var found bool
	curr := nodeOne
	for curr != nil {
		if curr == nodeThree {return false}
		if curr == nodeTwo {
			found = true
			break
		}
		if nodeTwo.Value > curr.Value {
			curr = curr.Right
		}else {curr = curr.Left}
	}

	if !found {
		for nodeThree != nil {
			if nodeThree == nodeOne {return false}
			if nodeThree == nodeTwo {
				found = true
				break
			}
			if nodeTwo.Value > nodeThree.Value {
				nodeThree = nodeThree.Right
			}else {nodeThree = nodeThree.Left}
		}
		if found {
			for nodeTwo != nil {
				if nodeTwo == nodeOne {return true}
				if nodeOne.Value > nodeTwo.Value {
					nodeTwo = nodeTwo.Right
				}else {nodeTwo = nodeTwo.Left}
			}
		}else {return false}
	}else {
		for nodeTwo != nil {
			if nodeTwo == nodeThree {return true}
			if nodeThree.Value > nodeTwo.Value {
				nodeTwo = nodeTwo.Right
			}else {nodeTwo = nodeTwo.Left}
		}
	}

	return false
}


// Time -> 0(N) Space -> 0(h)
func ValidateThreeNodes1(nodeOne, nodeTwo, nodeThree *BST) bool {
	var desc, ansc *BST

	desc = nodeTwo.FindNode(nodeOne, nodeThree)
	if desc == nil {return false}
	if desc == nodeOne {
		ansc = nodeThree
	}else {ansc = nodeOne}

	for ansc != nil {
		if ansc == nodeTwo {return true}
		if nodeTwo.Value > ansc.Value {
			ansc = ansc.Right
		}else {ansc = ansc.Left}
	}	
	
	return false
}


func (tree *BST) FindNode(nodeOne, nodeTwo *BST) *BST {
    if tree == nil {return nil}
	if tree == nodeOne {return nodeOne}
	if tree == nodeTwo {return nodeTwo}

	var node *BST
	node = tree.Left.FindNode(nodeOne, nodeTwo)
    if node != nil {return node}
	node = tree.Right.FindNode(nodeOne, nodeTwo)
	return node
}
