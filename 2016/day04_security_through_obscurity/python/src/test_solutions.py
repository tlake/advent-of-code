"""."""
import pytest
from solution1 import RoomAnalyzer


class TestSolution1:
    """."""

    @pytest.mark.parametrize("test_input, expected", [
        ("aaaaa-bbb-z-y-x-123[abxyz]", ("aaaaabbbzyx", 123, "abxyz")),
        ("a-b-c-d-e-f-g-h-987[abcde]", ("abcdefgh", 987, "abcde")),
        ("not-a-real-room-404[oarel]", ("notarealroom", 404, "oarel")),
        ("totally-real-room-200[decoy]", ("totallyrealroom", 200, "decoy"))
    ])
    def test_process_room_string(self, test_input, expected):
        """."""
        analyzer = RoomAnalyzer()
        assert(analyzer.process_room_string(test_input) == expected)

    @pytest.mark.parametrize("test_input, expected", [
        ("aaaaa-bbb-z-y-x-123[abxyz]", True),
        ("a-b-c-d-e-f-g-h-987[abcde]", True),
        ("not-a-real-room-404[oarel]", True),
        ("totally-real-room-200[decoy]", False)
    ])
    def test_room_is_real(self, test_input, expected):
        """."""
        analyzer = RoomAnalyzer()
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
        analyzer = RoomAnalyzer()
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
        """."""
        analyzer = RoomAnalyzer(test_input)
        assert(analyzer.analyze_input() == expected)
