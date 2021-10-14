package main

func lcm(n, m int) int {
	A, B := n, m
	if n < m {
		n, m = m, n
	}
	for m != 0 {
		n, m = m, n%m
	}
	return A * B / n
}

func solution(arr []int) int {
	num := arr[0]
	for i := 1; i < len(arr); i++ {
		num = lcm(num, arr[i])
	}
	return num
}
