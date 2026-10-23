"""
MATH 170 - Lab 9: Hours of Daylight
Fall 2026

This is the file that gets graded.

1. Work through lab09.ipynb and get each function working there.
2. Run the build cell near the end of the notebook. It collects your four
   functions and rewrites this file for you.
3. Run the check cell after it.
4. Commit, push to your own repository, and submit on Gradescope.

Changed your mind about an answer? Fix it in the notebook and run the build
cell again -- this file is rewritten from scratch each time.
"""

import numpy as np
import matplotlib.pyplot as plt

def declination(day):
    """
    The declination of the sun, in degrees, on day number day
    (1 = January 1). Works for one day or a NumPy array of days.

    day : the day of the year, a number or an array
    """
    # TODO: your code here
    return None


def day_length(day, latitude):
    """
    Hours from sunrise to sunset on day number day, at the given latitude.
    Works for one day or a NumPy array of days.

    day      : the day of the year, a number or an array (1 = January 1)
    latitude : degrees north of the equator (negative for south),
               between -66 and 66
    """
    # TODO: your code here
    return None


# Task 3 -- daily_change(hours): you write the whole function
# in the notebook, def line included.


def plot_daylight(latitudes, names, styles, filename):
    """
    Plot the hours of daylight over a year for several cities in one figure,
    save it as filename, and show it.

    latitudes : list of latitudes in degrees, one per city
    names     : list of city names, used as legend labels
    styles    : list of Matplotlib line styles, e.g. ['b-', 'r--']
    filename  : the name of the image file, e.g. 'daylight.png'
    """
    # TODO: your code here
    return None
