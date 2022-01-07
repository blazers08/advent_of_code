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
	var gama, epsi = "", ""

	for i := 0; i < len(data[0]); i++ {
		var zero, one int = 0, 0

		for _, ele := range data {
			if ele[i] == '0' {
				zero += 1
			} else {
				one += 1
			}
		}
		if zero > one || zero == one {
			gama += "0"
			epsi += "1"
		} else {
			gama += "1"
			epsi += "0"
		}
	}

	gama_int, _ := strconv.ParseInt(gama, 2, 64)
	epsi_int, _ := strconv.ParseInt(epsi, 2, 64)

	return gama_int * epsi_int
}

func read_input(fname string) ([]string, error) {
	datas, err := ioutil.ReadFile(fname)
	if err != nil {
		return nil, err
	}

	data := strings.Split(string(datas), "\n")

	return data, nil
}

func main() {
	data, err := read_input("../input/q5input.in")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(calulate_gama(data))
}
