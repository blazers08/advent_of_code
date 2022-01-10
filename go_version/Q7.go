package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
	// "reflect"
)

func read_input(fname string) ([]int, [][][]int, error) {
	datas, err := ioutil.ReadFile(fname)
	if err != nil {
		return nil, nil, err
	}

	var (
		tables  [][][]int
		board   [][]int
		numbers []int
	)

	data := strings.Split(string(datas), "\n")

	for _, n := range strings.Split(data[0], ",") {
		num, _ := strconv.Atoi(n)
		numbers = append(numbers, num)
	}

	for key, value := range data {
		if key < 2 {
			continue
		}

		if value == "" {
			continue
		}

		nums := strings.Fields(value)
		n := make([]int, 0)

		if len(nums) == 0 {
			continue
		}

		for _, num := range nums {
			num, _ := strconv.Atoi(num)
			n = append(n, num)
		}

		board = append(board, n)

		if len(board) != 5 {
			continue
		}

		tables = append(tables, board)
		board = nil
	}
	return numbers, tables, nil
}

func mark_board(board [][]int, number int) {
	for _, ele := range board {
		for i := 0; i < len(ele); i++ {
			if ele[i] == number {
				ele[i] = -1
			}
		}
	}
}

func check_win(board [][]int) bool {
	var win bool // default is False

	// check -
	for _, ele := range board {
		var count int = 0
		for _, i := range ele {
			if i == -1 {
				count += 1
			}
		}
		if count == len(ele) {
			win = true
			return win
		}
	}

	// check |
	for i := 0; i < 5; i++ {
		var count int = 0
		for _, element := range board {
			if element[i] == -1 {
				count += 1
			}
		}
		if count == 5 {
			win = true
			return win
		}
	}

	return win
}

func sumofunmarked(board [][]int) int {
	var total int = 0
	for _, ele := range board {
		for _, value := range ele {
			if value != -1 {
				total += value
			}
		}
	}
	return total
}

func main() {
	numbers, tables, err := read_input("../input/q7input.in")
	if err != nil {
		log.Fatal(err)
	}

	for _, num := range numbers {
		for _, board := range tables {
			mark_board(board, num)
			if check_win(board) == true {
				fmt.Println(num * sumofunmarked(board))
				os.Exit(0)
			}
		}
	}
}
