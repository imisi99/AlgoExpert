package main


import "fmt"


type AncestralTree struct {
	Value int
	Ancestor *AncestralTree
}


// Time -> 0(log(N)) Space -> 0(log(N))
func getYoungestCommonAncestor(top, node1, node2 *AncestralTree) *AncestralTree {
	ancestors := node1
	ancestor_list := make(map[*AncestralTree]bool)
	for ancestors != nil {
		ancestor_list[ancestors] = false
		ancestors = ancestors.Ancestor
	}

	for node2 != nil {
		if _, exists := ancestor_list[node2]; exists {
			return node2
		}
		node2 = node2.Ancestor
	}

	return top
}

// Time -> 0(log(N)) Space -> 0(1)
func getYoungestCommonAncestor1(top, node1, node2 * AncestralTree) *AncestralTree {
	var node1Count, node2Count int
	node1Tree := node1
	node2Tree := node2
	for node1Tree != nil {
		node1Count++
		node1Tree = node1Tree.Ancestor
	}
	for node2Tree != nil {
		node2Count++
		node2Tree = node2Tree.Ancestor
	}

	if node1Count > node2Count {
		return levelTree(node1, node2, node1Count-node2Count)
	}else {
		return levelTree(node2, node1, node2Count-node1Count)
	}

}


func levelTree(node, highnode *AncestralTree, diff int) *AncestralTree {
	levelNode := node
	for diff > 0 {
		levelNode = levelNode.Ancestor
		diff--
	}
	
	for levelNode != highnode{
		levelNode = levelNode.Ancestor
		highnode = highnode.Ancestor
	}
	return levelNode
}

func main() {
	top := AncestralTree{Value: 1}
	a := AncestralTree{Value: 2, Ancestor: &top}
	b := AncestralTree{Value: 3, Ancestor: &top}
	node1 := AncestralTree{Value: 4, Ancestor: &a}
	node2 := AncestralTree{Value: 7, Ancestor: &b}
	fmt.Println(getYoungestCommonAncestor(&top, &node1, &node2).Value)
}