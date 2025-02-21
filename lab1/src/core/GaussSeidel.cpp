#include "GaussSeidel.h"
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std; 

void GaussSeidel :: gaussSeidelMethod(vector<vector<double>> &matrix, vector<double> &x, double accuracy) {
    int n = matrix.size();
    while (true) {
        vector<double> new_x = x; 
        vector<double> error(n, 0); 

        for (int i = 0; i < n ; i ++) {
            double sum = 0;
            for (int j = 0; j < n; j ++) {
                if (i != j) sum += matrix[i][j] * x[j];
            }
            new_x[i] = (matrix[i][n] - sum) / matrix[i][i];
            error[i] = abs(new_x[i] - x[i]);
        }
        cout << "Iteration " << "Values of x: ";
        for (int i = 0; i < n; i++) {
            cout << new_x[i] << " ";
        }

        cout << "| Errors: ";
        for (int i = 0; i < n; i++) {
            cout << error[i] << " ";
        }
        cout << endl;
        double max_error = *max_element(error.begin(), error.end());
        if (max_error <= accuracy) {
            break;  
        }

        x = new_x; 
    }
}