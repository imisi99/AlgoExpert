package main

import "fmt"


type Node struct {
	Value string
	Children []*Node
}


// Time -> 0(v + e) Space -> 0(v)
func (n *Node) BreathFirst(array []string) []string{
	queue := make([]*Node, 0)
	queue = append(queue, n)
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		array = append(array, node.Value)
		if len(node.Children) > 0 {
			queue = append(queue, node.Children...)
		}
	}

	return array
}


func main() {
	children := []*Node{
		{Value: "B", Children: []*Node{
			{Value: "E"},
			{Value: "F"},
		}},
		{Value: "C"},
		{Value: "D"},
	}
	node := Node{
		Value: "A",
		Children: children,
	}

	fmt.Println(node.BreathFirst([]string{}))
}

