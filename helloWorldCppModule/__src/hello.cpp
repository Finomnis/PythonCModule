// In all C++ files, include its corresponding header file in the very first line.
// No need to include <pybind11.h> as we did that already in the header file.
// Just make sure that <pybind11.h> is included BEFORE any other header file.
#include "hello.h"

#include <iostream>


// Our function implementation
int hello(const std::string &name){
    std::cout << "Hello, " << name << "!" << std::endl;
    return 42;
}
