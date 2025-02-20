#include <iostream>
#include <string>
#include <vector>
#include "io/MatrixReader.h"

using namespace std;

int main() {
    vector<vector<double>> matrix;
    int n;
    while (true) {
        cout << "How will you enter matrix dimension? (1 - from the keyboard, 2 - from the file): ";
        int choice;
        cin >> choice; 
        if (choice == 1) {
            matrix = MatrixReader :: readFromKeyboard(n);
            break;
        } else if (choice == 2) {
            string filename;
            cout << "\nEnter file name: ";
            cin >> filename;
            matrix = MatrixReader :: readFromFile(filename, n);
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