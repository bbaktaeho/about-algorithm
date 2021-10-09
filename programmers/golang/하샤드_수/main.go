package main

// 나머지

import (
	"fmt"
	"strconv"
	"strings"
)

func solution(x int) bool {
	sum := 0
	for i := x; i > 0; i /= 10 {
		sum += i % 10
	}
	return x%sum == 0
}

func solution2(x int) bool {
	tmp := 0
	for _, a := range strings.Split(strconv.Itoa(x), "") {
		inter, _ := strconv.Atoi(a)
		fmt.Println(a, inter)
		tmp = tmp + inter
	}
	return x%tmp == 0
}

func main() {
	solution2(1023)
}
