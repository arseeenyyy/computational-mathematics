#include "Solver.h"
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include <sys/types.h>

#define INITIAL_N 4

using namespace std;

double left_rectangle(double (*f)(double), std::pair<double, double> limits, int n) {
    double result = 0;
    double h = (limits.second - limits.first) / n;
    for (int i = 0; i < n; i ++) {
        result += f(limits.first + i * h);
    }
    result *= h;
    return result;
}
double right_rectangle(double (*f)(double), std::pair<double, double> limits, int n) {
    double result = 0;
    double h = (limits.second - limits.first) / n;
    for (int i = 0 ; i < n + 1; i ++) {
        result += f(limits.first + i * h);
    }
    result *= h;
    return result;
}
double mid_rectangle(double (*f)(double), std::pair<double, double> limits, int n) {
    double result = 0;
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

std::pair<double, int> compute_integral(double (*f)(double), pair<double, double> limits, double accuracy, string method_name) {
    const IntegrationMethod* method = nullptr;
    for (const auto& m : INTEGRATION_METHODS) {
        if (m.name == method_name) {
            method = &m;
            break;
        }
    }
    auto coef_it = RUNGE_COEF.find(method_name);

    double coef = coef_it->second;

    int n = 4;
    double result = method->function(f, limits, n);
    double error = std::numeric_limits<double>::infinity();

    while (error > accuracy) {
        n *= 2;
        double new_result = method->function(f, limits, n);
        error = std::abs(new_result - result) / coef;
        result = new_result;
        if (n > 10000000) {
            cout << "reached splits limit (n > 10^6)";
            break;
        }
    }
    return {result, n};
}
bool get_breakpoints(double (*f)(double), std::pair<double, double> limits) {
    int n = 1000;
    double h = (limits.second - limits.first) / n;
    for (int i = 0; i <= n; i++) {
        double x = limits.first + i * h;
        try {
            double y = f(x);
            if (std::isinf(y) || std::isnan(y)) {
                cout << "gap in point: " << x << " (inf or NaN)\n";
                return true;
            }
        } catch (const char* e) {
            cout << "Exception: " << e << " in point x = " << x << "\n";
            return true;
        } catch (...) {
            cout << "wtf just happend... " << x << "\n";
            return true;
        }
    }
    return false;
}