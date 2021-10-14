package main

// dp, 피보나치

var arr [100001]int

func fibo(n int) int {
	if arr[n] != 0 {
		return arr[n]
	}
	return fibo(n-2) + fibo(n-1)
}

// 실패
// func solution(n int) int {
// 	arr[1], arr[2] = 1, 1
// 	for i := 3; i <= n; i++ {
// 		arr[i] = arr[i-2] + arr[i-1]
// 	}
// 	return arr[n] % 1234567
// }

func solution(n int) int {
	arr := []int{0, 1, 1}

	for i := 3; i <= n; i++ {
		arr[0], arr[1] = arr[1], arr[2]
		arr[2] = (arr[0] + arr[1]) % 1234567
	}
	return arr[2]
}
