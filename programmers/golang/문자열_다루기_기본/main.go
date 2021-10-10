package main

import (
	"fmt"
	"strconv"
)

func solution(s string) bool {
	_, err := strconv.Atoi(s)
	fmt.Println(len(s))
	if len(s) != 4 && len(s) != 6 || err != nil {
		return false
	}
	return true
}

func main() {
	solution("1234")
}
