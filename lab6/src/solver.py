import numpy as np
from math import inf

def euler_method(f, xi, y0, eps): 
    yi = [y0]
    h = xi[1] - xi[0] 
    for i in range(len(xi)):
        y_next = yi[i] + h * f(xi[i], yi[i])
        yi.append(y_next)
    return yi

def fourth_order_runge_kutta_method(f, xs, y0, eps):
    ys = [y0]
    h = xs[1] - xs[0]
    for i in range(len(xs)):
        k1 = h * f(xs[i], ys[i])
        k2 = h * f(xs[i] + h / 2, ys[i] + k1 / 2)
        k3 = h * f(xs[i] + h / 2, ys[i] + k2 / 2)
        k4 = h * f(xs[i] + h, ys[i] + k3)
        ys.append(ys[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
    return ys



def milne_method(f, xi, y0, eps):
    n = len(xi)
    h = xi[1] - xi[0]
    y = [y0]
    for i in range(1, 4):
        k1 = h * f(xi[i - 1], y[i - 1])
        k2 = h * f(xi[i - 1] + h / 2, y[i - 1] + k1 / 2)
        k3 = h * f(xi[i - 1] + h / 2, y[i - 1] + k2 / 2)
        k4 = h * f(xi[i - 1] + h, y[i - 1] + k3)
        y.append(y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

    for i in range(4, n):
        yp = y[i - 4] + 4 * h * (2 * f(xi[i - 3], y[i - 3]) - f(xi[i - 2], y[i - 2]) + 2 * f(xi[i - 1], y[i - 1])) / 3

        y_next = yp
        while True:
            yc = y[i - 2] + h * (f(xi[i - 2], y[i - 2]) + 4 * f(xi[i - 1], y[i - 1]) + f(xi[i], y_next)) / 3
            if abs(yc - y_next) < eps:
                y_next = yc
                break
            y_next = yc

        y.append(y_next)

    return y

def runge_rule(y_prev, y_curr, p):
    return abs(y_curr - y_prev) / (2 ** p - 1)

def exact_accuracy(xs, ys, exact_y, x0, y0):
    return max(abs(exact_y(x, x0, y0) - y) for x, y in zip(xs, ys))