"""Docstring."""

import io


def get_input():
    """Docstring."""
    with io.open("./input.txt") as fh:
        puzzle_input = fh.read().splitlines()

    return [line for line in puzzle_input if line.strip() != '']
