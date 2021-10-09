package main

import "fmt"

func solution(x int, n int) []int64 {
	var arr = make([]int64, n, n)
	arr[0] = int64(x)
	for i := 1; i < n; i++ {
		arr[i] = arr[i-1] + int64(x)
	}
	return arr
}

func main() {
	arr := solution(2, 5)
	fmt.Println(arr)
}
