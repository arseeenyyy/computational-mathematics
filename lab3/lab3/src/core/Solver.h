#ifndef SOLVER_H
#define SOLVER_H

#include <cstddef>
#include <functional>
#include <string>
#include <array>

typedef double (*Integrator)(double (*f)(double),std::pair<double, double> , double accuracy);

struct IntegrationMethod {
    Integrator function; 
    std::string name;
};

double left_rectangle(double (*f)(double), std::pair<double, double> limits,  double accuracy);
double right_rectangle(double (*f)(double), std::pair<double, double> limits,  double accuracy);
double mid_rectangle(double (*f)(double), std::pair<double, double> limits,  double accuracy);
double trapezoidal(double (*f)(double), std::pair<double, double> limits,  double accuracy);
double simpson(double (*f)(double), std::pair<double, double> limits,  double accuracy);

inline std::array<IntegrationMethod, 5> INTEGRATION_METHODS = {{
    {&left_rectangle, "left_rectangle"},
    {&mid_rectangle, "mid_rectangle"}, 
    {&right_rectangle, "right_rectangle"},
    {&trapezoidal, "trapezoidal"}, 
    {&simpson, "simpson"}
}};

#endif