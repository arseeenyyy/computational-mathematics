#include <iostream>
#include <string>
#include <vector>
#include "io/MatrixReader.h"

using namespace std;

int main() {
    vector<vector<double>> matrix;
    int n;
    double accuracy;
    while (true) {
        cout << "format of enter params:\nn (int size; 0 <= n <= 20)\naccuracy (double)\nmatrix params:\na_11 a_12 ... b_1n\na_21 a_22 ... b_2n\na_n1 a_n2 ... b_nn\n"; 
        cout << "How will you enter matrix dimension? (1 - from the keyboard, 2 - from the file): ";
        int choice;
        cin >> choice; 
        if (choice == 1) {
            matrix = MatrixReader :: readFromKeyboard(n, accuracy);
            break;
        } else if (choice == 2) {
            string filename;
            cout << "\nEnter file name: ";
            cin >> filename;
            matrix = MatrixReader :: readFromFile(filename, n, accuracy);
            break;
        }
        cout << "\n";
    }
    cout << "your matrix:\n"; 
    for (const auto& row: matrix) {
        for (double val: row) {
            cout << val << " ";
        }
        cout << "\n";
    }
    return 0;
}