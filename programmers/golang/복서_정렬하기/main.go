package main

import (
	"sort"
)

type Boxer struct {
	Id         int
	Weight     int
	Rate       float64
	OverWeight int
}

func GetIds(boxers []Boxer) (result []int) {
	for _, boxer := range boxers {
		result = append(result, boxer.Id)
	}
	return
}

func solution(weights []int, head2head []string) []int {
	boxerList := []Boxer{}
	gameCount := len(weights) - 1
	for i, weight := range weights {
		boxerList = append(boxerList, Boxer{Id: i + 1, Weight: weight})
		winCount := 0
		for j, gameResult := range head2head[i] {
			if i == j {
				continue
			}
			if 'W' == gameResult {
				if weight < weights[j] {
					boxerList[i].OverWeight += 1
				}
				winCount += 1
			}
		}
		boxerList[i].Rate = float64(winCount) / float64(gameCount)
	}

	sort.Slice(boxerList, func(i, j int) bool {
		if boxerList[i].Rate > boxerList[j].Rate {
			return true
		} else if boxerList[i].Rate == boxerList[j].Rate {
			if boxerList[i].OverWeight > boxerList[j].OverWeight {
				return true
			} else if boxerList[i].OverWeight == boxerList[j].OverWeight {
				return boxerList[i].Weight > boxerList[j].Weight
			}
			return false
		} else {
			return false
		}
	})
	return GetIds(boxerList)
}
