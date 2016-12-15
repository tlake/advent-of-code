#!/usr/bin/env python
"""Docstring."""

import re

from common import get_input


class Decompressor:
    """."""

    def __init__(self, compressed=None):
        """Initialize."""
        self.compressed = compressed if compressed else ''

    def decompress(self, compressed=None):
        """."""
        compressed = compressed if compressed else self.compressed
        decompressed, marker = [], re.search(r"\((\w+)\)", compressed)
        while marker:
            decompressed.append(compressed[:marker.start()])
            length, reps = [int(x) for x in marker.group()[1:-1].split('x')]
            decompressed.append(compressed[marker.end():marker.end() + length] * reps)
            compressed = compressed[marker.end() + length::]
            marker = re.search(r"\((\w+)\)", compressed)

        decompressed.append(compressed[0::])
        return ''.join(decompressed)


if __name__ == "__main__":
    d = Decompressor(get_input())
    print("Length of decompressed file: {}".format(len(d.decompress())))
