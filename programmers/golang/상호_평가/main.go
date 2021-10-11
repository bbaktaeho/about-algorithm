package main

func solution(scores [][]int) string {
	l := len(scores)
	result := ""
	for i := 0; i < l; i++ {
		max, min, sum := 0, 100, 0
		for j := 0; j < l; j++ {
			if i == j {
				continue // 자기가 자기를 추천한 점수는 제외
			}
			val := scores[j][i] // 세로
			sum += val
			if val > max {
				max = val
			}
			if val < min {
				min = val
			}
		}
		self := scores[i][i]
		avg := 0
		if self > max || self < min {
			avg = sum / (l - 1)
		} else {
			avg = (sum + self) / l
		}
		switch {
		case avg >= 90:
			result += "A"
		case avg >= 80:
			result += "B"
		case avg >= 70:
			result += "C"
		case avg >= 50:
			result += "D"
		default:
			result += "F"
		}
	}
	return result
}
