from io_manager import IOManager
from plotter import Plotter
from equations import EQUATIONS
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
            # func, interval, epsilon
            interval = io.set_interval()
            epsilon = io.set_epsilon()
            result = method['solver'].solve(equation['func'], interval, epsilon)
            print(result)
        if (choice == 2): 
            system_eq = io.select_system() 
            plotter.plot_system(system_eq)
        if (choice == 3): 
            break


if __name__ == "__main__":
    main()