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
        self.locations = [(0, 0)]
        self.new_loc = (0, 0)

    def _listify_input(self, input_string):
        """Turn a string of inputs into a list."""
        stripped_string = re.sub(r'\s+', '', input_string.strip())
        split_list = stripped_string.split(",")
        return [(x[0], int(x[1::])) for x in split_list]

    def make_rotation(self, rotation):
        """Turn left or right, and update self.facing."""
        if rotation == "r":
            self.facing += 1
        else:
            self.facing -= 1

        if self.facing > 3:
            self.facing = self.facing - 4
        elif self.facing < 0:
            self.facing = self.facing + 4

    def take_step(self):
        """Move [steps] forward and update coordinates."""
        if self.facing == 0:
            self.new_loc = (self.new_loc[0], self.new_loc[1] + 1)
        elif self.facing == 1:
            self.new_loc = (self.new_loc[0] + 1, self.new_loc[1])
        elif self.facing == 2:
            self.new_loc = (self.new_loc[0], self.new_loc[1] - 1)
        else:
            self.new_loc = (self.new_loc[0] - 1, self.new_loc[1])

    def travel(self, steps):
        """."""
        step = 1
        while step <= steps:
            self.take_step()

            if self.new_loc in self.locations:
                return True
            else:
                self.locations.append(self.new_loc)
                step += 1

        return False

    def run(self):
        """Step through the directions list and return the distance."""
        for direction in self.directions:
            rotation = direction[0]
            steps = direction[1]

            self.make_rotation(rotation)
            hq_found = self.travel(steps)

            if hq_found:
                return (abs(self.new_loc[0] + self.new_loc[1]))


if __name__ == "__main__":
    walker = Walker(get_input())
    print(walker.run())
