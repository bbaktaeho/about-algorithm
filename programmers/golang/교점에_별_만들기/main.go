package main

import (
	"fmt"
	"math"
	"sort"
	"strings"
)

func getCross(a, b []int) (bool, []int) {
	A, B, C, D, E, F := a[0], a[1], b[0], b[1], a[2], b[2]

	deno := float64(A*D - B*C)
	if deno == 0 {
		return false, nil
	}
	x := float64(B*F-E*D) / deno
	y := float64(E*C-A*F) / deno
	if math.Floor(x) == x && math.Floor(y) == y {
		return true, []int{int(x), int(y)}
	}
	return false, nil
}

// x축 최소, 최대
// y축 최소, 최대
func solution(line [][]int) []string {
	pointList := [][]int{}
	graph := []string{}
	min := math.Inf(1)
	max := math.Inf(-1)
	maxX, maxY, minX, minY := max, max, min, min
	for i := 0; i < len(line)-1; i++ {
		for j := 1 + i; j < len(line); j++ {
			isInt, point := getCross(line[i], line[j])
			if isInt {
				pointList = append(pointList, point)
				if maxX < float64(point[0]) {
					maxX = float64(point[0])
				}
				if minX > float64(point[0]) {
					minX = float64(point[0])
				}
				if maxY < float64(point[1]) {
					maxY = float64(point[1])
				}
				if minY > float64(point[1]) {
					minY = float64(point[1])
				}
			}
		}
	}

	sort.Slice(pointList, func(i, j int) bool {
		return pointList[i][1] > pointList[j][1]
	})

	row := strings.Repeat(".", 1+int(math.Abs(float64(maxX))+math.Abs(float64(minX))))
	// 좌표 찍기
	for y := maxY; y >= minY; y-- {
		r := []rune(row)
		for len(pointList) > 0 && pointList[0][1] == int(y) {
			r[pointList[0][0]-int(minX)] = '*'
			if len(pointList) == 1 {
				break
			}
			pointList = pointList[1:]
		}
		graph = append(graph, string(r))
	}

	return graph
}

func main() {
	fmt.Println(solution([][]int{{2, -1, 4}, {-2, -1, 4}, {0, -1, 1}, {5, -8, -12}, {5, 8, 12}}))
}
