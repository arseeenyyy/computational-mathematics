# https://mathdf.com/dif/ru/# - точные решения для построения графика
from math import sin, cos, exp
import matplotlib.pyplot as plt

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
        except: 
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

