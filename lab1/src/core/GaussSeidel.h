#ifndef GAUSS_SEIDEL_H
#define GAUSS_SEIDEL_H 

#include <vector>

using namespace std;
class GaussSeidel {
public:
    static void gaussSeidelMethod(vector<vector<double>> &matrix, vector<double> &x, double accuracy);
}; 

#endif
