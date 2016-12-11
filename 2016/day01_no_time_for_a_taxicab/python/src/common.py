"""Docstring."""

import io


def get_input():
    """Read input from a text file."""
    with io.open("./input.txt") as fh:
        puzzle_input = fh.read()

    return puzzle_input
