"""Find shortest taxicab distance."""

import re


class Walker(object):
    """Class for turning walking directions into distance from start."""

    def listify_input(self):
        """Turn a string of inputs into a list."""
        stripped_string = re.sub(r'\s+', '', self.input_string.lower().strip())
        split_list = stripped_string.split(",")
        for item in split_list:
            self.input_list.append((item[0:1], int(item[1::])))

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
        for direction in self.input_list:
            rotation = direction[0]
            steps = direction[1]

            self.make_rotation(rotation)
            hq_found = self.travel(steps)

            if hq_found:
                return (abs(self.new_loc[0] + self.new_loc[1]))

    def __init__(self, input_string):
        """Initialize."""
        self.input_string = input_string
        self.input_list = []
        self.listify_input()
        self.facing = 0
        self.locations = [(0, 0)]
        self.new_loc = (0, 0)


def main():
    """Execute primary logic."""
    puzzle_input = "R2, L3, R2, R4, L2, L1, R2, R4, R1, L4, L5, R5, R5, R2, R2, R1, L2, L3, L2, L1, R3, L5, R187, R1, R4, L1, R5, L3, L4, R50, L4, R2, R70, L3, L2, R4, R3, R194, L3, L4, L4, L3, L4, R4, R5, L1, L5, L4, R1, L2, R4, L5, L3, R4, L5, L5, R5, R3, R5, L2, L4, R4, L1, R3, R1, L1, L2, R2, R2, L3, R3, R2, R5, R2, R5, L3, R2, L5, R1, R2, R2, L4, L5, L1, L4, R4, R3, R1, R2, L1, L2, R4, R5, L2, R3, L4, L5, L5, L4, R4, L2, R1, R1, L2, L3, L2, R2, L4, R3, R2, L1, L3, L2, L4, L4, R2, L3, L3, R2, L4, L3, R4, R3, L2, L1, L4, R4, R2, L4, L4, L5, L1, R2, L5, L2, L3, R2, L2"
    walker = Walker(puzzle_input)
    print(walker.run())

if __name__ == "__main__":
    main()
