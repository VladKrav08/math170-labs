"""
MATH 170 - Lab 6: A Table for Any Formula
Fall 2026

This is the file that gets graded.

1. Work through lab06.ipynb and get each function working there.
2. Run the build cell near the end of the notebook. It collects your four
   functions and rewrites this file for you.
3. Run the check cell after it.
4. Commit, push to your own repository, and submit on Gradescope.

Changed your mind about an answer? Fix it in the notebook and run the build
cell again -- this file is rewritten from scratch each time.
"""

import sys
from math import *

def parse_args(argv):
    """
    The formula, a, b and n from a command line, returned as four values.

    argv : a list like sys.argv, e.g. ['tabulate.py', 'x**2', '0', '2', '4']
           -> 'x**2', 0.0, 2.0, 4
    """
    # TODO: your code here
    return None


def make_function(formula):
    """
    A function of x that evaluates formula.

    formula : a string with a formula in x, e.g. 'x**2 + 1' or 'sin(x)'
    """
    # TODO: your code here
    return None


def table(f, a, b, n):
    """
    The points x_0, ..., x_n splitting [a, b] into n equal steps, and the
    values f(x_k) at them, returned as two lists: xs, ys.

    f    : a function of one number
    a, b : the ends of the interval
    n    : the number of steps (there are n + 1 points)
    """
    # TODO: your code here
    return None


# Task 4 -- test_make_function(): you write the whole test function
# in the notebook, def line included.
