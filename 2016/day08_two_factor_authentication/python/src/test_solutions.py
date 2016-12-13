"""Tests."""

import pytest

from part1 import ScreenSimulator as ScreenSimulator1
# from part2 import ScreenSimulator as ScreenSimulator2


@pytest.fixture(scope="function")
def blank_screen():
    """."""
    return ScreenSimulator1(screen=[
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
    ])


@pytest.fixture(scope="function")
def two_by_two():
    """."""
    return ScreenSimulator1(screen=[
        ['#', '#', ' ', ' '],
        ['#', '#', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
    ])


class TestPart1UnitTests:
    """."""

    @pytest.mark.parametrize("test_width, test_height, expected", [
        (0, 0, [
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]),
        (2, 2, [
            ['#', '#', ' ', ' '],
            ['#', '#', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]),
        (4, 1, [
            ['#', '#', '#', '#'],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]),
        (1, 3, [
            ['#', ' ', ' ', ' '],
            ['#', ' ', ' ', ' '],
            ['#', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ])
    ])
    def test_rect(self, blank_screen, test_width, test_height, expected):
        """."""
        s = blank_screen
        s.rect(test_width, test_height)
        assert(s.screen == expected)

    @pytest.mark.parametrize("test_row, test_px, expected", [
        (1, 1, [
            ['#', '#', ' ', ' '],
            [' ', '#', '#', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]),
        (0, 0, [
            ['#', '#', ' ', ' '],
            ['#', '#', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]),
        (0, 4, [
            ['#', '#', ' ', ' '],
            ['#', '#', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]),
        (1, 3, [
            ['#', '#', ' ', ' '],
            ['#', ' ', ' ', '#'],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ])

    ])
    def test_rot_row(self, two_by_two, test_row, test_px, expected):
        """."""
        s = two_by_two
        s.rot_row(test_row, test_px)
        assert(s.screen == expected)

    @pytest.mark.parametrize("test_col, test_px, expected", [
        (1, 1, [
            ['#', ' ', ' ', ' '],
            ['#', '#', ' ', ' '],
            [' ', '#', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]),
        (0, 0, [
            ['#', '#', ' ', ' '],
            ['#', '#', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]),
        (0, 4, [
            ['#', '#', ' ', ' '],
            ['#', '#', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]),
        (1, 3, [
            ['#', '#', ' ', ' '],
            ['#', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', '#', ' ', ' ']
        ])

    ])
    def test_rot_col(self, two_by_two, test_col, test_px, expected):
        """."""
        s = two_by_two
        s.rot_col(test_col, test_px)
        assert(s.screen == expected)

# class TestPart2UnitTests:
#     """."""
#
#     @pytest.mark.parametrize("test_input, expected", [
#         ('input', 'expect'),
#     ])
#     def test_method(self, test_input, expected):
#         """."""
#         pass
