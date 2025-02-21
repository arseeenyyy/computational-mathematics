#ifndef GAUSS_SEIDEL_H
#define GAUSS_SEIDEL_H 

#include <vector>

using namespace std;
class GaussSeidel {
public:// static vector<vector<double>> gaussSeidelMethod(vector<vector<double>>, vector<double> &b, int n, double accuracy);
    static void gaussSeidelMethod(vector<vector<double>> &matrix, vector<double> &x, double accuracy);
}; 

#endif
