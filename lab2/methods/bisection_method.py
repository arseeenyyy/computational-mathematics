from result import Result

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
        while True: 
            iterations += 1
            x = (a + b) / 2
            fx = func(x)
            print(f'Iteration: {iterations}') 
            print(f'a = {a}') 
            print(f'b = {b}')
            print(f'x = {x}')
            print(f'f(a) = {fa}')
            print(f'f(b) = {fb}')
            print(f'f(x) = {fx}')
            print(f'|a - b| = {abs(a - b)}')
            print('='*10)
            if abs(prev_x - x) < epsilon: 
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






