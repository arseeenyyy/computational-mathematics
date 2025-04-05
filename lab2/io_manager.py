from equations import EQUATIONS
from methods import METHODS
class IOManager: 

    def show_menu(self): 
        print('Main menu:')
        print('1.Solve nonlinear equation')
        print('2.Solve system of nonlinear equations')
        print('3.Exit')
        return self._get_choice(1, 3)
    
    def select_equation(self):
        print("Available equaions")
        for i, eq in enumerate(EQUATIONS): 
            print(f'{i}, {eq['description']}')
        choice = self._get_choice(1, len(METHODS))
        return METHODS[choice - 1]
    def get_interval(self): 
        print("Set interval [a; b]:")
        a = self._get_float("a = ")
        b = self._get_float("a = ")
        while b <= a: 
            print("b should be > than a")
            a = self._get_float("a = ") 
            b = self._get_float("b = ")
        return (a, b)





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
                
