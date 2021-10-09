package main

import (
	"fmt"
)

// 두 수의 공통된 소인수를 모두 곱하면 최대공약수
// 두 수의 모든 소인수를 곱하면 최소공배수
// 유클리드 호제법: A를 B로 나눈 나머지를 R이라고 할 때 gcd(A, B) == gcd(B, R)

// func gcdLcm(a, b float64) []int {
// 	max, min := int(math.Max(a, b)), int(math.Min(a, b)) // 두 수 비교
// 	mod := max % min
// 	gcm := min // 이전 나머지
// 	for {
// 		if mod == 0 {
// 			break
// 		}
// 		gcm = mod
// 		mod = min % mod
// 		min = gcm
// 	}
// 	return []int{gcm, int(a) * int(b) / gcm}
// }

func solution(n int, m int) []int {
	A, B := n, m
	if n < m {
		n, m = m, n
	}
	for m != 0 {
		n, m = m, n%m
	}
	return []int{n, A * B / n}
}

func main() {
	fmt.Println(solution(2, 5))
}
