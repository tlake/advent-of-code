#!/usr/bin/env python
"""Docstring."""

from collections import Counter
from functools import reduce
from common import (
    get_input,
)


class RoomAnalyzer:
    """."""

    def __init__(self, input_list=[]):
        """."""
        self.input_list = input_list

    def process_room_string(self, room_string):
        """."""
        name = room_string[:-11].replace("-", "")
        sector_id = int(room_string[-10:-7])
        checksum = room_string[-6:-1]
        return name, sector_id, checksum

    def room_is_real(self, room_name, room_checksum):
        """."""
        counter = Counter(room_name)
        checked = ''.join(map(lambda x: x[0], sorted(counter.most_common(), key=lambda x: (-x[1], x[0]))))[:5]
        return bool(checked == room_checksum)

    def analyze_room(self, room_string):
        """."""
        name, sector_id, checksum = self.process_room_string(room_string)
        return sector_id if self.room_is_real(name, checksum) else 0

    def analyze_input(self):
        """."""
        return reduce((lambda x, y: x + y), list(map(self.analyze_room, self.input_list)))


if __name__ == "__main__":
    puzzle_input = get_input()
    analyzer = RoomAnalyzer(get_input())
    print(analyzer.analyze_input())
