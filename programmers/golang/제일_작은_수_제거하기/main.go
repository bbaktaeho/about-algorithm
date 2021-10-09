package main

func solution(arr []int) []int {
	if len(arr) == 1 {
		return []int{-1}
	}
	minIndx := 0
	for i := range arr {
		if arr[i] < arr[minIndx] {
			minIndx = i
		}
	}
	return append(arr[:minIndx], arr[minIndx+1:]...)
}
