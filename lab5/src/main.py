def read_input_from_keyboard(): 
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
                
            return x, xi, yi, None
    except IOError as error: 
        return None, None, None, f"Невозможно прочитать файл: {error}"

def main(): 
    filename = "test.txt"
    x, xi, yi, error = read_input_from_file(filename)
    if error:
        print(error)
    else:
        print(f"x: {x}\nxi: {xi}\nyi: {yi}")


if __name__ == "__main__": 
    main()