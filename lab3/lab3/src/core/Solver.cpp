#include "Solver.h"
#define INITIAL_N 4


double left_rectangle(double (*f)(double), std::pair<double, double> limits, double accuracy) {
    double result = 0;
    int n = INITIAL_N;
    double h = (limits.second - limits.first) / n;
    for (int i = 0; i < n; i ++) {
        result += f(limits.first + i * h);
    }
    result *= h;
    return result;
}
double right_rectangle(double (*f)(double), std::pair<double, double> limits,  double accuracy) {
    double result = 0;
    int n = INITIAL_N;
    double h = (limits.second - limits.first) / n;
    for (int i = 0 ; i < n + 1; i ++) {
        result += f(limits.first + i * h);
    }
    result *= h;
    return result;
}
double mid_rectangle(double (*f)(double), std::pair<double, double> limits,  double accuracy) {
    double result = 0;
    int n = INITIAL_N;
    double h = (limits.second - limits.first) / n;
    for (int i = 0; i < n; i ++) {
        result += f(limits.first + (i + 0.5) * h);
    }
    result *= h;
    return result;
}


double trapezoidal(double (*f)(double), std::pair<double, double> limits,  double accuracy) {
    return 1;
}
double simpson(double (*f)(double), std::pair<double, double> limits,  double accuracy) {
    return 1;
}