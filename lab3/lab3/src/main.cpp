#include <cstddef>
#include <iostream>
#include "funcs/Functions.h"

using namespace std;


int main() {
    for (size_t i = 0 ; i < AVAILABLE_FUNCTIONS.size() ; i ++) {
        const auto& func = AVAILABLE_FUNCTIONS[i];
        cout << func.name << "\n" << AVAILABLE_FUNCTIONS[i].function(1)<<"\n\n";
    }
    return 0;
}