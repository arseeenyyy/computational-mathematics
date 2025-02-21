#include "MatrixReader.h"
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

vector<vector<double>> MatrixReader :: readFromFile(const string &filename, int &n, double &accuracy) {
    ifstream file(filename);
    if (!file) {
        cerr << "Error opening file!\n";
        return {};
    }
    file >> n;
    if (n <= 0 || n > 20) {
        cerr << "Incorrect matrix size!\n";
        return {};
    }
    file >> accuracy;
    vector<vector<double>> matrix(n, vector<double>(n + 1));
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < n + 1; j ++) {
            file >> matrix[i][j];
        }
    }
    file.close();
    return matrix;
}
vector<vector<double>> MatrixReader :: readFromKeyboard(int &n, double &accuracy) {
    cout << "Enter matrix size(n <= 20): "; 
    cin >> n;
    if (n <= 0 || n > 20) {
        cerr << "Incorrect matrix size!\n";
        return {};
    }
    cout << "Enter accuracy (double): ";
    cin >> accuracy;
    cout << "Enter matrix params line by line\n";
    vector<vector<double>> matrix(n, vector<double>(n + 1)); 
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < n + 1; j ++) {
            cin >> matrix[i][j];
        }
    }
    return matrix;
}