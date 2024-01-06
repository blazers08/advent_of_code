package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
	// "reflect"
)

func read_input(fname string) ([]int, error) {
	datas, err := ioutil.ReadFile(fname)
	if err != nil {
		return nil, err
	}

	var data []int
	for _, num := range strings.Split(string(datas), ",") {
		tmp, _ := strconv.Atoi(num)
		data = append(data, tmp)
	}
	return data, nil
}

func fishcount(data []int, days int) int {
	var day int = 0

	for day < days {
		var tmp []int
		for i := 0; i < len(data); i++ {
			if data[i] == 0 {
				data[i] = 6
				tmp = append(tmp, 8)
			} else {
				data[i] -= 1
			}
		}
		data = append(data, tmp...)
		day++
	}
	return len(data)
}

func main() {
	fishes, err := read_input("../input/q11input.in")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(fishcount(fishes, 80))
}
