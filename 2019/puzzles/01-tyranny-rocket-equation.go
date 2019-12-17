package puzzles

import (
	"fmt"
	"strconv"
)

func NewDay1Puzzle() *Puzzle {
	return &Puzzle{
		Title:             "Day 1: The Tyranny of the Rocket Equation",
		Slug:              "01-tyranny-rocket-equation",
		PuzzleSolverIface: &Day1Solver{},
	}
}

type Day1Solver struct{}

func (s *Day1Solver) Solve(input []string) (ResultIface, error) {
	var result Result
	result.DayNum = 1

	part1, err := s.Part1(input)
	if err != nil {
		return nil, err
	}

	part2, err := s.Part2(input)
	if err != nil {
		return nil, err
	}

	result.Part1 = fmt.Sprintf("%d", part1)
	result.Part2 = fmt.Sprintf("%d", part2)

	return &result, nil
}

func (s *Day1Solver) Part1(input []string) (int, error) {
	var moduleMasses []int
	var fuelRequirements []int
	var sumFuelRequirements int

	for _, a := range input {
		i, err := strconv.Atoi(a)
		if err != nil {
			return 0, err
		}

		moduleMasses = append(moduleMasses, i)
	}

	for _, mass := range moduleMasses {
		fuelRequirements = append(fuelRequirements, s.calculateFuelMassOnly(mass))
	}

	for _, requirement := range fuelRequirements {
		sumFuelRequirements += requirement
	}

	return sumFuelRequirements, nil
}

// divide by 3, round down, subtract 2
// golang integer division is the same as decimal FLOOR(n/d)
func (s *Day1Solver) calculateFuelMassOnly(mass int) int {
	return (mass / 3) - 2
}

func (s *Day1Solver) Part2(input []string) (int, error) {
	var moduleMasses []int
	var fuelRequirements []int
	var sumFuelRequirements int

	for _, a := range input {
		i, err := strconv.Atoi(a)
		if err != nil {
			return 0, err
		}

		moduleMasses = append(moduleMasses, i)
	}

	for _, mass := range moduleMasses {
		fuelRequirements = append(fuelRequirements, s.calculateFuelIncludingFuel(mass))
	}

	for _, requirement := range fuelRequirements {
		sumFuelRequirements += requirement
	}

	return sumFuelRequirements, nil
}

func (s *Day1Solver) calculateFuelIncludingFuel(mass int) int {
	var calculatedFuel int

	calculateLoop := func() {
		mass = (mass / 3) - 2
		if mass > 0 {
			calculatedFuel += mass
		}
	}

	for mass > 0 {
		calculateLoop()
	}

	return calculatedFuel
}
