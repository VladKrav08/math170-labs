"""
MATH 170 - Lab 10: Heat in a Metal Rod
Fall 2026

This is the file that gets graded.

1. Work through lab10.ipynb and get each function working there.
2. Run the build cell near the end of the notebook. It collects your four
   functions and rewrites this file for you.
3. Run the check cell after it.
4. Commit, push to your own repository, and submit on Gradescope.

Changed your mind about an answer? Fix it in the notebook and run the build
cell again -- this file is rewritten from scratch each time.
"""

import numpy as np

def initial_temperature(x):
    """
    Temperature (degrees C) along the rod right after the torch:
    100 within 10 cm of the middle (|x - 50| <= 10), 20 everywhere else.
    Works for one position or a NumPy array of positions.

    x : position in cm, from 0 to 100, a number or an array
    """
    # TODO: your code here
    return None


def step(u, r):
    """
    The temperature along the rod one time step later.
    Returns a new array; u itself is left unchanged.

    u : NumPy array, the temperature at each point now
    r : the number in the update formula, between 0 and 0.5
    """
    # TODO: your code here
    return None


def simulate(u0, r, steps):
    """
    The temperature along the rod at the start and after each of steps
    time steps. Row k of the result is the temperature after k steps.

    u0    : array, the temperature at each point at the start
    r     : the number in the update formula, between 0 and 0.5
    steps : how many time steps to take
    """
    # TODO: your code here
    return None


def hot_zone(x, u, threshold):
    """
    Length in cm of the part of the rod hotter than threshold, from the
    first such point to the last one. 0.0 if no point is hotter.

    x         : array of positions along the rod, in cm
    u         : array of temperatures at those positions
    threshold : a temperature in degrees C
    """
    # TODO: your code here
    return None
