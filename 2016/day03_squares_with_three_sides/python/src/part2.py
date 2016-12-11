#!/usr/bin/env python
"""Docstring."""

import io
from common import (
    Sorter,
)


def get_input(file_loc="./input.txt"):
    """Docstring."""
    with io.open(file_loc) as fh:
        puzzle_input = fh.read().splitlines()

    puzzle_input = [line for line in puzzle_input if line.strip() != '']
    first, second, third = [], [], []
    for line in puzzle_input:
        triplet = line.split()
        first.append(triplet[0])
        second.append(triplet[1])
        third.append(triplet[2])

    puzzle_input = first + second + third
    new_input = []
    for i, item in enumerate(puzzle_input):
        if i % 3 == 0:
            new_input.append("{} {} {}".format(
                puzzle_input[i],
                puzzle_input[i + 1],
                puzzle_input[i + 2]
            ))
    return new_input


def main():
    """Docstring."""
    puzzle_input = get_input()
    sorter = Sorter(puzzle_input)
    print(sorter.find_possibles())


if __name__ == "__main__":
    main()
