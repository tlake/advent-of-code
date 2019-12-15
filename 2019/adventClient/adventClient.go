package adventClient

import (
	"github.com/tlake/advent-of-code/2019/puzzles"
)

type AdventClient struct {
	Puzzles map[string]puzzles.PuzzleIface
}

func NewAdventClient() *AdventClient {
	return &AdventClient{
		Puzzles: map[string]puzzles.PuzzleIface{
			"day1": puzzles.NewDay1Puzzle(),
			// "day2": puzzles.NewDay2Puzzle(),
			// "day3": puzzles.NewDay3Puzzle(),
			// "day4": puzzles.NewDay4Puzzle(),
		},
	}
}
