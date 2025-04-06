from io_manager import IOManager
from plotter import Plotter
from equations import EQUATIONS
from methods import METHODS
from methods import SYSTEM_METHODS
import numpy as np 

def main(): 
    io = IOManager()
    plotter = Plotter()
    while True:
        choice = io.show_menu() 
        if (choice == 1):
            equation = io.select_equation()
            plotter.plot_equation(equation['func'], equation['description'])
            method = io.select_method()
            if (method == METHODS[0]):
                # Bisection method
                # func, interval, epsilon
                interval = io.set_interval()
                epsilon = io.set_epsilon()
                result = method['solver'].solve(equation['func'], interval, epsilon)
                print(result)
            if (method == METHODS[1]): 
                #Newton Method
                # func, interval, epsilon, 
                interval = io.set_interval() 
                epsilon = io.set_epsilon()
                result = method['solver'].solve(equation['func'], interval, epsilon, equation['f_derivative'], equation['f_double_derivative']) 
                print(result)
            if (method == METHODS[2]): 
                #Simple iteration Method 
                # func, interval, epsilon
                interval = io.set_interval()
                epsilon = io.set_epsilon()
                result = method['solver'].solve(equation['func'], interval, epsilon, equation['f_derivative'], equation['f_double_derivative'], equation['func_phi'], equation['phi_derivative'])
                print(result)
        elif (choice == 2): 
            # System, newton method, initial approx,epsilon
            system_eq = io.select_system() 
            plotter.plot_system(system_eq)
            epsilon = io.set_epsilon()
            initial_approx = io.set_initial_approx() 
            result = SYSTEM_METHODS['solver'].solve(system_eq, epsilon, initial_approx) 
            print(result)
        if (choice == 3): 
            break



if __name__ == "__main__":
    main()