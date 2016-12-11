#!/usr/bin/env python
"""Docstring."""

import re
from collections import Counter

from common import get_input


class TLSTester:
    """."""

    def __init__(self, input_list=[]):
        """Initialize."""
        self.input_list = input_list

    def contains_abba(self, string):
        """."""
        i = 0
        while i < len(string) - 3:
            if (string[i] == string[i + 3] and
               string[i + 1] == string[i + 2] and
               string[i] != string[i + 1]):
                return True
            i += 1
        return False

    def batch_contains_abba(self, iterable):
        """."""
        return True in [self.contains_abba(x) for x in iterable]

    def ip_supports_tls(self, ip_string):
        """."""
        all_segments = re.split(r"\[(\w+)\]", ip_string)
        bracketed = re.findall(r"\[(\w+)\]", ip_string)
        unbracketed = [x for x in all_segments if x not in bracketed]
        return self.batch_contains_abba(unbracketed) and not self.batch_contains_abba(bracketed)

    def count_supported_ips(self, input_list=None):
        """."""
        input_list = input_list if input_list else self.input_list
        return Counter([self.ip_supports_tls(x) for x in input_list])[True]

if __name__ == "__main__":
    tester = TLSTester(get_input())
    print("Out of {} IPs, {} support TLS.".format(
        len(tester.input_list),
        tester.count_supported_ips()
    ))
