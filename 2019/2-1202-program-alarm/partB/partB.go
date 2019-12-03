package partB

import (
	"sync"

	"github.com/tlake/adventofcode2019/2-1202-program-alarm/common"
)

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

func Run(codeString string) int {
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
		c := common.NewIntCodeClient()
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
	return 100*success.A + success.B
}
