package puzzles

import "testing"

func Test_calculateFuelMassOnly(t *testing.T) {
	cases := map[int]int{
		12:     2,
		14:     2,
		1969:   654,
		100756: 33583,
	}

	solver := &Day1Solver{}

	for input, output := range cases {
		result := solver.calculateFuelMassOnly(input)
		if result != output {
			t.Errorf("Given input of %d, expected %d but result was %d", input, output, result)
		}
	}
}

func Test_calculateFuelIncludingFuel(t *testing.T) {
	cases := map[int]int{
		12:     2,
		14:     2,
		1969:   966,
		100756: 50346,
	}

	solver := &Day1Solver{}

	for input, output := range cases {
		result := solver.calculateFuelIncludingFuel(input)
		if result != output {
			t.Errorf("Given input of %d, expected %d but result was %d", input, output, result)
		}
	}
}
