package main

import "sort"

func solution(n int, lost []int, reserve []int) int {
	sort.Ints(lost)
	sort.Ints(reserve)
	for i := 0; i <= 1; i++ {
		for j := 0; j < len(reserve); j++ {
			for k := 0; k < len(lost); k++ {
				if reserve[j] == lost[k]+i || reserve[j] == lost[k]-i {
					lost[k] = lost[len(lost)-1]
					lost = lost[:len(lost)-1]
					reserve[j] = reserve[len(reserve)-1]
					reserve = reserve[:len(reserve)-1]
					j--
					break
				}
			}
		}
	}
	return n - len(lost)
}
