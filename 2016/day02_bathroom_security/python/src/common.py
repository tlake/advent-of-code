"""Docstring."""

import io


def get_input():
    """Docstring."""
    with io.open("./input.txt") as fh:
        puzzle_input = fh.read()

    sanitized_input = puzzle_input.lower().split("\n")
    sanitized_input = [line for line in sanitized_input if line.strip() != '']

    return sanitized_input


class Urinator(object):
    """Someone who really needs to pee.

    Presses the buttons in the right manner.
    """

    def __init__(self, keypad, instructions):
        """Init.

        'keypad' should be a graph-like Keypad object, as defined below.
        'instructions' should be a list of movements upon a keypad, with
            each value separated by a newline.
        """
        self.keypad = keypad
        self.instructions = instructions
        self.buttons_pressed = []

    def find_code(self):
        """Docstring."""
        combination = ''
        for i, line in enumerate(self.instructions):
            if i == 0:
                pos = self.keypad.start
            else:
                pos = self.buttons_pressed[-1]
            for char in line:
                if char == 'u':
                    pos = pos.up
                elif char == 'd':
                    pos = pos.down
                elif char == 'l':
                    pos = pos.left
                else:
                    pos = pos.right
            self.buttons_pressed.append(pos)

        for button in self.buttons_pressed:
            combination = combination + button.value

        return combination


class Button(object):
    """Docstring."""

    def __init__(self, value):
        """Docstring."""
        self.value = value
        self.up, self.down, self.left, self.right = None, None, None, None


class ThreeByThreeKeypad(object):
    """Docstring."""

    def __init__(self):
        """Docstring."""
        one = Button('1')
        two = Button('2')
        three = Button('3')
        four = Button('4')
        five = Button('5')
        six = Button('6')
        seven = Button('7')
        eight = Button('8')
        nine = Button('9')

        one.up, one.down, one.left, one.right = one, four, one, two
        two.up, two.down, two.left, two.right = two, five, one, three
        three.up, three.down, three.left, three.right = three, six, two, three
        four.up, four.down, four.left, four.right = one, seven, four, five
        five.up, five.down, five.left, five.right = two, eight, four, six
        six.up, six.down, six.left, six.right = three, nine, five, six
        seven.up, seven.down, seven.left, seven.right = four, seven, seven, eight
        eight.up, eight.down, eight.left, eight.right = five, eight, seven, nine
        nine.up, nine.down, nine.left, nine.right = six, nine, eight, nine

        self.start = five


class StarKeypad(object):
    """Docstring."""

    def __init__(self):
        """Docstring."""
        one = Button('1')
        two = Button('2')
        three = Button('3')
        four = Button('4')
        five = Button('5')
        six = Button('6')
        seven = Button('7')
        eight = Button('8')
        nine = Button('9')
        a = Button('A')
        b = Button('B')
        c = Button('C')
        d = Button('D')

        one.up, one.down, one.left, one.right = one, three, one, one
        two.up, two.down, two.left, two.right = two, six, two, three
        three.up, three.down, three.left, three.right = one, seven, two, four
        four.up, four.down, four.left, four.right = four, eight, three, four
        five.up, five.down, five.left, five.right = five, five, five, six
        six.up, six.down, six.left, six.right = two, a, five, seven
        seven.up, seven.down, seven.left, seven.right = three, b, six, eight
        eight.up, eight.down, eight.left, eight.right = four, c, seven, nine
        nine.up, nine.down, nine.left, nine.right = nine, nine, eight, nine
        a.up, a.down, a.left, a.right = six, a, a, b
        b.up, b.down, b.left, b.right = seven, d, a, c
        c.up, c.down, c.left, c.right = eight, c, b, c
        d.up, d.down, d.left, d.right = b, d, d, d

        self.start = five
