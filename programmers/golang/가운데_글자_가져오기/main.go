package main

func solution(s string) string {
	l := len(s)
	result := ""
	if l%2 == 0 {
		i := l/2 - 1
		result = s[i : i+2]
	} else {
		result = s[l/2 : l/2+1]
	}
	return result
}
