#!/usr/bin/env python3

import helloWorldRustModule

result = helloWorldRustModule.hello(name="world")
assert(result==42)

