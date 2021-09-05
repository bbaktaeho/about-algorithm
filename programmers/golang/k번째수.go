package main

import (
	"fmt"
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

func main() {
	result := solution([]int{1, 5, 2, 6, 3, 7, 4}, [][]int{{2, 5, 3}, {4, 4, 1}, {1, 7, 3}})
	fmt.Println(result)
}
