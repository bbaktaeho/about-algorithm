package main

func solution(arr []int) float64 {
	sum := 0
	for _, num := range arr {
		sum += num
	}
	return float64(sum) / float64(len(arr))
}
