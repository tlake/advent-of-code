package partA

import "github.com/tlake/adventofcode2019/2-1202-program-alarm/common"

func Run(codeString string) int {
	// before running the program:
	// replace position 1 with the value 12
	// replace position 2 with the value 2
	c := common.NewIntCodeClient()
	c.InitializeIntCode(codeString)
	c.IntCode[1] = 12
	c.IntCode[2] = 2

	c.ProcessIntCode()
	result := c.GetIntCodeRaw()
	return result[0]
}
