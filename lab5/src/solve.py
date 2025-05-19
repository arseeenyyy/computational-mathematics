from math import sin, sqrt, factorial
from prettytable import PrettyTable
from functools import reduce
import numpy as np
from matplotlib import pyplot as plt

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

def draw_plot(a, b, func, name, dx=0.001):
    xs, ys = [], []
    a -= dx
    b += dx
    x = a
    while x <= b:
        xs.append(x)
        ys.append(func(x))
        x += dx
    plt.plot(xs, ys, 'g', label=name)

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
    def L(x):
        total = 0.0
        n = len(xi)
        for i in range(n):
            l_i = 1.0
            for j in range(n):
                if j != i:
                    l_i *= (x - xi[j]) / (xi[i] - xi[j])
            total += yi[i] * l_i
        return total
    return L

def calculate_divided_differences(x, y):
    n = len(y)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    return coef


def newton_divided_difference_polynomial(xi, yi, n):
    coef = calculate_divided_differences(xi, yi)
    
    def poly(x):
        result = yi[0]  
        product = 1.0
        
        for k in range(1, len(xi)):
            product *= (x - xi[k-1])  
            result += coef[k] * product
            
        return result
    
    return poly

def gauss_polynomial(xs, ys, n):
    n_nodes = len(xs) - 1
    alpha_ind = n_nodes // 2
    fin_difs = [ys[:]]
    
    for k in range(1, n_nodes + 1):
        last = fin_difs[-1][:]
        fin_difs.append([last[i + 1] - last[i] for i in range(n_nodes - k + 1)])
    
    h = xs[1] - xs[0]
    
    dts1 = [0] + [(-1)**i * (i // 2 + 1) for i in range(1, n_nodes)]
    
    def f1(x):
        result = ys[alpha_ind]
        t = (x - xs[alpha_ind]) / h
        for k in range(1, n_nodes + 1):
            product = 1.0
            for j in range(k):
                product *= t + dts1[j]
            diff_index = len(fin_difs[k]) // 2
            result += product * fin_difs[k][diff_index] / factorial(k)
        return result
    
    def f2(x):
        result = ys[alpha_ind]
        t = (x - xs[alpha_ind]) / h
        for k in range(1, n_nodes + 1):
            product = 1.0
            for j in range(k):
                product *= t - dts1[j]
            diff_index = len(fin_difs[k]) // 2 - (1 if k % 2 == 1 else 0)
            if 0 <= diff_index < len(fin_difs[k]):
                result += product * fin_difs[k][diff_index] / factorial(k)
        return result
    
    return lambda x: f1(x) if x > xs[alpha_ind] else f2(x)

def stirling_polynomial(xs, ys, n):
    n = len(xs) - 1
    alpha_ind = n // 2
    fin_difs = [ys[:]]
    
    for k in range(1, n + 1):
        last = fin_difs[-1][:]
        fin_difs.append([last[i + 1] - last[i] for i in range(n - k + 1)])
    
    h = xs[1] - xs[0]
    dts1 = [0] + [(-1)**i * (i // 2 + 1) for i in range(1, n + 1)]
    
    def f1(x):
        result = ys[alpha_ind]
        t = (x - xs[alpha_ind]) / h
        for k in range(1, n + 1):
            product = 1.0
            for j in range(k):
                product *= t + dts1[j]
            diff_index = len(fin_difs[k]) // 2
            result += product * fin_difs[k][diff_index] / factorial(k)
        return result
    
    def f2(x):
        result = ys[alpha_ind]
        t = (x - xs[alpha_ind]) / h
        for k in range(1, n + 1):
            product = 1.0
            for j in range(k):
                product *= t - dts1[j]
            diff_index = len(fin_difs[k]) // 2 - (1 if k % 2 == 1 else 0)
            if 0 <= diff_index < len(fin_difs[k]):
                result += product * fin_difs[k][diff_index] / factorial(k)
        return result
    
    return lambda x: (f1(x) + f2(x)) / 2

def bessel_polynomial(xs, ys, n):
    n = len(xs) - 1
    alpha_ind = n // 2
    h = xs[1] - xs[0]
    
    fin_difs = [ys.copy()]
    for k in range(1, n + 1):
        fin_difs.append([fin_difs[k-1][i+1] - fin_difs[k-1][i] for i in range(n - k + 1)])
    
    def interpolate(x):
        t = (x - xs[alpha_ind]) / h
        result = (ys[alpha_ind] + ys[alpha_ind + 1]) / 2
        
        for k in range(1, min(n, len(fin_difs))):
            product = 1.0
            for j in range(k):
                m = (j + 1) // 2
                sign = -1 if j % 2 else 1
                product *= (t + sign * m)
            
            if k % 2 == 0:
                result += product * fin_difs[k][len(fin_difs[k])//2] / factorial(k)
            else:
                result += (t - 0.5) * product * fin_difs[k][len(fin_difs[k])//2] / factorial(k)
                
        return result
    
    return interpolate


def solve(xi, yi, x, n):
    uniform_grid = is_uniform_grid(xi)
    
    if uniform_grid:
        print("\nСетка равномерная")
        finite_diff_table = calculate_finite_differences(yi)
        print_finite_differences(xi, finite_diff_table)
        h = xi[1] - xi[0]  
        center_index = len(xi) // 2  
        a = xi[center_index]  
        t = (x - a) / h  
        print(f"Нормированный параметр t = {t:.4f}")
    else: 
        print("\nСетка неравномерная")
    print('\n' + '-' * 60)
    
    polynomials = []
    
    lagrange = lagrange_polynomial(xi, yi, n)
    polynomials.append(("Многочлен Лагранжа", lagrange))
    print("Многочлен Лагранжа:")
    print(f"P({x}) = {lagrange(x)}")
    print('-' * 60)
    
    if uniform_grid:
        if len(xi) % 2 == 1:  
            gauss = gauss_polynomial(xi, yi, n)
            polynomials.append(("Многочлен Гаусса", gauss))
            print("Многочлен Гаусса:")
            print(f"P({x}) = {gauss(x)}")
            print('-' * 60)
            print(f"Многочлен Бесселя не применяется: количество точек нечетное {n}")
            print('-' * 60)
            if abs(t) <= 0.25:
                stirling = stirling_polynomial(xi, yi, n)
                polynomials.append(("Многочлен Стирлинга", stirling))
                print("Многочлен Стирлинга (|t| <= 0.25):")
                print(f"P({x}) = {stirling(x)}")
                print('-' * 60)
            else:
                print("Многочлен Стирлинга не применяется (|t| > 0.25)")
                print('-' * 60)
                    
        else:  
            if 0.25 <= abs(t) <= 0.75:
                bessel = bessel_polynomial(xi, yi, n)
                polynomials.append(("Многочлен Бесселя", bessel))
                print("Многочлен Бесселя (0.25 <= |t| <= 0.75):")
                print(f"P({x}) = {bessel(x)}")
                print('-' * 60)
            else:
                print("Многочлен Бесселя не применяется (|t| < 0.25 или |t| > 0.75)")
                print('-' * 60)
    else:
        newton_divided = newton_divided_difference_polynomial(xi, yi, n)
        polynomials.append(("Многочлен Ньютона (раздел. разн.)", newton_divided))
        print("Многочлен Ньютона с разделенными разностями:")
        print(f"P({x}) = {newton_divided(x)}")
        print('-' * 60)
    
    for name, P in polynomials:
        plt.figure(figsize=(10, 6))
        draw_plot(xi[0], xi[-1], P, name)
        plt.title(f"Интерполяция ({name})")
        plt.xlabel("X")
        plt.ylabel("Y")
        for i in range(len(xi)):
            plt.scatter(xi[i], yi[i], c='b')
        plt.scatter(x, P(x), c='r', label=f"P({x}) = {P(x):.6f}")
        plt.legend()
        plt.grid(True)
        plt.show()