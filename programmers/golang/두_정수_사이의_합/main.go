package main

import (
	"math"
)

func solution(a int, b int) int {
	return (int(math.Abs(float64(a-b))+1) * (a + b) / 2)
}
func main() {
	(solution(3, 3))
	(solution(3, 5))
	(solution(3, 7))
	(solution(0, 55))
}
