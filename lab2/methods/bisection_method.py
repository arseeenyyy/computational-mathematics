from result import Result

class BisectionMethod: 
    def solve(self, func, interval, epsilon, max_iter = 100) -> Result:
        a, b = interval 
        iterations = 0
        while True:
            iterations += 1
             
