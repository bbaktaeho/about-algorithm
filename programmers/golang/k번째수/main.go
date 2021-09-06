package main

import (
	"sort"
)

func solution(array []int, commands [][]int) []int {
	result := []int{}

	for _, command := range commands {
		copyArr := make([]int, len(array))
		copy(copyArr, array)
		arr := copyArr[command[0]-1 : command[1]]
		sort.Ints(arr)
		result = append(result, arr[command[2]-1])
	}
	return result
}
