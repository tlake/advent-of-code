"""Tests."""
import pytest

from part1 import PasswordFinder as PasswordFinder1
from part2 import PasswordFinder as PasswordFinder2


class TestPart1UnitTests:
    """."""

    @pytest.mark.parametrize("test_input, expected", [
        ('abc', '18f47a30'),
    ])
    def test_find_password(self, test_input, expected):
        """."""
        finder = PasswordFinder1()
        assert(finder.find_password(test_input) == expected)


class TestPart2UnitTests:
    """."""

    @pytest.mark.parametrize("test_input, expected", [
        ('abc', '05ace8e3'),
    ])
    def test_find_password(self, test_input, expected):
        """."""
        finder = PasswordFinder2()
        assert(finder.find_password(test_input) == expected)
