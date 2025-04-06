from equations import EQUATIONS
from methods import METHODS
from equations import SYSTEM_EQUATIONS
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

    def select_system(self): 
        print('Available systems of nonlinear equations')
        for i, sys_eq in enumerate(SYSTEM_EQUATIONS): 
            print(f'{i}.\n{sys_eq['description']}')
        choice = self._get_choice(0, len(SYSTEM_EQUATIONS) - 1) 
        return SYSTEM_EQUATIONS[choice]

    def set_interval(self): 
        print("Set interval [a; b]:")
        a = self._get_float("a = ")
        b = self._get_float("b = ")
        while b <= a: 
            print("b should be > than a")
            a = self._get_float("a = ") 
            b = self._get_float("b = ")
        return (a, b)
    
    def set_initial_approx(self): 
        print('Set initial approx [x_0; y_0]:')
        x = self._get_float("x = ") 
        y = self._get_float("y = ")
        return (x, y)

    def set_epsilon(self): 
        return self._get_float("Set accuracy(ε): ")
    
    def get_input_mode(self):
        print('\nSelect input mode:')
        print('1. Keyboard input')
        print('2. File input')
        return self._get_choice(1, 2)
    
    def read_interval_epsilon(self): 
        file_path = self.read_filepath();
        try: 
            with open(file_path, 'r') as f: 
                lines = [line.strip() for line in f if line.strip()]
                a = float(lines[0])
                b = float(lines[1])
                epsilon = float(lines[2])

                if (b <= a): 
                    raise ValueError("b must be greater than a")
                if (epsilon <= 0): 
                    raise ValueError("epsilon must be > 0")
            return (a, b), epsilon    
        except Exception as e: 
            print(f'Error reading file: {e}')
            print("Please enter data manually")
            return self.set_interval(), self.set_epsilon()
        
    def read_initial_epsilon(self): 
        file_path = self.read_filepath()
        try:
            with open(file_path, 'r') as f:
                lines = [line.strip() for line in f if line.strip()]
                x = float(lines[0])
                y = float(lines[1])
                epsilon = float(lines[2])
                
                if epsilon <= 0:
                    raise ValueError("epsilon must be > 0")
                    
            return (x, y), epsilon
        except Exception as e:
            print(f"Error reading file: {e}")
            print("Please enter data manually")
            return self.set_initial_approx(), self.set_epsilon()
        
    def write_result_into_file(self, result):
        file_path = self.read_filepath()
        try: 
            with open(file_path, 'w') as f: 
                f.write(str(result))
            print(f'result was saved into file {file_path}')
        except Exception as e: 
            print(f'Error saving into file: {e}')

    def show_result(self, result: Result): 
        print("\n" + str(result))

    def read_filepath(self):
        return input("Enter file path: ").strip()
    
    def is_save_into_file(self): 
        print('Save result into file?')
        print('1. Yes')
        print('2. No')
        return self._get_choice(1, 2)

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
                
