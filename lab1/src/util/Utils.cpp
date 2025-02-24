#include "Utils.h"
#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

bool Utils::checkDiagonalDominance(vector<vector<double>> &matrix, int n) {
    for (int i = 0; i < n; i++) {
        double diag = std::abs(matrix[i][i]);
        double sum = 0;
        for (int j = 0; j < n; j++) {
            if (i != j) sum += std::abs(matrix[i][j]);
        }
        if (diag < sum) return false;
    }
    return true;
}

void Utils::permuteRows(vector<vector<double>> &matrix, int l, int r, bool &found) {
    if (l == r) {
        if (checkDiagonalDominance(matrix, r + 1)) {
            found = true;
        }
        return;
    }
    for (int i = l; i <= r; i++) {
        swap(matrix[l], matrix[i]);
        permuteRows(matrix, l + 1, r, found);
        if (found) return;
        swap(matrix[l], matrix[i]);
    }
}

bool Utils::makeMatrixDiagonalDominant(std::vector<std::vector<double>> &matrix, int n) {
    bool found = false;
    permuteRows(matrix, 0, n - 1, found);
    return found;
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
