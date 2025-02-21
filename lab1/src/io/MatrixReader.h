#ifndef MATRIX_READER_H
#define MATRIX_READER_H

#include <vector>
#include <string>

using namespace std;

class MatrixReader {
public: 
    static vector<vector<double>> readFromFile(const string &filename, int &n, double  &accuracy);
    static vector<vector<double>> readFromKeyboard(int &n, double &accuracy);
};

#endif
