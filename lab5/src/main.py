from math import sin, sqrt
from solve import solve

def read_input_from_keyboard():
    while True:  
        while True:
            try:
                x = float(input("Введите точку интерполяции: "))
                break
            except ValueError:
                print("Ошибка: введите число для точки интерполяции. Попробуйте снова.")
        
        xi = []
        yi = []
        print("Введите 'quit', чтобы закончить ввод")
        print("Введите узлы интерполяции (два числа через пробел):")
        
        while True:
            user_input = input().strip()
            if user_input.lower() == "quit":
                break
                
            point = user_input.split()
            if len(point) != 2:
                print("Неправильный ввод (нужно 2 числа). Такой ввод учитываться не будет. Продолжайте ввод или введите 'quit'")
                continue
                
            try:
                x_val = float(point[0])
                y_val = float(point[1])
                xi.append(x_val)
                yi.append(y_val)
            except ValueError:
                print("Ошибка: введены не числа. Такой ввод учитываться не будет. Продолжайте ввод или введите 'quit'")
        
        if len(xi) < 2:
            print("Ошибка: нужно ввести как минимум 2 узла интерполяции. Начнем сначала.")
            continue
        
        if x < min(xi) or x > max(xi):
            print(f"Ошибка: точка интерполяции должна находиться в отрезке [{min(xi)}, {max(xi)}]. Начнем сначала.")
            continue
        
        return x, xi, yi

def read_input_from_file(filename): 
    try: 
        with open(filename, "r") as file:
            xi = []
            yi = []
            x_read = False
            x = None
            
            for line in file: 
                line = line.strip()
                if not line:  
                    continue
                    
                if not x_read: 
                    try:
                        x = float(line)
                        x_read = True
                    except ValueError:
                        return None, None, None, f"Ошибка: первая строка файла должна содержать число (точку интерполяции)"
                else: 
                    point = line.split()
                    if len(point) == 2: 
                        try:
                            xi.append(float(point[0]))
                            yi.append(float(point[1]))
                        except ValueError:
                            print(f"Предупреждение: строка '{line}' пропущена - не содержит числа")
                    else:
                        print(f"Предупреждение: строка '{line}' пропущена - нужно 2 числа")
            
            if not x_read:
                return None, None, None, "Ошибка: файл не содержит точку интерполяции"
            if x < min(xi) or x > max(xi): 
                return None, None, None, f"Точка интерполяции должна лежать в отрезке [{min(xi)}:{max(xi)}]"
            return x, xi, yi, None
    except IOError as error: 
        return None, None, None, f"Невозможно прочитать файл: {error}"

def read_data_from_example(): 
    x = 0.523
    xi = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]
    yi = [1.5320, 2.5356, 3.5406, 4.5462, 5.5504, 6.5559, 7.5594]
    return x, xi, yi

def read_data_from_functions():
    print("Доступные функции:")
    print("1. x^2 - 5x")
    print("2. x^5")
    print("3. sin(x)")
    print("4. sqrt(x)")

    while True:
        try:
            func_number = int(input("Выберите функцию [1/2/3/4]: "))
            if func_number not in [1, 2, 3, 4]:
                print("Ошибка: введите число от 1 до 4")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число (1, 2, 3 или 4)")

    if func_number == 1:
        f = lambda x: x ** 2 - 5 * x
    elif func_number == 2:
        f = lambda x: x ** 5
    elif func_number == 3:
        f = lambda x: sin(x)
    elif func_number == 4:
        f = lambda x: sqrt(x)

    while True:
        try:
            n = int(input("Введите число узлов (n > 0): "))
            if n <= 0:
                print("Ошибка: число узлов должно быть положительным")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число")

    while True:
        try:
            x0 = float(input("Введите начальную точку интервала (x0): "))
            xn = float(input("Введите конечную точку интервала (xn): "))
            if x0 == xn:
                print("Ошибка: x0 и xn не должны совпадать")
                continue
            if x0 > xn: 
                print("Ошибка: x0 > xn")
                continue
            break
        except ValueError:
            print("Ошибка: введите число")

    h = (xn - x0) / n
    xi = [x0 + h * i for i in range(n)]
    yi = [f(x) for x in xi]

    while True:
        try:
            x_interp = float(input(f"Введите точку интерполяции (от {x0} до {xn}): "))
            if not (min(x0, xn) <= x_interp <= max(x0, xn)):
                print(f"Ошибка: точка должна быть между {x0} и {xn}")
                continue
            break
        except ValueError:
            print("Ошибка: введите число")

    return x_interp, xi, yi
def main():
    print("'fi' - file\n't' - terminal\n'e' - example\n'f' - function")
    while True:
        option = input("Выберите способ задания исходных данных [fi/t/e/f]: ")
        
        if option == "fi":
            while True:
                filename = input("Введите название файла: ")
                x, xi, yi, error = read_input_from_file(filename)
                
                if error is not None:
                    print(error)
                    another_try = input("Вы хотите попробовать еще раз? [y/n]: ")
                    if another_try.lower() != 'y':
                        print("Переход к вводу с клавиатуры")
                        x, xi, yi = read_input_from_keyboard()
                        break
                else:
                    break
            
            n = len(xi)
        
        elif option == "t":
            x, xi, yi = read_input_from_keyboard()
            n = len(xi)
        
        elif option == "e":
            x, xi, yi = read_data_from_example()
            n = len(xi)
        
        elif option == "f":
            x, xi, yi = read_data_from_functions()
            n = len(xi)
        
        else:
            print("Некорректный ввод")
            continue  
        
        if len(set(xi)) != len(xi):
            print("Узлы интерполяции не должны совпадать, повторите ввод")
            continue
        
        if xi != sorted(xi):
            print("X_i должны быть отсортированы, введите еще раз")
            continue
        
        print("Введенные данные:")
        print("xi:", xi)
        print("yi:", yi)
        print("x:", x)
        print("n:", n)
        
        solve(xi, yi, x, n)
        break  

if __name__ == "__main__":
    main()
