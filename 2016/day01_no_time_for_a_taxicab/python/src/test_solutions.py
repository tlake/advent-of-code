"""Taxicab tests."""

from part1 import Walker as Walker1
from part2 import Walker as Walker2


class TestPart1:
    """."""

    def test_example(self):
        """."""
        sample_input = "R2, L3, L8"
        walker = Walker1(sample_input)
        assert(walker.run() == 9)


class TestPart2:
    """."""

    def test_example_1(self):
        """."""
        sample_input = "R8, R4, R4, R8"
        walker = Walker2(sample_input)
        assert(walker.run() == 4)

    def test_example_2(self):
        """."""
        sample_input = "R4, L4, L4, L3, L3, L2, L2, L1, L1, L1"
        walker = Walker2(sample_input)
        assert(walker.run() == 5)
        """
        START
            0,0
        E4      (R4)
            1,0
            2,0
            3,0
            4,0
        N4      (L4)
            4,1
            4,2
            4,3
            4,4
        W4      (L4)
            3,4
            2,4
            1,4
            0,4
        S3      (L3)
            0,3
            0,2
            0,1
        E3      (L3)
            1,1
            2,1
            3,1
        N2      (L2)
            3,2
            3,3
        W2      (L2)
            2,3
            1,3
        S1      (L1)
            1,2
        E1      (L1)
            2,2
        N1      (L1)
            2,3 <---- = 5 blocks away
        """
