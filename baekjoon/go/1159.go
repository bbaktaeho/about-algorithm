package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var sc *bufio.Scanner

func init() {
	sc = bufio.NewScanner(os.Stdin)
}

func input() string {
	sc.Scan()
	return sc.Text()
}

func main() {
	N, _ := strconv.Atoi(input())

	fisrtName := make(map[byte]int)
	result := make([]string, 0, N)

	for N != 0 {
		name := input()
		first := name[0]
		if fisrtName[first] == 4 {
			result = append(result, string(first))
		}
		fisrtName[first]++
		N--
	}

	if len(result) == 0 {
		fmt.Println("PREDAJA")
	} else {
		answer := ""
		sort.Strings(result)
		for _, s := range result {
			answer += s
		}
		fmt.Println(answer)
	}
}
