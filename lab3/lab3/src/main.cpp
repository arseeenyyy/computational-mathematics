#include <iostream>
#include <string>

#include "funcs/Functions.h"
#include "core/Solver.h"
#include "io/Reader.h"

using namespace std;

int main() {
    char choice = 'y';
    
    do {
        int function;
        pair<double, double> limits;
        double accuracy;
        int integration_method;
        
        if (!read_params(function, limits, accuracy, integration_method)) {
            continue;
        }
        
        pair<double, int> result = compute_integral(
            AVAILABLE_FUNCTIONS[function].function, 
            limits, 
            accuracy, 
            INTEGRATION_METHODS[integration_method].name
        );
        
        cout << "\nResult: " << result.first 
             << "\nNumber of splits: " << result.second << endl;
        
        cout << "\nDo you want to continue? (y/n): ";
        cin >> choice;
        
        choice = tolower(choice);
        
    } while (choice == 'y');
    return 0;
}