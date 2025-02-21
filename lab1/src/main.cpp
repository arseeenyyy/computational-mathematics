#include <iostream>
#include <string>
#include <vector>
#include "io/MatrixReader.h"
#include "util/Utils.h"
#include "core/GaussSeidel.h"


using namespace std;

int main() {
    vector<vector<double>> matrix;
    int n;
    double accuracy;
    cout << "format of enter params:\nn (int size; 0 <= n <= 20)\naccuracy (double)\nmatrix params:\na_11 a_12 ... b_1n\na_21 a_22 ... b_2n\na_n1 a_n2 ... b_nn\n"; 
    while (true) {
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
    // Utils :: printMatrix(matrix, n);
    if (Utils :: checkDiagonalDominance(matrix, n)) {
        cout << "Matrix is diagonally dominant\n";
    } else {
        cout << "Matrix is not diagonally dominant. Trying to reorder...\n";
        if (! Utils :: makeMatrixDiagonalDominant(matrix, n)) {
            cout << "Impossible to make matrix diagonally dominant\n";
            return 1;
        }
        cout << "Matrix was reordered successfully\n";
    }

    // Utils :: printMatrix(matrix, n);
    double norm = Utils :: matrixNorm(matrix, n);
    cout << "Matrix norm: " << norm << "\n";
    vector<double> x(n, 0); 
    GaussSeidel :: gaussSeidelMethod(matrix, x, accuracy);
    return 0;
}