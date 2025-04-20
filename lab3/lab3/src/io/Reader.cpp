#include <cstddef>
#include <iostream>

#include "Reader.h"
#include "../funcs/Functions.h"
#include "../core/Solver.h"

using namespace std;

void read_params(int &function, pair<double, double> &limits, double &accuracy, int &integration_method) {
    cout << "Choose one function:\n";
    for (size_t i = 0; i < AVAILABLE_FUNCTIONS.size(); i ++) {
        cout << i + 1 << ": " << AVAILABLE_FUNCTIONS[i].name << "\n";
    }
    while (true) {
        cout << "your choice: ";
        cin >> function;
        if (function < 1 || function > 5) {
            cout << "\nChoose correct number of the function pls\n";
        } 
        function --;
        break;
    }  
    while (true) {
        cout << "Enter integration limits:\n";
        cout << "Left border (a): ";
        cin >> limits.first;
        cout << "Right border (b): ";
        cin >> limits.second;

        if (limits.first >= limits.second) {
            cout << "Error: Left border must be less than right border (a < b)\n";
        } else {
            break;
        }
    }
    cout << "Choose integration method:\n";
    for (size_t i = 0; i < INTEGRATION_METHODS.size(); i ++) {
        cout << i + 1 << ": " << INTEGRATION_METHODS[i].name << "\n";
    }
    while (true) {
        cout << "your choice: ";
        cin >> integration_method;
        if (integration_method < 1 || integration_method > 5) {
            cout << "\nChoose correct number of the integration method pls\n";
        }
        integration_method --;
        break;
    }
    while (true) {
        cout << "Enter accuracy: ";
        cin >> accuracy;
        if (accuracy < 0) {
            cout << "accuracy must be > 0\n";
        }
        break;
    }


}   
