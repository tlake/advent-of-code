package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"regexp"
	"strings"

	"github.com/tlake/advent-of-code/2019/adventClient"
	"github.com/urfave/cli/v2"
)

func main() {
	adventClient := adventClient.NewAdventClient()

	app := &cli.App{
		Name:  "go-advent 2019",
		Usage: "Solutions to the 2019 Advent of Code, written in Golang.",
	}

	commands := GetCommands(adventClient)

	for _, command := range commands {
		app.Commands = append(app.Commands, command)
	}

	if err := app.Run(os.Args); err != nil {
		log.Fatal(err)
	}
}

func GetCommands(adventClient *adventClient.AdventClient) []*cli.Command {
	return []*cli.Command{
		{
			Name:    "list",
			Aliases: []string{"l"},
			Usage:   "list the days for which solutions have been found",
			Action: func(c *cli.Context) error {
				var titles []string

				for i := 1; i <= len(adventClient.Puzzles); i++ {
					key := fmt.Sprintf("day%d", i)
					title := adventClient.Puzzles[key].GetTitle()
					titles = append(titles, title)
				}

				for _, title := range titles {
					fmt.Println(title)
				}

				return nil
			},
		},
		{
			Name:    "solve",
			Aliases: []string{"s"},
			Usage:   "run the solution for the given day (format: day1)",
			Action: func(c *cli.Context) error {
				arg := c.Args().First()
				if err := CheckDayArg(arg); err != nil {
					return err
				}

				puzzle := adventClient.Puzzles[arg]

				slug := puzzle.GetSlug()
				input, err := GetInput(slug)
				if err != nil {
					return err
				}

				result, err := puzzle.Solve(input)
				if err != nil {
					return err
				}

				result.Print()
				return nil
			},
		},
		{
			Name:    "prompt",
			Aliases: []string{"p"},
			Usage:   "print out the day's prompt (format: day1)",
			Action: func(c *cli.Context) error {
				arg := c.Args().First()
				if err := CheckDayArg(arg); err != nil {
					return err
				}

				puzzle := adventClient.Puzzles[arg]
				slug := puzzle.GetSlug()
				prompt, err := GetPrompt(slug)
				if err != nil {
					return err
				}

				fmt.Println(prompt)
				return nil
			},
		},
	}
}

func CheckDayArg(arg string) error {
	var err error

	// make sure that the argument looks like "day1" or "day11"
	re := regexp.MustCompile(`^([a-z]{3})([0-9]{1,2})$`)
	if valid := re.MatchString(arg); !valid {
		errmsg := fmt.Sprintf("Argument to solve must be in the form of 'day1'\n(received '%s')", arg)
		err = errors.New(errmsg)
	}

	return err
}

func GetInput(slug string) ([]string, error) {
	var lines []string

	f := fmt.Sprintf("inputs/%s.txt", slug)
	file, err := os.Open(f)
	if err != nil {
		return []string{}, err
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines, nil
}

func GetPrompt(slug string) (string, error) {
	var prompt string

	f := fmt.Sprintf("prompts/%s.md", slug)
	file, err := os.Open(f)
	if err != nil {
		return "", err
	}

	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	prompt = strings.Join(lines, "\n")

	return prompt, nil
}
