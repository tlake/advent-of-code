package common

import (
	"bufio"
	"log"
	"os"
)

func GetInput() []string {
	file, err := os.Open("./input.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}

func PasswordMeetsCriteria(password int) bool {
	var slice []int
	for password != 0 {
		slice = append([]int{password % 10}, slice...)
		password = password / 10
	}

	if success := LengthIsCorrect(slice); !success {
		return false
	}

	if success := AdjacencyIsCorrect(slice); !success {
		return false
	}

	if success := NeverDecreases(slice); !success {
		return false
	}

	return true
}

func LengthIsCorrect(pw []int) bool {
	return len(pw) == 6
}

func AdjacencyIsCorrect(pw []int) bool {
	var adjacencyFound bool

	for i := 0; i < len(pw)-2; i++ {
		if pw[i] == pw[i+1] {
			adjacencyFound = true
		}
	}

	return adjacencyFound
}

func NeverDecreases(pw []int) bool {
	for i := 1; i < len(pw); i++ {
		if pw[i] < pw[i-1] {
			return false
		}
	}

	return true
}
