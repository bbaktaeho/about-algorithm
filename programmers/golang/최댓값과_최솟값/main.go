package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func solution(s string) string {
	nums := strings.Fields(s)
	min := math.MaxInt64
	max := math.MinInt64
	for _, num := range nums {
		n, _ := strconv.Atoi(num)
		if max < n {
			max = n
		}
		if min > n {
			min = n
		}
	}
	return fmt.Sprintf("%d %d", min, max)
}
