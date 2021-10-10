package main

import "unicode"

func encode(alpha *[26]int, c rune, n int, isUpper bool) (result string) {
	newC := int(c) + n
	if newC > alpha[25] {
		if isUpper {
			newC = newC - int('Z') - 1 + int('A')
		} else {
			newC = newC - int('z') - 1 + int('a')
		}
		result += string(rune(newC))
	} else {
		result += string(rune(newC))
	}
	return
}

func solution(s string, n int) string {
	result := ""

	lowers, uppers := [26]int{int('a')}, [26]int{int('A')}
	for i := 1; i < 26; i++ {
		lowers[i] = lowers[i-1] + 1
		uppers[i] = uppers[i-1] + 1
	}

	for _, c := range s {
		if unicode.IsUpper(c) {
			result += encode(&uppers, c, n, true)
		} else if unicode.IsLower(c) {
			result += encode(&lowers, c, n, false)
		} else {
			result += string(c)
		}
	}
	return result
}

func solution2(s string, n int) string {
	result := make([]rune, len(s))
	offset := rune(n)
	for i, v := range s {
		if 'A' <= v && v <= 'Z' {
			result[i] = ((v + offset - 'A') % 26) + 'A'
		} else if 'a' <= v && v <= 'z' {
			result[i] = ((v + offset - 'a') % 26) + 'a'
		} else {
			result[i] = v
		}
	}
	return string(result)
}
