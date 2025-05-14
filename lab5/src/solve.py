from math import sin, sqrt, factorial
from prettytable import PrettyTable
from functools import reduce
import numpy as np

# разделенные разности для неравномерной сетки
# def calculate_divided_differences(xi, yi):
#     n = len(xi)
#     table = [[0.0 for _ in range(n)] for _ in range(n)]
    
#     for i in range(n):
#         table[i][0] = yi[i]
    
#     for j in range(1, n):
#         for i in range(n - j):
#             table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (xi[i+j] - xi[i])
    
#     return table

# вывод разделенных разностей
# def print_divided_differences(xi, table):
#     print("\nТаблица разделенных разностей (неравномерная сетка):")
#     pt = PrettyTable()
    
#     max_columns = len(xi)
    
#     headers = ["x_i", "y_i"]
#     for i in range(1, max_columns-1):
#         headers.append(f"{i}-я разн.")
#     pt.field_names = headers
    
#     for i in range(len(xi)):
#         row = [f"{xi[i]:.4f}", f"{table[i][0]:.6f}"]
        
#         for j in range(1, min(len(xi)-i, max_columns-1)):
#             row.append(f"{table[i][j]:.6f}")
        
#         while len(row) < len(headers):
#             row.append("")
            
#         pt.add_row(row)
    
#     print(pt)

# конечные разности 
def calculate_finite_differences(yi):
    n = len(yi)
    table = [[0.0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        table[i][0] = yi[i]
    
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i+1][j-1] - table[i][j-1]
    
    return table

# вывод конечных разностей
def print_finite_differences(xi, table):
    print("\nТаблица конечных разностей (равномерная сетка):")
    pt = PrettyTable()
    
    n = len(xi)
    headers = ["x_i", "y_i"] + [f"Δ^{i}y_i" for i in range(1, n)]
    pt.field_names = headers
    
    for i in range(n):
        row = [f"{xi[i]:.6f}", f"{table[i][0]:.6f}"]  # x_i и y_i
        
        for j in range(1, n - i):
            row.append(f"{table[i][j]:.6f}")
        
        row += [""] * (len(headers) - len(row))
        
        pt.add_row(row)
    
    pt.align = "r"
    pt.float_format = ".6"
    print(pt)

def is_uniform_grid(xi, tolerance=1e-6):
    if len(xi) < 2:
        return True
    
    h = xi[1] - xi[0]
    for i in range(1, len(xi)-1):
        if abs(xi[i+1] - xi[i] - h) > tolerance:
            return False
    return True

def lagrange_polynomial(xi, yi, n): 
    return lambda x: sum([
        yi[i] * reduce(
            lambda a, b: a * b,
                        [(x - xi[j]) / (xi[i] - xi[j])
            for j in range(n) if i != j])
        for i in range(n)])

def calculate_divided_differences(x, y):
    n = len(y)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    return coef


def newton_divided_difference_polynomial(xi, yi, n):
    coef = calculate_divided_differences(xi, yi)
    return lambda x: yi[0] + sum([
        coef[k] * reduce(lambda a, b: a * b, [x - xi[j] for j in range(k)]) for k in range(1, n)
    ])

def gauss_polynomial(xs, ys, n):
    n = len(xs) - 1
    alpha_ind = n // 2
    fin_difs = []
    fin_difs.append(ys[:])

    for k in range(1, n + 1):
        last = fin_difs[-1][:]
        fin_difs.append(
            [last[i + 1] - last[i] for i in range(n - k + 1)])

    h = xs[1] - xs[0]
    dts1 = [0, -1, 1, -2, 2, -3, 3, -4, 4]

    f1 = lambda x: ys[alpha_ind] + sum([
        reduce(lambda a, b: a * b,
               [(x - xs[alpha_ind]) / h + dts1[j] for j in range(k)])
        * fin_difs[k][len(fin_difs[k]) // 2] / factorial(k)
        for k in range(1, n + 1)])

    f2 = lambda x: ys[alpha_ind] + sum([
        reduce(lambda a, b: a * b,
               [(x - xs[alpha_ind]) / h - dts1[j] for j in range(k)])
        * fin_difs[k][len(fin_difs[k]) // 2 - (1 - len(fin_difs[k]) % 2)] / factorial(k)
        for k in range(1, n + 1)])

    return lambda x: f1(x) if x > xs[alpha_ind] else f2(x)

def solve(xi, yi, x, n):
    if is_uniform_grid(xi):
        print("\nСетка равномерная")
        finite_diff_table = calculate_finite_differences(yi)
        print_finite_differences(xi, finite_diff_table)
        print(lagrange_polynomial(xi, yi, n)(x))
        print(gauss_polynomial(x, xi, yi))
    else:
        print("\nСетка неравномерная")
        # divided_diff_table = calculate_divided_differences(xi, yi)
        print(lagrange_polynomial(xi, yi, n)(x))
        print(newton_divided_difference_polynomial(xi, yi, n)(x))
    
