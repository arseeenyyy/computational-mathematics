#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <cmath>

inline double f1(double x) {
    return x * x;  
}

inline double f2(double x) {
    return std::exp(x);
}

inline double f3(double x) {
    return 1.0 / x;
}

inline double f4(double x) {
    return -3.0 * x * x * x - 5.0 * x * x + 4.0 * x - 2.0;
}

inline double f5(double x) {
    return 5.0;
}

#endif