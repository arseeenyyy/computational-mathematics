import inspect
from math import sqrt, exp, log
import sys
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

