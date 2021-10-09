package main

import "math"

func solution(n int) int {
	result := 0
	for i := 1; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			result += i
			temp := n / i
			if temp != i {
				result += temp
			}
		}
	}
	return result
}
