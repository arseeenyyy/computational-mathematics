#ifndef UTILS_H 
#define UTILS_H

#include <vector>
#include <cmath>

using namespace std;

class Utils {
public:
    static bool checkDiagonalDominance(vector<vector<double>> &matrix, int n); 
    static bool makeMatrixDiagonalDominant(vector<vector<double>> &matrix, int n);
    static double matrixNorm(const vector<vector<double>> &matrix, int n);
    static void printMatrix(const vector<vector<double>> &matrix, int n);
    static void permuteRows(vector<vector<double>> &matrix, int l, int r, bool &found);

};

#endif
