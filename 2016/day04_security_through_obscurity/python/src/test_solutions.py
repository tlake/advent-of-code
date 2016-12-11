"""."""
import pytest

from solution1 import RoomAnalyzer as ra1
from solution2 import RoomAnalyzer as ra2


class TestPart1UnitTests:
    """."""

    @pytest.mark.parametrize("test_input, expected", [
        ("aaaaa-bbb-z-y-x-123[abxyz]", ("aaaaabbbzyx", 123, "abxyz")),
        ("a-b-c-d-e-f-g-h-987[abcde]", ("abcdefgh", 987, "abcde")),
        ("not-a-real-room-404[oarel]", ("notarealroom", 404, "oarel")),
        ("totally-real-room-200[decoy]", ("totallyrealroom", 200, "decoy"))
    ])
    def test_process_room_string(self, test_input, expected):
        """."""
        analyzer = ra1()
        assert(analyzer.process_room_string(test_input) == expected)

    @pytest.mark.parametrize("test_input, expected", [
        ("aaaaa-bbb-z-y-x-123[abxyz]", True),
        ("a-b-c-d-e-f-g-h-987[abcde]", True),
        ("not-a-real-room-404[oarel]", True),
        ("totally-real-room-200[decoy]", False)
    ])
    def test_room_is_real(self, test_input, expected):
        """."""
        analyzer = ra1()
        name, _, checksum = analyzer.process_room_string(test_input)
        assert(analyzer.room_is_real(name, checksum) == expected)

    @pytest.mark.parametrize("test_input, expected", [
        ("aaaaa-bbb-z-y-x-123[abxyz]", 123),
        ("a-b-c-d-e-f-g-h-987[abcde]", 987),
        ("not-a-real-room-404[oarel]", 404),
        ("totally-real-room-200[decoy]", 0)
    ])
    def test_analyze_room(self, test_input, expected):
        """."""
        analyzer = ra1()
        assert(analyzer.analyze_room(test_input) == expected)

    def test_analyze_input(self):
        """."""
        test_input = [
            "aaaaa-bbb-z-y-x-123[abxyz]",
            "a-b-c-d-e-f-g-h-987[abcde]",
            "not-a-real-room-404[oarel]",
            "totally-real-room-200[decoy]",
        ]
        expected = 1514
        analyzer = ra1(test_input)
        assert(analyzer.analyze_input() == expected)


class TestPart2UnitTests:
    """."""

    @pytest.mark.parametrize("test_input, expected", [
        (('a', 2), 'c'),
        (('a', 25), 'z'),
        (('a', 26), 'a'),
        (('z', 2), 'b'),
        (('a', 53), 'b'),
        ((' ', 2), ' ')
    ])
    def test__shift(self, test_input, expected):
        """."""
        analyzer = ra2()
        assert(analyzer._shift(test_input) == expected)

    def test_decipher(self):
        """."""
        test_input = ("qzmt zixmtkozy ivhz", 343)
        expected = "very encrypted name"
        analyzer = ra2()
        assert(analyzer.decipher(test_input[0], test_input[1]) == expected)
