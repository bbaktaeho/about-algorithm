package main

import (
	"fmt"
	"sort"
	"strings"
)

func findIndexForStrings(arr []string, target string) int {
	for i, v := range arr {
		if v == target {
			return i
		}
	}
	return 5
}

// 모든 table은 동일
func solution(table []string, languages []string, preference []int) string {
	groups := make(map[string][]string)
	for _, v := range table {
		group := strings.Fields(v) // [직군, 언어1, 언어2, 언어3, ...]
		groups[group[0]] = group[1:]
	}

	result := make(map[string]int)
	for i, la := range languages {
		for k, la_group := range groups {
			result[k] += preference[i] * (5 - findIndexForStrings(la_group, la))
		}
	}

	answers := []string{"SI"}
	answer_score := result["SI"]
	for k, v := range result {
		if answer_score < v {
			answers = []string{k}
			answer_score = v
		} else if answer_score == v {
			answers = append(answers, k)
		}
	}

	sort.Strings(answers)
	return answers[0]
}

func main() {
	result := solution([]string{"SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"}, []string{"PYTHON", "C++", "SQL"}, []int{7, 5, 5})
	fmt.Println(result)
}
