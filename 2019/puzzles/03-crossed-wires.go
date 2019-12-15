package puzzles

import "fmt"

type Day3Result struct {
	Part1 string
	Part2 string
}

func (r Day3Result) Print() {
	fmt.Println("Day 1 results:")
	fmt.Printf("Part 1: %s\n", r.Part1)
	fmt.Printf("Part 2: %s\n", r.Part2)
}

type Day3Puzzle struct{}

func NewDay3Puzzle() *Day3Puzzle {
	return &Day3Puzzle{}
}

func (p Day3Puzzle) Solve() (ResultIface, error) {
	return &Day2Result{}, nil
}

func (p Day3Puzzle) GetTitle() (string, error) {
	return "Day 3: Crossed Wires", nil
}

func (p Day3Puzzle) GetPrompt() (string, error) {
	return "", nil
}
