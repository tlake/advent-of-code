package partB

import (
	"github.com/tlake/adventofcode2019/04-secure-container/common"
	"log"
	"strconv"
	"strings"
)

func Run(input []string) int {
	strBounds := strings.Split(input[0], "-")
	lowerBound, err := strconv.Atoi(strBounds[0])
	if err != nil {
		log.Fatal("strconv error: ", err)
	}

	upperBound, err := strconv.Atoi(strBounds[1])
	if err != nil {
		log.Fatal("strconv error: ", err)
	}

	var successes []int
	for pw := lowerBound; pw <= upperBound; pw++ {
		result := common.PasswordMeetsCriteriaB(pw)
		if result {
			successes = append(successes, pw)
		}
	}

	return len(successes)
}
