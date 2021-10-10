package main

import "fmt"

func solution(seoul []string) string {
	for i, kim := range seoul {
		if kim == "Kim" {
			return fmt.Sprintf("김서방은 %d에 있다.\n", i)
		}
	}
	return ""
}
