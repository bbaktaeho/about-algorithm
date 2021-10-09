package main

import (
	"strings"
)

func solution(s string) string {
	result := []string{}
	for _, word := range strings.Split(s, " ") {
		newWord := ""
		for i, c := range word {
			if i%2 == 0 {
				newWord += strings.ToUpper(string(c))
			} else {
				newWord += strings.ToLower(string(c))
			}
		}
		result = append(result, newWord)
	}
	return strings.Join(result, " ")
}
