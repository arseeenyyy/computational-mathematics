import numpy as np

EQUATIONS = [
    {
        "description": "x^3 + 4.81x^2 - 17.37x + 5.38",
        "func": lambda x: x ** 3 + 4.81 * x ** 2 - 17.37 * x + 5.38,
        "f_derivative": lambda x: 3 * x ** 2 + 9.62 * x - 17.37, 
        "f_double_derivative": lambda x: 6 * x + 9.62,
        "func_phi": lambda x, lbd: x + lbd * (x ** 3 + 4.81 * x ** 2 - 17.37 * x + 5.38), 
        "phi_derivative": lambda x, lbd: 1 + lbd * (3 * x ** 2 + 9.62 * x - 17.37)
    }, 
    {
        "description": "sin(x) - 0.5",
        "func": lambda x: np.sin(x) - 0.5,
        "f_derivative": lambda x: np.cos(x), 
        "f_double_derivative": lambda x: - np.sin(x)
    }, 
    {
        "description": "x^3 - 2.18x^2 - 3.27x + 1.43", 
        "func": lambda x: x ** 3 - 2.18 * x ** 2 - 3.27 * x + 1.43, 
        "f_derivative": lambda x: 3 * x ** 2 - 4.36 * x - 3.27, 
        "f_double_derivative": lambda x: 6 * x - 4.36
    }
]

SYSTEM_EQUATIONS = [
    {
        "description": "[sin(y + 2) - x = 1.5\n"
                       "[y + cos(x - 2) = 0.5", 
        "system": [
            lambda x, y: np.sin(y + 2) - x - 1.5, 
            lambda x, y: y + np.cos(x - 2) - 0.5
        ]
    }, 
    {
        "description": "boba", 
        "system": [
            lambda x, y: np.sin(x + y) - 1.2 * x - 0.2, 
            lambda x, y: x**2 + 2 * y ** 2 - 1
        ]
    }
]