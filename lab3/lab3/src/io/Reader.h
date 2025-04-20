#ifndef READER_H
#define READER_H

#include <iostream>

class Reader {
public: 
    static void read_params(int &function, std::pair<double, double> &limits, double &accuracy, int &integration_method);
};

#endif
