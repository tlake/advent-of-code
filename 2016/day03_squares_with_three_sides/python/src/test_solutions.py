"""Tests."""

from solution1 import get_input as get_input_1
from solution2 import get_input as get_input_2


class TestPart1:
    """."""

    def test_input(self):
        """."""
        assert(get_input_1("./test_input.txt") == [
            '101 301 501',
            '102 302 502',
            '103 303 503',
            '201 401 601',
            '202 402 602',
            '203 403 603'
        ])


class TestPart2:
    """."""

    def test_input_rearrange(self):
        """."""
        assert(get_input_2("./test_input.txt") == [
            '101 102 103',
            '201 202 203',
            '301 302 303',
            '401 402 403',
            '501 502 503',
            '601 602 603'
        ])
