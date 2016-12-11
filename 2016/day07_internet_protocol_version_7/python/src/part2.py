#!/usr/bin/env python
"""Docstring."""

import re
from functools import reduce
from collections import Counter

from common import get_input


class SSLTester:
    """."""

    def __init__(self, input_list=[]):
        """Initialize."""
        self.input_list = input_list

    def find_aba(self, seq):
        """Return list: all 'aba's found in the string <seq>."""
        i = 0
        abas = []
        while i < len(seq) - 2:
            if (seq[i] == seq[i + 2] and
               seq[i] != seq[i + 1]):
                abas.append(seq[i:i + 3])
            i += 1
        return abas

    def batch_find_aba(self, seqs):
        """Return list: all 'aba's found from all strings in <seqs>."""
        return reduce(lambda x, y: x + y, [self.find_aba(x) for x in seqs], [])

    def has_corresponding_bab(self, input_key, seqs):
        """Return bool: <key> exists for any string in <seqs>."""
        key = input_key[1::] + input_key[1]
        return True in [key in x for x in seqs]

    def ip_supports_ssl(self, ip_string):
        """Return bool: <ip_string> supports SSL.

        True:
            some string in <unbracketed> contains 'aba' pattern
            AND some string in <bracketed> contains matching 'bab' pattern
        """
        all_segments = re.split(r"\[(\w+)\]", ip_string)
        bracketed = re.findall(r"\[(\w+)\]", ip_string)
        unbracketed = [x for x in all_segments if x not in bracketed]
        return True in [self.has_corresponding_bab(x, bracketed) for x in self.batch_find_aba(unbracketed)]

    def count_supported_ips(self, input_list=None):
        """Return int: number of items in <input_list> which support SSL."""
        input_list = input_list if input_list else self.input_list
        return Counter([self.ip_supports_ssl(x) for x in input_list])[True]

if __name__ == "__main__":
    tester = SSLTester(get_input())
    print("Out of {} IPs, {} support SSL.".format(
        len(tester.input_list),
        tester.count_supported_ips()
    ))
