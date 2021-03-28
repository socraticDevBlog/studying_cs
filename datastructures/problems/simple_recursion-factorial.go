package main

import "fmt"

func factorial (val int) int {
	if val == 0 {
	   return 1
	}
	
	return val * factorial(val - 1)
}

func main() {
	result := factorial(7) //expect 5040
	fmt.Println(result)
}
