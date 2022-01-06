package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func read_input(fname string) ([]int, error) {
	datas, err := ioutil.ReadFile(fname)
	if err != nil {
		return nil, err
	}

	data := strings.Split(string(datas), "\n")
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

func calcu_in_tro(data []int) int {
	var current int
	var increased int = 0

	for i := 0; i < len(data)-3+1; i++ {
		tmp := data[i] + data[i+1] + data[i+2]

		if current == 0 {
			current = tmp
		} else {
			if current < tmp {
				increased += 1
			}
		}
		current = tmp
	}
	return increased
}

func main() {
	data, err := read_input("../input/q1input.in")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(calcu_in_tro(data))
}
