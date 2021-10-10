package main

import (
	"math"
	"strings"
)

func solution(n int) string {
	str := []rune(strings.Repeat("수박", int(math.Floor(float64(n)/2)+1)))
	return string(str[:n])
}
