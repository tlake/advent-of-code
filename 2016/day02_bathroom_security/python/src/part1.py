#!/usr/bin/env python
"""Docstring."""

from common import (
    get_input,
    Urinator,
    ThreeByThreeKeypad,
)


def main():
    """Docstring."""
    urinator = Urinator(ThreeByThreeKeypad(), get_input())
    print(urinator.find_code())


if __name__ == "__main__":
    main()
