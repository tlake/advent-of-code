"""Docstring."""

import io


def get_input():
    """Docstring."""
    with io.open("./input.txt") as fh:
        puzzle_input = fh.read().splitlines()

    return [line for line in puzzle_input if line.strip() != '']


def blank_screen_array():
    """."""
    return [[' ' for x in range(50)] for x in range(6)]


def print_screen(screen_array):
    """."""
    print("+" + "-" * len(screen_array[0]) + "+")
    for row in screen_array:
        print("|" + ''.join(row) + "|")
    print("+" + "-" * len(screen_array[0]) + "+")
