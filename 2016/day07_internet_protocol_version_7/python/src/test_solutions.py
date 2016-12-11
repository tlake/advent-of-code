"""Tests."""
import pytest

from part1 import TLSTester as TLSTester1
# from part2 import TLSTester as TLSTester2


class TestPart1UnitTests:
    """."""

    @pytest.mark.parametrize("test_input, expected", [
        ("abba", True),
        ("abcd", False),
        ("aaaa", False),
        ("ioxxoj", True)
    ])
    def test_contains_abba(self, test_input, expected):
        """."""
        tls_tester = TLSTester1()
        assert(tls_tester.contains_abba(test_input) == expected)

    @pytest.mark.parametrize("test_input, expected", [
        (["abba", "mnop", "qrst"], True),
        (["abcd", "bdbd", "xyxy"], False),
        (["aaaa", "qwer", "tyui"], False),
        (["ioxxoj", "asdfgh", "zxcvbn"], True)
    ])
    def test_batch_contains_abba(self, test_input, expected):
        """."""
        tls_tester = TLSTester1()
        assert(tls_tester.batch_contains_abba(test_input) == expected)

    @pytest.mark.parametrize("test_input, expected", [
        ("abba[mnop]qrst", True),
        ("abcd[bddb]xyyx", False),
        ("aaaa[qwer]tyui", False),
        ("ioxxoj[asdfgh]zxcvbn", True)
    ])
    def test_ip_supports_tls(self, test_input, expected):
        """."""
        tls_tester = TLSTester1()
        assert(tls_tester.ip_supports_tls(test_input) == expected)

    def test_count_supported_ips(self):
        """."""
        test_input = [
            "abba[mnop]qrst",
            "abcd[bddb]xyyx",
            "aaaa[qwer]tyui",
            "ioxxoj[asdfgh]zxcvbn",
        ]
        expected = 2
        tls_tester = TLSTester1(test_input)
        assert(tls_tester.count_supported_ips() == expected)

# class TestPart2UnitTests:
#     """."""
#
#     @pytest.mark.parametrize("test_input, expected", [
#         ('input', 'expect'),
#     ])
#     def test_TLSTester(self, test_input, expected):
#         """."""
#         pass
