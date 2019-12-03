package partB

import (
	"log"
	"strconv"
)

func calculateFuel(mass int) int {
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
