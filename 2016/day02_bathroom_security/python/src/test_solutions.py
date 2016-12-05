"""Tests."""


from common import ThreeByThreeKeypad, Urinator


class TestClass1:
    """Poop."""

    def test_that_i_know_what_a_keypad_looks_like(self):
        """."""
        kp = ThreeByThreeKeypad()
        assert(kp.center.number == 5)

        assert(kp.center.up.number == 2)
        assert(kp.center.up.up.number == 2)
        assert(kp.center.up.down.number == 5)
        assert(kp.center.up.left.number == 1)
        assert(kp.center.up.right.number == 3)

        assert(kp.center.down.number == 8)
        assert(kp.center.down.up.number == 5)
        assert(kp.center.down.down.number == 8)
        assert(kp.center.down.left.number == 7)
        assert(kp.center.down.right.number == 9)

        assert(kp.center.left.number == 4)
        assert(kp.center.left.up.number == 1)
        assert(kp.center.left.down.number == 7)
        assert(kp.center.left.left.number == 4)
        assert(kp.center.left.right.number == 5)

        assert(kp.center.right.number == 6)
        assert(kp.center.right.up.number == 3)
        assert(kp.center.right.down.number == 9)
        assert(kp.center.right.left.number == 5)
        assert(kp.center.right.right.number == 6)

        assert(kp.center.up.left.number == 1)
        assert(kp.center.up.left.up.number == 1)
        assert(kp.center.up.left.down.number == 4)
        assert(kp.center.up.left.left.number == 1)
        assert(kp.center.up.left.right.number == 2)

        assert(kp.center.up.right.number == 3)
        assert(kp.center.up.right.up.number == 3)
        assert(kp.center.up.right.down.number == 6)
        assert(kp.center.up.right.left.number == 2)
        assert(kp.center.up.right.right.number == 3)

        assert(kp.center.down.left.number == 7)
        assert(kp.center.down.left.up.number == 4)
        assert(kp.center.down.left.down.number == 7)
        assert(kp.center.down.left.left.number == 7)
        assert(kp.center.down.left.right.number == 8)

        assert(kp.center.down.right.number == 9)
        assert(kp.center.down.right.up.number == 6)
        assert(kp.center.down.right.down.number == 9)
        assert(kp.center.down.right.left.number == 8)
        assert(kp.center.down.right.right.number == 9)

    def test_example(self):
        """."""
        sample_input = """ULL
RRDDD
LURDL
UUUUD"""
        urinator = Urinator(ThreeByThreeKeypad(), sample_input.lower().split("\n"))
        assert(urinator.find_code() == '1985')
