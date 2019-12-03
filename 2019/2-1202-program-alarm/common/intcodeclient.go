package common

import (
	"log"
	"strconv"
	"strings"
)

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
