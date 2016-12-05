"""."""


class Button(object):
    """Shut up."""

    def __init__(self, number):
        """Shut up."""
        self.number = int(number)
        self.up, self.down, self.left, self.right = None, None, None, None


class Keypad(object):
    """Shut up."""

    def __init__(self):
        """Shup up."""
        two = Button(2)
        three = Button(3)
        four = Button(4)
        five = Button(5)
        six = Button(6)
        seven = Button(7)
        eight = Button(8)
        nine = Button(9)
        one = Button(1)
        one.up, one.down, one.left, one.right = one, four, one, two
        two.up, two.down, two.left, two.right = two, five, one, three
        three.up, three.down, three.left, three.right = three, six, two, three
        four.up, four.down, four.left, four.right = one, seven, four, five
        five.up, five.down, five.left, five.right = two, eight, four, six
        six.up, six.down, six.left, six.right = three, nine, five, six
        seven.up, seven.down, seven.left, seven.right = four, seven, seven, eight
        eight.up, eight.down, eight.left, eight.right = five, eight, seven, nine
        nine.up, nine.down, nine.left, nine.right = six, nine, eight, nine
        self.center = five


class Urinator(object):
    """Someone who really needs to pee.

    Presses the buttons in the right manner.
    """

    def __init__(self, keypad, instructions):
        """Init.

        'keypad' should be a graph-like Keypad object, as defined above.
        'instructions' should be a list of movements upon a keypad, with
            each number separated by a newline.
        """
        self.keypad = keypad
        self.instructions = instructions
        self.buttons_pressed = []

    def find_code(self):
        """."""
        combination = ''
        for i, line in enumerate(self.instructions):
            if i == 0:
                pos = self.keypad.center
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
            combination = combination + str(button.number)

        return combination


def main():
    """."""
    puzzle_input = """RRLLRLLRULLRUUUDRDLDDLLLDDDDDUUURRRRUUDLRULURRRDRUDRUUDDRUDLLLRLDDDUDRDDRRLLLLRLRLULUURDRURRUULDRRDUDURRUURURDLURULLDUDRDLUUUUDDURRLLLUDLDLRDRRRDULLDLDULLDRLDLDURDLRRULLDDLDRLLLUDDLLRDURULLDDDDDUURURLRLRRDUURUULRLLLULLRLULLUUDRRLLDURLDDDDULUUDLUDDDULRLDURDDRUUDRRUUURLLLULURUDRULDRDUDUDRRDDULRURLLRRLRRLLDLULURDRDRULDRDRURUDLLRRDUUULDDDUURDLULDLRLLURRURLLUDURDDRUDRDLLLLDLRLDLDDRDRRDUUULLUULRRDLURLDULLDLDUUUULLLDRURLRULLULRLULUURLLRDDRULDULRLDRRURLURUDLRRRLUDLDUULULLURLDDUDDLLUDRUDRLDUDURRRRLRUUURLUDDUDURDUDDDLLRLRDDURDRUUDUDRULURLRLDRULDRRLRLDDDRDDDRLDUDRLULDLUDLRLRRRLRDULDDLRRDDLDDULDLLDU
RULLUDDUDLULRRDLLDRUDLLLDURLLLURDURLRDRRDLRDRDLLURRULUULUDUDDLLRRULLURDRLDURDLDDUURLUURLDLDLRLDRLRUULDRLRLDRLRLUDULURDULLLDRUDULDURURRRUDURDUDLRDRRURULRRLRLRRRRRRDRUDLDRULDRUDLRDLRRUDULDLRLURRRLLDRULULRUDULRLULLRLULDRUDUULLRUULDULDUDDUUULLLDRDDRRDLURUUDRRLRRRDLRRLULLLLDLRUULDLLULURUURURDRURLLDUDRRURRURRUUDDRRDDRRRRUDULULRLUULRRDDRDDLLUDLDLULLRLDRLLUULDURLDRULDDUDRUUUURRLDDUDRUURUDLLDLDLURDLULDRLLLULLLUDLLDLD
RDLDULURDLULRRDLRLLLULRUULURULLLDLLDDRLLURUUUURDRLURLLRLRLLLULRDLURDURULULDDUDDUDRLRLDLULLURRRUULUDRDURRRUDDDLUDLDLRLRRLLLRUULLLLURRDDDRRRUURULRLDRRRLRLUDDRRULDDDRUUDDRLLDULRLUDUDLDLDDDUDDLLDDRDRDUDULDRRUDRDRRDRLUURDLRDDDULLDRRRRRUDRLURDUURRDDRLUDLURRRLRDDDLRRLUULRLURDUUURRDLDDULLLRURRRUDRLUDLLDDDDDUDDRDULLUUDDURRLULLUDULUUDRLDRRRLLURLRRLLDLLLLUDRUUUDDULLRDLLDUDUDUURRUUUDRUURDRDLLDLDDULLDDRRULDLDDUUURLDLULLLRRLLRDDULLDLDLDDLDLDULURRDURURDRDRRDLR
RDRLRRUUDRLDUDLLDLUDLUUDUDLRRUUDRDDDLDDLLLRRRUDULLRRRRRURRRLUDDDLRRRRUUULDURDRULLDLRURRUULUDRURRRRLRURLRDUUDUDUDRDDURRURUDLLLLLRURUULRUURLLURDRUURLUDDDRLDDURDLDUDRURDRLRRRRUURDDRRRRURDLUUDRLDRDUULURUDDULLURRDUDLUULLDURRURLUDUUDRDDDUUDDUUUULDLDUDDLUDUUDRURLLULRUUULLRRDDUDDLULDDUUUDLUDDLDDLLRUUDRULLRRDRLLDLLRRLULLRRDDRLRDUULLLUULLDLLUDUDDLRDULUDLDLUDDRRRRDUDLUULLULDLRRDLULRLRRRULRURRDRLULDDUDLDLDULLURLLRDLURRULURDLURLUDRDRRUUDRLLUDDRLRDDUURLRRDUDLDRURDUUUDRRLLRDLDLLDRRURLUDURUULDUDLDDDDRUULLDDRLRURRDURLURRLDDRRRRLRLRDRURUDDRDLDRURLULDDL
RULRDLDDLRURDDDDDDRURLLLDDDUUULLRRDLDLURUURLUDLURRLUDUURDULDRUULDDURULDUULDDULLLUDLRULDRLDLRDDRRDLDDLLDRRUDDUDRDUULUDLLLDDLUUULDDUUULRRDULLURLULDLRLLLRLURLLRLRLDRDURRDUUDDURRULDDURRULRDRDUDLRRDRLDULULDRDURDURLLLDRDRLULRDUURRUUDURRDRLUDDRRLDLDLULRLLRRUUUDDULURRDRLLDLRRLDRLLLLRRDRRDDLDUULRLRRULURLDRLRDULUDRDLRUUDDDURUDLRLDRRUDURDDLLLUDLRLURDUDUDULRURRDLLURLLRRRUDLRRRLUDURDDDDRRDLDDLLDLRDRDDRLLLURDDRDRLRULDDRRLUURDURDLLDRRRDDURUDLDRRDRUUDDDLUDULRUUUUDRLDDD"""
    split_input = puzzle_input.lower().split("\n")
    keypad = Keypad()
    urinator = Urinator(keypad, split_input)
    print(urinator.find_code())

if __name__ == "__main__":
    main()
