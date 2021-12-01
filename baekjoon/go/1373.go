package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	s := bufio.NewScanner(os.Stdin)
	var binary string
	if s.Scan() {
		binary = s.Text()
	}
	dec, _ := strconv.ParseInt(binary, 2, 64)
	fmt.Println(fmt.Sprintf("%o", dec))
}
