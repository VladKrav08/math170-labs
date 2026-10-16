"""
MATH 170 - Lab 8: Measuring g with a Pendulum
Fall 2026

This is the file that gets graded.

1. Work through lab08.ipynb and get each function working there.
2. Run the build cell near the end of the notebook. It collects your four
   functions and rewrites this file for you.
3. Run the check cell after it.
4. Commit, push to your own repository, and submit on Gradescope.

Changed your mind about an answer? Fix it in the notebook and run the build
cell again -- this file is rewritten from scratch each time.
"""

from math import *

def g_from(length, period):
    """
    The acceleration of gravity, in m/s**2, from one pendulum measurement.
    Raises ValueError if length or period is not positive.

    length : length of the pendulum in meters
    period : time of one full swing in seconds
    """
    # TODO: your code here
    return None


def parse_line(line):
    """
    The name, length and period on one line of the sign-up sheet,
    e.g. 'Ana;0.30;1.10' -> ('Ana', 0.3, 1.1).
    Raises IndexError if a value is missing, ValueError if one is not a number,
    each with a message that quotes the line.

    line : one line of the file, as the loop over the file gives it
    """
    # TODO: your code here
    return None


def read_measurements(filename):
    """
    g from every good line of a sign-up sheet file, and a message for every bad one.
    Returns two lists: g_values, problems.

    filename : the name of a file in the sign-up sheet's format,
               e.g. 'pendulum_data.txt'
    """
    # TODO: your code here
    return None


# Task 4 -- test_g_from(): you write the whole test function
# in the notebook, def line included.
