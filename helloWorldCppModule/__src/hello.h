#ifndef MYPYBINDMODULE_HELLO_H
#define MYPYBINDMODULE_HELLO_H

// Always include <pybind11/pybind11.h> in the very first line of all header files and module.cpp
// In general, make sure that you include pybind11.h BEFORE all other header files.
#include <pybind11/pybind11.h>
namespace py = pybind11;


#include <string>


// Our hello world function definition
int hello(const std::string &name);


#endif
