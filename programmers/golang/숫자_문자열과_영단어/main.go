package main

import (
	"strconv"
	"strings"
)

func solution(s string) int {
	nums := []string{"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
	for i, num := range nums {
		s = strings.ReplaceAll(s, num, strconv.Itoa(i))
	}
	result, _ := strconv.Atoi(s)
	return result
}
