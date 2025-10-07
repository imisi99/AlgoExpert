package main

import "fmt"


// Time -> 0(ND) Space -> 0(N) where d is the denoms and n is the change 
func NumberOfWaysToMakeChange(n int, denoms []int) int {
	ways := make([]int, n+1)
	ways[0] = 1

	for _, d := range denoms {
		for i := range ways {
			if d <= i {
				ways[i] += ways[i-d]
			}
		}
	}
	fmt.Println(ways)
	return ways[n]

}

func main () {
	fmt.Println(NumberOfWaysToMakeChange(3, []int{14, 2}))
}