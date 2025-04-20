from result import Result
import numpy as np

class BisectionMethod: 
    def solve(self, func, interval, epsilon) -> Result: 
        a, b = interval
        iterations = 0
        prev_x = a
        fa, fb = func(a), func(b)
        if fa * fb > 0: 
            return Result(
                message="Error: Function must have opposite signs at interval endpoints"
            )
        sign_changes = self.count_roots(func, a, b)
        if sign_changes > 1: 
            return Result(
                message= f"Error: Function must have 1 root on interval [{a}:{b}]\n number of roots: {sign_changes}"
            )
        while True: 
            iterations += 1
            x = (a + b) / 2
            fx = func(x)
            print(f'Iteration: {iterations}') 
            # print(f'a = {a:.5f}') 
            # print(f'b = {b:.5f}')
            # print(f'x = {x:.5f}')
            # print(f'f(a) = {fa:.5f}')
            # print(f'f(b) = {fb:.5f}')
            # print(f'f(x) = {fx:.5f}')
            # print(f'|a - b| = {abs(a - b):.5f}')
            print('='*10)
            if abs(fx) < epsilon: 
                break
            if fa * fx < 0: 
                b, fb = x, fx
            else: 
                a, fa = x, fx
            prev_x = x
        return Result(
            root = x, 
            f_value= fx, 
            iterations = iterations
        )

    def count_roots(self, func, a, b, step = 0.1):
        x_points = np.arange(a, b + step, step)
        y_values = [func(x) for x in x_points]
        sign_changes = 0
        prev_sign = np.sign(y_values[0])
        for y in y_values[1:]: 
            current_sign = np.sign(y) 
            if current_sign == 0: 
                sign_changes += 1
                prev_sign = 0
            elif current_sign != prev_sign and prev_sign != 0: 
                sign_changes += 1
                prev_sign = current_sign
        
        return sign_changes




