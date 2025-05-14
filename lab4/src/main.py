import inspect
from math import sqrt, exp, log
import sys
import matplotlib.pyplot as plt

from matrix import solve_sle

def linear_approx(xi, yi, n): 
    sx = sum(xi)
    sxx = sum(x ** 2 for x in xi)
    sy = sum(yi)
    sxy = sum(x * y for x, y in zip(xi, yi))

    a, b = solve_sle(
        [
        [n, sx], 
        [sx, sxx]
        ], 
        [sy, sxy], 2)
    return lambda xi: a + b * xi, a, b

def quadratic_approx(xi, yi, n): 
    sx = sum(xi)
    sxx = sum(x ** 2 for x in xi)
    sxxx = sum(x ** 3 for x in xi)
    sxxxx = sum(x ** 4 for x in xi)
    sy = sum(yi)
    sxy = sum(x * y for x, y in zip(xi, yi))
    sxxy = sum(x * x * y for x, y in zip(xi, yi))
    a, b, c = solve_sle(
        [
            [n, sx, sxx],
            [sx, sxx, sxxx],
            [sxx, sxxx, sxxxx]
        ],
        [sy, sxy, sxxy],
        3
    )
    return lambda xi: a + b * xi + c * xi ** 2, a, b, c

def cubic_approximation(xi, yi, n):
    sx = sum(xi)
    sxx = sum(x ** 2 for x in xi)
    sxxx = sum(x ** 3 for x in xi)
    sxxxx = sum(x ** 4 for x in xi)
    sxxxxx = sum(x ** 5 for x in xi)
    sxxxxxx = sum(x ** 6 for x in xi)
    sy = sum(yi)
    sxy = sum(x * y for x, y in zip(xi, yi))
    sxxy = sum(x * x * y for x, y in zip(xi, yi))
    sxxxy = sum(x * x * x * y for x, y in zip(xi, yi))
    a, b, c, d = solve_sle(
        [
            [n, sx, sxx, sxxx],
            [sx, sxx, sxxx, sxxxx],
            [sxx, sxxx, sxxxx, sxxxxx],
            [sxxx, sxxxx, sxxxxx, sxxxxxx]
        ],
        [sy, sxy, sxxy, sxxxy],
        4
    )
    return lambda xi: a + b * xi + c * xi ** 2 + d * xi ** 3, a, b, c, d

def exponential_approximation(xs, ys, n):
    ys_ = list(map(log, ys))
    _, a_, b_ = linear_approx(xs, ys_, n)
    a = exp(a_)
    b = b_
    return lambda xi: a * exp(b * xi), a, b


def logarithmic_approximation(xs, ys, n):
    xs_ = list(map(log, xs))
    _, a_, b_ = linear_approx(xs_, ys, n)
    a = a_
    b = b_
    return lambda xi: a + b * log(xi), a, b


def power_approximation(xs, ys, n):
    xs_ = list(map(log, xs))
    ys_ = list(map(log, ys))
    _, a_, b_ = linear_approx(xs_, ys_, n)
    a = exp(a_)
    b = b_
    return lambda xi: a * xi ** b, a, b
# коэф корреляции Пирсона
def compute_correlation(x, y, n): 
    av_x = sum(x) / n
    av_y = sum(y) / n
    return sum((x - av_x) * (y - av_y) for x, y in zip(x, y)) / \
        sqrt(sum((x - av_x) ** 2 for x in x) * sum((y - av_y) ** 2 for y in y))
#СКО
def compute_mse(x, y, fi, n):
    return sqrt(sum(((fi(xi) - yi) ** 2 for xi, yi in zip(x, y))) / n)
#Мера отклонения
def compute_measure_of_deviation(x, y, fi, n):
    epss = [fi(xi) - yi for xi, yi in zip(x, y)]
    return sum((eps ** 2 for eps in epss))

