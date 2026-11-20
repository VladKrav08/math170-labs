"""
MATH 170 - Lab 13: How Fast Are the Days Getting Shorter?
Fall 2026

This is the file that gets graded.

1. Work through lab13.ipynb and get each class working there.
2. Run the build cell near the end of the notebook. It collects your classes
   and your test function and rewrites this file for you.
3. Run the check cell after it.
4. Commit, push to your own repository, and submit on Gradescope.

Changed your mind about an answer? Fix it in the notebook and run the build
cell again -- this file is rewritten from scratch each time.
"""

class Diff:
    """Base class for numerical derivatives: keeps the function f and the step h."""

    def __init__(self, f, h=1E-5):
        self.f, self.h = f, h

    def set_stepsize(self, h):
        self.h = h

    def values(self, xs):
        """
        The derivative at every point in the list xs, as a list: one number
        for each x, in the same order. It must work for every subclass, each
        with its own formula.
        """
        # TODO: your code here
        return None


class Forward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h


class Central2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)


class Backward1(Diff):
    """f'(x) from f(x) and f(x - h): one step back."""

    def __call__(self, x):
        """The backward-difference approximation of f'(x), with step self.h."""
        # TODO: your code here
        return None


class Richardson(Central2):
    """Two Central2 answers, with steps h and h/2, combined into a better one."""

    def __call__(self, x):
        """
        (4*D(h/2) - D(h))/3, where D(step) is Central2's answer with that step.
        Get each D with super().__call__(x), change the step with set_stepsize,
        and leave the step as it was before returning.
        """
        # TODO: your code here
        return None


def test_family():
    """Check every class in the family on a straight line, where each one is exact."""
    # TODO: your code here
    return None
