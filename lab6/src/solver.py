import numpy as np

def euler_method(f, xi, y0, eps): 
    yi = [y0]
    h = xi[1] - xi[0] 
    for i in range(len(xi)):
        y_next = yi[i] + h * f(xi[i], yi[i])
        yi.append(y_next)
    return yi

def improved_euler_method(f, xi, y0, eps):
    yi = [y0]
    h = xi[1] - xi[0]
    for i in range(len(xi)):
        y_pred = f(xi[i], yi[i])
        y_corr = f(xi[i] + h, yi[i] + h * y_pred)
        yi.append(yi[i] + 0.5 * h * (y_pred + y_corr))
    return yi


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
