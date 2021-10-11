package main

import (
	"strings"
	"time"
)

func solution(a int, b int) string {
	loc, _ := time.LoadLocation("Asia/Seoul")
	t := time.Date(2016, time.Month(a), b, 1, 1, 1, 1, loc)
	return strings.ToUpper(t.Weekday().String()[:3])
}
