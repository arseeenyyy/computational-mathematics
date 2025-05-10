import inspect
from math import sqrt, exp, log
import syi
import matplotlib.pyplot as plt

from matrix import solve_sle

def linear_approx(xi, yi, n): 
    sx = sum(xi)
    sxx = sum(x ** 2 for x in xi)
    sy = sum(yi)
    sxy = sum(x * y for x, y in zip(xi, yi))

    a, b = solve_sle(
        [
        [n, sx], 
        [sx, sxx]
        ], 
        [sy, sxy], 2)
    return lambda x: a + b * x, a, b

def quadratic_approx(xi, yi, n): 
    sx = sum(xi)
    sxx = sum(x ** 2 for x in xi)
    sxxx = sum(x ** 3 for x in xi)
    sxxxx = sum(x ** 4 for x in xi)
    sy = sum(yi)
    sxy = sum(x * y for x, y in zip(xi, yi))
    sxxy = sum(x * x * y for x, y in zip(xi, yi))
    a, b, c = solve_sle(
        [
            [n, sx, sxx],
            [sx, sxx, sxxx],
            [sxx, sxxx, sxxxx]
        ],
        [sy, sxy, sxxy],
        3
    )
    return lambda x: a + b * x + c * x ** 2, a, b, c

def cubic_approximation(xi, yi, n):
    sx = sum(xi)
    sxx = sum(x ** 2 for x in xi)
    sxxx = sum(x ** 3 for x in xi)
    sxxxx = sum(x ** 4 for x in xi)
    sxxxxx = sum(x ** 5 for x in xi)
    sxxxxxx = sum(x ** 6 for x in xi)
    sy = sum(yi)
    sxy = sum(x * y for x, y in zip(xi, yi))
    sxxy = sum(x * x * y for x, y in zip(xi, yi))
    sxxxy = sum(x * x * x * y for x, y in zip(xi, yi))
    a, b, c, d = solve_sle(
        [
            [n, sx, sxx, sxxx],
            [sx, sxx, sxxx, sxxxx],
            [sxx, sxxx, sxxxx, sxxxxx],
            [sxxx, sxxxx, sxxxxx, sxxxxxx]
        ],
        [sy, sxy, sxxy, sxxxy],
        4
    )
    return lambda xi: a + b * xi + c * xi ** 2 + d * xi ** 3, a, b, c, d
