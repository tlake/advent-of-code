package common

import (
	"testing"
)

func TestClientInitializeIntCode(t *testing.T) {
	c := NewIntCodeClient()

	expected := []int{1, 2, 3, 4, 5}
	c.InitializeIntCode("1,2,3,4,5")
	for i := range expected {
		if c.IntCode[i] != expected[i] {
			t.Errorf("Expected '%v', got '%v'.\n", expected, c.IntCode)
		}
	}
}

func TestClientProcessIntCode(t *testing.T) {
	c := NewIntCodeClient()

	cases := map[string]string{
		"1,0,0,0,99":          "2,0,0,0,99",
		"2,3,0,3,99":          "2,3,0,6,99",
		"2,4,4,5,99,0":        "2,4,4,5,99,9801",
		"1,1,1,4,99,5,6,0,99": "30,1,1,4,2,5,6,0,99",
	}

	for input, expected := range cases {
		c.InitializeIntCode(input)
		c.ProcessIntCode()
		output := c.GetIntCodeString()

		if output != expected {
			t.Errorf("Failure: Given input '%s', expected '%s' but got '%s'.\n", input, expected, output)
		}
	}
}
