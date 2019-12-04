package partB

import "testing"

func TestCalculateFuel(t *testing.T) {
	cases := map[int]int{
		12:     2,
		14:     2,
		1969:   966,
		100756: 50346,
	}

	for input, output := range cases {
		result := calculateFuel(input)
		if result != output {
			t.Errorf("Given input of %d, expected %d but result was %d", input, output, result)
		}
	}
}
