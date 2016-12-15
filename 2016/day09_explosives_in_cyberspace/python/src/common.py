"""Docstring."""

import io


def get_input():
    """Docstring."""
    with io.open("./input.txt") as fh:
        puzzle_input = fh.read()

    return puzzle_input
