class Result: 
    root: float 
    f_value: float 
    iterations: int
    def __init__(self, root = None, f_value = None, iterations = 0, message = None):
        self.root = root
        self.f_value = f_value
        self.iterations = iterations 
        self.message = message
    
    def is_valid(self): 
        return self.root is not None 

    def __str__(self):
        if not self.is_valid(): 
            return f"oopsie, smth went wrong..."
        return (
            f"Result:\n"
            f"Root: {self.root}"
            f"Function value: {self.f_value}"
            f"Number of iterations: {self.iterations}"
        )