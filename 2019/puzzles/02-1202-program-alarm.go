package puzzles

import (
	"log"
	"strconv"
	"strings"
	"sync"
)

func NewDay2Puzzle() *Puzzle {
	return &Puzzle{
		Title:             "Day 2: 1202 Program Alarm",
		Slug:              "02-1202-program-alarm",
		PuzzleSolverIface: &Day2Solver{},
	}
}

type Day2Solver struct{}

func (s *Day2Solver) Solve(input []string) (ResultIface, error) {
	var result Result
	result.DayNum = 2

	part1, err := s.Part1(input[0])
	if err != nil {
		return nil, err
	}

	part2, err := s.Part2(input[0])
	if err != nil {
		return nil, err
	}

	result.Part1 = part1
	result.Part2 = part2

	return &result, nil
}

func (s *Day2Solver) Part1(codeString string) (string, error) {
	// before running the program:
	// replace position 1 with the value 12
	// replace position 2 with the value 2
	c := NewIntCodeClient()
	c.InitializeIntCode(codeString)
	c.IntCode[1] = 12
	c.IntCode[2] = 2

	c.ProcessIntCode()
	intSlice := c.GetIntCodeRaw()
	result := strconv.Itoa(intSlice[0])

	return result, nil
}

type Pair struct {
	A int
	B int
}

type Success struct {
	A          int
	B          int
	Result     int
	CodeString string
}

func (s *Day2Solver) Part2(codeString string) (string, error) {
	// find the pair of values for addresses 1 and 2
	// that cause the program to write 19690720 to address 0.
	// these two values will each be between 0 and 99 inclusive.
	// the answer to this puzzle is 100 * the value at address 1 plus
	// the value at address 2.

	var wg sync.WaitGroup

	successChan := make(chan Success, 2)
	defer close(successChan)

	check := func(pair Pair, codeString string, successChan chan<- Success, wg *sync.WaitGroup) {
		defer wg.Done()
		c := NewIntCodeClient()
		c.InitializeIntCode(codeString)
		c.IntCode[1] = pair.A
		c.IntCode[2] = pair.B
		c.ProcessIntCode()
		result := c.GetIntCodeRaw()

		if result[0] == 19690720 {
			successChan <- Success{pair.A, pair.B, result[0], c.GetIntCodeString()}
		}
	}

	for a := 0; a < 100; a++ {
		for b := 0; b < 100; b++ {
			pair := Pair{a, b}
			wg.Add(1)
			go check(pair, codeString, successChan, &wg)
		}

		wg.Wait()
		if len(successChan) > 0 {
			break
		}
	}

	success := <-successChan
	intResult := 100*success.A + success.B
	result := strconv.Itoa(intResult)

	return result, nil
}

type IntCodeClient struct {
	IntCode []int
}

func NewIntCodeClient() *IntCodeClient {
	return new(IntCodeClient)
}

func (c *IntCodeClient) InitializeIntCode(codeString string) {
	c.IntCode = []int{}
	splitCode := strings.Split(codeString, ",")
	for _, s := range splitCode {
		i, err := strconv.Atoi(s)
		if err != nil {
			log.Fatal("strconv error,", err)
		}

		c.IntCode = append(c.IntCode, i)
	}
}

func (c *IntCodeClient) ProcessIntCode() {
	var currentIndex int

	for currentIndex < len(c.IntCode) {
		opCode := c.IntCode[currentIndex]
		indices := c.IntCode[currentIndex+1 : currentIndex+4]

		switch {
		case opCode == 1:
			c.OpCode1(indices[0], indices[1], indices[2])
			currentIndex += 4
		case opCode == 2:
			c.OpCode2(indices[0], indices[1], indices[2])
			currentIndex += 4
		case opCode == 99:
			return
		default:
			log.Fatalf("Encountered unknown OpCode '%d' at index '%d'\nIntCode: %v\n", c.IntCode[currentIndex], currentIndex, c.IntCode)
			return
		}
	}
}

func (c *IntCodeClient) OpCode1(indexA, indexB, indexDest int) {
	result := c.IntCode[indexA] + c.IntCode[indexB]
	c.IntCode[indexDest] = result
}

func (c *IntCodeClient) OpCode2(indexA, indexB, indexDest int) {
	result := c.IntCode[indexA] * c.IntCode[indexB]
	c.IntCode[indexDest] = result
}

func (c *IntCodeClient) GetIntCodeRaw() []int {
	return c.IntCode
}

func (c *IntCodeClient) GetIntCodeString() string {
	var intStrings []string
	for _, i := range c.IntCode {
		intStrings = append(intStrings, strconv.Itoa(i))
	}

	return strings.Join(intStrings, ",")
}
