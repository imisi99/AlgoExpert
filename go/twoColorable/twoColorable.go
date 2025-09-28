package main

import "fmt"


// Time -> 0(v + e) Space -> (v) where v is the vertices(length of edges) and e is the edge(max length of a single edge)
func TwoColorable(edges [][]int) bool {

	set := make(map[int]string, 0)

	edgeLen := len(edges)
	var edge int
	for edge < edgeLen {
		if _, exists := set[edge]; !exists {
			set[edge] = "blue"
		}

		color := set[edge]
		for _, node := range edges[edge] {
			if _, exists := set[node]; !exists {
				set[node] = SetColor(color)
			}

			color1 := set[node]
			if color1 == color {return false}
		}
		edge++
	}

	return true
}

func SetColor(color string) string {
	if color == "blue" {return "yellow"}
	return "blue"
}

func main() {
	fmt.Println(TwoColorable([][]int{{1}, {0}}))
	fmt.Println(TwoColorable([][]int{{1, 2}, {0, 2}, {0, 1}}))
}
