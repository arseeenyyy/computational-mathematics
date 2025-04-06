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
        if choice == 1:
            equation = io.select_equation()
            plotter.plot_equation(equation['func'], equation['description'])
            method = io.select_method()
            
            input_mode = io.get_input_mode()
            
            if method == METHODS[0]:  # Bisection method
                if input_mode == 1:
                    interval = io.set_interval()
                    epsilon = io.set_epsilon()
                else: 
                    interval, epsilon = io.read_interval_epsilon()
                
                result = method['solver'].solve(equation['func'], interval, epsilon)
                print(result)
                
            elif method == METHODS[1]:  # Newton Method
                if input_mode == 1:
                    interval = io.set_interval() 
                    epsilon = io.set_epsilon()
                else:
                    interval, epsilon = io.read_interval_epsilon()
                
                result = method['solver'].solve(
                    equation['func'], 
                    interval, 
                    epsilon, 
                    equation['f_derivative'], 
                    equation['f_double_derivative']
                ) 
                print(result)
                
            elif method == METHODS[2]:  # Simple iteration Method
                if input_mode == 1:
                    interval = io.set_interval()
                    epsilon = io.set_epsilon()
                else:
                    interval, epsilon = io.read_interval_epsilon()
                
                result = method['solver'].solve(
                    equation['func'], 
                    interval, 
                    epsilon, 
                    equation['f_derivative'], 
                    equation['f_double_derivative'],
                    equation['func_phi'], 
                    equation['phi_derivative']
                )
                print(result)
            
            if result.message is None:
                save_in = io.is_save_into_file()
                if save_in == 1: 
                    io.write_result_into_file(result)
                
        elif choice == 2:  # System of equations
            system_eq = io.select_system() 
            plotter.plot_system(system_eq)
            
            input_mode = io.get_input_mode()
            if input_mode == 1:
                epsilon = io.set_epsilon()
                initial_approx = io.set_initial_approx()
            else:
                initial_approx, epsilon = io.read_initial_epsilon()
            
            result = SYSTEM_METHODS['solver'].solve(system_eq, epsilon, initial_approx) 
            print(result)
            
            if result.message is None:
                save_in = io.is_save_into_file()
                if save_in == 1:
                    io.write_result_into_file(result)
                
        elif choice == 3: 
            break

if __name__ == "__main__":
    main()