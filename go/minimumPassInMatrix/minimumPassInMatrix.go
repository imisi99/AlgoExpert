package main

import "fmt"

type Tuple struct {
	col int
	row int
}


// Time -> 0(wh) Space -> 0(wh) where w and h are the width and height
func MinimumPassesOfMatrix(matrix [][]int) int{
	positive := make([]Tuple, 0)

	var col int
	for col < len(matrix) {
		var row int
		for row < len(matrix[col]) {
			if matrix[col][row] > 0 {
				positive = append(positive, Tuple{col: col, row: row})
			}
			row++
		}
		col++
	}

	var pass int

	for len(positive) > 0 {
		nextPositive := (make([]Tuple, 0))

		for _, val := range positive {
			col, row := val.col, val.row
			nextPositive = checkSides(col, row, nextPositive, matrix)
		}

		positive = nextPositive
		if len(positive) > 0 {pass++}
	}

	col = 0
	for col < len(matrix) {
		var row int
		for row < len(matrix[col]) {
			if matrix[col][row] < 0 {
				return -1
			}
			row++
		}
		col++
	}

	return pass
}


func checkSides(col, row int, positive []Tuple, matrix [][]int) []Tuple{
	if col - 1 >= 0 {
		if matrix[col-1][row] < 0 {
			matrix[col-1][row] *= -1
			positive = append(positive, Tuple{col: col-1, row: row})
		}
	}

	if col + 1 < len(matrix) {
		if matrix[col+1][row] < 0 {
			matrix[col+1][row] *= -1
			positive = append(positive, Tuple{col: col+1, row: row})
		}
	}

	if row - 1 >= 0 {
		if matrix[col][row-1] < 0 {
			matrix[col][row-1] *= -1
			positive = append(positive, Tuple{col: col, row: row-1})
		}
	}

	if row + 1 < len(matrix[0]) {
		if matrix[col][row+1] < 0 {
			matrix[col][row+1] *= -1
			positive = append(positive, Tuple{col: col, row: row+1})
		}
	}
	return positive
}


func main() {
	fmt.Println(MinimumPassesOfMatrix([][]int{{0, -2, -1}, {-5, 2, 0}, {-6, -2, 0}}))
}