package partB

import "github.com/tlake/adventofcode2019/3-crossed-wires/common"

func Run(inputs []string) int {
	c := common.NewWireClient()
	c.InitializeWirePaths((inputs))
	c.ProcessInstructions()
	result := c.FindFewestSteps()
	return result
}
