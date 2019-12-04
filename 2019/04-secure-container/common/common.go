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

func PasswordMeetsCriteriaA(password int) bool {
	slice := ConvertIntToIntSlice(password)

	if success := LengthIsCorrect(slice); !success {
		return false
	}

	if success := HasAdjacentDuplicates(slice); !success {
		return false
	}

	if success := NeverDecreases(slice); !success {
		return false
	}

	return true
}

func PasswordMeetsCriteriaB(password int) bool {
	slice := ConvertIntToIntSlice(password)

	if success := LengthIsCorrect(slice); !success {
		return false
	}

	if success := ContainsDouble(slice); !success {
		return false
	}

	if success := NeverDecreases(slice); !success {
		return false
	}

	return true
}

func ConvertIntToIntSlice(pw int) []int {
	var slice []int
	for pw != 0 {
		slice = append([]int{pw % 10}, slice...)
		pw = pw / 10
	}

	return slice
}

func LengthIsCorrect(pw []int) bool {
	return len(pw) == 6
}

func HasAdjacentDuplicates(pw []int) bool {
	var adjacencyFound bool

	for i := 0; i < len(pw)-1; i++ {
		if pw[i] == pw[i+1] {
			adjacencyFound = true
			break
		}
	}

	return adjacencyFound
}

func ContainsDouble(pw []int) bool {
	var doubleFound bool

	a, b := 0, 1
	for a < len(pw)-1 {
		for b < len(pw) && pw[a] == pw[b] {
			b++
		}

		if len(pw[a:b]) == 2 {
			doubleFound = true
		}

		if a < len(pw)-1 {
			a = b
			b = a + 1
		}
	}

	return doubleFound
}

func NeverDecreases(pw []int) bool {
	for i := 1; i < len(pw); i++ {
		if pw[i] < pw[i-1] {
			return false
		}
	}

	return true
}
