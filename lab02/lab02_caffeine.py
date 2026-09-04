"""
MATH 170 - Lab 2: Caffeine in the Bloodstream
Fall 2026

This is the file that gets graded.

1. Work through lab02.ipynb and get each function working there.
2. Run the build cell near the end of the notebook. It collects your five
   functions and rewrites this file for you.
3. Run the check cell after it.
4. Commit, push to your own repository, and submit on Gradescope.

Changed your mind about an answer? Fix it in the notebook and run the build
cell again -- this file is rewritten from scratch each time.
"""

from math import log


def caffeine_remaining(dose_mg, hours, half_life):
    """
    Milligrams of caffeine remaining after a given number of hours.

    dose_mg    : milligrams taken in
    hours      : hours elapsed since the dose
    half_life  : half-life in hours (about 5 for caffeine)
    """
    # TODO: your code here
    return None


def dose_from_label(label_mg, servings):
    """
    Total caffeine in milligrams, from a label amount given as text.

    label_mg  : caffeine per serving, as a string, e.g. "95"
    servings  : how many servings, a number
    """
    # TODO: your code here
    return None


def report_line(hours, mg):
    """
    One row of a caffeine table, as a string.

    hours : hours since the dose
    mg    : milligrams remaining
    """
    # TODO: your code here
    return None


def hours_until(dose_mg, target_mg, half_life):
    """
    Hours until the caffeine level falls to target_mg.

    dose_mg    : milligrams taken in
    target_mg  : the level you are waiting for
    half_life  : half-life in hours
    """
    # TODO: your code here
    return None


def caffeine_at_bedtime(dose_mg, drink_hour, bed_hour, half_life):
    """
    Milligrams still present at bedtime.

    dose_mg     : milligrams taken in
    drink_hour  : hour of the drink, 24-hour clock (3 pm = 15)
    bed_hour    : hour you go to bed, 24-hour clock (11 pm = 23)
    half_life   : half-life in hours
    """
    # TODO: your code here
    return None
