package main

import (
	"fmt"
)

func sub() {
	s2 := make([]int, 3)
	s2[0] = 2
	fmt.Println(s2)
}

func intf() {
	var x interface{} = 3
	i, isInt := x.(int)
}

func main() {
	go intf()
	go sub()
	var s1 []int
	s1[0] = 1
	fmt.Println(s1)
}