package main

import "fmt"

// Time -> 0(N) Space -> 0(N)
func SunsetViews(buildings []int, direction string) []int {
	var max int
	result := make([]int, 0)
	if direction == "EAST" {
		start, stop := len(buildings) - 1, 0
		for start >= stop {
			if buildings[start] > max {
				result = append(result, start)
				max = buildings[start]
			}
			start--
		}
		for i, j:=0, len(result)-1; i < j; i, j = i+1, j-1 {
			result[i], result[j] = result[j], result[i]
		}
		return result
	}else {
		start, stop := 0, len(buildings) - 1
		for start <= stop {
			if buildings[start] > max {
				result = append(result, start)
				max = buildings[start]
			}
			start++
		}
		return result
	}
}


func main() {
	array := []int{3, 5, 4, 4, 3, 1, 3, 2}
	fmt.Println(SunsetViews(array, "EAST"))
	fmt.Println(SunsetViews(array, "WEST"))
}