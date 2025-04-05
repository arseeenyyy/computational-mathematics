from .bisection_method import BisectionMethod
from .newton_method import NewtonMethod
from .simple_iteration_method import SimpleIterationMethod

METHODS = [
    {
        "name": "Bisection Method",
        "solver": BisectionMethod() 
    },
    {
        "name": "Newton Method", 
        "solver": NewtonMethod() 
    }, 
    {
        "name": "Simple Iteration Method",
        "solver": SimpleIterationMethod()
    }
]