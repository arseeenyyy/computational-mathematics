#ifndef SOLVER_H
#define SOLVER_H

#include <cstddef>
#include <functional>
#include <string>
#include <array>

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

inline std::array<IntegrationMethod, 5> INTEGRATION_METHODS = {{
    {&left_rectangle, "left_rectangle"},
    {&mid_rectangle, "mid_rectangle"}, 
    {&right_rectangle, "right_rectangle"},
    {&trapezoidal, "trapezoidal"}, 
    {&simpson, "simpson"}
}};

#endif