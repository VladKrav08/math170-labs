"""
MATH 170 - Lab 12: A Thanksgiving Kitchen
Fall 2026

This is the file that gets graded.

1. Work through lab12.ipynb and get each class working there.
2. Run the build cell near the end of the notebook. It collects your three
   classes and your test function and rewrites this file for you.
3. Run the check cell after it.
4. Commit, push to your own repository, and submit on Gradescope.

Changed your mind about an answer? Fix it in the notebook and run the build
cell again -- this file is rewritten from scratch each time.
"""

class Turkey:
    """A frozen turkey, thawing in the fridge."""

    def __init__(self, pounds):
        """
        A turkey of the given weight, straight from the freezer: it has
        thawed for 0 hours so far. Store the weight as _pounds and the
        hours of thawing as _hours.
        """
        # TODO: your code here
        return None

    def thaw(self, hours):
        """
        Record that the turkey spent this many more hours in the fridge:
        the hours it has thawed so far, _hours, go up by hours.
        thaw returns nothing -- it only changes the turkey. For example,
        a new turkey after thaw(24) and then thaw(24) has thawed 48 hours.
        """
        # TODO: your code here
        return None

    def hours_left(self):
        """
        Hours of thawing the turkey still needs: 6 hours per pound in all,
        minus the hours it has had so far. Never less than 0.
        """
        # TODO: your code here
        return None


class Pitcher:
    """A pitcher of iced tea."""

    def __init__(self, cups, sugar):
        """
        cups  : cups of tea in the pitcher
        sugar : teaspoons of sugar stirred into the whole pitcher
        Store them as _cups and _sugar.
        """
        # TODO: your code here
        return None

    def sweetness(self):
        """Teaspoons of sugar per cup."""
        # TODO: your code here
        return None

    def __add__(self, other):
        """
        The two pitchers poured together: a new Pitcher. Neither self
        nor other changes.
        """
        # TODO: your code here
        return None


class Thermometer:
    """A dial thermometer, corrected with two temperatures we know."""

    def __init__(self, read1, true1, read2, true2):
        """
        At the true temperature true1 the dial reads read1, and at true2 it
        reads read2. Store the slope and the shift of the straight line
        true = slope*reading + shift as _slope and _shift.
        """
        # TODO: your code here
        return None

    def __call__(self, reading):
        """The true temperature when the dial shows reading."""
        # TODO: your code here
        return None


def test_thermometer():
    """Check Thermometer on readings whose true temperature we know."""
    # TODO: your code here
    return None
