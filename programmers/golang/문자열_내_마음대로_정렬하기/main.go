package main

import (
	"sort"
)

func solution(strings []string, n int) []string {
	sort.Slice(strings, func(i, j int) bool {
		a := []rune(strings[i])
		b := []rune(strings[j])
		if a[n] < b[n] {
			return true
		} else if a[n] == b[n] {
			return strings[i] < strings[j]
		} else {
			return false
		}
	})
	return strings
}

func solution2(strings []string, n int) []string {
	sort.Slice(strings, func(i, j int) bool {
		if strings[i][n] == strings[j][n] {
			return strings[i] < strings[j]
		}
		return strings[i][n] < strings[j][n]
	})
	
	return strings
}
