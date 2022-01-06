package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

type Pair struct {
	move  string
	steps int
}

func read_input(fname string) ([]Pair, error) {
	datas, err := ioutil.ReadFile(fname)
	if err != nil {
		return nil, err
	}

	data := strings.Split(string(datas), "\n")
	cleaned_data := []Pair{}

	for _, val := range data {
		sorted := strings.Split(string(val), " ")
		n, _ := strconv.Atoi(sorted[1])
		cleaned_data = append(cleaned_data, Pair{sorted[0], n})
	}
	return cleaned_data, nil
}

func calculate(data []Pair) int {
	var horizontal int = 0
	var aim int = 0
	var depth int = 0

	for _, ele := range data {
		if ele.move == "forward" {
			horizontal += ele.steps
			depth += aim * ele.steps
		} else if ele.move == "down" {
			aim += ele.steps
		} else {
			aim -= ele.steps
		}
	}
	return horizontal * depth
}

func main() {
	data, err := read_input("../input/q3input.in")
	if err != nil {
		log.Fatal(err)
	}
	// fmt.Println(data)
	fmt.Println(calculate(data))
}
