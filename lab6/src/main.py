# https://mathdf.com/dif/ru/# - точные решения для построения графика
from math import sin, cos, exp, inf
import matplotlib.pyplot as plt
from solver import euler_method, improved_euler_method, milne_method
import sys
from prettytable import PrettyTable

def select_odu():
    print("ОДУ:")
    print('1. y + (1 + x)*y^2')
    print('2. x + y')
    print('3. sin(x) - y')
    print('4. y / x')
    print('5. e^x\n')
    while True: 
        try: 
            option = int(input("Выберите ОДУ [1/2/3/4/5]: "))
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
            elif option == 4: 
                f = lambda x, y: y / x
                exact_y = lambda x, x0, y0: (x*y0) / x0
                break
            elif option == 5: 
                f = lambda x, y: exp(x)
                exact_y = lambda x, x0, y0: y0 - exp(x0) + exp(x)
                break
            else: 
                print("Некорректный ввод, попробуйте еще раз\n") 
        except ValueError: 
            print("Некорректный ввод, попробуйте еще раз\n") 
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


def solve(f, x0, xn, n, y0, exact_y, eps): 
    methods = [
        ("метод Эйлера", euler_method), 
        ("усовершенествованный метод Эйлера", improved_euler_method), 
        ("метод Милана", milne_method)
    ]
    for name, method in methods: 
        ni = n
        print(name + ":\n")
        try: 
            iters = 0
            xi = [x0 + i * ((xn - x0) / ni) for i in range(ni)]
            yi = method(f, xi, y0, eps)
            inaccuracy = inf
            while inaccuracy > eps: 
                if (iters >= 20): 
                    print(f"не удалось увеличить точность за {iters} итераций")
                    break;
                iters += 1
                ni *= 2
                xi = [x0 + i * (xn - x0) / ni for i in range(ni)]
                new_yi = method(f, xi, y0, eps)
                if method is milne_method:
                    inaccuracy = max([abs(exact_y(x, x0, y0) - y) for x, y in zip(xi, new_yi)])
                else: 
                    p = 2 
                    coef = 2 ** p - 1
                    inaccuracy = abs(new_yi[-1] - yi[-1]) / coef
                yi = new_yi.copy()
            
            if (iters != 1):
                print(f"Для точности eps={eps} интервал был разбит на n={ni} частей с шагом h={round((xn - x0) / ni, 6)} за {iters} итераций.\n")
            else:
                print(f"Для точности eps={eps} интервал был разбит на n={ni} частей с шагом h={round((xn - x0) / ni, 6)}.\n")
            print("y:\t[", *map(lambda x: round(x, 5), yi), "]")
            print("y_точн:\t[", *map(lambda x: round(exact_y(x, x0, y0), 5), xi), "]")
            print()
            if method is milne_method:
                print(f"Погрешность (max|y_iточн - y_i|): {inaccuracy}")
            else:
                print(f"Погрешность (по правилу Рунге): {inaccuracy}")
            print('-' * 30 + '\n')
            plt.figure(figsize=(10, 6))
            plt.title(name)
            
            draw_plot(xi[0], xi[-1], exact_y, x0, y0)
            plt.plot([], [], 'b-', label='Точное решение', color='blue')  
            
            for i in range(len(xi)):
                plt.scatter(xi[i], yi[i], c='red', label='Численное решение' if i == 0 else "")  
            
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.legend()
            plt.grid(True)
            plt.show()
        except OverflowError:
            print('-' * 30 + '\n')
            print("overflow error")

def get_number_input(str): 
    while True: 
        try: 
            user_input = input(str) 
            if user_input.lower == "quit": 
                sys.exit(0)
            return float(user_input)
        except ValueError:
            print("Некорректный ввод")

def get_input_params(): 
    while True: 
        try:
            print("\nВведите параметры (или 'quit' для выхода):")
            x0 = get_number_input('Введите первый элемент интервала x0: ')
            xn = get_number_input('Введите последний элемент интервала xn: ')
            
            if xn <= x0:
                print('Ошибка: xn должен быть больше x0.')
                continue
                
            n = int(get_number_input('Введите количество элементов в интервале n: '))
            if n <= 1:
                print('Ошибка: количество элементов n должно быть > 1.')
                continue
                
            y0 = get_number_input('Введите y0: ')
            eps = get_number_input('Введите точность eps: ')
            
            return x0, xn, n, y0, eps
            
        except KeyboardInterrupt:
            sys.exit(0)      


def main(): 
    f, exact_y = select_odu()
    x0, xn, n, y0, eps = get_input_params()
    solve(f, x0, xn, n, y0, exact_y, eps)

if __name__ == "__main__": 
    main()