#!/usr/bin/env python
"""Docstring."""

from hashlib import md5

from common import get_input


class PasswordFinder(object):
    """."""

    def __init__(self):
        """Initialize."""
        self.integer = 0
        self.password = [None for x in range(8)]

    def get_digest(self, source):
        """."""
        return md5(source.encode()).hexdigest()

    def find_password(self, door_id):
        """."""
        while None in self.password:
            digest = self.get_digest(str(door_id) + str(self.integer))
            if digest[:5] == "00000":
                try:
                    i = int(digest[5])
                    if i < 8 and self.password[i] is None:
                        self.password[i] = digest[6]
                except ValueError:
                    pass

            self.integer += 1

        return ''.join(self.password)


if __name__ == "__main__":
    finder = PasswordFinder()
    print("Finding password for Door ID {}...".format(get_input()))
    print(finder.find_password(get_input()))
