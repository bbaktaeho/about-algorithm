package main

import "fmt"

func main() {
	var N, F int
	fmt.Scanln(&N)
	fmt.Scanln(&F)

	N = N / 100 * 100
	for N%F != 0 {
		N++
	}

	result := N % 100
	if result < 10 {
		fmt.Println("0" + fmt.Sprint(result))
	} else {
		fmt.Println(result)
	}
}
