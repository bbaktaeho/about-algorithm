package main

// 1. 입력된 수가 짝수라면 2로 나눔, 홀수면 3을 곱하고 1을 더함
// 결과로 나온 수에 같은 작업을 1이 될 때까지 반복

func solution(num int) int {
	count := 0
	for {
		if count > 500 {
			return -1
		}
		if num == 1 {
			return count
		}
		count++
		if num%2 == 0 {
			num = num / 2
		} else {
			num = num*3 + 1
		}
	}
}
