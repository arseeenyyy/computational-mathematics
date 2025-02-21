#include "Utils.h"
#include <cmath>
#include <vector>
#include <iostream>

using namespace std;


bool Utils :: checkDiagonalDominance(vector<vector<double>> &matrix, int n) {
    for (int i = 0; i < n; i ++) {
        double diag = abs(matrix[i][i]);
        double sum = 0; 
        for (int j = 0; j < n; j ++) {
            if (i != j) sum += abs(matrix[i][j]);
        }
        if (diag < sum) return false;
    }
    return true;
}
bool Utils :: makeMatrixDiagonalDominant(vector<vector<double>> &matrix, int n) {
    for (int i = 0; i < n; i++) {
        int bestRow = i;
        double maxDiag = abs(matrix[i][i]);
        for (int k = i + 1; k < n; k++) {
            if (abs(matrix[k][i]) > maxDiag) {
                maxDiag = abs(matrix[k][i]);
                bestRow = k;
            }
        }
        if (bestRow != i) {
            swap(matrix[i], matrix[bestRow]);
        }
    }
    return checkDiagonalDominance(matrix, n); 
}
double Utils :: matrixNorm(const vector<vector<double>> &matrix, int n) {
    double maxSum = 0;
    for (int i = 0; i < n; i ++) {
        double rowSum = 0; 
        for (int j = 0; j < n; j ++) {
            rowSum += abs(matrix[i][j]);
        }
        maxSum = max(rowSum, maxSum);
    }
    return maxSum;
}

void Utils :: printMatrix(const vector<vector<double>> &matrix, int n) {
    cout << "Your matrix:\n"; 
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << "| " << matrix[i][n] << "\n"; 
    }
}
