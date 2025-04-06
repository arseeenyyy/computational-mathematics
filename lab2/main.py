from io_manager import IOManager
from plotter import Plotter
from equations import EQUATIONS
from methods import METHODS
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
                interval = io.set_interval() 
                epsilon = io.set_epsilon()
                result = method['solver'].solve(equation['func'], interval, epsilon, equation['f_derivative'], equation['f_double_derivative']) 
                #Newton Method
                # func, interval, epsilon, 
                print(result)

            if (method == METHODS[2]): 
                #Simple iteration Method, 
                print("test2")

        if (choice == 2): 
            system_eq = io.select_system() 
            plotter.plot_system(system_eq)
        if (choice == 3): 
            break



if __name__ == "__main__":
    main()