#!/usr/bin/env python
"""Docstring."""

from collections import Counter

from common import get_input


class ErrorCorrector:
    """."""

    def __init__(self, messages):
        """Initialize."""
        self.messages = messages
        self.columns = [''.join(x) for x in zip(*self.messages)]

    def correct(self):
        """."""
        return ''.join([Counter(x).most_common()[-1][0] for x in self.columns])

if __name__ == "__main__":
    ec = ErrorCorrector(get_input())
    print(ec.correct())
