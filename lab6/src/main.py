# https://mathdf.com/dif/ru/# - точные решения для построения графика
# значение щага с которым дошли до необходимой погрешности
from math import sin, cos, exp, inf
import matplotlib.pyplot as plt
from solver import euler_method, fourth_order_runge_kutta_method, milne_method, exact_accuracy, runge_rule
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

def solve(f, x0, xn, n, y0, exact_y, eps):
    print()
    methods = [("Euler method", euler_method),
               ("Fourth order runge kutta methid", fourth_order_runge_kutta_method),
               ("Milne method", milne_method)]

    for name, method in methods:
        ni = n
        print(name)

        try:
            iters = 0

            xs = [x0 + i * ((xn - x0) / ni) for i in range(ni)]
            ys = method(f, xs, y0, eps)
            inaccuracy = inf

            while inaccuracy > eps:
                if (iters >= 20):
                    print(f"Unable to reach epsilon within {iters}")
                    break

                iters += 1
                ni *= 2
                xs = [x0 + i * (xn - x0) / ni for i in range(ni)]
                new_ys = method(f, xs, y0, eps)

                if method is milne_method:
                    inaccuracy = max([abs(exact_y(x, x0, y0) - y) for x, y in zip(xs, new_ys)])
                else:
                    p = 4 if method is fourth_order_runge_kutta_method else 2
                    coef = 2**p - 1
                    inaccuracy = abs(new_ys[-1] - ys[-1]) / coef

                ys = new_ys.copy()
            if (iters != 1):
                print(f"epsilon: {eps}\ninterval was splitted in {ni} parts\nh: {round((xn - x0) / ni, 6)}\niterations: {iters}")
            else:
                print(f"epsilon: {eps}\ninterval was splitted in {ni} parts\nh: {round((xn - x0) / ni, 6)}")
            table = PrettyTable()
            exact_table = PrettyTable()
            table.field_names = ["x_i", "y_i"]
            for i in range(len(xs)): 
                table.add_row([xs[i], ys[i]])
            print(table)
            exact_table.field_names = ["x_i", "y_i"]
            for i in range(len(xs)): 
                exact_table.add_row([xs[i], exact_y(xs[i], x0, y0)])
            print(exact_table)

            print()
            if method is milne_method:
                print(f"Accuracy (max|y_i_exac - y_i|): {inaccuracy}\n")
                print("-" * 30)
            else:
                print(f"Accuracy (Runge rule): {inaccuracy}\n")
                print("-" * 30)

            plt.title(name)
            draw_plot(xs[0], xs[-1], exact_y, x0, y0)
            for i in range(len(xs)):
                plt.scatter(xs[i], ys[i], c='r')

            plt.xlabel("X")
            plt.ylabel("Y")
            plt.show()
        except OverflowError:
            print('-' * 30 + '\n')
def main(): 
    f, exact_y = select_odu()
    y0, x0, xn, h, eps = get_input_params()
    print_initial_data(y0, x0, xn, h, eps)
    print("-"*60)
    n = int((xn - x0) / h)
    solve(f, x0, xn, n, y0, exact_y, eps)

if __name__ == "__main__": 
    main()