#include "Solver.h"


double left_rectangle(double (*f)(double), std::pair<double, double> limits, double accuracy) {
    double result = 0;
    int initial_n = 4;
    double h = (limits.second - limits.first) / initial_n;
    for (int i = 0; i < initial_n; i ++) {
        result += f(limits.first + i * h);
    }
    return result;

}
double right_rectangle(double (*f)(double), std::pair<double, double> limits,  double accuracy) {
    return 1;
}
double mid_rectangle(double (*f)(double), std::pair<double, double> limits,  double accuracy) {
    return 1;
}
double trapezoidal(double (*f)(double), std::pair<double, double> limits,  double accuracy) {
    return 1;
}
double simpson(double (*f)(double), std::pair<double, double> limits,  double accuracy) {
    return 1;
}