#include "Utils.h"
#include <iostream>
#include <cmath>
#include <vector>

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
