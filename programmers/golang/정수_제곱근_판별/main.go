package main

import (
	"math"
)

func solution(n int64) int64 {
	x := int64(math.Sqrt(float64(n)))
	if x*x == n {
		return (x + 1) * (x + 1)
	}
	return -1
}
