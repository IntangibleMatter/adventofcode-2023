package main

import (
	"bufio"
	f "fmt"
	"os"
	"sort"
	"strconv"
	str "strings"
)

var seeds []int
var s2s, s2f, f2w, w2l, l2t, t2h, h2l [][3]int

func openFile() []string {
	file, err := os.Open("./demoinput")

	var lines []string

	if err != nil {
		f.Println("Err", err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		f.Println(err)
	}

	return lines
}

func main() {
	lines := openFile()


	initializeArrays(lines)

	var locations []int

	for _, seed := range seeds {
		locations = append(locations, mapVal(mapVal(mapVal(mapVal(mapVal(mapVal(mapVal(seed,s2s), s2f), f2w), w2l), l2t), t2h), h2l))
	}

	sort.Ints(locations)

	f.Println(locations)

}


func mapVal(value int, arr [][3]int) int {
	for _, subarr := range arr {
		if value >= subarr[1] && value < subarr[1] + subarr[2] {
			return subarr[0] + (value - subarr[1])
		} else { continue }
	}
	return value
}


func initializeArrays(lines []string) {
	category := ""

	for _, line := range lines {
		if line == "" {

		} else if str.HasPrefix(line, "seeds:") {
			seeds = str2int(str.Split(line, ":"))
		} else if str.HasSuffix(line, "map:") {
			category = str.Fields(line)[0]
		} else {
			ints := str2int(str.Fields(line))
			arrints := sliceintsto3ints(ints)

			switch category {
			case "seed-to-soil":
				s2s = append(s2s, arrints)
			case "soil-to-fertilizer":
				s2f = append(s2f, arrints)
			case "fertilizer-to-water":
				f2w = append(f2w, arrints)
			case "water-to-light":
				w2l = append(w2l, arrints)
			case "light-to-temperature":
				l2t = append(l2t, arrints)
			case "temperature-to-humidity":
				t2h = append(t2h, arrints)
			case "humidity-to-location":
				h2l = append(h2l, arrints)
			default:
				f.Println("You messed up bud. Category is", category, ".")
			}
		}
	}
}

func str2int(str []string) []int {
	var ints []int

	for _, s := range str {
		i, err := strconv.Atoi(s)
		if err != nil {
			f.Println("Error handling string", s)
		}
		ints = append(ints, i)
	}

	return ints
}

func sliceintsto3ints(ints []int) [3]int {
	var newints [3]int

	for i := 0; i < 3; i++ {
		newints[i] = ints[i]
	}

	return newints
}
