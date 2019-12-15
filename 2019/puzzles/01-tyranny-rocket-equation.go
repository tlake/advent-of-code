package puzzles

import (
	"fmt"
	"strconv"
)

type Day1Result struct {
	Part1 string
	Part2 string
}

func (r Day1Result) Print() {
	fmt.Println("Day 1 results:")
	fmt.Printf("Part 1: %s\n", r.Part1)
	fmt.Printf("Part 2: %s\n", r.Part2)
}

type Day1Puzzle struct {
	Title string
	Slug  string
}

func NewDay1Puzzle() *Day1Puzzle {
	return &Day1Puzzle{
		Title: "Day 1: The Tyranny of the Rocket Equation",
		Slug:  "01-tyranny-rocket-equation",
	}
}

func (p Day1Puzzle) GetTitle() (string, error) {
	return p.Title, nil
}

func (p Day1Puzzle) GetSlug() (string, error) {
	return p.Slug, nil
}

func (p Day1Puzzle) Solve(input []string) (ResultIface, error) {
	var result Day1Result

	part1, err := p.day1part1(input)
	if err != nil {
		return nil, err
	}

	part2, err := p.day1part2(input)
	if err != nil {
		return nil, err
	}

	result.Part1 = fmt.Sprintf("%d", part1)
	result.Part2 = fmt.Sprintf("%d", part2)

	return result, nil
}

func (p Day1Puzzle) day1part1(input []string) (int, error) {
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
		fuelRequirements = append(fuelRequirements, calculateFuelMassOnly(mass))
	}

	for _, requirement := range fuelRequirements {
		sumFuelRequirements += requirement
	}

	return sumFuelRequirements, nil
}

// divide by 3, round down, subtract 2
// golang integer division is the same as decimal FLOOR(n/d)
func calculateFuelMassOnly(mass int) int {
	return (mass / 3) - 2
}

func (p Day1Puzzle) day1part2(input []string) (int, error) {
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
		fuelRequirements = append(fuelRequirements, calculateFuelIncludingFuel(mass))
	}

	for _, requirement := range fuelRequirements {
		sumFuelRequirements += requirement
	}

	return sumFuelRequirements, nil
}

func calculateFuelIncludingFuel(mass int) int {
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
