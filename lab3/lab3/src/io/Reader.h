#ifndef READER_H
#define READER_H

#include <iostream>


using namespace std;


class Reader {
public: 
    static void read_params(int &function, pair<double, double> &limits, double &accuracy, double &inital_splits);
};

#endif
