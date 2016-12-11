#!/usr/bin/env python
"""Find shortest taxicab distance."""

import re

from common import get_input


class Walker(object):
    """Class for turning walking directions into distance from start."""

    def __init__(self, input_string):
        """Initialize."""
        self.directions = self._listify_input(input_string.lower())
        self.steps = [0, 0, 0, 0]
        self.facing = 0

    def _listify_input(self, input_string):
        """Turn a string of inputs into a list."""
        stripped_string = re.sub(r'\s+', '', input_string.strip())
        split_list = stripped_string.split(",")
        return [(x[0], int(x[1::])) for x in split_list]

    def run(self):
        """Step through the directions list and return the distance."""
        for direction in self.directions:
            rotate = direction[0]
            steps = direction[1]
            if rotate == "r" and self.facing < 3:
                self.facing += 1
            elif rotate == 'r':
                self.facing = 0
            elif rotate == 'l' and self.facing > 0:
                self.facing -= 1
            else:
                self.facing = 3

            self.steps[self.facing] += steps

        return (
            abs(self.steps[0] - self.steps[2]) +
            abs(self.steps[1] - self.steps[3])
        )


if __name__ == "__main__":
    walker = Walker(get_input())
    print(walker.run())
