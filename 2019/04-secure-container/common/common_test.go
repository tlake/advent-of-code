package common

import "testing"

type IntTestCase struct {
	PW       int
	Expected bool
}

type IntSliceTestCase struct {
	PW       []int
	Expected bool
}

func TestPasswordMeetsCriteriaA(t *testing.T) {
	testCases := []IntTestCase{
		IntTestCase{122345, true},
		IntTestCase{112233, true},
		IntTestCase{111122, true},
		IntTestCase{111123, true},
		IntTestCase{123444, true},
		IntTestCase{111111, true},
		IntTestCase{11122, false},
		IntTestCase{223450, false},
		IntTestCase{123789, false},
		IntTestCase{135679, false},
	}

	for _, testCase := range testCases {
		if result := PasswordMeetsCriteriaA(testCase.PW); result != testCase.Expected {
			t.Errorf("Password %d reported as %v when it should have been %v\n", testCase.PW, result, testCase.Expected)
		}
	}
}

func TestPasswordMeetsCriteriaB(t *testing.T) {
	testCases := []IntTestCase{
		IntTestCase{122345, true},
		IntTestCase{112233, true},
		IntTestCase{111122, true},
		IntTestCase{11122, false},
		IntTestCase{111123, false},
		IntTestCase{123444, false},
		IntTestCase{111111, false},
		IntTestCase{223450, false},
		IntTestCase{123789, false},
		IntTestCase{135679, false},
	}

	for _, testCase := range testCases {
		if result := PasswordMeetsCriteriaB(testCase.PW); result != testCase.Expected {
			t.Errorf("Password %d reported as %v when it should have been %v\n", testCase.PW, result, testCase.Expected)
		}
	}
}

func TestLengthIsCorrect(t *testing.T) {
	testCases := []IntSliceTestCase{
		IntSliceTestCase{[]int{1, 1, 1, 1, 1, 1}, true},
		IntSliceTestCase{[]int{1, 1, 1, 1, 1}, false},
		IntSliceTestCase{[]int{1, 1, 1, 1, 1, 1, 1}, false},
	}

	for _, testCase := range testCases {
		if result := LengthIsCorrect(testCase.PW); result != testCase.Expected {
			t.Errorf("Password %d reported as %v when it should have been %v\n", testCase.PW, result, testCase.Expected)
		}
	}
}

func TestHasAdjacentDuplicates(t *testing.T) {
	testCases := []IntSliceTestCase{
		IntSliceTestCase{[]int{1, 1, 2, 3, 4, 5}, true},
		IntSliceTestCase{[]int{1, 2, 3, 4, 5, 5}, true},
		IntSliceTestCase{[]int{1, 2, 2, 3, 2, 3}, true},
		IntSliceTestCase{[]int{1, 1, 2, 2, 3, 3}, true},
		IntSliceTestCase{[]int{1, 1, 1, 1, 2, 2}, true},
		IntSliceTestCase{[]int{1, 1, 1, 1, 1, 1}, true},
		IntSliceTestCase{[]int{1, 2, 3, 4, 4, 4}, true},
		IntSliceTestCase{[]int{1, 2, 3, 4, 5, 6}, false},
	}

	for _, testCase := range testCases {
		if result := HasAdjacentDuplicates(testCase.PW); result != testCase.Expected {
			t.Errorf("Password %d reported as %v when it should have been %v\n", testCase.PW, result, testCase.Expected)
		}
	}
}

func TestNeverDeccreases(t *testing.T) {
	testCases := []IntSliceTestCase{
		IntSliceTestCase{[]int{1, 1, 1, 1, 1, 1}, true},
		IntSliceTestCase{[]int{1, 2, 2, 3, 4, 5}, true},
		IntSliceTestCase{[]int{1, 1, 1, 1, 1, 2}, true},
		IntSliceTestCase{[]int{1, 2, 2, 2, 2, 2}, true},
		IntSliceTestCase{[]int{1, 2, 3, 2, 3, 4}, false},
		IntSliceTestCase{[]int{1, 0, 2, 3, 4, 5}, false},
		IntSliceTestCase{[]int{1, 2, 3, 4, 5, 4}, false},
	}

	for _, testCase := range testCases {
		if result := NeverDecreases(testCase.PW); result != testCase.Expected {
			t.Errorf("Password %d reported as %v when it should have been %v\n", testCase.PW, result, testCase.Expected)
		}
	}
}

func TestContainsDouble(t *testing.T) {
	testCases := []IntSliceTestCase{
		IntSliceTestCase{[]int{1, 1, 2, 3, 4, 5}, true},
		IntSliceTestCase{[]int{1, 2, 3, 4, 5, 5}, true},
		IntSliceTestCase{[]int{1, 2, 2, 3, 2, 3}, true},
		IntSliceTestCase{[]int{1, 1, 2, 2, 3, 3}, true},
		IntSliceTestCase{[]int{1, 1, 1, 1, 2, 2}, true},
		IntSliceTestCase{[]int{1, 1, 1, 1, 1, 1}, false},
		IntSliceTestCase{[]int{1, 2, 3, 4, 5, 6}, false},
		IntSliceTestCase{[]int{1, 2, 3, 4, 4, 4}, false},
	}

	for _, testCase := range testCases {
		if result := ContainsDouble(testCase.PW); result != testCase.Expected {
			t.Errorf("Password %d reported as %v when it should have been %v\n", testCase.PW, result, testCase.Expected)
		}
	}
}
