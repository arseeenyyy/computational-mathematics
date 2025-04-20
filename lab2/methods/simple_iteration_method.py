import numpy as np
from scipy.differentiate import derivative
from result import Result
class SimpleIterationMethod: 
    def solve(self, func, interval, epsilon, first_derivative, double_derivative, func_phi, phi_derivative): 
        a, b = interval
        iterations = 0 
        if func(a) * func(b) > 0: 
            return Result(
                message = "Error: Function must have opposite signs at interval endpoints"
            )
        sign_changes = self.count_roots(func, a, b)
        if sign_changes > 1: 
            return Result(
                message= f"Error: Function must have 1 root on interval [{a}:{b}]\n number of roots: {sign_changes}"
            )
        max_derivative = max(abs(first_derivative(a)), abs(first_derivative(b)))

        lbd = 1 / max_derivative
        if first_derivative((a + b) / 2) > 0:
            lbd = - lbd
        print(f'lambda param: {lbd}')
        for x in np.linspace(a, b, 100, endpoint = True): 
            if (abs(phi_derivative(x, lbd)) >= 1):
                return Result(
                    message = f'Function does not converge on [{a};{b}] at point = {x}'
                )
        print(phi_derivative(a, lbd)) 
        print(phi_derivative(b, lbd))
        print('='*20)
        prev_x = 0
        if (func(a) * double_derivative(a) > 0): 
            prev_x = a
        elif func(b) *  double_derivative(b) > 0: 
            prev_x = b
        else: 
            prev_x = (a + b) / 2
        x1 = 0
        while True: 
            iterations += 1
            x1 = func_phi(prev_x, lbd)
            print(f'Iteration: {iterations}')
            print(f'x_k = {prev_x:.5f}')
            print(f'x_k+1 = {x1:.5f}')
            print(f'f(x_k+1) = {func(x1):.5f}')
            print(f'|x_k+1 - x_k| = {abs(x1 - prev_x):.5f}')
            print('='*10)
            if (abs(prev_x - x1) < epsilon):
                break
            prev_x = x1
        return Result(
            root= x1,
            f_value= func(x1), 
            iterations= iterations
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




        
                

    
