"""Tests."""
import pytest

from part1 import Decompressor as Decompressor1
# from part2 import Decompressor as Decompressor2


test_strings = [
    "ADVENT",
    "A(1x5)BC",
    "(3x3)XYZ",
    "A(2x2)BCD(2x2)EFG",
    "(6x1)(1x3)A",
    "X(8x2)(3x3)ABCY"
]

test_decoded_strings = [
    "ADVENT",
    "ABBBBBC",
    "XYZXYZXYZ",
    "ABCBCDEFEFG",
    "(1x3)A",
    "X(3x3)ABC(3x3)ABCY"
]


class TestPart1UnitTests:
    """."""

    @pytest.mark.parametrize(
        "test_input, expected",
        zip(test_strings, test_decoded_strings)
    )
    def test_decompress(self, test_input, expected):
        """."""
        d = Decompressor1()
        assert(d.decompress(test_input) == expected)


# class TestPart2UnitTests:
#     """."""
#
#     @pytest.mark.parametrize("test_input, expected", [
#         ('input', 'expect'),
#     ])
#     def test_method(self, test_input, expected):
#         """."""
#         pass
