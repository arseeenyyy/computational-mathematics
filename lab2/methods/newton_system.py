import numpy as np
from result import Result

class NewtonSystemMethod: 
    def solve(self, system_eq, epsilon, initial_approx):
        x0, y0 = initial_approx
        f1, f2 = system_eq['system']
        jacobian = system_eq['jacobian'] 
        iterations = 0
        
        while True: 
            iterations += 1
            f_val = np.array([f1(x0, y0), f2(x0, y0)])

            j11, j12 = jacobian[0][0](x0, y0), jacobian[0][1](x0, y0)
            j21, j22 = jacobian[1][0](x0, y0), jacobian[1][1](x0, y0)
            jac = np.array([[j11, j12], [j21, j22]])
            if np.linalg.det(jac) == 0: 
                return Result(
                    message= 'Error: Jacobian matrix is singular'
                )
            delta = np.linalg.solve(jac, -f_val)
            prev_solution = np.array([x0, y0])
            x0 += delta[0]
            y0 += delta[1]
            solution = np.array([x0, y0])
            print(f'Iteration: {iterations}')
            print(f'Previous solution: x = {prev_solution[0]:.8f}, y = {prev_solution[1]:.8f}')
            print(f'Current solution: x = {x0:.8f}, y = {y0:.8f}')
            print(f'Difference: |Δx| = {abs(x0 - prev_solution[0]):.8f}, |Δy| = {abs(y0 - prev_solution[1]):.8f}')
            print(f'Function values: f1 = {f_val[0]:.8f}, f2 = {f_val[1]:.8f}')
            print('='*10)
        
            if (abs(x0 - prev_solution[0]) < epsilon and 
                abs(y0 - prev_solution[1]) < epsilon):
                break
        return Result(
            root=solution,
            f_value= np.array(f1(*solution), f2(*solution)), 
            iterations=iterations
        )
            