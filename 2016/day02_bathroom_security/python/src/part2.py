#!/usr/bin/env python
"""Docstring."""

from common import (
    get_input,
    Urinator,
    StarKeypad,
)


def main():
    """Docstring."""
    urinator = Urinator(StarKeypad(), get_input())
    print(urinator.find_code())


if __name__ == "__main__":
    main()
