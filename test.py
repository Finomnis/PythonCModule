#!/usr/bin/env python

import helloWorldModule

result = helloWorldModule.hello("world")

# Check result, used for verification in circleci
assert (result==42), "Getting result from C function did not work!"

