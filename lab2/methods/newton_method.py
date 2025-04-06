import numpy as np
from scipy.differentiate import derivative
from result import Result


class NewtonMethod: 


    def second_derivative(func): 
        pass
    
    def initial_approx(): 
        pass
    

    def solve(self, func, interval, epsilon, max_iter = 100): 
        a, b = interval 
        iterations = 0 
        fa, fb = func(a), func(b)
        if fa * fb > 0: 
            return Result(
                message = "Error: Function must have opposite signs at interval endpoints"
            )
        x = a
        prev_x = x
        while True: 
            iterations += 1
            fx = func(prev_x)
            df = derivative(func, prev_x)
            x = prev_x - fx / df
            diff = abs(x - prev_x)

            print(f'Iteration: {iterations}')
            print(f'x_k: {prev_x}') 
            print(f'f(x_k): {fx}')
            print(f'df(x_k): {df}')
            print(f'x_k+1: {x}')
            print(f'|x_k+1 - x_k|: {diff}')
            print('='*10)
            if (diff) < epsilon: 
                break
        return Result(
            root = x, 
            f_value = func(func(x)),
            iterations = iterations
        )



