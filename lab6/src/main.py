# https://mathdf.com/dif/ru/# - точные решения для построения графика
# значение щага с которым дошли до необходимой погрешности
from math import sin, cos, exp, inf
import matplotlib.pyplot as plt
from solver import euler_method, improved_euler_method, milne_method
import sys
from prettytable import PrettyTable

def select_odu():
    print("ODU")
    print('1. y\' = y + (1 + x)*y^2')
    print('2. y\' = x + y')
    print('3. y\' = sin(x) - y')
    while True: 
        try: 
            option = int(input("Select ODU [1/2/3]: "))
            if option == 1: 
                f = lambda x, y: y + (1 + x) * y ** 2
                exact_y = lambda x, x0, y0: -exp(x) / (x*exp(x) - (x0*exp(x0)*y0 + exp(x0)) / y0)
                break
            elif option == 2: 
                f = lambda x, y: x + y
                exact_y = lambda x, x0, y0: exp(x - x0) * (y0 + x0 + 1) - x - 1
                break
            elif option == 3: 
                f = lambda x, y: sin(x) - y
                exact_y = lambda x, x0, y0: (2*exp(x0)* y0-exp(x0)*sin(x0)+exp(x0)*cos(x0)) / (2*exp(x)) + (sin(x)) / 2 - (cos(x)) / 2
                break
            else: 
                print("Incorrect input, try again\n") 
        except ValueError: 
            print("Incorrect input, try again\n") 
    return f, exact_y

def draw_plot(a, b, func, x0, y0, dx=0.01):
    xs, ys = [], []
    a -= dx
    b += dx
    x = a
    while x <= b:
        xs.append(x)
        ys.append(func(x, x0, y0))
        x += dx
    plt.plot(xs, ys, 'g')

def get_input_params():
    while True:
        try:
            y0 = float(input("Initial condition (y_0): "))
            break
        except ValueError:
            print("Incorrect input, please enter a number")

    while True:
        try:
            x0 = float(input("x_0: "))
            xn = float(input("x_n: "))
            if x0 >= xn:
                print("Incorrect input, x_0 must be less than x_n, try again")
            else:
                break
        except ValueError:
            print("Incorrect input, please enter numbers")

    while True:
        try:
            h = float(input("h: "))
            if h <= 0:
                print("Incorrect input, h must be positive, try again")
            else:
                break
        except ValueError:
            print("Incorrect input, please enter a number")

    while True:
        try:
            eps = float(input("epsilon: "))
            if eps <= 0:
                print("Incorrect input, epsilon must be positive, try again")
            else:
                break
        except ValueError:
            print("Incorrect input, please enter a number")

    return y0, x0, xn, h, eps

def print_initial_data(y0, x0, xn, h, eps): 
    table = PrettyTable()
    table.field_names = ["y0", "x0", "xn", "h", "eps"] 
    table.add_row([y0, x0, xn, h, eps])
    print(table)

def main(): 
    f, exact_y = select_odu()
    y0, x0, xn, h, eps = get_input_params()
    print_initial_data(y0, x0, xn, h, eps)

if __name__ == "__main__": 
    main()