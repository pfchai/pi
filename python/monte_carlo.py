# -*- coding: utf-8 -*-

import random
import numpy as np


def use_monte_carlo(num_points=10**6):
    points_inside_circle = 0
    total_points = num_points

    for _ in range(num_points):
        # Generate a random x-coordinate between -1 and 1
        x = random.uniform(-1, 1)
        # Generate a random y-coordinate between -1 and 1
        y = random.uniform(-1, 1)

        # Calculate the distance from the origin (0, 0)
        distance = x**2 + y**2

        # If the point falls inside the quarter circle
        if distance <= 1:
            points_inside_circle += 1

    pi_estimate = 4 * (points_inside_circle / total_points)
    return pi_estimate


def buffon(a, l, n):
    import math

    # a为平行线之间的长度,n实验次数,l针的长度
    k = 0
    m = 2 * l / a

    for _ in range(n):
        x = random.uniform(0, l/2)
        y = random.uniform(0, math.pi/2)
        if x < (a / 2) * np.sin(y):
            k += 1

    p = k / n
    return m / p


if __name__ == '__main__':
    print(use_monte_carlo())
    print(buffon(1, 1, 10**5))
