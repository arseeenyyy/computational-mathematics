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
    if (accuracy == 0) {
        cerr << "Incorrect accuracy!\n";
        return {};
    }
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
    while (true) {
        cout << "Enter matrix size (n <= 20): "; 
        cin >> n;
        if (n > 0 && n <= 20) {
            break; 
        } else {
            cerr << "Incorrect matrix size! Please enter a value between 1 and 20.\n";
        }
    }
    while (true) {
        cout << "Enter accuracy (double): ";
        cin >> accuracy;
        if (accuracy > 0) {
            break;  
        } else {
            cerr << "Accuracy must be positive. Please enter a positive value.\n";
        }
    }
    cout << "Enter matrix params line by line\n";
    vector<vector<double>> matrix(n, vector<double>(n + 1)); 
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < n + 1; j ++) {
            cin >> matrix[i][j];
        }
    }
    return matrix;
}