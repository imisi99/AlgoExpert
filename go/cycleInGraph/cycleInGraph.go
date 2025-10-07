package main

import "fmt"


// Time -> 0(v + e) Space -> 0(v) where v is the vertice and e is the edge
func CycyleInGraph(edges [][]int) bool{
	set := make(map[int]int, 0)

	for node:=0; node < len(edges); node++ {
		if set[node] == 2 {continue}

		if CheckCycle(node, edges, set) {return true}
	}

	return false
}


func CheckCycle(node int, edges [][]int, set map[int]int) bool{
	edge := edges[node]
	set[node] = 1

	for _, vertice := range edge {
		if set[vertice] == 2 {continue}
		if set[vertice] == 1 {return true}

		if CheckCycle(vertice, edges, set) {return true}
	}

	set[node] = 2
	return false
}


func main() {
	fmt.Println(CycyleInGraph(([][]int{{1, 3}, {2, 3, 4}, {0}, {}, {2, 5}, {}})))
}