def compute_coefficient_of_determination(xs, ys, fi, n):
    av_fi = sum(fi(x) for x in xs) / n
    return 1 - sum((y - fi(x)) ** 2 for x, y in zip(xs, ys)) / sum((y - av_fi) ** 2 for y in ys)

def get_str_content_of_func(func):
    str_func = inspect.getsourcelines(func)[0][0]
    return str_func.split('lambda xi: ')[-1].split(',')[0].strip().replace('xi', 'x')

def draw_plot(x, y):
    plt.scatter(x, y, label="Вводные точки")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Приближение функции различными методами")
    plt.show()

def draw_func(func, name, x, dx=0.001):
    a = x[0]
    b = x[-1]
    xs, ys = [], []
    a -= 0.1
    b += 0.1
    x = a
    while x <= b:
        xs.append(x)
        ys.append(func(x))
        x += dx
    plt.plot(xs, ys, label=name)

def get_coeffs_str(coeffs):
    if len(coeffs) == 2:
        return '(a, b)'
    if len(coeffs) == 3:
        return '(a, b, c)'
    if len(coeffs) == 4:
        return '(a, b, c, d)'
    return '(a, b, c, d, e)'


def run(functions, x, y, n):
    best_mse = float("inf")
    best_func = None

    mses = []

    for approximation, name in functions:
        try:
            fi, *coeffs = approximation(x, y, n)

            s = compute_measure_of_deviation(x, y, fi, n) # отклонение 
            mse = compute_mse(x, y, fi, n) # mse 
            r2 = compute_coefficient_of_determination(x, y, fi, n) # R^2

            if mse <= best_mse:
                mses.append((mse, name))
                best_mse = mse
                best_func = name

            draw_func(fi, name, x)

            print(f"{name} функция:")
            print(f"Функция: f(x) =", get_str_content_of_func(fi))
            print(f"Коэффициенты {get_coeffs_str(coeffs)}: {list(map(lambda cf: round(cf, 4), coeffs))}")
            print(f"Среднеквадратичное отклонение: σ = {mse:.5f}")
            if r2 >= 0.95:
                r2_status = 'высокая точность аппроксимации'
            elif r2 >= 0.75:
                r2_status = 'удовлетворительная точность аппроксимации'
            elif r2 >= 0.5:
                r2_status = 'слабая точность аппроксимации'
            else:
                r2_status = 'точность аппроксимации недостаточна'

            print(f"Коэффициент детерминации: R^2 = {r2:.5f}, ({r2_status})")
            print(f"Мера отклонения: S = {s:.5f}")
            if approximation == linear_approx:
                correlation = compute_correlation(x, y, n)
                rc = abs(correlation)
                if rc < 0.05:
                    pir_status = 'связь между переменными отсутствует'
                elif rc < 0.3:
                    pir_status = 'связь слабая'
                elif rc < 0.5:
                    pir_status = 'связь умеренная'
                elif rc < 0.7:
                    pir_status = 'связь заметная'
                elif rc < 0.9:
                    pir_status = 'связь высокая'
                elif rc <= 0.99:
                    pir_status = 'связь весьма высокая'
                else:
                    pir_status = 'строгая линейная функциональная зависимость'

                print(f"Коэффициент корреляции Пирсона: r = {correlation}, ({pir_status})")

        except Exception as e:
            print(f"Ошибка приближения {name} функции: {e}\n")

        print(('-' * 30) + '\n')

    best_funcs = []
    for m, n in mses:
        if abs(m - best_mse) < 0.0000001:
            best_funcs.append(n)

    if len(best_funcs) == 1:
        print(f"Лучшая функция приближения: {best_func}")
    else:
        print(f"Лучшие функции приближения:")
        for n in best_funcs:
            print(f'{n}')

    draw_plot(x, y)


