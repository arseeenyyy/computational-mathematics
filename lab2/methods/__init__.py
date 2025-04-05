from .bisection_method import BisectionMethod
from .newton_method import NewtonMethod
from .simple_iteration_method import SimpleIterationMethod
from .newton_system import NewtonSystemMethod

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

SYSTEM_METHODS = {
    "name": "Newton Method", 
    "solver": NewtonSystemMethod()
}