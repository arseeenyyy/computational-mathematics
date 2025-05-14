from math import sin, sqrt
from prettytable import PrettyTable

# разделенные разности для неравномерной сетки
def calculate_divided_differences(xi, yi):
    n = len(xi)
    table = [[0.0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        table[i][0] = yi[i]
    
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (xi[i+j] - xi[i])
    
    return table

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


def solve(xi, yi, x, n):
    if is_uniform_grid(xi):
        print("\nСетка равномерная")
        finite_diff_table = calculate_finite_differences(yi)
        print_finite_differences(xi, finite_diff_table)
    else:
        print("\nСетка неравномерная")
        divided_diff_table = calculate_divided_differences(xi, yi)
    
