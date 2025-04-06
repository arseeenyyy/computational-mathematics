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
        "description": "-x/2 + e^x+5sin(x)",
        "func": lambda x: -x / 2 + np.exp(x) + 5 * np.sin(x),
        "f_derivative": lambda x: -0.5 + np.exp(x) + 5 * np.cos(x), 
        "f_double_derivative": lambda x: np.exp(x) - 5 * np.sin(x),
        "func_phi": lambda x, lbd: x + lbd * (-x / 2 + np.exp(x) + 5 * np.sin(x)), 
        "phi_derivative": lambda x, lbd: 1 + lbd * (-0.5 + np.exp(x) + 5 * np.cos(x))
    }, 
    {
        "description": "x^3 - 2.18x^2 - 3.27x + 1.43", 
        "func": lambda x: x ** 3 - 2.18 * x ** 2 - 3.27 * x + 1.43, 
        "f_derivative": lambda x: 3 * x ** 2 - 4.36 * x - 3.27, 
        "f_double_derivative": lambda x: 6 * x - 4.36, 
        "func_phi": lambda x, lbd: x + lbd * (x ** 3 - 2.18 * x ** 2 - 3.27 * x + 1.43),
        "phi_derivative": lambda x, lbd: 1 + lbd * (3 * x ** 2 - 4.36 * x - 3.27)
    }
]

SYSTEM_EQUATIONS = [
    {
        "description": "[sin(y + 2) - x = 1.5\n"
                       "[y + cos(x - 2) = 0.5", 
        "system": [
            lambda x, y: np.sin(y + 2) - x - 1.5, 
            lambda x, y: y + np.cos(x - 2) - 0.5
        ], 
        "jacobian": [
            [lambda x, y: -1, lambda x, y: np.cos(y + 2)], 
            [lambda x, y: -np.sin(x - 2), lambda x, y: 1]
        ]
    }, 
    {
        "description": "[x^2 + y^2 = 4\n"
                       "[y = 3x^2", 
        "system": [
            lambda x, y: x ** 2 + y ** 2 - 4, 
            lambda x, y: y - 3 * x ** 2
        ], 
        "jacobian": [
            [lambda x, y: 2 * x, lambda x, y: 2 * y], 
            [lambda x, y: -6 * x, lambda x, y: 1]
        ]
    }
]