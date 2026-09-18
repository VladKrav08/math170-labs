"""
MATH 170 - Lab 4: A Month of Weather
Fall 2026

This is the file that gets graded.

1. Work through lab04.ipynb and get each function working there.
2. Run the build cell near the end of the notebook. It collects your five
   functions and rewrites this file for you.
3. Run the check cell after it.
4. Commit, push to your own repository, and submit on Gradescope.

Changed your mind about an answer? Fix it in the notebook and run the build
cell again -- this file is rewritten from scratch each time.
"""

import math


def to_celsius(temps_f):
    """
    The same temperatures in degrees Celsius, as a new list.

    temps_f : a list of temperatures in degrees Fahrenheit
    """
    # TODO: your code here
    return None


def daily_swing(highs, lows):
    """
    High minus low for each day, as a list.

    highs : a list of daily highs
    lows  : a list of daily lows, the same length as highs
    """
    # TODO: your code here
    return None


def corrected(readings, offset):
    """
    Return ONE list: a new list of the corrected temperatures, each one
    offset lower than the reading it came from.

    The raw readings are not part of what you return. `readings` itself must
    come out of this function exactly as it went in -- unchanged -- so that
    whoever called it still has the original numbers.

    readings : a list of temperatures, not to be modified
    offset   : how far too high the thermometer reads
    """
    # TODO: your code here
    return None


def month_mean(month):
    """
    Average of every temperature in a list of weeks.

    month : a list of lists; each inner list is one week of temperatures
    """
    # TODO: your code here
    return None


def split_week(week):
    """
    One week split into (weekdays, weekend).

    week : a list of seven values, Monday first
    """
    # TODO: your code here
    return None
