from math import factorial

def build_finite_differences_table(xi, yi):
    n = len(yi)
    table = []

    table.append(yi.copy())

    for k in range(1, n):
        current_diff = []
        for i in range(n - k):
            diff = table[k-1][i+1] - table[k-1][i]
            current_diff.append(diff)
        table.append(current_diff)

    return table

def print_finite_differences_table(xi, table):
    print("\nТаблица конечных разностей:")
    print("x_i\t\ty_i\t\tΔy_i\t\tΔ²y_i\t\t...\n")
    # print("-" * 100)

    n = len(xi)
    for i in range(n):
        row = [f"{xi[i]:.4f}"]
        for k in range(min(len(table), n - i)):
            row.append(f"{table[k][i]:.4f}")
        print("\t\t".join(row))

def lagrange_interpolation(xi, yi, x): 
    n = len(xi)
    result = 0.0
    
    for i in range(n):
        l_i = 1.0
        for j in range(n):
            if j != i:
                l_i *= (x - xi[j]) / (xi[i] - xi[j])
        result += yi[i] * l_i
    
    return result

def divided_differences(xi, yi):
    n = len(xi)
    coef = yi.copy()
    
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (xi[i] - xi[i-j])
    
    return coef

def newton_divided_difference(xi, yi, x):
    coef = divided_differences(xi, yi)
    n = len(xi)
    result = coef[0]
    
    for k in range(1, n):
        term = coef[k]
        for j in range(k):
            term *= (x - xi[j])
        result += term
    
    return result