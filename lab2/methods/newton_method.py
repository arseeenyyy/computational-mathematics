import numpy as np
from scipy.differentiate import derivative
from result import Result


class NewtonMethod: 

    def solve(self, func, interval, epsilon, first_derivative, double_derivative): 
        a, b = interval 
        iterations = 0 
        fa, fb = func(a), func(b)
        if fa * fb > 0: 
            return Result(
                message = "Error: Function must have opposite signs at interval endpoints"
            )
        
        print("calculating initial approx...")
        prev_x = 0
        if func(a) * double_derivative(a) > 0: 
            prev_x = a 
        elif func(b) * double_derivative(b) > 0: 
            prev_x = b
        else: 
            prev_x = (a + b) / 2
        x = prev_x

        while True: 
            iterations += 1
            fx = func(prev_x)
            df = first_derivative(prev_x)
            x = prev_x - fx / df
            diff = abs(x - prev_x)

            print(f'Iteration: {iterations}')
            print(f'x_k: {prev_x:.5f}') 
            print(f'f(x_k): {fx:.5f}')
            print(f'df(x_k): {df:.5f}')
            print(f'x_k+1: {x:.5f}')
            print(f'|x_k+1 - x_k|: {diff:.5f}')
            print('='*10)
            if abs(prev_x - x) < epsilon: 
                break
            prev_x = x
        return Result(
            root = x, 
            f_value = func(x),
            iterations = iterations
        )



