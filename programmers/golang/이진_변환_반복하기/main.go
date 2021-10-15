package main

import (
	"fmt"
	"strconv"
	"strings"
)

func solution(s string) []int {
	count := 0
	zeroCount := 0
	for s != "1" {
		count++
		x := strings.Count(s, "1")
		zeroCount += len(s) - x
		s = strconv.FormatInt(int64(x), 2)
	}
	return []int{count, zeroCount}
}

func main() {
	fmt.Println(solution("110010101001"))
}
