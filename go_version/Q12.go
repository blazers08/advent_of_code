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
	var day, count int = 0, 0
	var fish_map = make(map[int]int)

	for _, fish := range data {
		if _, ok := fish_map[fish]; ok {
			fish_map[fish] += 1
		} else {
			fish_map[fish] = 1
		}
	}

	for day < days {
		var tmp = make(map[int]int)

		for fish, count := range fish_map {
			if fish == 0 {
				tmp[6] += count
				tmp[8] += count
			} else {
				tmp[fish-1] += count
			}
		}
		day++
		fish_map = tmp
	}

	for _, cnt := range fish_map {
		count += cnt
	}
	return count
}

func main() {
	fishes, err := read_input("../input/q11input.in")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(fishcount(fishes, 256))
}