package main

import "strings"

func solution(phone_number string) string {
	l := len(phone_number)
	ast := strings.Repeat("*", l-4)
	result := ast + string([]rune(phone_number)[l-4:])
	return result
}
