package main

import (
	"fmt"
	"strings"
)

// Time -> 0(N+M) Space -> 0(N)
func UnderScorifySubString(str, substring string) string {
	var locations [][]int
	var i int
	for i < len(str) {
		idx := strings.Index(str[i:], substring)
		if idx == -1 {break}
		start := i + idx
		end := start + len(substring)
		locations = append(locations, []int{start, end})
		i = start + 1
	}

	if len(locations) == 0 {return str}
	newlocation := [][]int{locations[0]}
	for _, val := range locations[1:] {
		last := newlocation[len(newlocation)-1]

		if val[0] <= last[1] {
			last[1] = val[1]
		}else {newlocation = append(newlocation, val)}
	}

	i = 0
	var j int
	var result strings.Builder
	for i < len(str) {
		if j < len(newlocation) && i == newlocation[j][0] {
			result.WriteString("_"+str[i:newlocation[j][1]]+"_")
			i = newlocation[j][1]
			j += 1
		}else {
			result.WriteString(string(str[i]))
			i++
		}
	}
	return result.String()
}

func main() {
	fmt.Println(UnderScorifySubString("testesttesttestest is not going well", "test"))
}