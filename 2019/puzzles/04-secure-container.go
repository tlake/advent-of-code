package puzzles

import "fmt"

type Day4Result struct {
	Part1 string
	Part2 string
}

func (r Day4Result) Print() {
	fmt.Println("Day 1 results:")
	fmt.Printf("Part 1: %s\n", r.Part1)
	fmt.Printf("Part 2: %s\n", r.Part2)
}

type Day4Puzzle struct{}

func NewDay4Puzzle() *Day4Puzzle {
	return &Day4Puzzle{}
}

func (p Day4Puzzle) Solve() (ResultIface, error) {
	return &Day4Result{}, nil
}

func (p Day4Puzzle) GetTitle() (string, error) {
	return "Day 4: Secure Container", nil
}

func (p Day4Puzzle) GetPrompt() (string, error) {
	return "", nil
}
