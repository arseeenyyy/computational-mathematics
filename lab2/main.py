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
            print(method)
            



if __name__ == "__main__":
    main()