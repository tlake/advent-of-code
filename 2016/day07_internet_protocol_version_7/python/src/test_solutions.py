"""Tests."""
import pytest

from part1 import TLSTester
from part2 import SSLTester


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
        tls_tester = TLSTester()
        assert(tls_tester.contains_abba(test_input) == expected)

    @pytest.mark.parametrize("test_input, expected", [
        (["abba", "mnop", "qrst"], True),
        (["abcd", "bdbd", "xyxy"], False),
        (["aaaa", "qwer", "tyui"], False),
        (["ioxxoj", "asdfgh", "zxcvbn"], True)
    ])
    def test_batch_contains_abba(self, test_input, expected):
        """."""
        tls_tester = TLSTester()
        assert(tls_tester.batch_contains_abba(test_input) == expected)

    @pytest.mark.parametrize("test_input, expected", [
        ("abba[mnop]qrst", True),
        ("abcd[bddb]xyyx", False),
        ("aaaa[qwer]tyui", False),
        ("ioxxoj[asdfgh]zxcvbn", True)
    ])
    def test_ip_supports_tls(self, test_input, expected):
        """."""
        tls_tester = TLSTester()
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
        tls_tester = TLSTester(test_input)
        assert(tls_tester.count_supported_ips() == expected)


class TestPart2UnitTests:
    """."""

    @pytest.mark.parametrize("test_input, expected", [
        ('aba', ['aba']),
        ('asdfdsa', ['dfd']),
        ('asdsdf', ['sds', 'dsd']),
        ('asdf', []),
        ('asdfffdsa', [])
    ])
    def test_find_aba(self, test_input, expected):
        """."""
        ssl_tester = SSLTester()
        assert(ssl_tester.find_aba(test_input) == expected)

    @pytest.mark.parametrize("test_input, expected", [
        ([], []),
        (['asdfdgh'], ['dfd']),
        (['asdsf', 'asdfd'], ['sds', 'dfd']),
        (['asds', 'asdfdfg'], ['sds', 'dfd', 'fdf'])
    ])
    def test_batch_find_aba(self, test_input, expected):
        """."""
        ssl_tester = SSLTester()
        assert(ssl_tester.batch_find_aba(test_input) == expected)

    @pytest.mark.parametrize("test_key, test_seq, expected", [
        ('aba', ['bab'], True),
        ('aba', ['aba', 'asdffssdsds', 'asdfs'], False),
        ('bab', ['suuebb', 'aeth', 'aaabaa'], True)
    ])
    def test_has_corresponding_bab(self, test_key, test_seq, expected):
        """."""
        ssl_tester = SSLTester()
        assert(ssl_tester.has_corresponding_bab(test_key, test_seq) == expected)

    @pytest.mark.parametrize("test_input, expected", [
        ('aba[bab]xyz', True),
        ('xyx[xyx]xyx', False),
        ('aaa[kek]eke', True),
        ('zazbz[bzb]cdb', True)
    ])
    def test_ip_supports_ssl(self, test_input, expected):
        """."""
        ssl_tester = SSLTester()
        assert(ssl_tester.ip_supports_ssl(test_input) == expected)

    def test_count_supported_ips(self):
        """."""
        test_input = [
            'aba[bab]xyz',
            'xyx[xyx]xyx',
            'aaa[kek]eke',
            'zazbz[bzb]cdb'
        ]
        expected = 3
        ssl_tester = SSLTester()
        assert(ssl_tester.count_supported_ips(test_input) == expected)
