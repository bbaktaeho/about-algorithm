package main

import (
	"strings"
)

// 실패
// func solution(s string) string {
// 	words := strings.Fields(s)
// 	for i, word := range words {
// 		runes := []rune(strings.ToLower(word))
// 		runes[0] = unicode.ToUpper(runes[0])
// 		words[i] = string(runes)
// 	}
// 	return strings.Join(words, " ")
// }

func solution(s string) string {
	return strings.Title(strings.ToLower(s))
}
