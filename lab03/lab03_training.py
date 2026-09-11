"""
MATH 170 - Lab 3: Building a Half-Marathon Plan
Fall 2026

This is the file that gets graded.

1. Work through lab03.ipynb and get each function working there.
2. Run the build cell near the end of the notebook. It collects your four
   functions and rewrites this file for you.
3. Run the check cell after it.
4. Commit, push to your own repository, and submit on Gradescope.

Changed your mind about an answer? Fix it in the notebook and run the build
cell again -- this file is rewritten from scratch each time.
"""

import math


def reached_goal(distance, goal, tol):
    """
    True if distance has reached goal, allowing for round-off.

    distance : miles actually covered
    goal     : miles you were aiming for
    tol      : how far apart the two may be and still count as equal
    """
    # TODO: your code here
    return None


def weeks_to_goal(start_miles, growth_pct, goal_miles):
    """
    Number of weeks of growth needed to reach goal_miles.

    start_miles : today's long run, in miles
    growth_pct  : percent added each week (10 means 10%)
    goal_miles  : the distance you are training for
    """
    # TODO: your code here
    return None


def weekly_plan(start_miles, growth_pct, weeks):
    """
    The long run for each week, as a list of miles.

    start_miles : today's long run, in miles
    growth_pct  : percent added each week (10 means 10%)
    weeks       : how many weeks the list should cover
    """
    # TODO: your code here
    return None


def total_miles(plan):
    """
    Total mileage of a plan.

    plan : a list of weekly long-run distances
    """
    # TODO: your code here
    return None
