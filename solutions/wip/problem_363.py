# By what percentage does the length of a Bezier curve approximating a quater circle actually differ from a quarter circle?

# NOT SOLVED

import math

v = 4 * (math.sqrt(2) - 1) / 3

p_0 = (1, 0)
p_1 = (1, v)
p_2 = (v, 1)
p_3 = (0, 1)

bezier_points = [p_0, p_1, p_2, p_3]

def error_percentage(length):
    return 100 * (length - math.pi) / math.pi

def bezier(points, t):
    return points[0] * (1 - t) ** 3 + 3 * (1 - t) ** 2 * t * points[1] + 3 * (1 - t) * t ** 2 * points[2] + points[3] * t ** 3
