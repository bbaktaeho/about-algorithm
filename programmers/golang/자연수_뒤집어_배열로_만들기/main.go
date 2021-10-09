package main

import (
	"container/list"
	"strconv"
)

// 나머지 문제

func Reverse(s string) (result []int) {
	li := list.New()
	for _, v := range s {
		num, _ := strconv.Atoi(string(v))
		li.PushFront(num)
	}
	for i := li.Front(); i != nil; i = i.Next() {
		result = append(result, i.Value.(int))
	}
	return
}

func solution(n int64) []int {
	return Reverse(strconv.Itoa(int(n)))
}

func solution2(n int64) []int64 {
	result := []int64{}

	for n > 0 {
		result = append(result, n%10)
		n = n / 10
	}
	return result
}
