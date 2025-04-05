from io_manager import IOManager
from plotter import Plotter
from equations import EQUATIONS
import numpy as np 

def main(): 
    plotter = Plotter()
    plotter.plot_equation(lambda x: np.sin(x)*np.exp(-0.1*x) - 0.5, 
                     "biba boba")

if __name__ == "__main__":
    main()