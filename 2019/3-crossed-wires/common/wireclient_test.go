package common

import "testing"

type ProblemSet struct {
	ID                 int
	InstructionStringA string
	InstructionStringB string
	Result             int
}

func TestShortestDistance(t *testing.T) {
	problemSets := []ProblemSet{
		ProblemSet{
			ID:                 0,
			InstructionStringA: "R8,U5,L5,D3",
			InstructionStringB: "U7,R6,D4,L4",
			Result:             6,
		},
		ProblemSet{
			ID:                 1,
			InstructionStringA: "R75,D30,R83,U83,L12,D49,R71,U7,L72",
			InstructionStringB: "U62,R66,U55,R34,D71,R55,D58,R83",
			Result:             159,
		},
		ProblemSet{
			ID:                 2,
			InstructionStringA: "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
			InstructionStringB: "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
			Result:             135,
		},
	}

	for _, problemSet := range problemSets {
		c := NewWireClient()
		c.InitializeWirePaths([]string{problemSet.InstructionStringA, problemSet.InstructionStringB})
		c.ProcessInstructions()
		result := c.FindShortestDistance()

		if result != problemSet.Result {
			t.Errorf("ProblemSet %d failure: Expected %d, got %d.\n", problemSet.ID, problemSet.Result, result)
		}
	}
}

func TestFewestSteps(t *testing.T) {
	problemSets := []ProblemSet{
		ProblemSet{
			ID:                 0,
			InstructionStringA: "R8,U5,L5,D3",
			InstructionStringB: "U7,R6,D4,L4",
			Result:             30,
		},
		ProblemSet{
			ID:                 1,
			InstructionStringA: "R75,D30,R83,U83,L12,D49,R71,U7,L72",
			InstructionStringB: "U62,R66,U55,R34,D71,R55,D58,R83",
			Result:             610,
		},
		ProblemSet{
			ID:                 2,
			InstructionStringA: "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
			InstructionStringB: "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
			Result:             410,
		},
	}

	for _, problemSet := range problemSets {
		c := NewWireClient()
		c.InitializeWirePaths([]string{problemSet.InstructionStringA, problemSet.InstructionStringB})
		c.ProcessInstructions()
		result := c.FindFewestSteps()

		if result != problemSet.Result {
			t.Errorf("ProblemSet %d failure: Expected %d, got %d.\n", problemSet.ID, problemSet.Result, result)
		}
	}
}
