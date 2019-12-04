package common

import (
	"log"
	"math"
	"sort"
	"strconv"
	"strings"
)

type WireInstruction struct {
	Direction string
	Distance  int
}

type WireCoordinate struct {
	X     int
	Y     int
	Steps int
}

type WireClient struct {
	WireAInstructions []WireInstruction
	WireBInstructions []WireInstruction
	WireACoordinates  []WireCoordinate
	WireBCoordinates  []WireCoordinate
	WireCrossings     []WireCoordinate
}

func NewWireClient() *WireClient {
	return new(WireClient)
}

func (c *WireClient) InitializeWirePaths(pathStrings []string) {
	if len(pathStrings) != 2 {
		log.Fatal("Client requires two path strings.")
	}

	c.WireAInstructions = []WireInstruction{}
	c.WireBInstructions = []WireInstruction{}

	for i, pathString := range pathStrings {
		paths := strings.Split(pathString, ",")
		for _, path := range paths {
			direction := string(path[0])
			distance, err := strconv.Atoi(path[1:])
			if err != nil {
				log.Fatal("Strconv error: ", err)
			}

			instruction := WireInstruction{direction, distance}
			if i == 0 {
				c.WireAInstructions = append(c.WireAInstructions, instruction)
			} else {
				c.WireBInstructions = append(c.WireBInstructions, instruction)
			}
		}
	}
}

func (c *WireClient) ProcessInstructions() {
	c.TraceWirePaths()
	c.FindWireCrossings()
}

func (c *WireClient) TraceWirePaths() {
	processInstructions := func(instructionSet []WireInstruction) []WireCoordinate {
		coordinateSet := []WireCoordinate{WireCoordinate{0, 0, 0}}

		for _, instruction := range instructionSet {
			// D -> -y U -> +y
			// L -> -x R -> +x
			for i := 0; i < instruction.Distance; i++ {
				prev := coordinateSet[len(coordinateSet)-1]
				new := WireCoordinate{X: prev.X, Y: prev.Y, Steps: prev.Steps}

				switch instruction.Direction {
				case "U":
					new.Y++
				case "R":
					new.X++
				case "D":
					new.Y--
				case "L":
					new.X--
				}

				new.Steps++
				coordinateSet = append(coordinateSet, new)
			}
		}

		return coordinateSet[1:]
	}

	c.WireACoordinates = processInstructions(c.WireAInstructions)
	c.WireBCoordinates = processInstructions(c.WireBInstructions)
}

func (c *WireClient) FindWireCrossings() {
	var wireCrossings []WireCoordinate

	for _, a := range c.WireACoordinates {
		for _, b := range c.WireBCoordinates {
			if a.X == b.X && a.Y == b.Y {
				new := WireCoordinate{X: a.X, Y: a.Y, Steps: a.Steps + b.Steps}
				wireCrossings = append(wireCrossings, new)
			}
		}
	}

	c.WireCrossings = wireCrossings
}

func (c *WireClient) FindShortestDistance() int {
	distances := c.FindCrossingDistances()
	sort.Ints(distances)
	return distances[0]
}

func (c *WireClient) FindCrossingDistances() []int {
	var distances []int

	for _, crossing := range c.WireCrossings {
		distance := int(math.Abs(float64(crossing.X))) + int(math.Abs(float64(crossing.Y)))
		distances = append(distances, distance)
	}

	return distances
}

func (c *WireClient) FindFewestSteps() int {
	var steps []int

	for _, crossing := range c.WireCrossings {
		steps = append(steps, crossing.Steps)
	}

	sort.Ints(steps)
	return steps[0]
}
