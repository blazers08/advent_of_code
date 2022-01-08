package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
	// "reflect"
)

func calulate_gama(data []string) int64 {
	oxy := make([]string, len(data))
	co2 := make([]string, len(data))
	copy(oxy, data)
	copy(co2, data)

	final_oxy := cal(oxy, "oxy")
	final_co2 := cal(co2, "co2")

	gama_int, _ := strconv.ParseInt(final_oxy[0], 2, 64)
	epsi_int, _ := strconv.ParseInt(final_co2[0], 2, 64)

	return gama_int * epsi_int
}

func cal(data []string, cate string) []string {
	var i int = 0

	for len(data) > 1 {
		var zeros, ones int = 0, 0
		var tmp []string

		for _, ele := range data {
			if ele[i] == '0' {
				zeros += 1
			} else {
				ones += 1
			}
		}

		if cate == "oxy" {
			if zeros > ones {
				for _, item := range data {

					if item[i] == '0' {
						tmp = append(tmp, item)
						data = nil
						data = tmp
					}
				}
			} else {
				for _, item := range data {
					if item[i] == '1' {
						tmp = append(tmp, item)
						data = nil
						data = tmp
					}
				}
			}
		} else {
			if zeros > ones {
				for _, item := range data {
					if item[i] == '1' {
						tmp = append(tmp, item)
						data = nil
						data = tmp
					}
				}
			} else {
				for _, item := range data {
					if item[i] == '0' {
						tmp = append(tmp, item)
						data = nil
						data = tmp
					}
				}
			}
		}
		i += 1
	}
	return data
}

func read_input(fname string) ([]string, error) {
	datas, err := ioutil.ReadFile(fname)
	if err != nil {
		return nil, err
	}

	data := strings.Split(string(datas), "\r\n")

	return data, nil
}

func main() {
	data, err := read_input("../input/q5input.in")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(calulate_gama(data))
}
