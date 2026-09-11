"""
MATH 170 - Lab 3: Building a Half-Marathon Plan
Fall 2026

Built from lab03.ipynb by the build cell at the end of the notebook.
To change something: edit the task cell, run it, and run the build cell again.
"""

import math

def reached_goal(distance, goal, tol):
    """
    True if distance has reached goal, allowing for round-off.

    distance : miles actually covered
    goal     : miles you were aiming for
    tol      : how far apart the two may be and still count as equal
    """
    return abs(goal - distance) <= tol


def weeks_to_goal(start_miles, growth_pct, goal_miles):
    """
    Number of weeks of growth needed to reach goal_miles.

    start_miles : today's long run, in miles
    growth_pct  : percent added each week (10 means 10%)
    goal_miles  : the distance you are training for
    """
    #(i) Start_miles is the initial starting point, growth_pct is by how many percentiles the run lenght goes up every week,goal_miles is the end point of run lenght
    #(ii) growth_pct is repeated every week, since it is 10% growth every week
    #(iii) that goal_miles >= start_miles
    #(iv) it changes by 10%, changes by current_miles*(1+growth_pct)
    growth = growth_pct/100
    t = 0
    while goal_miles >= start_miles:
        start_miles += start_miles*growth
        t += 1



    return t


def weekly_plan(start_miles, growth_pct, weeks):
    """
    The long run for each week, as a list of miles.

    start_miles : today's long run, in miles
    growth_pct  : percent added each week (10 means 10%)
    weeks       : how many weeks the list should cover
    """
    plan = []
    t = 0
    while weeks > t:
        plan.append(start_miles)
        start_miles += start_miles*(growth_pct/100)
        t+=1
    return plan


def total_miles(plan):
    """
    Total mileage of a plan.

    plan : a list of weekly long-run distances
    """
    d = 0
    l = len(plan)
    for i in range(l):
        d += plan[i]
    return d
