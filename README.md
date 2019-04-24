# PythonCModule
A simple python module that acts as an interface for C/C++ code.

It is specifically written and tested for Python 3.x, it does NOT work with Python 2.

[![CircleCI](https://circleci.com/gh/Finomnis/PythonCModule.svg?style=svg)](https://circleci.com/gh/Finomnis/PythonCModule)
[![Build status](https://ci.appveyor.com/api/projects/status/i2vbur3oauom6j4m?svg=true)](https://ci.appveyor.com/project/Finomnis/pythoncmodule)
[![Build Status](https://travis-ci.org/Finomnis/PythonCModule.svg?branch=master)](https://travis-ci.org/Finomnis/PythonCModule)

## Features
Using this template as a basis for custom C modules has the following advantages:
* Automatic building, no explicit compilation necessary
* Automatic rebuilding when C code has changed
* Compatibility with IDEs like PyCharm
* Automatic compiler detection, due to the usage of python's setuptools
* Very small and easy to understand

## Usage
### C
Before you create your own C modules, you can verify that your system is set up correctly by executing the ``test.py`` script.
If everything is correct, you should see a bunch of compiler commands followed by ``Hello, world!``.

To create your own C module, just copy and rename the ``helloWorldModule`` folder to wherever you want your module to be.

Then, modify the ``__src`` folder contents:
* Put your methods in header and source file combinations. Try to mimik the style of ``hello.h`` and ``hello.c``.
* Adjust ``module.c`` to include your function headers and add your functions to the ``methods`` array.
* Add python wrappers for your functions to ``wrappers.py``.

### C++
Before you create your own C++ modules, you can verify that your system is set up correctly by executing the ``testCpp.py`` script.
If everything is correct, you should see a bunch of compiler commands followed by ``Hello, world!``.

The C++ version needs the following libraries:
* setuptools
* pybind11

To create your own C++ module, just copy and rename the ``helloWorldCppModule`` folder to wherever you want your module to be.

Then, modify the ``__src`` folder contents:
* Put your methods in header and source file combinations. Try to mimik the style of ``hello.h`` and ``hello.cpp``.
* Adjust ``module.cpp`` to include your function headers and add your functions to the PYBIND11_MODULE definition.
* Add python wrappers for your functions to ``wrappers.py``.

## Tested Python Versions

| Operating System | Python Version (C) | Python Version (C++) |
| ---------------- |:------------------:|:--------------------:|
| Windows          | &ge; 3.5           | &ge; 3.5             |
| Windows (x64)    | &ge; 3.5           | &ge; 3.5             |
| Linux            | &ge; 3.5           | &ge; 3.5             |
| Mac OS           | &ge; 3.6           | &ge; 3.6             |
