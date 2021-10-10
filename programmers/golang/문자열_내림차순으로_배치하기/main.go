package main

import "sort"

func solution(s string) string {
	strs := []rune(s)
	sort.Slice(strs, func(i, j int) bool {
		return strs[i] > strs[j]
	})
	return string(strs)
}
