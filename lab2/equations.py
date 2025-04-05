import numpy as np

EQUATIONS = [
    {
        "description": "x^2 - 2",
        "func": lambda x: x**2 - 2
    }, 
    {
        "description": "sin(x) - 0.5",
        "func": lambda x: np.sin(x) - 0.5 
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