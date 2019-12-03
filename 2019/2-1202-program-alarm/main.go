package main

import (
	"fmt"

	"github.com/tlake/adventofcode2019/2-1202-program-alarm/common"
	"github.com/tlake/adventofcode2019/2-1202-program-alarm/partA"
	"github.com/tlake/adventofcode2019/2-1202-program-alarm/partB"
)

func main() {
	input := common.GetInput()
	codeString := input[0]

	resultA := partA.Run(codeString)
	fmt.Printf("Part A result: %v\n", resultA)

	resultB := partB.Run(codeString)
	fmt.Printf("Part B result: %v\n", resultB)
}
