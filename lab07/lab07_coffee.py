"""
MATH 170 - Lab 7: A Cooling Cup of Coffee
Fall 2026

This is the file that gets graded.

1. Work through lab07.ipynb and get each function working there.
2. Run the build cell near the end of the notebook. It collects your four
   functions and rewrites this file for you.
3. Run the check cell after it.
4. Commit, push to your own repository, and submit on Gradescope.

Changed your mind about an answer? Fix it in the notebook and run the build
cell again -- this file is rewritten from scratch each time.
"""

from math import *

def read_log(filename):
    """
    The readings in a logger file, as two lists of floats: minutes, temps.

    filename : the name of a file in the logger's format, e.g. 'coffee_log.txt'
    """
    # TODO: your code here
    return None


def write_table(filename, minutes, temps, model):
    """
    Write a file with a header line, then one line per reading:
    the minute, the measured temperature, and model(minute).

    filename : the file to write
    minutes  : list of times in minutes
    temps    : list of temperatures, one per minute
    model    : a function of the time in minutes
    """
    header = '   min  measured     model'
    # TODO: your code here
    return None


def add_to_logbook(filename, label, temps):
    """
    Add one line to the end of filename, e.g.
        Mug 1: 16 readings, 89.9 C to 38.7 C
    Whatever the file already holds stays there.

    filename : the logbook file
    label    : a name for this run, e.g. 'Mug 1'
    temps    : the list of temperatures measured in this run
    """
    # TODO: your code here
    return None


# Task 4 -- test_read_log(): you write the whole test function
# in the notebook, def line included.
