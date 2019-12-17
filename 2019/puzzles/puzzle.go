package puzzles

import (
	"fmt"
)

type PuzzleIface interface {
	PuzzleInfoIface
	PuzzleSolverIface
}

type PuzzleInfoIface interface {
	GetTitle() string
	GetSlug() string
}

type PuzzleSolverIface interface {
	Solve([]string) (ResultIface, error)
}

type ResultIface interface {
	Print()
}

// Puzzle is a partially-complete struct that will satisfy the PuzzleIface interface.
// By defining GetTitle() and GetSlug() as methods for the Puzzle receiver, the struct
// already implements the PuzzleInfoIface interface, and those methods make use of the
// struct's Title and Slug fields. When Puzzle is instantiated, an object which satisfies
// the PuzzleSolverIface interface must be provided. This is an object that supplies a
// Solve() method, and the implementation of this method is the greatest variance
// amongst puzzle solutions in this project.
type Puzzle struct {
	Title string
	Slug  string
	PuzzleSolverIface
}

func (p *Puzzle) GetTitle() string {
	return p.Title
}

func (p *Puzzle) GetSlug() string {
	return p.Slug
}

type Result struct {
	DayNum int
	Part1  string
	Part2  string
}

func (r *Result) Print() {
	fmt.Printf("Day %d results:\n", r.DayNum)
	fmt.Printf("Part 1: %s\n", r.Part1)
	fmt.Printf("Part 2: %s\n", r.Part2)
}
