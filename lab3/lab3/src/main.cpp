#include <iostream>
#include "funcs/Functions.h"
#include "core/Solver.h"
#include "io/Reader.h"

using namespace std;


int main() {
    int function; 
    pair<double, double> limits;
    double accuracy;
    int integration_method;
    read_params(function, limits, accuracy, integration_method);
    // cout << "function: " << AVAILABLE_FUNCTIONS[function].name << "\n";
    // cout << "limits: " << limits.first << " " << limits.second << "\n";
    // cout << "accuracy: " << accuracy;
    // cout << "Integration method: " << INTEGRATION_METHODS[integration_method].name;
    double result = INTEGRATION_METHODS[integration_method].function(AVAILABLE_FUNCTIONS[function].function, limits, accuracy);
    cout << result;

    return 0;
}