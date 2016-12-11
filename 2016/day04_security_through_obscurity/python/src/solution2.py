#!/usr/bin/env python
"""Docstring."""

from collections import Counter

from common import get_input


class RoomAnalyzer:
    """."""

    def __init__(self, input_list=[]):
        """."""
        self.input_list = input_list

    def process_room_string(self, room_string):
        """."""
        name = room_string[:-11].replace("-", " ")
        sector_id = int(room_string[-10:-7])
        checksum = room_string[-6:-1]
        return name, sector_id, checksum

    def room_is_real(self, room_name, room_checksum):
        """."""
        counter = Counter(room_name.replace(" ", ""))
        checked = ''.join(map(lambda x: x[0], sorted(counter.most_common(), key=lambda x: (-x[1], x[0]))))[:5]
        return checked == room_checksum

    def _shift(self, char_and_shift):
        """."""
        char, amount = char_and_shift[0], char_and_shift[1] % 26
        if char == ' ':
            return char

        o = ord(char) + amount
        new = o if o < 123 else o - 26

        return chr(new)

    def decipher(self, room_name, shift):
        """."""
        room_name = room_name.lower()
        shift = shift % 26
        return ''.join(map(self._shift, [(x, shift) for x in room_name]))

    def analyze_room(self, room_string):
        """."""
        name, sector_id, checksum = self.process_room_string(room_string)
        return (self.decipher(name, sector_id), sector_id) if self.room_is_real(name, checksum) else None

    def analyze_input(self):
        """."""
        return list(filter(lambda x: x is not None and all([k in x[0] for k in ["north", "pole", "object", "storage"]]), map(self.analyze_room, self.input_list)))


if __name__ == "__main__":
    puzzle_input = get_input()
    analyzer = RoomAnalyzer(get_input())
    print(analyzer.analyze_input())
