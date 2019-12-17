package puzzles

import (
	"strconv"
	"strings"
)

func NewDay4Puzzle() *Puzzle {
	return &Puzzle{
		Title:             "Day 2: Secure Container",
		Slug:              "04-secure-container",
		PuzzleSolverIface: &Day4Solver{},
	}
}

type Day4Solver struct{}

func (s *Day4Solver) Solve(input []string) (ResultIface, error) {
	var result Result
	result.DayNum = 4

	part1, err := s.Part1(input)
	if err != nil {
		return nil, err
	}

	part2, err := s.Part2(input)
	if err != nil {
		return nil, err
	}

	result.Part1 = part1
	result.Part2 = part2
	return &result, nil
}

func (s *Day4Solver) Part1(input []string) (string, error) {
	strBounds := strings.Split(input[0], "-")
	lowerBound, err := strconv.Atoi(strBounds[0])
	if err != nil {
		return "", nil
	}

	upperBound, err := strconv.Atoi(strBounds[1])
	if err != nil {
		return "", err
	}

	var successes []int
	for pw := lowerBound; pw <= upperBound; pw++ {
		result := PasswordMeetsCriteriaA(pw)
		if result {
			successes = append(successes, pw)
		}
	}

	intResult := len(successes)
	result := strconv.Itoa(intResult)

	return result, nil
}

func (s *Day4Solver) Part2(input []string) (string, error) {
	strBounds := strings.Split(input[0], "-")
	lowerBound, err := strconv.Atoi(strBounds[0])
	if err != nil {
		return "", nil
	}

	upperBound, err := strconv.Atoi(strBounds[1])
	if err != nil {
		return "", nil
	}

	var successes []int
	for pw := lowerBound; pw <= upperBound; pw++ {
		result := PasswordMeetsCriteriaB(pw)
		if result {
			successes = append(successes, pw)
		}
	}

	intResult := len(successes)
	result := strconv.Itoa(intResult)

	return result, nil
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
