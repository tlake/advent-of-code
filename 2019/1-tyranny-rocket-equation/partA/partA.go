package partA

import (
	"log"
	"strconv"
)

// divide by 3, round down, subtract 2
// golang integer division is the same as decimal FLOOR(n/d)
func calculateFuel(mass int) int {
	return (mass / 3) - 2
}

func Run(input []string) int {
	var moduleMasses []int
	var fuelRequirements []int
	var sumFuelRequirements int

	for _, a := range input {
		i, err := strconv.Atoi(a)
		if err != nil {
			log.Fatal(err)
		}

		moduleMasses = append(moduleMasses, i)
	}

	for _, mass := range moduleMasses {
		fuelRequirements = append(fuelRequirements, calculateFuel(mass))
	}

	for _, requirement := range fuelRequirements {
		sumFuelRequirements += requirement
	}

	return sumFuelRequirements
}
