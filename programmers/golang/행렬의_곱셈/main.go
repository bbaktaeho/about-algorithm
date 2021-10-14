package main

func solution(arr1 [][]int, arr2 [][]int) [][]int {
	matrix := [][]int{}
	for _, one := range arr1 {
		row := []int{}
		for j := 0; j < len(arr2[0]); j++ {
			result := 0
			for k, n := range one {
				result += n * arr2[k][j]
			}
			row = append(row, result)
		}
		matrix = append(matrix, row)
	}
	return matrix
}
