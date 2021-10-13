package main

import "math"

func isPrime(n int) bool {
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func solution(nums []int) int {
	answer := 0
	l := len(nums)
	for i := 0; i < l-2; i++ {
		for j := i + 1; j < l-1; j++ {
			for k := j + 1; k < l; k++ {
				if isPrime(nums[i] + nums[j] + nums[k]) {
					answer++
				}
			}
		}
	}
	return answer
}
