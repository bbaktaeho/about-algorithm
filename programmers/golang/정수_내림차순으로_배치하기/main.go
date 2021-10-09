package main

import (
	"sort"
	"strconv"
	"strings"
)

func solution(n int64) int64 {
	arr := strings.Split(strconv.Itoa(int(n)), "")
	sort.Sort(sort.Reverse(sort.StringSlice(arr)))
	result, _ := strconv.Atoi(strings.Join(arr, ""))
	return int64(result)
}
