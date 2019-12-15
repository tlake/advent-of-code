package puzzles

import "fmt"

type Day2Result struct {
	Part1 string
	Part2 string
}

func (r Day2Result) Print() {
	fmt.Println("Day 1 results:")
	fmt.Printf("Part 1: %s\n", r.Part1)
	fmt.Printf("Part 2: %s\n", r.Part2)
}

type Day2Puzzle struct{}

func NewDay2Puzzle() *Day2Puzzle {
	return &Day2Puzzle{}
}

func (p Day2Puzzle) Solve() (ResultIface, error) {
	return &Day2Result{}, nil
}

func (p Day2Puzzle) GetTitle() (string, error) {
	return "Day 2: 1202 Program Alarm", nil
}

func (p Day2Puzzle) GetPrompt() (string, error) {
	return "", nil
}
