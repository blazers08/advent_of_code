package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
	// "reflect"
)

func calculate_increase(data []int) int {
	var current int
	var increased int = 0

	for _, ele := range data {
		if current == 0 {
			current = ele
		} else {
			if current < ele {
				increased += 1
			}
			current = ele
		}
	}
	return increased
}

func read_input(fname string) ([]int, error) {
	datas, err := ioutil.ReadFile(fname)
	if err != nil {
		return nil, err
	}

	data := strings.Split(string(datas), "\r\n")
	numbers := make([]int, 0, len(data))

	for _, ele := range data {
		n, err := strconv.Atoi(ele)
		if err != nil {
			return nil, err
		}
		numbers = append(numbers, n)
	}
	return numbers, nil
}

func main() {
	data, err := read_input("../input/q1input.in")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(calculate_increase(data))
}
