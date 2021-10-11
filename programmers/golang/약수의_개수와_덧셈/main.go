package main

import "math"

func solution(left int, right int) int {
	result := 0
	for i := left; i <= right; i++ {
		count := 0
		for j := 1; j <= int(math.Sqrt(float64(i)))+1; j++ {
			if i%j == 0 {
				divisor := i / j
				if j == divisor {
					count += 1
				} else {
					count += 2
				}
			}
		}
		if count%2 == 0 {
			result += i
		} else {
			result -= i
		}
	}
	return result
}
