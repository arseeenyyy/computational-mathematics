#include "Solver.h"
#include <cmath>

#define INITIAL_N 4

using namespace std;

double left_rectangle(double (*f)(double), std::pair<double, double> limits, double accuracy, int n) {
    double result = 0;
    n = 4;
    double h = (limits.second - limits.first) / n;
    for (int i = 0; i < n; i ++) {
        result += f(limits.first + i * h);
    }
    result *= h;
    return result;
}
double right_rectangle(double (*f)(double), std::pair<double, double> limits, int n) {
    double result = 0;
    n = 4;
    double h = (limits.second - limits.first) / n;
    for (int i = 0 ; i < n + 1; i ++) {
        result += f(limits.first + i * h);
    }
    result *= h;
    return result;
}
double mid_rectangle(double (*f)(double), std::pair<double, double> limits, int n) {
    double result = 0;
    n = 4;
    double h = (limits.second - limits.first) / n;
    for (int i = 0; i < n; i ++) {
        result += f(limits.first + (i + 0.5) * h);
    }
    result *= h;
    return result;
}

double trapezoidal(double (*f)(double), std::pair<double, double> limits, int n) {
    double h = (limits.second - limits.first) / n;
    double result = (f(limits.first) + f(limits.second)) / 2;
    for (int i = 0; i < n; i ++) {
        result += f(limits.first + i * h);
    } 
    result *= h;
    return result;
}

double simpson(double (*f)(double), std::pair<double, double> limits, int n) {
    double h = (limits.second - limits.first) / n;
    double result = f(limits.first) + f(limits.second);
    for (int i = 1; i < n; i ++) {
        double coef = 3 + pow(-1, i + 1);
        result += coef * f(limits.first + i * h);
    }
    result *= h/3;
    return result;
}