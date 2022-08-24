package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"regexp"
	"strconv"
	"strings"
	// "reflect"
)

func read_input(fname string) ([]string, error) {
	datas, err := ioutil.ReadFile(fname)
	if err != nil {
		return nil, err
	}

	var data []string
	point := regexp.MustCompile(" -> |\n").Split(string(datas), -1)
	for _, item := range point {
		data = append(data, strings.TrimSpace(item))
	}

	return data, nil
}

func count_overlap_point(data []string) int {
	type Pair struct {
		x, y int
	}

	vent_map := map[Pair]int{}
	var count int = 0

	for i := 0; i < len(data); i += 2 {
		start_x, _ := strconv.Atoi(strings.Split(data[i], ",")[0])
		start_y, _ := strconv.Atoi(strings.Split(data[i], ",")[1])
		end_x, _ := strconv.Atoi(strings.Split(data[i+1], ",")[0])
		end_y, _ := strconv.Atoi(strings.Split(data[i+1], ",")[1])

		start := Pair{start_x, start_y}
		end := Pair{end_x, end_y}

		// |
		if start.x == end.x {
			if start.y > end.y {
				for i := end.y; i < start.y+1; i += 1 {
					pos := Pair{start.x, i}
					if _, ok := vent_map[pos]; ok {
						vent_map[pos] += 1
					} else {
						vent_map[pos] = 1
					}
				}
			} else {
				for i := start.y; i < end.y+1; i += 1 {
					pos := Pair{start.x, i}
					if _, ok := vent_map[pos]; ok {
						vent_map[pos] += 1
					} else {
						vent_map[pos] = 1
					}
				}
			}
			// -
		} else if start.y == end.y {
			if start.x > end.x {
				for i := end.x; i < start.x+1; i += 1 {
					pos := Pair{i, start.y}
					if _, ok := vent_map[pos]; ok {
						vent_map[pos] += 1
					} else {
						vent_map[pos] = 1
					}
				}
			} else {
				for i := start.x; i < end.x+1; i += 1 {
					pos := Pair{i, start.y}
					if _, ok := vent_map[pos]; ok {
						vent_map[pos] += 1
					} else {
						vent_map[pos] = 1
					}
				}
			}
		} else {
		}
	}

	for _, value := range vent_map {
		if value >= 2 {
			count += 1
		}
	}

	return count
}

func main() {
	data, err := read_input("../input/q9input.in")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(count_overlap_point(data))
}
