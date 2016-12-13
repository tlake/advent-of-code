#!/usr/bin/env python
"""Docstring."""

from collections import Counter
from itertools import chain

from common import (
    get_input,
    blank_screen_array,
    print_screen
)


class ScreenSimulator:
    """."""

    def __init__(self, commands=None, screen=None):
        """Initialize."""
        self.commands = commands
        self.screen = blank_screen_array() if not screen else screen

    def print_screen(self):
        """."""
        print_screen(self.screen)

    def rect(self, a, b):
        """Turn on all pixels in top left of screen in rectangle <a> wide and <b> tall."""
        for ri, row in enumerate(self.screen):
            for ci, col in enumerate(row):
                if ci < a and ri < b:
                    self.screen[ri][ci] = '#'

    def rot_row(self, row, px):
        """."""
        px = px % len(self.screen[0])
        self.screen[row] = [x for x in self.screen[row][-px:] + self.screen[row][:-px]]

    def rot_col(self, col, px):
        """."""
        px = px % len(self.screen)
        flipped = [x for x in zip(*self.screen)]
        flipped[col] = flipped[col][-px:] + flipped[col][:-px]
        self.screen = [list(x) for x in zip(*flipped)]

    def parse_command(self, command_string):
        """."""
        cmd = command_string.split()
        if cmd[0] == "rect":  # rect 1x1
            self.rect(int(cmd[1].split("x")[0]), int(cmd[1].split("x")[1]))

        elif cmd[1] == "row":  # rotate row y=0 by 10
            self.rot_row(int(cmd[2][2:]), int(cmd[-1]))

        elif cmd[1] == "column":  # rotate column x=0 by 10
            self.rot_col(int(cmd[2][2:]), int(cmd[-1]))

    def process_commands(self, commands=None):
        """."""
        commands = commands if commands else self.commands
        for cmd in commands:
            self.parse_command(cmd)

    def count_pixels(self, screen=None):
        """."""
        screen = screen if screen else self.screen
        return Counter(list(chain.from_iterable(screen)))['#']


if __name__ == "__main__":
    s = ScreenSimulator(get_input())
    s.process_commands()
    s.print_screen()
    print("Number of illuminated pixels: {}".format(s.count_pixels()))
