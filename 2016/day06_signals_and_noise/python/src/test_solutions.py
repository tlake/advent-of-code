"""Tests."""

from part1 import ErrorCorrector as ErrorCorrector1
from part2 import ErrorCorrector as ErrorCorrector2


class TestPart1UnitTests:
    """."""

    def test_correct(self):
        """."""
        test_input = [
            "eedadn",
            "drvtee",
            "eandsr",
            "raavrd",
            "atevrs",
            "tsrnev",
            "sdttsa",
            "rasrtv",
            "nssdts",
            "ntnada",
            "svetve",
            "tesnvt",
            "vntsnd",
            "vrdear",
            "dvrsen",
            "enarar",
        ]
        expected = "easter"
        ec = ErrorCorrector1(test_input)
        assert(ec.correct() == expected)


class TestPart2UnitTests:
    """."""

    def test_correct(self):
        """."""
        test_input = [
            "eedadn",
            "drvtee",
            "eandsr",
            "raavrd",
            "atevrs",
            "tsrnev",
            "sdttsa",
            "rasrtv",
            "nssdts",
            "ntnada",
            "svetve",
            "tesnvt",
            "vntsnd",
            "vrdear",
            "dvrsen",
            "enarar",
        ]
        expected = "advent"
        ec = ErrorCorrector2(test_input)
        assert(ec.correct() == expected)
