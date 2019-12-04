package common

import "testing"

func TestPasswordMeetsCriteria(t *testing.T) {
	passwords := map[int]bool{
		111111: true,
		223450: false,
		123789: false,
		122345: true,
		111123: true,
		135679: false,
	}

	for password, expected := range passwords {
		if result := PasswordMeetsCriteria(password); result != expected {
			t.Errorf("Password %d reported as %v when it should have been %v\n", password, result, expected)
		}
	}
}
