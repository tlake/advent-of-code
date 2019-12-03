#!/bin/bash

if [[ $# -ne 1 ]] ; then
    echo "This script needs to be called with an argument."
    echo "The argument is the name of the project to initialize."
    echo "Something like '01-tyranny-rocket-equation'."
    exit 1
fi

PROJECT_NAME=$1

REPO_NAME="github.com/tlake/adventofcode2019"

ADVENT_LOCATION=$(pwd)
PROJECT_LOCATION="${ADVENT_LOCATION}/${PROJECT_NAME}"

# create directories
mkdir -p \
    "${PROJECT_LOCATION}/common" \
    "${PROJECT_LOCATION}/partA" \
    "${PROJECT_LOCATION}/partB"

cd ${PROJECT_LOCATION}

touch "input.txt" "README.md"
go mod init "${REPO_NAME}/${PROJECT_NAME}"

cat << EOF > common/common.go
package common

import (
	"bufio"
	"log"
	"os"
)

func GetInput() []string {
	file, err := os.Open("./input.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}
EOF

cat << EOF > ./main.go
package main

import (
	"fmt"

	"${REPO_NAME}/${PROJECT_NAME}/common"
	"${REPO_NAME}/${PROJECT_NAME}/partA"
	"${REPO_NAME}/${PROJECT_NAME}/partB"
)

func main() {
	input := common.GetInput()

	resultA := partA.Run(input)
	fmt.Printf("Part A result: %v\n", resultA)

	resultB := partB.Run(input)
	fmt.Printf("Part B result: %v\n", resultB)
}
EOF

for part in partA partB ; do
    cat << EOF > ${part}/${part}.go ;
package ${part}

func Run(input []string) int {
    return len(input)
}
EOF

	cat << EOF > ${part}/${part}_test.go ;
package ${part}

import "testing"

func Test(t *testing.T) {

}
EOF

done

go mod tidy

cd ${ADVENT_LOCATION}
