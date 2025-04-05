from equations import EQUATIONS
from methods import METHODS
from result import Result
class IOManager: 

    def show_menu(self): 
        print('Main menu:')
        print('1.Solve nonlinear equation')
        print('2.Solve system of nonlinear equations')
        print('3.Exit')
        return self._get_choice(1, 3)
    
    def select_equation(self): 
        print('Available equations') 
        for i, eq in enumerate(EQUATIONS): 
            print(f'{i}. {eq['description']}')
        choice = self._get_choice(0, len(EQUATIONS) - 1)
        return EQUATIONS[choice]
    
    def select_method(self): 
        print('Available methods')
        for i, met in enumerate(METHODS):
            print(f'{i}. {met['name']}')
        choice = self._get_choice(0, len(METHODS) - 1) 
        return METHODS[choice]

    




    def get_interval(self): 
        print("Set interval [a; b]:")
        a = self._get_float("a = ")
        b = self._get_float("a = ")
        while b <= a: 
            print("b should be > than a")
            a = self._get_float("a = ") 
            b = self._get_float("b = ")
        return (a, b)
    
    def get_epsilon(self): 
        return self._get_float("Set accuracy(ε): ")
    
    def show_result(self, result: Result): 
        print("\n" + str(result))



    def _get_choice(self, min_val, max_val): 
        while True: 
            try:
                choice = int(input("Enter var: "))
                if min_val <= choice <= max_val: 
                    return choice
                print(f'Enter var from {min_val} to {max_val}') 
            except ValueError:
                print("Enter int value")
    
    def _get_float(self, pr):
        while True: 
            try: 
                return float(input(pr))
            except ValueError: 
                print("Enter numeric value")
                
