package main

func solution(arr1 [][]int, arr2 [][]int) [][]int {
	matrix := [][]int{}
	for i := 0; i < len(arr1); i++ {
		arr := []int{}
		for j := 0; j < len(arr1[i]); j++ {
			arr = append(arr, arr1[i][j] + arr2[i][j])
		}
		matrix = append(matrix, arr)
	}
    return matrix
}

	