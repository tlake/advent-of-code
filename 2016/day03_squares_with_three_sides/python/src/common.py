"""Docstring."""


class Sorter():
    """."""

    def __init__(self, puzzle_input):
        """Init."""
        self.possible_triangles = 0
        self.triangles = []
        for line in puzzle_input:
            triplet = line.split()
            for i, item in enumerate(triplet):
                triplet[i] = int(item)
            triplet.sort()
            self.triangles.append(triplet)

    def find_possibles(self):
        """."""
        for triangle in self.triangles:
            if triangle[0] + triangle[1] > triangle[2]:
                self.possible_triangles += 1

        return self.possible_triangles
