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

    return puzzle_input


def main():
    """Docstring."""
    puzzle_input = get_input()
    sorter = Sorter(puzzle_input)
    print(sorter.find_possibles())


if __name__ == "__main__":
    main()
