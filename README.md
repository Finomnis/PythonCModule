# PythonCModule
A simple python module that acts as an interface for C code.

It is specifically written and tested for Python 3.x, it does NOT work with Python 2.

## Usage
Before you add your own C modules, make sure that your system is set up correctly by executing the ``test.py`` script.
If everything is correct, you should see a bunch of compiler commands and then ``Hello, world!``.

To create your own C module, just copy and rename the ``helloWorldModule`` folder to wherever you want your module to be.

Then, modify the ``__src`` folder contents:
* Put your methods in header and source file combinations. Try to mimik the style of ``hello.h`` and ``hello.c``.
* Adjust ``module.c`` to include your function headers and add your functions to the ``methods`` array.
* Add python wrappers for your functions to ``wrappers.py``.
