package main

func solution(absolutes []int, signs []bool) int {
	result := 0
	for i, n := range absolutes {
		if !signs[i] {
			result -= n
		} else {
			result += n
		}
	}
	return result
}