def read_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            x = []
            y = []
            for line in file:
                point = line.strip().split()
                if len(point) == 2:
                    x.append(float(point[0]))
                    y.append(float(point[1]))

        return x, y, None
    except IOError as err:
        return None, None, "! Невозможно прочитать файл {0}: {1}".format(filename, err)

def read_data_from_input():
    x = []
    y = []
    while True:
        user_input = input()
        if user_input.lower() == 'quit':
            break
            
        point = user_input.strip().split()
        if len(point) != 2:
            print("! Неправильный ввод. Введенная точка не будет использована.")
            continue
            
        try:
            x_val = float(point[0])
            y_val = float(point[1])
            x.append(x_val)
            y.append(y_val)
        except ValueError:
            print(f"! Ошибка преобразования чисел в строке '{user_input}'. Введенная точка не будет использована.")
    
    return x, y

def main():
    print("'f' - file\n't' - terminal\n")
    while True:
        print("Введите способ задания данных: [f/t]: ")
        option = input("")
        if option == 'f':
            while True:
                filename = input("Введите имя файла: ")
                x, y, error = read_data_from_file(filename)
                if error != None:
                    print(error)
                    one_more_time = input("Вы хотите попробовать другое имя файла? [y/n]: ")
                    if one_more_time == 'y':
                        continue
                    else:
                        print('Ввод с клавиатуры:')
                        print('Введите \'quit\', чтобы закончить ввод')
                        x, y = read_data_from_input()
                else:
                    n = len(x)
                    if n < 8 or n > 12:
                        print(f"! Ошибка: количество точек должно быть от 8 до 12. В вашем файле {n} точек.")
                        continue
                    break
            break
        elif option == 't':
            while True:
                print("Введите 'quit', чтобы закончить ввод")
                x, y = read_data_from_input()
                n = len(x)
                if n < 8:
                    print(f"! Ошибка: введено слишком мало точек ({n}). Минимум 8 точек.")
                    print("Пожалуйста, введите точки снова:")
                    continue
                elif n > 12:
                    print(f"! Ошибка: введено слишком много точек ({n}). Максимум 12 точек.")
                    print("Пожалуйста, введите точки снова:")
                    continue
                else:
                    break
            break
        else:
            print("! Некорректный ввод. Попробуйте еще раз")

    if all(map(lambda xi: xi > 0, x)):
        if all(map(lambda yi: yi > 0, y)):
            functions = [
                (linear_approx,             "Линейная"),
                (quadratic_approx,          "Полиноминальная 2-й степени"),
                (cubic_approximation,        "Полиноминальная 3-й степени"),
                (exponential_approximation,  "Экспоненциальная"),
                (logarithmic_approximation,  "Логарифмическая"),
                (power_approximation,        "Степенная")
            ]
        else:
            functions = [
                (linear_approx,              "Линейная"),
                (quadratic_approx,           "Полиноминальная 2-й степени"),
                (cubic_approximation,        "Полиноминальная 3-й степени"),
                (logarithmic_approximation,  "Логарифмическая"),
            ]
    else:
        if all(map(lambda yi: yi > 0, y)):
            functions = [
                (linear_approx,              "Линейная"),
                (quadratic_approx,           "Полиноминальная 2-й степени"),
                (cubic_approximation,        "Полиноминальная 3-й степени"),
                (exponential_approximation,  "Экспоненциальная"),
            ]
        else:
            functions = [
                (linear_approx,              "Линейная"),
                (quadratic_approx,           "Полиноминальная 2-й степени"),
                (cubic_approximation,        "Полиноминальная 3-й степени"),
            ]

    with open('out.txt', 'w') as output:
        option = input("Вывод в файл или в терминал? [f/t] ")
        if option == 'f':
            print("Выбран вариант вывода в файл 'out.txt'")
            sys.stdout = output
        else:
            print("Выбран вариант вывода в терминал.")
            print('\n' + ('-' * 30))

        run(functions, x, y, n)


if __name__ == "__main__":
    main()