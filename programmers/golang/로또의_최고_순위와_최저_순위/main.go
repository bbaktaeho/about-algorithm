package main

import "sort"

func solution(lottos []int, win_nums []int) []int {
	rank := []int{6, 6, 5, 4, 3, 2, 1}
	max := 0
	min := 0

	sort.Ints(win_nums)
	for _, lo := range lottos {
		if lo == 0 {
			max++
		} else {
			index := sort.SearchInts(win_nums, lo)
			if index < 6 && lo == win_nums[index] {
				max++
				min++
			}
		}

	}
	return []int{rank[max], rank[min]}
}

func main() {
	solution([]int{44, 1, 0, 0, 31, 25}, []int{31, 10, 45, 1, 6, 19})
}
