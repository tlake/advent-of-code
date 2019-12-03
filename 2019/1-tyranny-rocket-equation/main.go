package main

import (
	"fmt"

	"github.com/tlake/adventofcode2019/1-tyranny-rocket-equation/common"
	"github.com/tlake/adventofcode2019/1-tyranny-rocket-equation/partA"
	"github.com/tlake/adventofcode2019/1-tyranny-rocket-equation/partB"
)

func main() {
	input := common.GetInput()

	resultA := partA.Run(input)
	fmt.Printf("Part A result: %v\n", resultA)

	resultB := partB.Run(input)
	fmt.Printf("Part B result: %v\n", resultB)
}
