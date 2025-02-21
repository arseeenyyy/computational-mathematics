#include "GaussSeidel.h"
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>  // Для форматированного вывода

using namespace std;

void GaussSeidel::gaussSeidelMethod(vector<vector<double>> &matrix, vector<double> &x, double accuracy) {
    int n = matrix.size();
    int iteration = 0;
    for (int i = 0; i < n; i++) {
        x[i] = matrix[i][n] / matrix[i][i];
    }

    cout << setw(7) << "№";
    for (int i = 0; i < n; i++) {
        cout << setw(10) << "x" + to_string(i + 1);  
    }
    for (int i = 0; i < n; i++) {
        cout << setw(1) << "ε" + to_string(i + 1);  
    }
    cout << endl;

    
    while (true) {
        vector<double> new_x = x;  
        vector<double> epsilon(n, 0);

        for (int i = 0; i < n; i++) {
            double sum = 0;
            for (int j = 0; j < n; j++) {
                if (i != j) sum += matrix[i][j] * new_x[j];
            }
            new_x[i] = (matrix[i][n] - sum) / matrix[i][i];
            epsilon[i] = abs(new_x[i] - x[i]);
        }

        cout << setw(7) << iteration + 1; 
        for (int i = 0; i < n; i++) {
            cout << setw(10) << fixed << setprecision(4) << new_x[i];  
        }
        for (int i = 0; i < n; i++) {
            cout << setw(10) << fixed << setprecision(4) << epsilon[i]; 
        }
        cout << endl;

        double max_error = *max_element(epsilon.begin(), epsilon.end());
        if (max_error <= accuracy) {
            break;  
        }
        x = new_x;
        iteration++;
    }
    cout << "\nMethod converged in " << iteration + 1 << " iterations.\n";
}
