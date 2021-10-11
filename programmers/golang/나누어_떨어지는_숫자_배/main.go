package main

import "sort"

func solution(arr []int, divisor int) []int {
	result := []int{}
	for _, n := range arr {
		if n%divisor == 0 {
			result = append(result, n)
		}
	}
	sort.Ints(result)
	if len(result) == 0 {
		result = append(result, -1)
	}
	return result
}
