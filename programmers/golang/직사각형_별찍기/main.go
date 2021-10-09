package main

import (
	"fmt"
	"strings"
)

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	str := strings.Repeat("*", a) + "\n"
	result := strings.Repeat(str, b)
	fmt.Print(result)
}
