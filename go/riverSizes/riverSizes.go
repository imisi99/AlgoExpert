package main

import (
	"fmt"
)


type Tuple struct {
	col int
	row int
}


// Time -> 0(wh) Space -> 0(wh) where w and h is the width and height of the matrix 
func RiverSizes(matrix [][]int) []int {
	endcol, endrow := len(matrix), len(matrix[0])
	set, array := make(map[Tuple]bool, 0), make([]int, 0)
	col := 0
	for col < endcol {
		row := 0
		for row < endrow {
			if _, exist := set[Tuple{col: col, row: row}]; exist {row++; continue}
			if matrix[col][row] == 0 {set[Tuple{col: col, row: row}] = true; row++; continue}

			sum := CheckSide(col, row, matrix, set)
			array = append(array, sum)

			set[Tuple{col: col, row: row}] = true
			row++
		}
		col++
	}

	return array
}


func CheckSide(col, row int, matrix [][]int, set map[Tuple]bool) int {
	sum := 0
	if _, exists := set[Tuple{col: col, row: row}]; exists {return sum}
	set[Tuple{col: col, row: row}] = true
	if row < 0 || row >= len(matrix[0]) || col < 0 || col >= len(matrix) {return sum}
	if matrix[col][row] == 1 {
		sum += 1
	}else {return sum}

	sum += CheckSide(col+1, row, matrix, set)
	sum += CheckSide(col-1, row, matrix, set)
	sum += CheckSide(col, row-1, matrix, set)
	sum += CheckSide(col, row+1, matrix, set)
	return sum
}


func main() {
	fmt.Println(RiverSizes([][]int{{1, 0, 0, 1, 0}, {1, 0, 1, 0, 0}, {0, 0, 1, 0, 1}, {1, 0, 1, 0, 1}, {1, 0, 1, 1, 0}}))
}