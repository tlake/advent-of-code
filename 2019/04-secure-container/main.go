package main

import (
	"fmt"

	"github.com/tlake/adventofcode2019/04-secure-container/common"
	"github.com/tlake/adventofcode2019/04-secure-container/partA"
	"github.com/tlake/adventofcode2019/04-secure-container/partB"
)

func main() {
	input := common.GetInput()

	resultA := partA.Run(input)
	fmt.Printf("Part A result: %v\n", resultA)

	resultB := partB.Run(input)
	fmt.Printf("Part B result: %v\n", resultB)
}
