#ifndef SOLVER_H
#define SOLVER_H

#include <cstddef>
#include <functional>
#include <string>
#include <array>
#include <map>

typedef double (*Integrator)(double (*f)(double),std::pair<double, double>, int n);

struct IntegrationMethod {
    Integrator function; 
    std::string name;
};

double left_rectangle(double (*f)(double), std::pair<double, double> limits, int n);
double right_rectangle(double (*f)(double), std::pair<double, double> limits, int n);
double mid_rectangle(double (*f)(double), std::pair<double, double> limits, int n);
double trapezoidal(double (*f)(double), std::pair<double, double> limits, int n);
double simpson(double (*f)(double), std::pair<double, double> limits, int n);

std::pair<double, int> compute_integral(double (*f)(double), std::pair<double, double> limits, double accuracy, std::string method_name);

inline std::array<IntegrationMethod, 5> INTEGRATION_METHODS = {{
    {&left_rectangle, "left_rectangle"},
    {&mid_rectangle, "mid_rectangle"}, 
    {&right_rectangle, "right_rectangle"},
    {&trapezoidal, "trapezoidal"}, 
    {&simpson, "simpson"}
}};

inline const std::map<std::string, double> RUNGE_COEF = {
    {"left_rectangle", 1.0},
    {"right_rectangle", 1.0},
    {"mid_rectangle", 3.0},
    {"trapezoidal", 3.0},
    {"simpson", 15.0}
};

#endif