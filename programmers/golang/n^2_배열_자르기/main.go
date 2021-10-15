package main

import "math"

func solution(n int, left int64, right int64) []int {
	arr := []int{}
	for i := left; i <= right; i++ {
		div := float64(i / int64(n))
		mod := float64(i % int64(n))
		arr = append(arr, int(math.Max(div, mod))+1)
	}
	return arr
}

func main() {
	solution(3, 2, 5)
}