#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <cmath>
#include <cstddef>
#include <string>
#include <array>
#include <vector>

using MathFunction = double(double);

struct FunctionInfo {
    MathFunction* function;   
    std::string name;         
};

inline double f1(double x) { return x * x; }
inline double f2(double x) { return std::exp(x); }
inline double f3(double x) { return 1.0 / x; }
inline double f4(double x) { 
    return -3.0 * x * x * x - 5.0 * x * x + 4.0 * x - 2.0; 
}
inline double f5(double x) { return 5.0; }

inline std::array<FunctionInfo, 5> AVAILABLE_FUNCTIONS = {{
    {&f1, "x^2"},
    {&f2, "e^x"},
    {&f3, "1/x"},
    {&f4, "-3x³-5x²+4x-2"},
    {&f5, "5"}
}};

// std::vector<double> find_discontinuities(MathFunction* func, double a, double b, size_t n = 1000) {
//     //pass

// };



#endif 